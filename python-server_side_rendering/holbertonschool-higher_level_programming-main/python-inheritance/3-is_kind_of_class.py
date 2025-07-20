#!/usr/bin/python3
"""Define a function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Function is_kind_of_class taking two arguement

    Args:
        obj: Object to check
        a_class: The instance to check"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
