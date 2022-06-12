# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""CLI scripts for suds."""
import copy
import itertools
import math
import typing as t
from collections.abc import Iterable
from collections.abc import Sequence


class InvalidBoardPosition(Exception):
    """The Sudoku Board would be invalid in this state."""


LEGAL_VALUES = frozenset(range(1, 10))


def _verify_sudoku_values(values: Iterable[int]):
    # Filter out legal values.  If anything remains, it is an invalid value so return False
    for _dummy in (v for v in values if v not in LEGAL_VALUES):
        return False
    return True


class SudokuCell:
    """Information that defines a generic cell in the SudokuBoard."""

    def __init__(self, potential_values: t.Union[Iterable[int], int, None] = None):
        if potential_values is None:
            potential_values = range(1, 10)  # 1-9
        elif not isinstance(potential_values, Iterable):
            potential_values = {potential_values}

        # Note: Change to set before validation in case we are passed an iterator
        potential_values = frozenset(potential_values)
        if not _verify_sudoku_values(potential_values):
            raise ValueError('Potential values must all be from this set of numbers:'
                             f' {", ".join(str(v) for v in LEGAL_VALUES)},'
                             f' not {potential_values}')

        self._potential_values: frozenset[int] = potential_values

    def __repr__(self):
        return str(self.value) if self.value else repr(set(self._potential_values))

    @property
    def solved(self) -> bool:
        """If all but one value have been eliminated, then this is True."""
        if len(self.potential_values) != 1:
            return False
        return True

    @property
    def value(self) -> t.Union[int, None]:
        """Value of the cell or None if there is more than one possible value."""
        if len(self._potential_values) == 1:
            return next(iter(self._potential_values))
        return None

    @value.setter
    def value(self, value: int):
        """Set the value to a single number."""
        new_value: frozenset[int] = frozenset((value, ))
        if not _verify_sudoku_values(new_value):
            raise ValueError('Cell values must be from this set of numbers:'
                             f' {", ".join(str(v) for v in LEGAL_VALUES)},'
                             f' not {value}')

        if value not in self.potential_values:
            raise ValueError('Attempt to set cell to a value that has been eliminated.')

        self._potential_values = new_value

    @property
    def potential_values(self):
        """Cell values that will not cause an immediate violation of the sudoku rules."""
        return self._potential_values

    def __isub__(self, other: t.Union[Iterable[int], int]):
        """
        Remove one or more potential values that the cell could be.

        :arg other: An int between 1 and 9 or an iterable of ints between 1 and 9 which
            are values that the cell cannot be.
        """
        if not isinstance(other, Iterable):
            other = frozenset((other, ))

        new_potential_values = self.potential_values.difference(other)
        if not new_potential_values:
            raise ValueError(f'Removing {", ".join(str(elem) for elem in other)}'
                             ' would leave the cell with no solutions')

        self._potential_values = new_potential_values

        return self

    def __eq__(self, other):
        """Test for equality with other SudokuCells."""
        if not isinstance(other, SudokuCell):
            return super().__eq__(other)

        return self.potential_values == other.potential_values


class SudokuBoard:
    """Encapsulates a Board in the Sudoku game."""

    def __init__(self, old_board: 'SudokuBoard' = None):
        """Create a Sudoku Board."""
        # FIXME: Seems like some of these should be computed from others
        self.num_rows: int = 9
        self.num_columns: int = 9
        self.num_boxes: int = 9

        if old_board:
            self._store: list[list[SudokuCell]] = copy.deepcopy(old_board._store)
        else:
            # Create the backing store
            self._store: list[list[SudokuCell]] = []
            for _count in range(0, self.num_rows):
                self._store.append([SudokuCell() for _dummy in range(0, self.num_columns)])

    @classmethod
    def from_list_of_rows(cls, rows: Sequence[Sequence[int]]) -> 'SudokuBoard':
        """
        Alternate constructor that reads from a list of rows.

        The list of rows looks like this:

        * A nine element Sequence.
        * Each element is a Sequence of nine ints.
        * Each int must be from 0 to 9 inclusive.
        * 0 represents  blank cell.
        * Example:
            (
                (0, 0, 7, 0, 0, 0, 0, 0, 6),
                (0, 6, 0, 8, 0, 0, 2, 0, 5),
                (0, 0, 8, 0, 6, 9, 3, 0, 0),
                (7, 0, 6, 0, 3, 8, 1, 0, 0),
                (4, 8, 9, 0, 1, 0, 7, 6, 3),
                (0, 0, 3, 9, 7, 0, 5, 0, 8),
                (0, 0, 5, 6, 8, 0, 4, 0, 0),
                (8, 0, 4, 0, 0, 7, 0, 5, 0),
                (6, 0, 0, 0, 0, 0, 9, 0, 0),
            )
        """
        new_board = cls()

        initial_data = {}
        for ridx, row in enumerate(rows):
            for cidx, cell in enumerate(row):
                if cell:
                    initial_data[(ridx, cidx)] = cell

        new_board.update(initial_data)

        return new_board

    @property
    def rows(self):
        """Rows on the Sudoku Board."""
        return tuple(tuple(r) for r in self._store)

    @property
    def columns(self):
        """Columns on the Sudoku Board."""
        column_view = [[] for _c in range(0, self.num_columns)]
        for row in self._store:
            for column_idx, cell in enumerate(row):
                column_view[column_idx].append(cell)

        return tuple(tuple(c) for c in column_view)

    @property
    def boxes(self):
        """
        Sub-squares on the Sudoku Board.

        Sudoku boards are divided into sub-squares which each must contain all of the sudoku
        numbers.  :attr:`boxes` holds a view of the data which reflects those sub-squares.
        """
        box_view = [[] for _c in range(0, self.num_boxes)]
        box_set = int(math.sqrt(self.num_boxes))

        for row_idx, row in enumerate(self._store):
            most_significant_digit = row_idx // box_set
            for column_idx, cell in enumerate(row):
                least_significant_digit = column_idx // box_set
                box_idx = int(f'{most_significant_digit}{least_significant_digit}', base=3)
                box_view[box_idx].append(cell)
        return tuple(tuple(b) for b in box_view)

    def valid(self) -> bool:
        """Validate the present state of the board."""
        # A sudoku unit is a subset of the board that must contain one and only one of each number.
        for sudoku_unit in itertools.chain(self.rows, self.columns, self.boxes):
            # Only check filled spaces on this unit of the board
            sudoku_unit = [cell.value for cell in sudoku_unit if cell.value]
            if sudoku_unit and len(frozenset(sudoku_unit)) != len(sudoku_unit):
                # Invalid if a number has repeated in this unit
                return False
        return True

    def update(self, updates: dict[tuple[int, int], int]):
        """Update a board by filling in one or more squares."""
        old_store = copy.deepcopy(self._store)

        for element, value in updates.items():
            try:
                self._store[element[0]][element[1]].value = value
            except ValueError as e:
                raise InvalidBoardPosition('The update would violate the known'
                                           f' constraints of cell {element}: {e}') from e

        if not self.valid():
            self._store = old_store
            raise InvalidBoardPosition('The updates would make an invalid Sudoku')
