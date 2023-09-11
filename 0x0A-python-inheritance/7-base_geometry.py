#!/usr/bin/python3
"""A base Geometry class"""
class BaseGeometry:
    """ A base class for Geometry classes"""
    def area(self):
        """Calculates the area of the geometry obj"""
        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        """Validates the value witha name
        
           Args:
               name (str): The name of the value
               value (int): The value to validate
           Raises:
                 TypeError: If value is not an integer
                 ValueError: if value is less than 0
            """
            if not isinstance(value, int):
                raise TypeError(f'{name} must be an integer')
            if value <= 0:
                raise ValueError(f'{name} must be greater than 0')
