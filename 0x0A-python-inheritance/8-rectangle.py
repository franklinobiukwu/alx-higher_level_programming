#!/usr/bin/python3
"""Module that contains a class that raises an exception"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """This is a class that raises an exception"""

    def __init__(self, width, height):
        """Initialize rectangle instances"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
