# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""Strategies that filter values that are already present in the Row/Column/Box."""
import typing as t

from ..strategy import Strategy

# These are all identifiers which are only used for type checking.  Frequently, they have to be
# used as strings otherwise python will fail when they are referenced in an annotation so disable
# the pylint check for them.
if t.TYPE_CHECKING:  # pragma: nocover
    # pylint: disable=unused-import
    from ..board import SudokuBoard


# Strategies are classes because they may have to save state.  However, most strategies are very
# simple so there is usually only one method.
# pylint: disable=too-few-public-methods
class NumberInUnit(Strategy):
    """Filters values that are already present in one unit of a SudokuBoard."""

    board_unit: str
    """
    Name of a SudokuBoard view attribute.

    This should be replaced with a simple class variable returning a simple string name for
    a SudokuBoard view attribute.

    For instance, for the strategy that filters numbers that are already present in
    a SudokuBoard's rows, do this::

        class NumberInRow(NumberInUnit):
            board_unit = 'rows'
    """

    def __init__(self):
        """Initialize and fail if we're still abstract."""
        # Provoke an error on instantiation.  This will cause the plugin loading to ignore this
        # class.
        self.board_unit  # pylint: disable=pointless-statement

    @classmethod
    def process_board(cls, board: 'SudokuBoard'):
        """Filter values that are already present in one unit of a SudokuBoard."""
        for unit in getattr(board, cls.board_unit):
            unit_contents = [cell.value for cell in unit if cell.value]

            if not unit_contents:
                continue

            for cell in unit:
                if not cell.value:
                    cell -= unit_contents


class NumberInRow(NumberInUnit):
    """Filter numbers that are already present in the row of the SudokuBoard."""

    board_unit = 'rows'


class NumberInColumn(NumberInUnit):
    """Filter numbers that are already present in the column of the SudokuBoard."""

    board_unit = 'columns'


class NumberInBox(NumberInUnit):
    """Filter numbers that are already present in the box of the SudokuBoard."""

    board_unit = 'boxes'
