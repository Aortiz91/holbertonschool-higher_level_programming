#!/usr/bin/python3
"""Function that creates an Object from a "JSON file"
"""


import json


def load_from_json_file(filename):
    """ json.load() loads a JSON formatted file and returns


    Args:
        - filenanme: JSON file to be converted to python obj
    """

    with open(filename, 'r') as f:
        return json.load(f)
