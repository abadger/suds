# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""Savefile routines for suds."""
import typing as t

import pydantic as p


# pylint: disable=too-few-public-methods
class LocalConfig:
    """Settings for all of our models."""
    extra = p.Extra.forbid


class BaseModel(p.BaseModel):
    """BaseModel with our preferred default configuration."""
    Config = LocalConfig


class BoardSchema(BaseModel):
    """Structure defining a sudoku board."""
    # 9 rows of 9 items containing 0 (meaning the cell is blank) through 9
    rows: p.conlist(
        p.conlist(p.conint(gt=-1, lt=10), min_items=9, max_items=9), min_items=9, max_items=9)


class SaveFileSchema(BaseModel):
    """
    Defines the sructure of a savefile.

    .. note:: This is a mapping rather than a list for potential future expansion.
    """
    board: BoardSchema


# pylint: enable=too-few-public-methods


def load_save_file(file: t.Union[str, t.TextIO]) -> SaveFileSchema:
    """
    Load a SudokBoard from a savefile.

    :arg file: This can be a fle name or a file-like object.
    """
    if isinstance(file, str):
        save_file_data = SaveFileSchema.parse_file(file)
    else:
        save_file_data = SaveFileSchema.parse_raw(file.read())

    return save_file_data
