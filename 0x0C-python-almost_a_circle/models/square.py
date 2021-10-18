#!/usr/bin/python3
""" Will create a class Square inherits from Rectangle"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a class Square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor

        Args:
            - size: size
            - x: x
            - y: y
            - id: id
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Gets size"""

        return self.width

    @size.setter
    def size(self, value):
        """Sets size"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        """Returns string"""

        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """ Public method that assigns an argument to each attrubite

        Args:
            - id
            - width
            - height
            - x
            - y
        """

        if args and len(args) != 0:
            index = 0
            for arg in args:
                if index == 0:
                    self.id = arg
                elif index == 1:
                    self.width = arg
                elif index == 2:
                    self.x = arg
                elif index == 3:
                    self.y = arg
                index += 1
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """Public method that returns the dictionary representation of
        a Square"""

        dictionary = {'id': self.id, 'size': self.size,
                      'x': self.x, 'y': self.y}
        return dictionary
