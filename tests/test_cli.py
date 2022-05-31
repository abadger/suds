import json
import sys

from suds import cli

good_data = [
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


def test_main(monkeypatch, tmpdir):
    tmpsavefile = tmpdir / 'save.json'
    with open(tmpsavefile, 'w') as f:
        f.write(json.dumps({'board': {'rows': good_data}}))

    monkeypatch.setattr(sys, 'argv', ['--filename', str(tmpsavefile)])

    assert cli.main() == 0
