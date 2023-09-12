#!/usr/bin/python3
"""Module of MyInt class that inherits from int"""


class MyInt(int):
    """class that invert in operators == and !="""

    def __eq__(self, value):
        """function that sets == operator to !="""
        return self.real != value

    def __ne__(self, value):
        """function that sets != operator to =="""
        return self.real == value
