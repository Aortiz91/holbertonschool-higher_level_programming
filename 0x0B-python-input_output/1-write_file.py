#!/usr/bin/python3
"""Function that writes a string to a text file (UTF8) and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """Write a text into filename


    Args:
        - filename: Name of the file to be written
        - text: text to write

    Returns: Total number of characters written
    """

    with open(filename, 'w') as f:
        return f.write(text)
