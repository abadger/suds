import copy

import pytest

from . import testdata
from suds import board as board


def _list_to_tuple(list_instance):
    """Turn a list of lists into a tuple of tuples."""
    accumulator = []
    for element in list_instance:
        if isinstance(element, list):
            accumulator.append(_list_to_tuple(element))
        else:
            accumulator.append(element)

    return tuple(accumulator)


@pytest.fixture
def sboard(request):
    sudoku_data_marker = request.node.get_closest_marker('sudoku_data')
    if sudoku_data_marker:
        new_board = board.SudokuBoard()
        new_board._store = copy.deepcopy(sudoku_data_marker.args[0])
        return new_board
    return board.SudokuBoard()


class TestSudokuBoardInit:
    """Tests for SudokuBoard creation."""

    def test_create_with_defaults(self):
        new_board = board.SudokuBoard()

        # Tuple of tuples of None.  9 rows and 9 columns
        assert new_board.rows == _list_to_tuple(testdata.BLANK_BOARD_DATA)

    def test_create_from_old_board(self):
        initial_board = board.SudokuBoard()
        new_board = board.SudokuBoard(initial_board)
        assert new_board is not initial_board
        assert new_board._store is not initial_board._store
        assert new_board._store[0] is not initial_board._store[0]
        assert new_board._store == initial_board._store

    def test_create_from_list_of_rows(self):
        new_board = board.SudokuBoard.from_list_of_rows(testdata.GOOD_DATA['board']['rows'])

        internal_representation = []
        for row in testdata.GOOD_DATA['board']['rows']:
            internal_representation.append(tuple(c or None for c in row))

        assert new_board.rows == _list_to_tuple(internal_representation)


class TestSudokuBoardViews:
    """Test the SudokuBoard properties that return different views of the data."""

    @pytest.mark.sudoku_data(testdata.ONE_EACH_BOARD_ROWS_DATA)
    def test_rows(self, sboard):
        assert sboard.rows == _list_to_tuple(testdata.ONE_EACH_BOARD_ROWS_DATA)

    @pytest.mark.sudoku_data(testdata.ONE_EACH_BOARD_ROWS_DATA)
    def test_columns(self, sboard):
        assert sboard.columns == _list_to_tuple(testdata.ONE_EACH_BOARD_COLUMNS_DATA)

    @pytest.mark.sudoku_data(testdata.ONE_EACH_BOARD_ROWS_DATA)
    def test_boxes(self, sboard):
        assert sboard.boxes == _list_to_tuple(testdata.ONE_EACH_BOARD_BOXES_DATA)


class TestSudokuBoardUpdate:

    def test_update_serially_success(self, sboard):
        for row_idx, row in enumerate(testdata.ONE_EACH_BOARD_ROWS_DATA):
            for column_idx, cell in ((i, c) for (i, c) in enumerate(row) if c is not None):
                sboard.update({(row_idx, column_idx): cell})

        assert sboard.rows == _list_to_tuple(testdata.ONE_EACH_BOARD_ROWS_DATA)

    def test_update_batched_success(self, sboard):
        board_data = {}
        for row_idx, row in enumerate(testdata.ONE_EACH_BOARD_ROWS_DATA):
            for column_idx, cell in ((i, c) for (i, c) in enumerate(row) if c is not None):
                board_data[(row_idx, column_idx)] = cell
        sboard.update(board_data)

        assert sboard.rows == _list_to_tuple(testdata.ONE_EACH_BOARD_ROWS_DATA)

    @pytest.mark.sudoku_data(testdata.ONE_EACH_BOARD_ROWS_DATA)
    def test_update_failure(self, sboard):
        with pytest.raises(board.InvalidBoardPosition):
            sboard.update({(0, 1): 1})
