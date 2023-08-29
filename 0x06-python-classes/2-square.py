#!/usr/bin/python3
"""
A square class to represent square shapes
with private instance attribute and validation
"""
class Square:
    def init(self, size):
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
