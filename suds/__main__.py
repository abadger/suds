# Suds -- A sudoku solver
# Copyright: (C) 2022  Toshio Kuratomi
# License: AGPL-3.0-or-later
# See the LICENSE file for more details
"""The main entrypoint for suds."""
# pylint bug: https://github.com/PyCQA/pylint/issues/3624
from .cli import main  # pylint: disable=relative-beyond-top-level

if __name__ == "__main__":
    main()
