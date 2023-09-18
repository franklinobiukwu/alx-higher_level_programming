#!/usr/bin/python3
"""Module of read_file - A function that reads a text file and
    prints it to stdout.
"""


def read_file(filename=""):
    """function that prints the content of a text file

        Args:
            filename: name of file
    """
    with open(filename, "r", encoding="utf-8") as file:
        print(file.read(), end="")
