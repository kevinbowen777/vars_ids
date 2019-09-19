# vars_ids()

## Installation #

    git clone git://github.com/kevinbowen777/vars_ids.git

## Description #

    Python module used to filter out globals and dunder methods and print
	local variables, their values, and ids.

	This module was originally used in PyCon 2019 - Python by Immersion
	video - https://pyvideo.org/pycon-us-2019/python-by-immersion.html

## Usage #
In IPython:
    [22]: %load vars_ids.py

    [23]: _vars_ids()
    'name        value              id'
    '----        -----              --'
    'matrix      [[1, 2, 3          140021322106184'
    "animal      'wombat'           140021326025928"
    "people      {'name':           140021336068384"
    'counter     42.394             140021323417376'

## License #
The original PyCon 2019 Python by Immersion Tutorial by Stuart Williams is licensed under a [Creative
Commons Attribution-Share Alike 2.5 Canada License](http://creativecommons.org/licenses/by-sa/2.5/ca/)
