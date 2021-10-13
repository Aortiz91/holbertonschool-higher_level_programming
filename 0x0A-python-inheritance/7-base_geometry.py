#!/usr/bin/python3
"""Will define a class"""


class BaseGeometry():
    """Defines a class BaseGeometry"""

    def area(self):
        """Public instance method area that
        is not implemented"""

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Public instance method that validates a given value

            Args:
                -name: name of the type of value, always a string
                -value: Value to validate
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
