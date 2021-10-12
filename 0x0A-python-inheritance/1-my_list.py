#!/usr/bin/python3
""" 1-my_list.py:
Creates a class MyList that inherits from list the Public instance method
that prints the list, but sorted ascending
"""


class MyList(list):
    """Creates the subclass MyList that inherits from list

    Args:
        list: superclass of MyList
    """

    def print_sorted(self):
        """ Module that prints the list sorted in ascending order
        """
        copylist = self[:]
        copylist.sort()
        print("{}".format(copylist))
