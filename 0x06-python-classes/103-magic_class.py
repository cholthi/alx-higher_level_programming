#!/usr/bin/python3
import math


"""
Python MagicClass class
"""
class MagicClass:
    def __init__(self, radius=0):
        """ Initializes MagicClass"""
        if type(radius) is not int and type(radiuss) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates area of the MagicClass class"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Calculates circumference of the MagicClass class"""
        return (2 * math.pi * self.__radius)
