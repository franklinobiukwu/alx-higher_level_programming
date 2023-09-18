#!/usr/bin/python3
"""Module of to_json_string - A function that returns
    the JSON representation of an object (string)
"""
import json


def to_json_string(my_obj):
    """A function that returns the JSON representation
        of an object (string)

        Args:
            my_obj: object (string) to be converted to JSON

        Returns:
            JSON representation of my_obj
    """
    return json.dumps(my_obj)
