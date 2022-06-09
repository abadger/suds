import json
import sys

from . import testdata
from suds import cli


def test_main(monkeypatch, tmpdir):
    tmpsavefile = tmpdir / 'save.json'
    with open(tmpsavefile, 'w') as f:
        f.write(json.dumps({'board': {'rows': testdata.GOOD_DATA['board']['rows']}}))

    monkeypatch.setattr(sys, 'argv', ['--filename', str(tmpsavefile)])

    assert cli.main() == 0
