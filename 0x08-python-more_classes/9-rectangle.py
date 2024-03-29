#!/usr/bin/python3
"""
Empty Rectangle class module
"""


class Rectangle:
    """Empty Rectangle class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        type(self).number_of_instances += 1

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.

        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return (rect_1)
        return (rect_2)

    def square(cls, size=0):
        """Returns a new Rectangle instance that is a square

        Args:
            size (int): A rectangle size to set width and height of Rectangle
        """

        return (cls(size, size))

    def __str__(self):
        """Returns the string representation of the rectangle class"""

        if self.__width == 0 or self.__height == 0:
            return ('')

        ret = []
        for i in range(0, self.__height):
            for _ in range(0, self.__width):
                ret.append(str(self.print_symbol))
            if i != self.__height - 1:
                ret.append('\n')
        return (''.join(ret))

    def __repr__(self):
        """Returns this class represntation for eval"""

        cls = self.__class__.__name__
        return (f'{cls}({self.__width}, {self.__height})')

    def __del__(self):
        """prints a message when instance of Rectangle is deleted"""
        self.number_of_instances -= 1
        print('Bye rectangle ...')
