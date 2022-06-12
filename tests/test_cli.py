import json
import sys

import pytest

from . import testdata
from suds import cli


@pytest.mark.parametrize('board_data, expected_output',
                         ((testdata.EASY_DATA['board']['rows'], testdata.EASY_DATA_SOLVED_OUTPUT), )
                         )
def test_main_solved(board_data, expected_output, monkeypatch, tmpdir, capsys):
    tmpsavefile = tmpdir / 'save.json'
    with open(tmpsavefile, 'w') as f:
        f.write(json.dumps({'board': {'rows': board_data}}))

    monkeypatch.setattr(sys, 'argv', ['--filename', str(tmpsavefile)])

    ret_code = cli.main()
    output = capsys.readouterr().out

    assert ret_code == 0
    assert expected_output in output


@pytest.mark.parametrize('board_data, expected_output', (
    (testdata.EXTREME_DATA['board']['rows'], testdata.EXTREME_DATA_SOLVED_OUTPUT),
    (testdata.WITH_BLANK_UNIT_DATA['board']['rows'], testdata.WITH_BLANK_UNIT_DATA_SOLVED_OUTPUT),
))
def test_main_unsolved(board_data, expected_output, monkeypatch, tmpdir, capsys):
    tmpsavefile = tmpdir / 'save.json'
    with open(tmpsavefile, 'w') as f:
        f.write(json.dumps({'board': {'rows': board_data}}))

    monkeypatch.setattr(sys, 'argv', ['--filename', str(tmpsavefile)])

    ret_code = cli.main()
    output = capsys.readouterr().out

    assert ret_code == 1
    assert 'I was not smart enough to solve this sudoku' in output
    assert expected_output not in output
