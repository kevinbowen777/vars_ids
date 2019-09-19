#!/usr/bin/env python3

# {{{ ------------------------------------------------------------------- #
#
# Name: vars_ids.py
# Purpose: This script displays active local variables and their values
# Compatible:
# Requirements:
#
# Version: 0.1.0
# Author: Kevin Bowen <kevin.bowen@gmail.com>
#
# Original source:
# Updated: 20190918
#
# }}} ------------------------------------------------------------------- #


import pprint
__all__ = ['_vars_ids']
_CLUTTER = globals().copy()
def _vars_ids():
    """
    Show names, values, and ids, ignoring any existing names.
    """
    rows = [(key, repr(value), id(value))
            for key, value in globals().items()
            if key not in _CLUTTER and not key.startswith('_')]
    titles = ['name    value  id'.split(),
              '----    -----  --'.split()]
    for name, value, id_ in titles + rows:
        print('{:8.8}  {:8.8}  {}'.format(name, value, id_))
