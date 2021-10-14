#!/usr/bin/python3
"""Function that returns the dictionary description with simple data structure
(list, dictionary, string, integer and boolean) for JSON serialization of
an object
"""


import json


def class_to_json(obj):
    """ Createds dictionary description of a specified object

    Args:
        - obj: Instance of a Class

    Returns: Diccionary description of the object
    """
    return obj.__dict__
