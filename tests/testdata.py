"""
Data that multiple tests can use.
"""
import copy
import json
import typing as t

if t.TYPE_CHECKING:  # pragma: no cover
    # Could use later but currently just boilerplate to make flake8 happy about importing typing
    pass

EASY_DATA = {
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

EASY_DATA_JSON = json.dumps(EASY_DATA)

EASY_DATA_OUTPUT = '\n'.join((
    '    7           6',
    '  6   8     2   5',
    '    8   6 9 3    ',
    '7   6   3 8 1    ',
    '4 8 9   1   7 6 3',
    '    3 9 7   5   8',
    '    5 6 8   4    ',
    '8   4     7   5  ',
    '6           9    ',
))

EASY_DATA_SOLVED = (
    (3, 4, 7, 5, 2, 1, 8, 9, 6),
    (9, 6, 1, 8, 4, 3, 2, 7, 5),
    (5, 2, 8, 7, 6, 9, 3, 1, 4),
    (7, 5, 6, 4, 3, 8, 1, 2, 9),
    (4, 8, 9, 2, 1, 5, 7, 6, 3),
    (2, 1, 3, 9, 7, 6, 5, 4, 8),
    (1, 9, 5, 6, 8, 2, 4, 3, 7),
    (8, 3, 4, 1, 9, 7, 6, 5, 2),
    (6, 7, 2, 3, 5, 4, 9, 8, 1),
)

EASY_DATA_SOLVED_OUTPUT = '\n'.join((
    '3 4 7 5 2 1 8 9 6',
    '9 6 1 8 4 3 2 7 5',
    '5 2 8 7 6 9 3 1 4',
    '7 5 6 4 3 8 1 2 9',
    '4 8 9 2 1 5 7 6 3',
    '2 1 3 9 7 6 5 4 8',
    '1 9 5 6 8 2 4 3 7',
    '8 3 4 1 9 7 6 5 2',
    '6 7 2 3 5 4 9 8 1',
))

EXTREME_DATA = {
    'board': {
        'rows': [
            [0, 8, 0, 0, 0, 6, 0, 0, 0],
            [5, 0, 0, 8, 7, 0, 3, 0, 0],
            [0, 0, 0, 0, 0, 4, 0, 7, 0],
            [0, 4, 0, 2, 1, 0, 0, 3, 0],
            [0, 0, 9, 0, 0, 0, 5, 0, 0],
            [0, 0, 0, 0, 0, 7, 0, 0, 0],
            [0, 0, 0, 6, 0, 0, 0, 0, 0],
            [0, 2, 0, 3, 8, 0, 0, 1, 0],
            [4, 0, 0, 0, 0, 0, 0, 0, 2],
        ]
    }
}

EXTREME_DATA_JSON = json.dumps(EXTREME_DATA)

EXTREME_DATA_OUTPUT = '\n'.join((
    '  8       6      ',
    '5     8 7   3    ',
    '          4   7  ',
    '  4   2 1     3  ',
    '    9       5    ',
    '          7      ',
    '      6          ',
    '  2   3 8     1  ',
    '4               2',
))

EXTREME_DATA_SOLVED = (
    (7, 8, 4, 1, 3, 6, 2, 9, 5),
    (5, 6, 2, 8, 7, 9, 3, 4, 1),
    (3, 9, 1, 5, 2, 4, 8, 7, 6),
    (6, 4, 5, 2, 1, 8, 7, 3, 9),
    (1, 7, 9, 4, 6, 3, 5, 2, 8),
    (2, 3, 8, 9, 5, 7, 1, 6, 4),
    (8, 1, 7, 6, 4, 2, 9, 5, 3),
    (9, 2, 6, 3, 8, 5, 4, 1, 7),
    (4, 5, 3, 7, 9, 1, 6, 8, 2),
)

EXTREME_DATA_SOLVED_OUTPUT = '\n'.join((
    '7 8 4 1 3 6 2 9 5',
    '5 6 2 8 7 9 3 4 1',
    '3 9 1 5 2 4 8 7 6',
    '6 4 5 2 1 8 7 3 9',
    '1 7 9 4 6 3 5 2 8',
    '2 3 8 9 5 7 1 6 4',
    '8 1 7 6 4 2 9 5 3',
    '9 2 6 3 8 5 4 1 7',
    '4 5 3 7 9 1 6 8 2',
))

WITH_BLANK_UNIT_DATA = {
    'board': {
        'rows': [
            [0, 0, 0, 6, 1, 0, 8, 0, 7],
            [0, 0, 0, 9, 0, 7, 0, 0, 0],
            [0, 0, 0, 0, 8, 0, 0, 2, 9],
            [0, 0, 3, 0, 0, 0, 2, 5, 4],
            [0, 0, 7, 3, 0, 1, 9, 0, 0],
            [6, 5, 8, 0, 0, 0, 7, 0, 0],
            [3, 4, 0, 0, 9, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 3, 0, 0, 0],
            [5, 0, 9, 0, 0, 4, 0, 0, 0],
        ]
    }
}

WITH_BLANK_UNIT_DATA_JSON = json.dumps(WITH_BLANK_UNIT_DATA)

WITH_BLANK_UNIT_DATA_OUTPUT = '\n'.join((
    '      6 1   8   7',
    '      9   7      ',
    '        8     2 9',
    '    3       2 5 4',
    '    7 3   1 9    ',
    '6 5 8       7    ',
    '3 4     9        ',
    '      1   3      ',
    '5   9     4      ',
))

WITH_BLANK_UNIT_DATA_SOLVED = (
    (7, 8, 4, 1, 3, 6, 2, 9, 5),
    (5, 6, 2, 8, 7, 9, 3, 4, 1),
    (3, 9, 1, 5, 2, 4, 8, 7, 6),
    (6, 4, 5, 2, 1, 8, 7, 3, 9),
    (1, 7, 9, 4, 6, 3, 5, 2, 8),
    (2, 3, 8, 9, 5, 7, 1, 6, 4),
    (8, 1, 7, 6, 4, 2, 9, 5, 3),
    (9, 2, 6, 3, 8, 5, 4, 1, 7),
    (4, 5, 3, 7, 9, 1, 6, 8, 2),
)

WITH_BLANK_UNIT_DATA_SOLVED_OUTPUT = '\n'.join((
    '7 8 4 1 3 6 2 9 5',
    '5 6 2 8 7 9 3 4 1',
    '3 9 1 5 2 4 8 7 6',
    '6 4 5 2 1 8 7 3 9',
    '1 7 9 4 6 3 5 2 8',
    '2 3 8 9 5 7 1 6 4',
    '8 1 7 6 4 2 9 5 3',
    '9 2 6 3 8 5 4 1 7',
    '4 5 3 7 9 1 6 8 2',
))

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
