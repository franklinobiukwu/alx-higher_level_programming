#!/usr/bin/python3

"""This module defines a Square class"""


class Square:
    """A Square class that sets a square"""

    def __init__(self, size=0):
        """Magic function that initializes this class
        Args:
            size: the size of the square
        Raises:
            TypeError: if the size is not an integer
            ValueError: if the size is less than zero
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size
