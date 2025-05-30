#!/usr/bin/python3
"""Is Kind Of Class function module"""


def is_kind_of_class(obj, a_class):
    """Check if object is an instance or an instance of a subclass"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
