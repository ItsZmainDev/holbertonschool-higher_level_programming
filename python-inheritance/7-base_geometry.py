#!/usr/bin/python3
"""Base Geometry class module"""


class BaseGeometry:
    """Base Geometry class"""
    def area(self):
        """raises an Exception with the message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function that validates value"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0") 
