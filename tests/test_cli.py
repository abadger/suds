import copy
import typing as t

import pytest

from suds import cli

BLANK_BOARD_DATA: t.List[t.List[t.Optional[int]]] = [[None] * 9 for _c in range(0, 9)]

# The following are all "rotations" of each other
ONE_EACH_BOARD_ROWS_DATA = copy.deepcopy(BLANK_BOARD_DATA)
ONE_EACH_BOARD_ROWS_DATA[0][0] = 1
ONE_EACH_BOARD_ROWS_DATA[1][3] = 2
ONE_EACH_BOARD_ROWS_DATA[2][6] = 3
ONE_EACH_BOARD_ROWS_DATA[3][1] = 4
ONE_EACH_BOARD_ROWS_DATA[4][4] = 5
ONE_EACH_BOARD_ROWS_DATA[5][7] = 6
ONE_EACH_BOARD_ROWS_DATA[6][2] = 7
ONE_EACH_BOARD_ROWS_DATA[7][5] = 8
ONE_EACH_BOARD_ROWS_DATA[8][8] = 9

ONE_EACH_BOARD_COLUMNS_DATA = copy.deepcopy(BLANK_BOARD_DATA)
ONE_EACH_BOARD_COLUMNS_DATA[0][0] = 1
ONE_EACH_BOARD_COLUMNS_DATA[1][3] = 4
ONE_EACH_BOARD_COLUMNS_DATA[2][6] = 7
ONE_EACH_BOARD_COLUMNS_DATA[3][1] = 2
ONE_EACH_BOARD_COLUMNS_DATA[4][4] = 5
ONE_EACH_BOARD_COLUMNS_DATA[5][7] = 8
ONE_EACH_BOARD_COLUMNS_DATA[6][2] = 3
ONE_EACH_BOARD_COLUMNS_DATA[7][5] = 6
ONE_EACH_BOARD_COLUMNS_DATA[8][8] = 9

ONE_EACH_BOARD_BOXES_DATA = copy.deepcopy(BLANK_BOARD_DATA)
ONE_EACH_BOARD_BOXES_DATA[0][0] = 1
ONE_EACH_BOARD_BOXES_DATA[1][3] = 2
ONE_EACH_BOARD_BOXES_DATA[2][6] = 3
ONE_EACH_BOARD_BOXES_DATA[3][1] = 4
ONE_EACH_BOARD_BOXES_DATA[4][4] = 5
ONE_EACH_BOARD_BOXES_DATA[5][7] = 6
ONE_EACH_BOARD_BOXES_DATA[6][2] = 7
ONE_EACH_BOARD_BOXES_DATA[7][4] = 8
ONE_EACH_BOARD_BOXES_DATA[8][8] = 9


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
def board(request):
    sudoku_data_marker = request.node.get_closest_marker('sudoku_data')
    if sudoku_data_marker:
        board = cli.SudokuBoard()
        board._store = copy.deepcopy(sudoku_data_marker.args[0])
        return board
    return cli.SudokuBoard()


class TestSudokuBoardInit:
    """Tests for SudokuBoard creation."""

    def test_create_with_defaults(self):
        new_board = cli.SudokuBoard()

        # Tuple of tuples of None.  9 rows and 9 columns
        assert new_board.rows == _list_to_tuple(BLANK_BOARD_DATA)

    def test_create_from_old_board(self):
        initial_board = cli.SudokuBoard()
        new_board = cli.SudokuBoard(initial_board)
        assert new_board is not initial_board
        assert new_board._store is not initial_board._store
        assert new_board._store[0] is not initial_board._store[0]
        assert new_board._store == initial_board._store


class TestSudokuBoardViews:
    """Test the SudokuBoard properties that return different views of the data."""

    @pytest.mark.sudoku_data(ONE_EACH_BOARD_ROWS_DATA)
    def test_rows(self, board):
        board.rows == _list_to_tuple(ONE_EACH_BOARD_ROWS_DATA)

    @pytest.mark.sudoku_data(ONE_EACH_BOARD_ROWS_DATA)
    def test_columns(self, board):
        board.columns == _list_to_tuple(ONE_EACH_BOARD_COLUMNS_DATA)

    @pytest.mark.sudoku_data(ONE_EACH_BOARD_ROWS_DATA)
    def test_boxes(self, board):
        board.boxes == _list_to_tuple(ONE_EACH_BOARD_BOXES_DATA)


class TestSudokuBoardUpdate:

    def test_update_serially_success(self, board):
        for row_idx, row in enumerate(ONE_EACH_BOARD_ROWS_DATA):
            for column_idx, cell in ((i, c) for (i, c) in enumerate(row) if c is not None):
                board.update({(row_idx, column_idx): cell})

        assert board.rows == _list_to_tuple(ONE_EACH_BOARD_ROWS_DATA)

    def test_update_batched_success(self, board):
        board_data = {}
        for row_idx, row in enumerate(ONE_EACH_BOARD_ROWS_DATA):
            for column_idx, cell in ((i, c) for (i, c) in enumerate(row) if c is not None):
                board_data[(row_idx, column_idx)] = cell
        board.update(board_data)

        assert board.rows == _list_to_tuple(ONE_EACH_BOARD_ROWS_DATA)

    @pytest.mark.sudoku_data(ONE_EACH_BOARD_ROWS_DATA)
    def test_update_failure(self, board):
        with pytest.raises(cli.InvalidBoardPosition):
            board.update({(0, 1): 1})


def test_main():
    assert cli.main() == 0
