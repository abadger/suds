import pytest

from suds import board


@pytest.fixture
def sboard(request):
    """Fixture that returns a SudokuBoard populated with data from the sudoku_data mark."""
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
