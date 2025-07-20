#!/usr/bin/python3
"""defines a class Square with area"""


class Square:
    """Square class with private size attribute and area computation"""
    def __init__(self, size=0):
        self.size = size

    def size(self, value):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Return the current square area"""
        return self.__size * self.__size
