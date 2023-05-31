#!/usr/bin/python3

"""Python class Square."""


class Square:
    """A square class."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Computes area of this class."""
        return (self.__size * self.__size)

    @property
    def size(self):
        """Getter for size attribute."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for size attribute."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
