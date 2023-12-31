#!/usr/bin/python3
"""A Rectangle class that defines a rectangle"""


class Rectangle:
    """This is a rectangle class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize instance of class with width attribute
            Args:
                width: represents the width of a rectangle
                height: represents the height of a rectangle
            Raises:
                TypeError: if width or height is not an integer
                ValueError: if width or height is less that zero
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """method that gets the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """method that sets the width of rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """method that gets the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """method that sets the height of rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
