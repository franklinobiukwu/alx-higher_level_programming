#!/usr/bin/python3
"""A Rectangle class that defines a rectangle"""


class Rectangle:
    """This is a rectangle class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize instance of class with width attribute"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """method that gets the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, width):
        """method that sets the width of rectangle"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """method that gets the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """method that sets the height of rectangle"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
