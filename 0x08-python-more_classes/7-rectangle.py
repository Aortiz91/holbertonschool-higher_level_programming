#!/usr/bin/python3
"""Define a new class named Rectangle"""


class Rectangle:
    """Constructor with Rectangle's width and height"""

    number_of_instances = 0
    print_symbol = '#'

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
        self.__width = width
        self.__height = height
        self.number_of_instances += 1

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

    def area(self):
        """Public instance method that returns Rectangle's area"""
        return self.__width*self.__height

    def perimeter(self):
        """Public instance method that returns Rectangle's perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Return string"""
        if self.__height == 0 or self.__width == 0:
            return ''
        string = ''
        for i in range(self.__height):
            for j in range(self.__width):
                string += str(self.print_symbol)
            string += '\n'
        string = ''
        return string[:-1]

    def __repr__(self):
        """ Return string"""
        return"Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes instance"""
        print("Bye rectangle...")
        self.number_of_instances -= 1
