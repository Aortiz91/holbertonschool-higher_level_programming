#!/usr/bin/python3
"""function that returns True if the object is an instance of, or if the object
is an instance of a class that inherited from, the specified class;
otherwise False.
"""


def inherits_from(obj, a_class):
    """Determine if an object is instance of a_class that inherited
    from the a_class

    Args:
        -obj: Object to evaluate
        -a_class: Class to determine

    Returns: True if obj is instance of a_class or False otherwise."""

    return issubclass(type(obj), a_class) and type(obj) != a_class
