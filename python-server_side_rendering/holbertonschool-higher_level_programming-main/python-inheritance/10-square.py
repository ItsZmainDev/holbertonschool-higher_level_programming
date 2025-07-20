#!/usr/bin/python3
"""Define a Class Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a class Square that inherit from rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return self.__size * self.__size
