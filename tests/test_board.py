import itertools
import re
from collections.abc import Iterable

import pytest

from . import testdata
from suds import board

INVALID_CELL_VALUES = (
    10,
    0,
    -1,
    (1, 3, 8, 0),
)


def _list_to_tuple(list_instance):
    """Turn a list of lists into a tuple of tuples."""
    accumulator = []
    for element in list_instance:
        if isinstance(element, list):
            accumulator.append(_list_to_tuple(element))
        else:
            accumulator.append(element)

    return tuple(accumulator)


def _values_to_cells(values):
    """Take an iterator of 9 ints and return a list of SudokuCells with those as the values."""
    for row in values:
        yield [
            board.SudokuCell(potential_values=elem) if elem else board.SudokuCell() for elem in row
        ]


def input_format_to_view_format(values):
    """Take an iterator of 9 ints and return the format that a view of a SudokuBoard would use."""
    return _list_to_tuple(_values_to_cells(values))


@pytest.fixture
def sboard(request):
    new_board = board.SudokuBoard()
    sudoku_data_marker = request.node.get_closest_marker('sudoku_data')

    if not sudoku_data_marker:
        return new_board

    board_update_format = {}
    for row_idx, row in enumerate(sudoku_data_marker.args[0]):
        for col_idx, cell_value in enumerate(row):
            if cell_value:
                board_update_format[(row_idx, col_idx)] = cell_value

    new_board.update(board_update_format)
    return new_board


#
# SudokuCell tests
#


class TestVerifySudokuValues:

    @pytest.mark.parametrize('values', (
        (1, 2),
        {1, 2},
        [1, 2],
        range(1, 10),
    ))
    def test_good_sudoku_values(self, values):
        assert board._verify_sudoku_values(values)

    @pytest.mark.parametrize('values',
                             itertools.chain(
                                 ({v} for v in INVALID_CELL_VALUES if isinstance(v, Iterable)),
                                 (v for v in INVALID_CELL_VALUES if not isinstance(v, Iterable)),
                             ))
    def test_bad_sudoku_values(self, values):
        assert board._verify_sudoku_values((values, )) is False


class TestSudokuCellCreation:
    """Test SudokuCell."""

    def test_create_cell_defaults(self):
        cell = board.SudokuCell()

        assert cell.value is None
        assert cell.potential_values == frozenset((1, 2, 3, 4, 5, 6, 7, 8, 9))

    def test_create_cell_given_values(self):
        cell = board.SudokuCell(potential_values=(1, 3, 5, 8))

        assert cell.value is None
        assert cell.potential_values == frozenset((1, 3, 5, 8))

    def test_create_cell_given_one_value(self):
        cell = board.SudokuCell(potential_values=7)

        assert cell.value == 7
        assert cell.potential_values == frozenset((7, ))

    @pytest.mark.parametrize('value', INVALID_CELL_VALUES)
    def test_create_cell_invalid(self, value):
        with pytest.raises(
                ValueError, match='Potential values must all be from this'
                ' set of numbers:.*'):
            board.SudokuCell(potential_values=value)


class TestSudokuCellMethods:

    @pytest.mark.parametrize('potential_values, representation', (
        (None, '{1, 2, 3, 4, 5, 6, 7, 8, 9}'),
        (1, '1'),
        ((1, 2), '{1, 2}'),
    ))
    def test_repr(self, potential_values, representation):
        cell = board.SudokuCell(potential_values=potential_values)
        assert repr(cell) == representation

    def test_get_value_not_yet_solved(self):
        cell = board.SudokuCell(potential_values=(3, 5, 7))

        assert cell.value is None

    def test_get_value_solved(self):
        cell = board.SudokuCell(potential_values=(3, ))

        assert cell.value == 3

    def test_set_value(self):
        cell = board.SudokuCell()
        assert cell.value is None

        cell.value = 8

        assert cell.value == 8
        assert cell.potential_values == frozenset((8, ))

    @pytest.mark.parametrize('value', (v for v in INVALID_CELL_VALUES if isinstance(v, int)))
    def test_set_value_invalid(self, value):
        cell = board.SudokuCell()

        with pytest.raises(ValueError, match='Cell values must be from this set of numbers: .*'):
            cell.value = value

    def test_set_value_eliminated(self):
        cell = board.SudokuCell(potential_values=(1, 2, 3))

        with pytest.raises(
                ValueError, match='Attempt to set cell to a value that'
                ' has been eliminated.'):
            cell.value = 4

    def test_get_potential_values(self):
        cell = board.SudokuCell(potential_values=(5, 2))

        assert cell.potential_values == frozenset((5, 2))

    @pytest.mark.parametrize('initial, removed, expected', (
        (range(1, 10), (1, 3, 5, 7, 9), frozenset((2, 4, 6, 8))),
        ((1, 3, 5), 7, frozenset((1, 3, 5))),
        ((1, 3, 5), 3, frozenset((1, 5))),
        ((1, 3, 5), (7, 9), frozenset((1, 3, 5))),
        ((1, 3, 5), (1, 7, 9), frozenset((3, 5))),
    ))
    def test_isub(self, initial, removed, expected):
        cell = board.SudokuCell(potential_values=initial)

        cell -= removed

        assert cell.potential_values == expected

    def test_isub_eliminates_all(self):
        cell = board.SudokuCell(potential_values=3)

        with pytest.raises(
                ValueError, match='Removing 3 would leave the cell with'
                ' no solutions'):
            cell -= 3

    @pytest.mark.parametrize('cell, other', (
        (board.SudokuCell(), board.SudokuCell()),
        (board.SudokuCell(potential_values=3), board.SudokuCell(potential_values=3)),
        (board.SudokuCell(potential_values=(4, 3)), board.SudokuCell(potential_values=(3, 4))),
    ))
    def test_eq_equal(self, cell, other):
        assert cell == other

    @pytest.mark.parametrize('cell, other', (
        (board.SudokuCell(potential_values=3), board.SudokuCell(potential_values=4)),
        (board.SudokuCell(potential_values=3), board.SudokuCell(potential_values=(3, 4))),
        (board.SudokuCell(potential_values=(1, 2)), board.SudokuCell(potential_values=(3, 4))),
        (board.SudokuCell(potential_values=3), 3),
        (board.SudokuCell(potential_values=(3, 4)), 3),
        (board.SudokuCell(potential_values=(3, 4)), board.SudokuCell()),
    ))
    def test_eq_not_equal(self, cell, other):
        assert cell != other


#
# SudokuBoard tests
#


class TestSudokuBoardInit:
    """Tests for SudokuBoard creation."""

    def test_create_with_defaults(self):
        new_board = board.SudokuBoard()

        # Tuple of tuples of None.  9 rows and 9 columns
        assert new_board.rows == input_format_to_view_format(testdata.BLANK_BOARD_DATA)

    def test_create_from_old_board(self):
        initial_board = board.SudokuBoard()
        new_board = board.SudokuBoard(initial_board)

        # Check that we have a copy, not the same storage and cells
        assert new_board is not initial_board
        assert new_board._store is not initial_board._store
        assert new_board._store[0] is not initial_board._store[0]
        assert new_board._store[0][0] is not initial_board._store[0][0]

        # Check that the values are the same
        assert new_board._store == initial_board._store

    def test_create_from_list_of_rows(self):
        new_board = board.SudokuBoard.from_list_of_rows(testdata.GOOD_DATA['board']['rows'])

        internal_representation = []
        for row in testdata.GOOD_DATA['board']['rows']:
            internal_representation.append(tuple(c or None for c in row))

        assert new_board.rows == input_format_to_view_format(internal_representation)


class TestSudokuBoardViews:
    """Test the SudokuBoard properties that return different views of the data."""

    @pytest.mark.sudoku_data(testdata.ONE_EACH_BOARD_ROWS_DATA)
    def test_rows(self, sboard):
        assert sboard.rows == input_format_to_view_format(testdata.ONE_EACH_BOARD_ROWS_DATA)

    @pytest.mark.sudoku_data(testdata.ONE_EACH_BOARD_ROWS_DATA)
    def test_columns(self, sboard):
        assert sboard.columns == input_format_to_view_format(testdata.ONE_EACH_BOARD_COLUMNS_DATA)

    @pytest.mark.sudoku_data(testdata.ONE_EACH_BOARD_ROWS_DATA)
    def test_boxes(self, sboard):
        assert sboard.boxes == input_format_to_view_format(testdata.ONE_EACH_BOARD_BOXES_DATA)


class TestSudokuBoardUpdate:

    def test_update_serially_success(self, sboard):
        for row_idx, row in enumerate(testdata.ONE_EACH_BOARD_ROWS_DATA):
            for column_idx, cell in ((i, c) for (i, c) in enumerate(row) if c):
                sboard.update({(row_idx, column_idx): cell})

        assert sboard.rows == input_format_to_view_format(testdata.ONE_EACH_BOARD_ROWS_DATA)

    def test_update_batched_success(self, sboard):
        board_data = {}
        for row_idx, row in enumerate(testdata.ONE_EACH_BOARD_ROWS_DATA):
            for column_idx, cell in ((i, c) for (i, c) in enumerate(row) if c):
                board_data[(row_idx, column_idx)] = cell

        sboard.update(board_data)

        assert sboard.rows == input_format_to_view_format(testdata.ONE_EACH_BOARD_ROWS_DATA)

    @pytest.mark.sudoku_data(testdata.ONE_EACH_BOARD_ROWS_DATA)
    def test_update_failure(self, sboard):
        with pytest.raises(
                board.InvalidBoardPosition, match='The updates would make an invalid Sudoku'):
            sboard.update({(0, 1): 1})

    def test_update_known_constraints(self, sboard):
        sboard._store[0][1] -= 3
        with pytest.raises(
                board.InvalidBoardPosition,
                match=re.escape('The update would violate the known constraints of cell (0, 1):'
                                ' Attempt to set cell to a value that has been eliminated.')):
            sboard.update({(0, 1): 3})
