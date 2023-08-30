#!/usr/bin/python3
"""
A square class to represent square shapes
with private instance attribute and validation
"""


class Square:
    """Square class for square shapes"""
    def __init__(self, size=0, position=(0,0)):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        if not isinstance(vale[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    def size(self):
        return (self.__size)

    def size(self,value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
    def position(self):
        return (self.__position)

    def position(self, value):
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print('#', end='')
            if i == self.__size - 1:
                print(end='')
            else:
                print()
