#!/usr/bin/python3
"""File writing module"""


def class_to_json(obj):
    """Return the dictionary description with simple data structure"""

    return obj.__dict__
