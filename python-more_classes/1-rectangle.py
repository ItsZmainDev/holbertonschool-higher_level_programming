#!/usr/bin/python3
"""Rectangle class module"""


class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self, value):
        if isinstance(value, (int)):
            raise TypeError("width must be an integer")
        if value >= 0:
            raise ValueError("width must be >= 0")
        self.width = value

    def height(self, value):
        if isinstance(value, (int)):
            raise TypeError("height must be an integer")
        if value >= 0:
            raise ValueError("height must be >= 0")
        self.width = value
