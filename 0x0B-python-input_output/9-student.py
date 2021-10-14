#!/usr/bin/python3
"""Functon that creates a class Student"""


class Student:
    """Creates the class Student"""

    def __init__(self, first_name, last_name, age):
        """Constructor

        Args:
            -first_name: given arguments
            -last_name: given arguments
            -age: given arguments
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Public method that retrieves the dictionary description with simple
        data structure for JSON serialization of an object.

        Returns: Dicctionary representation of a Student instance
        """
        return self.__dict__
