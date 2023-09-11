#!/usr/bin/python3
"""Module that contains a class that raises an exception"""


class BaseGeometry:
    """This is a class that raises an exception"""
    def area(self):
        """Method that raises exception"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
