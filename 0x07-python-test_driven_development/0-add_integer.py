#!/usr/bin/python3
"""This module contains a function that adds two integers"""


def add_integer(a, b=98):
    """Function that returns the sum of two integer

        Args:
            a: first argument
            b: second argument

        Returns:
            sum of a and b

        Raises:
            TypeError: if either a or b is not an integer of a float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
