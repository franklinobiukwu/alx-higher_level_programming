#!/usr/bin/python3
"""Module that defines function that adds attribute to object if possible"""


def add_attribute(obj, attribute, value):
    """Function that adds new attribute to object if possible"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
