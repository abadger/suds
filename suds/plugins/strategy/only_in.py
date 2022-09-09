# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""Strategies to set the value if is the only possible cell in the Row/Column/Box to have that."""
import abc
import typing as t
from collections import defaultdict

from ...strategy import Strategy

# These are all identifiers which are only used for type checking.  Frequently, they have to be
# used as strings otherwise python will fail when they are referenced in an annotation so disable
# the pylint check for them.
if t.TYPE_CHECKING:  # pragma: nocover
    # pylint: disable=unused-import
    from ...board import SudokuBoard


# Strategies are classes because they may have to save state.  However, most strategies are very
# simple so there is usually only one method.
# pylint: disable=too-few-public-methods
class OnlyInUnit(Strategy, metaclass=abc.ABCMeta):
    """Set numbers that are only allowed in one cell of a unit."""

    board_unit: str
    """
    Name of a SudokuBoard view attribute.

    This should be replaced with a simple class variable returning a simple string name for
    a SudokuBoard view attribute.

    For instance, for the strategy that filters numbers that are already present in
    a SudokuBoard's rows, do this::

        class OnlyInRow(OnlyInUnit):
            board_unit = 'rows'
    """

    def __init__(self):
        """Initialize and fail if we're still abstract."""
        # Provoke an error on instantiation.  This will cause the plugin loading to ignore this
        # class.
        self.board_unit  # pylint: disable=pointless-statement

    @classmethod
    def process_board(cls, board: 'SudokuBoard'):
        """Set values that can only occur in one cell of a unit."""
        for unit in getattr(board, cls.board_unit):
            potentials = defaultdict(list)
            for cell in unit:
                for potential in cell.potential_values:
                    potentials[potential].append(cell)

            for potential, cells_allowed in potentials.items():
                if len(cells_allowed) == 1:
                    cells_allowed[0].value = potential


class OnlyInRow(OnlyInUnit):
    """Set numbers that are only allowed in one cell of a row."""

    board_unit = 'rows'


class OnlyInColumn(OnlyInUnit):
    """Set numbers that are only allowed in one cell of a column."""

    board_unit = 'columns'


class OnlyInBox(OnlyInUnit):
    """Set numbers that are only allowed in one cell of a box."""

    board_unit = 'boxes'
