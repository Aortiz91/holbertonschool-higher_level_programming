#!/usr/bin/python3
"""Will define a class"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Defines a class Rectangle that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiation"""

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
