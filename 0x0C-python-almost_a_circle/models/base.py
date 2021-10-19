#!/usr/bin/python3
""" Will create a class base for all other classes"""

import json
import os


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

    @classmethod
    def save_to_file(cls, list_objs):
        """Class method that writes the JSON string representation of
        list_objs to a file"""

        if list_objs is None or list_objs == []:
            list_objs = "[]"
        else:
            list_objs = [i.to_dictionary() for i in list_objs]
            filename = cls.__name__ + '.json'
            with open(filename, 'w') as jsonfile:
                jsonfile.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """ Static method that returns the list of the JSON string
        representation json_string"""

        if json_string is None or json_string == '':
            emptylist = []
            return emptylist
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.
        """

        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Class method that returns a list of instances."""

        filename = cls.__name__ + ".json"
        listofinst = []
        list_dicts = []
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                list_dicts = cls.from_json_string(f.read())
                for dictionaries in list_dicts:
                    listofinst.append(cls.create(**dictionaries))
        return listofinst
