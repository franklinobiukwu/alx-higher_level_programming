#!/usr/bin/python3
"""
    Module of write_file - A function that writes a string
    to a text file and returns the number of characters written.
"""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
