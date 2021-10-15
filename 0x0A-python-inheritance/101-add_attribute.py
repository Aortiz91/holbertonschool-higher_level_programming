#!/usr/bin/python3
"""Function that adds an attribute to an instance if possible"""


def add_attribute(obj, name, value):
    """Addts attribute

    Args:
        -obj: name of the object instance
        -name: name of the attribute
        -value: value of the attribute to set
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
