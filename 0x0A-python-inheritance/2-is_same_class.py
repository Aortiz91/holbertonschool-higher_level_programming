#!/usr/bin/python3
""" Function that returns True if the object is exactly an instance of
the specified class, otherwise False
"""


def is_same_class(obj, a_class):
    """Determine if an object is instance of a_class

    Args:
        -obj: Object to evaluate
        -a_class: Class to determine

    Returns: True if obj is instance of a_class or False otherwise."""
    return (True if type(obj) is a_class else False)
