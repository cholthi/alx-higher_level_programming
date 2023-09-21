#!/usr/bin/python3
'''A class that represents a rectangle and inherits from Base'''
from models.base import Base


class Rectangle(Base):
    '''A class representing A rectangle shape'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initializes a Rectangle

        Args:
            width (int): width of a rectangle
            height (int): Height of a rectangle
            x (int): The x coordinate of a rectangle
            y (int): The y coordinate of a rectangle
            id (int): The id of this rectangle instance
        Raises:
              TypeError: if width or height is not an int
              ValueError: if width or height is less than 0
              TypeError: if x or y is not an int
              ValueError: if x or y is less than 0
        '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        '''width value accessor'''
        return (self.__width)

    @width.setter
    def width(self, value):
        '''width value mutator'''
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        '''height value accessor'''
        return (self.__height)

    @height.setter
    def height(self, value):
        '''height value mutator'''
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height  must be > 0')
        self.__height = value

    @property
    def x(self):
        '''x value accessor'''
        return (self.__x)

    @x.setter
    def x(self, value):
        '''x value mutator'''
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value <= 0:
            raise ValueError('x must be > 0')
        self.__x = value

    @property
    def y(self):
        '''x value accessor'''
        return (self.__y)

    @y.setter
    def y(self, value):
        '''y value muttator'''
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value <= 0:
            raise ValueError('y must be > 0')
        self.__y = value

    def area(self):
        '''Calcualtes the arear of a rectangle

        Returns:
               (int): The area of a rectangle shape
        '''
        return (self.__width * self.__height)

    def display(self):
        '''Displays the rectangle using ascii character'''
        if self.__width == 0 or self.__height == 0:
            print()
            return

        [print() for y in range(self.__y)]
        for row in range(0, self.__height):
            [print(" ", end="") for x in range(self.__x)]
            [print('#', end='') for col in range(0, self.__width)]
            print()

    def __str__(self):
        '''Returns string representation of this class'''
        return (f'[{type(self).__name__}] ({self.id}) {self.__x}'
                f'/{self.__y} - {self.__width}/{self.__height}')

    def update(self, *args, **kwargs):
        '''Updates attributes of this class instance'''
        if args and len(args) != 0:
            if args[0] is None:
                self.__init__(
                        self.width, self.height, self.x, self.y)
            else:
                self.id = args[0]

                self.width = args[1]
                self.height = args[2]
                self.x = args[3]
                self.y = args[4]
        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == 'id':
                    if v is None:
                        self.__init__(
                            self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == 'width':
                    self.width = v
                elif k == 'height':
                    self.height = v
                elif k == 'x':
                    self.x = v
                elif k == 'y':
                    self.y = v

    def to_dictionary(self):
        '''Returns the dict representation of the rectangle'''
        return ({
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
            })
