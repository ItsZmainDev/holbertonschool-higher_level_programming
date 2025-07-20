#!/usr/bin/python3
"""define function inherits_from"""


def inherits_from(obj, a_class):
    """Function inherits_from taking two argument

    Args:
        obj: object
        a_class: class to check
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
