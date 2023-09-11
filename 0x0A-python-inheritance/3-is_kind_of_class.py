#!/usr/bin/python3
"""Module of function that returns True if the object is an instance
of, or if the object is an instance of a class that inherites from the
specified class; otherwise False"""


def is_kind_of_class(obj, a_class):
    """function that returns True if object is am instance of a class
    or if the object is an instance of a class that inherites from the
    specified class"""
    if isinstance(obj, a_class):
        return True
    return False
