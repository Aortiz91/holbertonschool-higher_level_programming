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

    def to_json(self, attrs=None):
        """Public method that retrieves the dictionary description with simple
        data structure for JSON serialization of an object.

        Args:
            -attrs: If is a list of strings, only attribute
            names contained in this list must be retrieved. Otherwise, all
            attributes must be retrieved

        Returns: Dicctionary representation of a Student instance
        """
        if attrs is None:
            return self.__dict__
        else:
            new_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    new_dict[i] = getattr(self, i)
            return new_dict
        return self.__dict__
