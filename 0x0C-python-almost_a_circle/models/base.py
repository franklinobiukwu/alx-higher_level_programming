#!/usr/bin/python3
"""Module of Base class"""
import json


class Base:
    """This is the base class for all classes in this project.
        It manages the id attribution in all other classes in
        this project and helps avoid code duplication.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """returns the JSON string representation"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
