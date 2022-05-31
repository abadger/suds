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
    print(board.rows)
    # board.update({(0, 0): 1, (0, 1): 2})
    # print(board.rows)
    # board.update({(0, 2): 2})
    # print(board.rows)
    return 0
