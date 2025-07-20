#!/usr/bin/python3
"""Define function is_same_class"""


def is_same_class(obj, a_class):
    """Function is_same_class take two argument

    Args:
        obj: Object
        a_class: Class to check the type"""
    if type(obj) is a_class:
        return True
    else:
        return False
