#!/usr/bin/python3
""" Will create a class base for all other classes"""


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
