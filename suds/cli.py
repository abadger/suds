# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""CLI scripts for suds."""
import argparse
import sys
import typing as t

from .board import SudokuBoard
from .savefile import load_save_file
from .strategy import load_strategies


def parse_args(args: t.Sequence[str]) -> argparse.Namespace:
    """
    Parser the commandline.

    :arg args: The argument list.

    """
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='The filename containing the json encoded sudoku board')

    args: argparse.Namespace = parser.parse_args(args)

    return args


def main() -> int:
    """Run suds."""
    args = parse_args(sys.argv[1:])
    save_data = load_save_file(args.filename)

    board: SudokuBoard = SudokuBoard.from_list_of_rows(save_data.board.rows)
    strategies = load_strategies()

    while not board.solved:
        old_board = SudokuBoard(board)

        for strategy in strategies:
            strategy.process_board(board)

        if old_board == board:
            break
    else:
        # Success
        print('The solution is:\n')
        print(board.format())
        return 0

    print('I was not smart enough to solve this sudoku\n')
    print(board.format())
    return 1
