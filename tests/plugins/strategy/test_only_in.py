import copy

import pytest

from ... import testdata
from suds.board import SudokuCell
from suds.plugins.strategy import only_in


@pytest.mark.sudoku_data(testdata.BLANK_BOARD_DATA)
def test_only_in_row(sboard):
    # Set up a row where one cell is the only one that can be 9
    general_cell = SudokuCell()
    general_row = (general_cell, ) * 9

    row1_pre = []
    for _dummy in range(0, 8):
        cell = copy.deepcopy(general_cell)
        cell -= 9
        row1_pre.append(cell)

    row1_pre.append(copy.deepcopy(general_cell))
    sboard._store[0] = row1_pre

    # We expect the last cell in the row will be 9 after the strategy runs
    row1_post = copy.deepcopy(row1_pre)
    row1_post[8].value = 9
    row1_post = tuple(row1_post)

    strat = only_in.OnlyInRow()

    strat.process_board(sboard)

    assert sboard.rows == (
        row1_post,
        general_row,
        general_row,
        general_row,
        general_row,
        general_row,
        general_row,
        general_row,
        general_row,
    )


@pytest.mark.sudoku_data(testdata.BLANK_BOARD_DATA)
def test_only_in_column(sboard):
    # Set up a column where one cell is the only one that can be 9
    general_cell = SudokuCell()
    general_col = (general_cell, ) * 9

    col1_pre = []
    for _dummy in range(0, 8):
        cell = copy.deepcopy(general_cell)
        cell -= 9
        col1_pre.append(cell)

    col1_pre.append(copy.deepcopy(general_cell))

    # Place the column into the board's internal storage.  The board is stored as rows internally.
    for row_idx, cell in enumerate(col1_pre):
        sboard._store[row_idx][0] = cell

    # We expect the last cell in the col will be 9 after the strategy runs
    col1_post = copy.deepcopy(col1_pre)
    col1_post[8].value = 9
    col1_post = tuple(col1_post)

    strat = only_in.OnlyInColumn()

    strat.process_board(sboard)

    assert sboard.columns == (
        col1_post,
        general_col,
        general_col,
        general_col,
        general_col,
        general_col,
        general_col,
        general_col,
        general_col,
    )


@pytest.mark.sudoku_data(testdata.BLANK_BOARD_DATA)
def test_only_in_box(sboard):
    # Set up a box where one cell is the only one that can be 9
    general_cell = SudokuCell()
    general_box = (general_cell, ) * 9

    box1_pre = []
    for _dummy in range(0, 8):
        cell = copy.deepcopy(general_cell)
        cell -= 9
        box1_pre.append(cell)

    box1_pre.append(copy.deepcopy(general_cell))

    # Place the column into the board's internal storage.  The board is stored as rows internally.
    for box_pos, cell in enumerate(box1_pre):
        col_idx = box_pos % 3
        row_idx = box_pos // 3
        sboard._store[row_idx][col_idx] = cell

    # We expect the last cell in the box will be 9 after the strategy runs
    box1_post = copy.deepcopy(box1_pre)
    box1_post[8].value = 9
    box1_post = tuple(box1_post)

    strat = only_in.OnlyInBox()

    strat.process_board(sboard)

    assert sboard.boxes == (
        box1_post,
        general_box,
        general_box,
        general_box,
        general_box,
        general_box,
        general_box,
        general_box,
        general_box,
    )
