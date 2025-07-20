#!/usr/bin/python3
"""Look up function"""


def lookup(obj):
    """ function that returns the list of available attributes
    and methods of an object

    Args:
        obj: Object
    """
    return dir(obj)
