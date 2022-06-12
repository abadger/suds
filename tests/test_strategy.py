import copy

import pytest

from . import testdata
from suds import strategy
from suds.board import SudokuCell


@pytest.mark.sudoku_data(testdata.EASY_DATA['board']['rows'])
def test_number_in_row(sboard):
    strat = strategy.NumberInRow()

    strat.process_board(sboard)

    general_cell = SudokuCell()
    general_cell -= (7, 6)
    row1 = [general_cell] * 9
    row1[2] = SudokuCell(potential_values=7)
    row1[8] = SudokuCell(potential_values=6)
    row1 = tuple(row1)

    general_cell = SudokuCell()
    general_cell -= (2, 5, 6, 8)
    row2 = [general_cell] * 9
    row2[1] = SudokuCell(potential_values=6)
    row2[3] = SudokuCell(potential_values=8)
    row2[6] = SudokuCell(potential_values=2)
    row2[8] = SudokuCell(potential_values=5)
    row2 = tuple(row2)

    general_cell = SudokuCell()
    general_cell -= (3, 6, 8, 9)
    row3 = [general_cell] * 9
    row3[2] = SudokuCell(potential_values=8)
    row3[4] = SudokuCell(potential_values=6)
    row3[5] = SudokuCell(potential_values=9)
    row3[6] = SudokuCell(potential_values=3)
    row3 = tuple(row3)

    general_cell = SudokuCell()
    general_cell -= (1, 3, 6, 7, 8)
    row4 = [general_cell] * 9
    row4[0] = SudokuCell(potential_values=7)
    row4[2] = SudokuCell(potential_values=6)
    row4[4] = SudokuCell(potential_values=3)
    row4[5] = SudokuCell(potential_values=8)
    row4[6] = SudokuCell(potential_values=1)
    row4 = tuple(row4)

    general_cell = SudokuCell()
    general_cell -= (1, 3, 4, 6, 7, 8, 9)
    row5 = [general_cell] * 9
    row5[0] = SudokuCell(potential_values=4)
    row5[1] = SudokuCell(potential_values=8)
    row5[2] = SudokuCell(potential_values=9)
    row5[4] = SudokuCell(potential_values=1)
    row5[6] = SudokuCell(potential_values=7)
    row5[7] = SudokuCell(potential_values=6)
    row5[8] = SudokuCell(potential_values=3)
    row5 = tuple(row5)

    general_cell = SudokuCell()
    general_cell -= (3, 5, 7, 8, 9)
    row6 = [general_cell] * 9
    row6[2] = SudokuCell(potential_values=3)
    row6[3] = SudokuCell(potential_values=9)
    row6[4] = SudokuCell(potential_values=7)
    row6[6] = SudokuCell(potential_values=5)
    row6[8] = SudokuCell(potential_values=8)
    row6 = tuple(row6)

    general_cell = SudokuCell()
    general_cell -= (4, 5, 6, 8)
    row7 = [general_cell] * 9
    row7[2] = SudokuCell(potential_values=5)
    row7[3] = SudokuCell(potential_values=6)
    row7[4] = SudokuCell(potential_values=8)
    row7[6] = SudokuCell(potential_values=4)
    row7 = tuple(row7)

    general_cell = SudokuCell()
    general_cell -= (4, 5, 7, 8)
    row8 = [general_cell] * 9
    row8[0] = SudokuCell(potential_values=8)
    row8[2] = SudokuCell(potential_values=4)
    row8[5] = SudokuCell(potential_values=7)
    row8[7] = SudokuCell(potential_values=5)
    row8 = tuple(row8)

    general_cell = SudokuCell()
    general_cell -= (6, 9)
    row9 = [general_cell] * 9
    row9[0] = SudokuCell(potential_values=6)
    row9[6] = SudokuCell(potential_values=9)
    row9 = tuple(row9)

    assert sboard.rows == (
        row1,
        row2,
        row3,
        row4,
        row5,
        row6,
        row7,
        row8,
        row9,
    )


@pytest.mark.sudoku_data(testdata.EASY_DATA['board']['rows'])
def test_number_in_column(sboard):
    strat = strategy.NumberInColumn()

    strat.process_board(sboard)

    general_cell = SudokuCell()
    general_cell -= (4, 6, 7, 8)
    col1 = [general_cell] * 9
    col1[3] = SudokuCell(potential_values=7)
    col1[4] = SudokuCell(potential_values=4)
    col1[7] = SudokuCell(potential_values=8)
    col1[8] = SudokuCell(potential_values=6)
    col1 = tuple(col1)

    general_cell = SudokuCell()
    general_cell -= (6, 8)
    col2 = [general_cell] * 9
    col2[1] = SudokuCell(potential_values=6)
    col2[4] = SudokuCell(potential_values=8)
    col2 = tuple(col2)

    general_cell = SudokuCell()
    general_cell -= (3, 4, 5, 6, 7, 8, 9)
    col3 = [general_cell] * 9
    col3[0] = SudokuCell(potential_values=7)
    col3[2] = SudokuCell(potential_values=8)
    col3[3] = SudokuCell(potential_values=6)
    col3[4] = SudokuCell(potential_values=9)
    col3[5] = SudokuCell(potential_values=3)
    col3[6] = SudokuCell(potential_values=5)
    col3[7] = SudokuCell(potential_values=4)
    col3 = tuple(col3)

    general_cell = SudokuCell()
    general_cell -= (6, 8, 9)
    col4 = [general_cell] * 9
    col4[1] = SudokuCell(potential_values=8)
    col4[5] = SudokuCell(potential_values=9)
    col4[6] = SudokuCell(potential_values=6)
    col4 = tuple(col4)

    general_cell = SudokuCell()
    general_cell -= (1, 3, 6, 7, 8)
    col5 = [general_cell] * 9
    col5[2] = SudokuCell(potential_values=6)
    col5[3] = SudokuCell(potential_values=3)
    col5[4] = SudokuCell(potential_values=1)
    col5[5] = SudokuCell(potential_values=7)
    col5[6] = SudokuCell(potential_values=8)
    col5 = tuple(col5)

    general_cell = SudokuCell()
    general_cell -= (7, 8, 9)
    col6 = [general_cell] * 9
    col6[2] = SudokuCell(potential_values=9)
    col6[3] = SudokuCell(potential_values=8)
    col6[7] = SudokuCell(potential_values=7)
    col6 = tuple(col6)

    general_cell = SudokuCell()
    general_cell -= (1, 2, 3, 4, 5, 7, 9)
    col7 = [general_cell] * 9
    col7[1] = SudokuCell(potential_values=2)
    col7[2] = SudokuCell(potential_values=3)
    col7[3] = SudokuCell(potential_values=1)
    col7[4] = SudokuCell(potential_values=7)
    col7[5] = SudokuCell(potential_values=5)
    col7[6] = SudokuCell(potential_values=4)
    col7[8] = SudokuCell(potential_values=9)
    col7 = tuple(col7)

    general_cell = SudokuCell()
    general_cell -= (6, 5)
    col8 = [general_cell] * 9
    col8[4] = SudokuCell(potential_values=6)
    col8[7] = SudokuCell(potential_values=5)
    col8 = tuple(col8)

    general_cell = SudokuCell()
    general_cell -= (3, 5, 6, 8)
    col9 = [general_cell] * 9
    col9[0] = SudokuCell(potential_values=6)
    col9[1] = SudokuCell(potential_values=5)
    col9[4] = SudokuCell(potential_values=3)
    col9[5] = SudokuCell(potential_values=8)
    col9 = tuple(col9)

    assert sboard.columns == (
        col1,
        col2,
        col3,
        col4,
        col5,
        col6,
        col7,
        col8,
        col9,
    )


@pytest.mark.sudoku_data(testdata.EASY_DATA['board']['rows'])
def test_number_in_box(sboard):
    strat = strategy.NumberInBox()

    strat.process_board(sboard)

    general_cell = SudokuCell()
    general_cell -= (6, 7, 8)
    box1 = [general_cell] * 9
    box1[2] = SudokuCell(potential_values=7)
    box1[4] = SudokuCell(potential_values=6)
    box1[8] = SudokuCell(potential_values=8)
    box1 = tuple(box1)

    general_cell = SudokuCell()
    general_cell -= (6, 8, 9)
    box2 = [general_cell] * 9
    box2[3] = SudokuCell(potential_values=8)
    box2[7] = SudokuCell(potential_values=6)
    box2[8] = SudokuCell(potential_values=9)
    box2 = tuple(box2)

    general_cell = SudokuCell()
    general_cell -= (2, 3, 5, 6)
    box3 = [general_cell] * 9
    box3[2] = SudokuCell(potential_values=6)
    box3[3] = SudokuCell(potential_values=2)
    box3[5] = SudokuCell(potential_values=5)
    box3[6] = SudokuCell(potential_values=3)
    box3 = tuple(box3)

    general_cell = SudokuCell()
    general_cell -= (3, 4, 6, 7, 8, 9)
    box4 = [general_cell] * 9
    box4[0] = SudokuCell(potential_values=7)
    box4[2] = SudokuCell(potential_values=6)
    box4[3] = SudokuCell(potential_values=4)
    box4[4] = SudokuCell(potential_values=8)
    box4[5] = SudokuCell(potential_values=9)
    box4[8] = SudokuCell(potential_values=3)
    box4 = tuple(box4)

    general_cell = SudokuCell()
    general_cell -= (1, 3, 7, 8, 9)
    box5 = [general_cell] * 9
    box5[1] = SudokuCell(potential_values=3)
    box5[2] = SudokuCell(potential_values=8)
    box5[4] = SudokuCell(potential_values=1)
    box5[6] = SudokuCell(potential_values=9)
    box5[7] = SudokuCell(potential_values=7)
    box5 = tuple(box5)

    general_cell = SudokuCell()
    general_cell -= (1, 3, 5, 6, 7, 8)
    box6 = [general_cell] * 9
    box6[0] = SudokuCell(potential_values=1)
    box6[3] = SudokuCell(potential_values=7)
    box6[4] = SudokuCell(potential_values=6)
    box6[5] = SudokuCell(potential_values=3)
    box6[6] = SudokuCell(potential_values=5)
    box6[8] = SudokuCell(potential_values=8)
    box6 = tuple(box6)

    general_cell = SudokuCell()
    general_cell -= (4, 5, 6, 8)
    box7 = [general_cell] * 9
    box7[2] = SudokuCell(potential_values=5)
    box7[3] = SudokuCell(potential_values=8)
    box7[5] = SudokuCell(potential_values=4)
    box7[6] = SudokuCell(potential_values=6)
    box7 = tuple(box7)

    general_cell = SudokuCell()
    general_cell -= (6, 7, 8)
    box8 = [general_cell] * 9
    box8[0] = SudokuCell(potential_values=6)
    box8[1] = SudokuCell(potential_values=8)
    box8[5] = SudokuCell(potential_values=7)
    box8 = tuple(box8)

    general_cell = SudokuCell()
    general_cell -= (4, 5, 9)
    box9 = [general_cell] * 9
    box9[0] = SudokuCell(potential_values=4)
    box9[4] = SudokuCell(potential_values=5)
    box9[6] = SudokuCell(potential_values=9)
    box9 = tuple(box9)

    assert sboard.boxes == (
        box1,
        box2,
        box3,
        box4,
        box5,
        box6,
        box7,
        box8,
        box9,
    )


@pytest.mark.sudoku_data(testdata.WITH_BLANK_UNIT_DATA['board']['rows'])
def test_number_in_box_with_blank_boxes(sboard):
    strat = strategy.NumberInBox()

    strat.process_board(sboard)

    general_cell = SudokuCell()
    box1 = [general_cell] * 9
    box1 = tuple(box1)

    general_cell = SudokuCell()
    general_cell -= (1, 6, 7, 8, 9)
    box2 = [general_cell] * 9
    box2[0] = SudokuCell(potential_values=6)
    box2[1] = SudokuCell(potential_values=1)
    box2[3] = SudokuCell(potential_values=9)
    box2[5] = SudokuCell(potential_values=7)
    box2[7] = SudokuCell(potential_values=8)
    box2 = tuple(box2)

    general_cell = SudokuCell()
    general_cell -= (2, 7, 8, 9)
    box3 = [general_cell] * 9
    box3[0] = SudokuCell(potential_values=8)
    box3[2] = SudokuCell(potential_values=7)
    box3[7] = SudokuCell(potential_values=2)
    box3[8] = SudokuCell(potential_values=9)
    box3 = tuple(box3)

    general_cell = SudokuCell()
    general_cell -= (3, 5, 6, 7, 8)
    box4 = [general_cell] * 9
    box4[2] = SudokuCell(potential_values=3)
    box4[5] = SudokuCell(potential_values=7)
    box4[6] = SudokuCell(potential_values=6)
    box4[7] = SudokuCell(potential_values=5)
    box4[8] = SudokuCell(potential_values=8)
    box4 = tuple(box4)

    general_cell = SudokuCell()
    general_cell -= (1, 3)
    box5 = [general_cell] * 9
    box5[3] = SudokuCell(potential_values=3)
    box5[5] = SudokuCell(potential_values=1)
    box5 = tuple(box5)

    general_cell = SudokuCell()
    general_cell -= (2, 4, 5, 7, 9)
    box6 = [general_cell] * 9
    box6[0] = SudokuCell(potential_values=2)
    box6[1] = SudokuCell(potential_values=5)
    box6[2] = SudokuCell(potential_values=4)
    box6[3] = SudokuCell(potential_values=9)
    box6[6] = SudokuCell(potential_values=7)
    box6 = tuple(box6)

    general_cell = SudokuCell()
    general_cell -= (3, 4, 5, 9)
    box7 = [general_cell] * 9
    box7[0] = SudokuCell(potential_values=3)
    box7[1] = SudokuCell(potential_values=4)
    box7[6] = SudokuCell(potential_values=5)
    box7[8] = SudokuCell(potential_values=9)
    box7 = tuple(box7)

    general_cell = SudokuCell()
    general_cell -= (1, 3, 4, 9)
    box8 = [general_cell] * 9
    box8[1] = SudokuCell(potential_values=9)
    box8[3] = SudokuCell(potential_values=1)
    box8[5] = SudokuCell(potential_values=3)
    box8[8] = SudokuCell(potential_values=4)
    box8 = tuple(box8)

    general_cell = SudokuCell()
    box9 = [general_cell] * 9
    box9 = tuple(box9)

    assert sboard.boxes == (
        box1,
        box2,
        box3,
        box4,
        box5,
        box6,
        box7,
        box8,
        box9,
    )


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

    strat = strategy.OnlyInRow()

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

    strat = strategy.OnlyInColumn()

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

    strat = strategy.OnlyInBox()

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


def test_load_strategies():
    strategies = strategy.load_strategies()

    assert len(strategies) >= 1
    assert len(strategies) == len([s for s in strategies if isinstance(s, strategy.Strategy)])
