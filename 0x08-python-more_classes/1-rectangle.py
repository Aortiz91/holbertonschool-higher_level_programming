#!/usr/bin/python3
"""Define a new class named Rectangle"""


class Rectangle:
    """Constructor with Rectangle's width and height"""

    def __init__(self, width=0, height=0):
        """initializing instance"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")   
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Retrieves instance Rectangle's width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets instance Rectangle's width

        Args:
            value: width value, must be type int and positive
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves instance Rectangle's height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets instance Rectangle's height

        Args:
            value: height value, must be type int and positive
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value
