# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""CLI scripts for suds."""
from .board import SudokuBoard


def main() -> int:
    """Run suds."""
    board = SudokuBoard()
    print(board.rows)
    board.update({(0, 0): 1, (0, 1): 2})
    print(board.rows)
    # board.update({(0, 2): 2})
    # print(board.rows)
    return 0
