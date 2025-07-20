#!/usr/bin/python3
"""Defines a class Square with size and area"""


class Square:
    """Square class with private size attribute and area computation"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the current square area"""
        return self.__size * self.__size
