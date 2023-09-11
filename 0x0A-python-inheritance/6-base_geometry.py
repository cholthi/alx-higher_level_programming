#!/usr/bin/python3
"""A base Geometry class"""


class BaseGeometry:
    """ A base class for Geometry classes"""
    def area(self):
        """Calculates the area of the geometry obj"""
        raise Exception('area() is not implemented')
