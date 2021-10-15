#!/usr/bin/python3
"""Will define a class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Defines a class Square that inherits from Rectangle"""

    def __init__(self, size):
        """Instantiation"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Returns a string"""
        return str("[Squeare] {}/{}".format(self.__size, self.__size))
