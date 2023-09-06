#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangle:
    """This class defines a rectangle
        Args:
            width:
            height:


    """
    def __init__(self, width=0, height=0):
        """Instantiates rectangle objects"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width of rectangle object"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """sets the width of rectangle object"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrieves the height of rectangle object"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """sets the height of rectangle object"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of rectangle object"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns perimeter of rectangle object"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """prints rectangle object with character #"""
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for column in range(self.__height):
            for row in range(self.__width):
                rectangle_str += "#"
            if column != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str
