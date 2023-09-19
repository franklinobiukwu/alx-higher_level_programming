#!/usr/bin/python3

"""Module for rectangle class: Defines attributes and
    methods of a rectangle.
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class. Extends the Base class. Contains attributes
        and methods for rectangle instances."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances of class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return the value of Rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set the value of Rectangle width"""
        self.__width = width

    @property
    def height(self):
        """return the value of Rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set the value of Rectangle height"""
        self.__height = height

    @property
    def x(self):
        """return the value of x"""
        return self.__x

    @x.setter
    def x(self, x):
        """set the value of x"""
        self.__x = x

    @property
    def y(self):
        """return the value of y"""
        return self.__y

    @y.setter
    def y(self, y):
        """set the value of y"""
        self.__y = y
