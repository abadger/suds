# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""Strategies for finding more Sudoku values."""
import abc
import typing as t
from collections import defaultdict

# These are all identifiers which are only used for type checking.  Frequently, they have to be
# used as strings otherwise python will fail when they are referenced in an annotation so disable
# the pylint check for them.
if t.TYPE_CHECKING:  # pragma: nocover
    # pylint: disable=unused-import
    from .board import SudokuBoard


# Strateies are classes because they may have to save state.  However, most strategies are very
# simple so there is usually only one method.
# pylint: disable=too-few-public-methods
@t.runtime_checkable
class Strategy(t.Protocol, metaclass=abc.ABCMeta):
    """
    Strategy for finding Sudoku values.

    Strategies are classes so that they can save state if needed.  Each strategy is instantiated
    once per SudokuBoard.  If a strategy does not need to save state, it can set its process_board()
    method to be a classmethod or staticmethod.
    """

    @classmethod
    @abc.abstractmethod
    def process_board(cls, board: 'SudokuBoard'):
        """
        Modify the board inplace to narrow down what Sudoku values are possible.

        :arg board: The SudokuBoard to work on.  It is expected that you will modify this in-place.
        """


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


class OnlyInUnit(Strategy):
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

    @classmethod
    def process_board(cls, board: 'SudokuBoard'):
        """Sets values that can only occur in one cell of a unit."""
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


def load_strategies() -> tuple[Strategy, ...]:
    """Load and return strategies."""
    # Note: In the future, strategies will be plugin based.  This function will then hold the logic
    # to find and load all the strategies.
    return (
        NumberInBox(),
        NumberInColumn(),
        NumberInRow(),
        OnlyInRow(),
        OnlyInColumn(),
        OnlyInBox(),
    )
