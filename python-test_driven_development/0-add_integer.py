#!/usr/bin/python3
"""
Module function to add two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats (floats are cast to integers).

    Args:
        a: First number (int or float)
        b: Second number (int or float, default = 98)

    Returns:
        int: The sum of a and b after casting to integers

    Raises:
        TypeError: If a or b is not an int or float
        ValueError: If a or b is NaN or infinity
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float) and a != a:
        raise ValueError("a must be a finite number")
    if isinstance(b, float) and b != b:
        raise ValueError("b must be a finite number")
    if isinstance(a, float) and (a == float('inf') or a == -float('inf')):
        raise ValueError("a must be a finite number")
    if isinstance(b, float) and (b == float('inf') or b == -float('inf')):
        raise ValueError("b must be a finite number")
    return int(a) + int(b)
