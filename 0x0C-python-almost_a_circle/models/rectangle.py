#!/usr/bin/python3
""" Will create a class Rectangle with private attrubites each
with it's own public getter and setter"""


from models.base import Base


class Rectangle(Base):
    """Define a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor

        Args:
            - width: width
            - height: height
            - x: x
            - y: y
            - id: id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y

        super().__init__(id)

    @property
    def width(self):
        """Gets width"""

        return self.__width

    @property
    def height(self):
        """Gets height"""

        return self.__height

    @property
    def x(self):
        """Gets x"""

        return self.__x

    @property
    def y(self):
        """Gets y"""

        return self.__y

    @width.setter
    def width(self, value):
        """Sets width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ sets height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """ sets x attribute"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """ Sets y attribute"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Returns the area value of the Rectangle instance"""

        return self.__width * self.__height

    def display(self):
        """Public Method that prints in stdout the Rectangle instance
        with the character #"""

        for m in range(self.__y):
            print()
        for i in range(self.__height):
            for n in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns string"""

        return "[Rectangle] ({}) {}/{} - {}/{})".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args):
        """ Public methot that assigns an argument to each attrubite

        Args:
            - id
            - width
            - height
            - x
            - y
        """
        for arg in args:
            if (args[0]):
                self.id = args[0]
            elif (args[1]):
                self.__width = args[1]
            elif (args[2]):
                self._height = args[2]
            elif (args[3]):
                self.__x = args[3]
            elif (args[4]):
                self.__y = args[4]
