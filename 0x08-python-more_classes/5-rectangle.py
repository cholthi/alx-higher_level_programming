#!/usr/bin/python3
"""
Empty Rectangle class module
"""


class Rectangle:
    """Empty Rectangle class """

    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    @property
    def width(self):
        """Returns the value of the width property"""

        return (self.__width)

    @width.setter
    def width(self, value):
        """Sets the value of the width attribute"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Returns the value of the height"""

        return (self.__height)

    @height.setter
    def height(self, value):
        """Sets the value of the height"""

        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""

        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""

        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__height * self.__width) * 2)

    def __str__(self):
        """Returns the string representation of the rectangle class"""

        if self.__width == 0 or self.__height == 0:
            return ('')

        ret = []
        for i in range(0, self.__height):
            for _ in range(0, self.__width):
                ret.append('#')
            if i != self.__height - 1:
                ret.append('\n')
        return (''.join(ret))

    def __repr__(self):
        """Returns this class represntation for eval"""

        cls = self.__class__.__name__
        return (str(f"{cls}({self.__width}, {self.__height})"))

    def __del__(self):
        """Print a message when Rectangle is deleted."""
        print("Bye rectangle...")
