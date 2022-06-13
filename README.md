# Suds

[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/abadger/suds/main.svg)](https://results.pre-commit.ci/latest/github/abadger/suds/main)
[![Coverage](https://github.com/abadger/suds/actions/workflows/coverage.yml/badge.svg)](https://github.com/abadger/suds/actions/workflows/coverage.yml)
[![codecov](https://codecov.io/gh/abadger/suds/branch/main/graph/badge.svg?token=GD9HJBEQSM)](https://codecov.io/gh/abadger/suds)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/abadger/suds.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/abadger/suds/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/abadger/suds.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/abadger/suds/context:python)
[![Code Scanning - Action](https://github.com/abadger/suds/actions/workflows/codeql.yml/badge.svg)](https://github.com/abadger/suds/actions/workflows/codeql.yml)

A *sud*oku *s*olver

<!-- TOC -->

## Overview

Suds is a simple sudoku solver.  It doesn't aim to be the fastest or best.
Don't expect it to be able to solve anything but the easiest sudokus.  Suds
really exists for me to play around with Python, how to setup the
infrastructure around a Python application, and so forth.  It's a playground
for me to learn rather than a best of breed solver.

## Usage

```bash
git clone git@github.com:abadger/suds.git
cd suds
python -m suds FILENAME.json
```

`FILENAME.json` contains a json data structure with a sudoku board.  It should
look something like this:

``` json
{"board":
    {"rows":
        [
            [0, 0, 7, 0, 0, 0, 0, 0, 6],
            [0, 6, 0, 8, 0, 0, 2, 0, 5],
            [0, 0, 8, 0, 6, 9, 3, 0, 0],
            [7, 0, 6, 0, 3, 8, 1, 0, 0],
            [4, 8, 9, 0, 1, 0, 7, 6, 3],
            [0, 0, 3, 9, 7, 0, 5, 0, 8],
            [0, 0, 5, 6, 8, 0, 4, 0, 0],
            [8, 0, 4, 0, 0, 7, 0, 5, 0],
            [6, 0, 0, 0, 0, 0, 9, 0, 0]
        ]
    }
}
```

If suds is able to solve the Sudoku puzzle, it will print out the solution and
exit with code 0:

``` console
The solution is:

3 4 7 5 2 1 8 9 6
9 6 1 8 4 3 2 7 5
5 2 8 7 6 9 3 1 4
7 5 6 4 3 8 1 2 9
4 8 9 2 1 5 7 6 3
2 1 3 9 7 6 5 4 8
1 9 5 6 8 2 4 3 7
8 3 4 1 9 7 6 5 2
6 7 2 3 5 4 9 8 1
```

If it can't, it will print a message and as much of the board as it was able to
fill in.  In this case, its exit code will be 1.
