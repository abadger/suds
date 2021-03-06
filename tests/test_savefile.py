import io

from . import testdata
from suds import savefile


def test_load_save_file_filename(tmpdir):
    tmpsavefile = tmpdir / 'save.json'
    with open(tmpsavefile, 'w', encoding='utf-8') as f:
        f.write(testdata.EASY_DATA_JSON)

    assert savefile.load_save_file(tmpsavefile) == testdata.EASY_DATA


def test_load_save_file_file_obj():
    file_obj = io.StringIO(testdata.EASY_DATA_JSON)

    assert savefile.load_save_file(file_obj) == testdata.EASY_DATA
