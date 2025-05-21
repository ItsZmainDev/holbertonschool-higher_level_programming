#!/usr/bin/python3
"""Define a Square class with are"""


class Square:
    """Square class with private size attribute and area computation"""
    def __init__(self, size=0):
        self.size = size

    def size(self, value):
        """Set size value"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return square area"""
        return self.__size * self.__size
