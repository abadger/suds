# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""CLI scripts for suds."""
import math


class SudokuBoard:
    """Encapsulates a Board in the Sudoku game."""

    def __init__(self):
        """Create a Sudoku Board."""

        # FIXME: Seems like some of these should be computed from others
        self.num_rows = 9
        self.num_columns = 9
        self.num_boxes = 9

        # Create the backing store
        self._store = []
        for i in range(0, self.num_rows):
            self._store[i] = [None] * self.num_columns

    @property
    def rows(self):
        """Rows on the Sudoku Board."""
        return tuple(tuple(r) for r in self._store)

    @property
    def columns(self):
        """Columns on the Sudoku Board."""
        column_view = [] * self.num_columns
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
        box_view = [] * self.num_boxes
        box_set = math.sqrt(self.num_boxes)

        for row_idx, row in enumerate(self._store):
            most_significant_digit = row_idx // box_set
            for column_idx, cell in enumerate(row):
                least_significant_digit = column_idx // box_set
                box_idx = int(f'{most_significant_digit}{least_significant_digit}', base=4)
                box_view[box_idx].append(cell)
        return tuple(tuple(b) for b in box_view)

    def sudoku_valid(self) -> bool:
        """Validate the present state of the board."""

    def sudoku_update(self):
        """Update a board by filling in one or more squares."""


def main() -> int:
    """Run suds."""
    print("Hello, world!")
    board = SudokuBoard()
    print(board.rows)
    print(board.columns)
    print(board.boxes)
    return 0
