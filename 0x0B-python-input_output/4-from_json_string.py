#!/usr/bin/python3
"""Function that returns an object (Python data structure) represented
by a JSON string
"""


import json


def from_json_string(my_str):
    """ json.load() loads a JSON formatted file and returns
            a Python dictionary >object.
        json.loads() returns a Python dictionary object from
            a JSON formatted string.
        json.dump() returns a JSON formatted file from
            a Python dictionary object
        json.dumps() returns a JSON formatted string from
            a Python dictionary object


    Args:
        - my_str: JSON string to be represented as a Python object

    Returns: a Python object
    """

    return json.loads(my_str)
