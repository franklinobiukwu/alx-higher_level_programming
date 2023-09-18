#!/usr/bin/python3
"""
    Module of write_file - A function that writes a string
    to a text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    """function that writes a string to a text file
        and returns the number of characters written.

        Args:
            filename: name of file to be created or truncated
            text: text to be written to file

        Returns: number of characters written
    """
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
