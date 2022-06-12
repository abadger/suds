"""
Data that multiple tests can use.
"""
import copy
import json
import typing as t

if t.TYPE_CHECKING:  # pragma: no cover
    # Could use later but currently just boilerplate to make flake8 happy about importing typing
    pass

GOOD_DATA = {
    'board': {
        'rows': [
            [0, 0, 7, 0, 0, 0, 0, 0, 6],
            [0, 6, 0, 8, 0, 0, 2, 0, 5],
            [0, 0, 8, 0, 6, 9, 3, 0, 0],
            [7, 0, 6, 0, 3, 8, 1, 0, 0],
            [4, 8, 9, 0, 1, 0, 7, 6, 3],
            [0, 0, 3, 9, 7, 0, 5, 0, 8],
            [0, 0, 5, 6, 8, 0, 4, 0, 0],
            [8, 0, 4, 0, 0, 7, 0, 5, 0],
            [6, 0, 0, 0, 0, 0, 9, 0, 0],
        ]
    }
}

GOOD_DATA_JSON = json.dumps(GOOD_DATA)

BAD_DATA = {
    'board': {
        'rows': [
            [7, 0, 7, 0, 0, 0, 0, 0, 6],
            [0, 6, 0, 8, 0, 0, 2, 0, 5],
            [0, 0, 8, 0, 6, 9, 3, 0, 0],
            [7, 0, 6, 0, 3, 8, 1, 0, 0],
            [4, 8, 9, 0, 1, 0, 7, 6, 3],
            [0, 0, 3, 9, 7, 0, 5, 0, 8],
            [0, 0, 5, 6, 8, 0, 4, 0, 0],
            [8, 0, 4, 0, 0, 7, 0, 5, 0],
            [6, 0, 0, 0, 0, 0, 9, 0, 0],
        ]
    }
}

BAD_DATA_JSON = json.dumps(BAD_DATA)

BLANK_BOARD_DATA: t.List[t.List[int]] = [[0] * 9 for _c in range(0, 9)]

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
ONE_EACH_BOARD_BOXES_DATA[7][5] = 8
ONE_EACH_BOARD_BOXES_DATA[8][8] = 9
