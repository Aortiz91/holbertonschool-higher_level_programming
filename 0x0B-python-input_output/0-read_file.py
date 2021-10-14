#!/usr/bin/python3
"""Function that reads a text file (UTF8) using the with keyboard so the file
is properly closed after its suite finishes, and prints it to the stdout
"""


def read_file(filename=""):
    """Module to read a file's content and prints to stdout


    Args:
        - filename: Name of the file to read
    """

    with open(filename) as f:
        read_data = f.read()
        print(read_data, end="")
