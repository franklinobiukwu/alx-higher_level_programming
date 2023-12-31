#!/usr/bin/python3
"""This module contains a function that returns True if the object is
an instance of a class that inherited (directly or indirectly) from
the specified class ; otherwise False"""


def inherits_from(obj, a_class):
    """Return True if object is an instance of a class that
    is inherited (directly or indirectly) from the specified class"""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    return False
