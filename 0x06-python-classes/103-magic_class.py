#!/usr/bin/python3

"""
Python MagicClass class
"""

import math


class MagicClass:
    """magicClass class"""

    def __init__(self, radius=0):
        """ Initializes MagicClass

        Agr:
          radius (int or float): radius of the MagicClass class
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Calculates area of the MagicClass class"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """Calculates circumference of the MagicClass class"""
        return (2 * math.pi * self.__radius)
