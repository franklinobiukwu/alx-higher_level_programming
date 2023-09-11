#!/usr/bin/python3
"""Module that returns True if object is exactly an instance
of the specified class"""


def is_same_class(obj, a_class):
    """Function that returns True id object is an
    instance of the specified class"""
    if type(obj) == a_class:
        return True
    return False
