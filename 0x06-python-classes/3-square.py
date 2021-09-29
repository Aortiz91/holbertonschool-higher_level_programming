#!/usr/bin/python3
"""Defines a square"""


class Square():
    """Defining class Square"""
    def __init__(self, size=0):
        """Initializing self size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns self area"""
        return self.__size*self.__size
