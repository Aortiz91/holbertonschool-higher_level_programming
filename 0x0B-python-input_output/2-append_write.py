#!/usr/bin/python3
"""Function that appends a string at the end of a text file (UTF8)
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """Appends a text into filename


    Args:
        - filename: Name of the file to be written
        - text: text to write

    Returns: Total number of characters written
    """

    with open(filename, 'a') as f:
        return f.write(text)
