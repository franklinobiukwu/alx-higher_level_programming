#!/usr/bin/python3
from models.base import Base

"""Model for rectangle class"""


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize instances of class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """return Rectangle width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Set Rectangle width"""
        self.__width = width

    @property
    def height(self):
        """return Rectangle height"""
        return self.__height

    @height.setter
    def height(self, height):
        """set Rectangle height"""
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
