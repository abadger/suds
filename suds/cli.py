# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""CLI scripts for suds."""
from . import board


def main() -> int:
    """Run suds."""
    game_board = board.SudokuBoard()
    print(game_board.rows)
    game_board.update({(0, 0): 1, (0, 1): 2})
    print(game_board.rows)
    return 0
