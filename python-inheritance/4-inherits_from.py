#!/usr/bin/python3
"""Inherits From function module"""


def inherits_from(obj, a_class):
    """Check if object is an instance of class that inherited from a class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
