#!/usr/bin/python3
"""Defines a square"""


class Square():
    """Defining class Square"""

    def __init__(self, size=0):
        """Initializing self size"""
        if (isinstance(size, int) == False):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
             
    def area(self):
        """Defining self area"""

        return (self.__size * self.__size)
