#!/usr/bin/python3
"""Function that returns the JSON representation of an object (string)
"""


import json


def to_json_string(my_obj):
    """ json.load() loads a JSON formatted file and returns
            a Python dictionary >object.
        json.loads() returns a Python dictionary object from
            a JSON formatted string.
        json.dump() returns a JSON formatted file from
            a Python dictionary object
        json.dumps() returns a JSON formatted string from
            a Python dictionary object


    Args:
        - my_obj: object to reprensent as JSON

    Returns: A JSON formatted string from a Python dictionary object
    """

    return json.dumps(my_obj)
