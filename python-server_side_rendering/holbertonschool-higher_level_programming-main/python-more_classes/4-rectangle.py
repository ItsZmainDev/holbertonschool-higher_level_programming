#!/usr/bin/python3
"""Defines a class Rectangle"""


class Rectangle:
    """Defines a class Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize a new rectangle

        Args:
            width (int): width of rectangle
            height (int): height of rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for width

        Returns:
            int: Width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width

        Args:
            value (int): The width value to set

        Raises:
            TypeError: If width is not an integer
            ValueError: If width if less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height

        Returns:
            int: Height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height

        Args:
            value (int): The height value to set

        Raises:
            TypeError: If height is not an integer
            ValueError: if height is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Method to return the area

        Returns:
            int: Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Method to return the perimeter
        Returns:
            int: Perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Print a rectangle"""
        if self.__width == 0 or self.__height == 0:
            print()
            return
        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        """Return a string representation of the rectangle
        to be able to recreate a new instance"""
        return "Rectangle({}, {})".format(self.__width, self.__height)
