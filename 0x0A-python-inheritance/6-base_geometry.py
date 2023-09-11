#!/usr/bin/python3
"""Module that contains a class that raises an exception"""


class BaseGeometry:
    """This is a class that raises an exception"""
    def area(self):
        raise Exception("area() is not implemented")
