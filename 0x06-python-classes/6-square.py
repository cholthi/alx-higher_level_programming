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
        if not isinstance(position[0], int) or not isinstance(position[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        if self.__size == 0:
            print()
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            print(''.rjust(self.__position[0]), end='')
            for j in range(0, self.__size):
                print('#', end='')
            print()
