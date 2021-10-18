#!/usr/bin/python3
""" Will create a class base for all other classes"""

import json


class Base():
    """Define a class Base"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor that receives id

        Args:
            - id: instance id"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Static method that returns the JSON string representation
        of a list of dictionaries"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation of
        list_objs to a file""" 
