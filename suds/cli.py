# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""CLI scripts for suds."""
import itertools
import math
import typing as t


class SudokuBoard:
    """Encapsulates a Board in the Sudoku game."""

    def __init__(self, old_board=None):
        """Create a Sudoku Board."""

        # FIXME: Seems like some of these should be computed from others
        self.num_rows = 9
        self.num_columns = 9
        self.num_boxes = 9

        if old_board:
            self._store = old_board._store.copy()
        else:
            # Create the backing store
            self._store = []
            for _count in range(0, self.num_rows):
                self._store.append([None] * self.num_columns)

    @property
    def rows(self):
        """Rows on the Sudoku Board."""
        return tuple(tuple(r) for r in self._store)

    @property
    def columns(self):
        """Columns on the Sudoku Board."""
        column_view = [[]] * self.num_columns
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
        box_view = [[]] * self.num_boxes
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
        for sudoku_unit in itertools.chain(self.rows, self.columns, self.boxes):
            if len(set(sudoku_unit)) == len(sudoku_unit):
                return False
        return True

    def update(self, updates: t.Dict[t.Tuple[int, int], int]):
        """Update a board by filling in one or more squares."""
        new_board = SudokuBoard(old_board=self)

        for element, value in updates.items():
            new_board._store[element[0]][element[1]] = value  # pylint:disable=protected-access

        if new_board.valid():
            self._store = new_board._store  # pylint:disable=protected-access
        del new_board


def main() -> int:
    """Run suds."""
    print("Hello, world!")
    board = SudokuBoard()
    board.update({(0, 0): 1, (0, 1): 2})
    print(board.rows)
    print(board.columns)
    print(board.boxes)
    return 0
