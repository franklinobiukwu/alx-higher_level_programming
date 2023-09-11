#!/usr/bin/python3
"""Demonstrating class inheritance"""


class MyList(list):
    """Class that inherits list"""
    def print_sorted(self):
        """Function that prints elemets of a list in,
        sorted in ascending order"""
        print(sorted(self))
