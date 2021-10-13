#!/usr/bin/python3
"""Function that  that writes an Object to a text file, using
    a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """ json.load() loads a JSON formatted file and returns


    Args:
        - my_obj: Object to be writted from
        - filenanme: file to be written
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
