#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """A class that defines a rectangle
        Args:
            width: represnts the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError:
            ValueError:
    """
    def __init__(self, width=0, height=0):
        """method that initializes instances of rectangle class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieves the width of rectangle object"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width of rectangle object"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """retrieves the height of rectangle"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height of rectangle"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """method that returns the area of a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """method that returns the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)
