#!/usr/bin/python3
"""Is Same Class function module"""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a specified class"""
    if type(obj) is a_class:
        return True
    else:
        return False
