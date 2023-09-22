#!/usr/bin/python3
"""Module for Square class that inherits from Rectangle class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initiatializes class attribute"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """returns the size of the square"""
        return self.width

    @size.setter
    def size(self, value):
        """set square size"""
        self.width = value
        self.height = value
