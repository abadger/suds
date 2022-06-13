# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""Strategies for finding more Sudoku values."""
import abc
import sys
import typing as t

from straight.plugin import load

# These are all identifiers which are only used for type checking.  Frequently, they have to be
# used as strings otherwise python will fail when they are referenced in an annotation so disable
# the pylint check for them.
if t.TYPE_CHECKING:  # pragma: nocover
    # pylint: disable=unused-import
    from .board import SudokuBoard


# Strategies are classes because they may have to save state.  However, most strategies are very
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


def load_strategies() -> list[Strategy]:
    """Load and return strategies."""

    plugins = load('suds.strategy_plugins', subclasses=Strategy)

    only_good_plugins = []
    for plugin in plugins:
        try:
            only_good_plugins.append(plugin())
        except Exception as e:  # pylint: disable=broad-except
            # Any error instantiating the plugin is recoverable.  But we need to log that the
            # exception happened.
            # FIXME: Replace sys.stderr with actual logging
            sys.stderr.write(f'Error loading {plugin.__name__}: {e}\n')

    return only_good_plugins
