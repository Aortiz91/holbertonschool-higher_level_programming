#!/usr/bin/python3
"""MyInteger function that creates a class with
== and != operations inverted"""


class MyInt(int):
    """ Defines a class MyInt that inherits from int"""

    def __eq__(self, value):
        """Methor that overrides the operator == """
        return False

    def __ne__(self, value):
        """ Method that overrides the operator != """
        return True
