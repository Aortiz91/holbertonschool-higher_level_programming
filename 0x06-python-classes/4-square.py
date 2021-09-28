#!/usr/bin/python3
class Square():
    def __init__(self, size=0):
       if (isinstance(size, int) == False):
           raise TypeError ("size must be an integer")
       elif (size < 0):
           raise ValueError ("size must be >= 0")
       else:
            self.__size = size

            @property
            def size(self):
                return self.__size
            @property
            def size(self, value):
                return 
            
    def area(self):
        return (self.__size * self.__size)
