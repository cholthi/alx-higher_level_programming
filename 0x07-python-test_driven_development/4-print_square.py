#!/usr/bin/python3
"""provides a function that prints a square with the character #"""


def print_square(size):
    """Prints a square using a # with size size
    
    Args:
      size (int): size of the square
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        [print('#', end='') for _ in range(size)]
        print()
