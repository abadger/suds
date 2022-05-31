# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""CLI scripts for suds."""
import copy
import itertools
import math
import typing as t


class InvalidBoardPosition(Exception):
    """The Sudoku Board would be invalid in this state."""


class SudokuBoard:
    """Encapsulates a Board in the Sudoku game."""

    def __init__(self, old_board=None):
        """Create a Sudoku Board."""
        # FIXME: Seems like some of these should be computed from others
        self.num_rows = 9
        self.num_columns = 9
        self.num_boxes = 9

        if old_board:
            self._store = copy.deepcopy(old_board._store)
        else:
            # Create the backing store
            self._store = []
            for _count in range(0, self.num_rows):
                self._store.append([None] * self.num_columns)

    @classmethod
    def from_list_of_rows(cls, rows: t.Sequence[t.Sequence[int]]) -> 'SudokuBoard':
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
            sudoku_unit = [num for num in sudoku_unit if num]
            if sudoku_unit and len(frozenset(sudoku_unit)) != len(sudoku_unit):
                # Invalid if a number has repeated in this unit
                return False
        return True

    def update(self, updates: t.Dict[t.Tuple[int, int], int]):
        """Update a board by filling in one or more squares."""
        old_store = copy.deepcopy(self._store)

        for element, value in updates.items():
            self._store[element[0]][element[1]] = value

        if not self.valid():
            self._store = old_store
            raise InvalidBoardPosition('The updates would make an invalid Sudoku')
