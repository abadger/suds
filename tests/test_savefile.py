import io
import json

from suds import savefile

good_data = {
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

good_data_json = json.dumps(good_data)


def test_load_save_file_filename(tmpdir):
    tmpsavefile = tmpdir / 'save.json'
    with open(tmpsavefile, 'w', encoding='utf-8') as f:
        f.write(good_data_json)

    assert savefile.load_save_file(tmpsavefile) == good_data


def test_load_save_file_file_obj():
    file_obj = io.StringIO(good_data_json)

    assert savefile.load_save_file(file_obj) == good_data
