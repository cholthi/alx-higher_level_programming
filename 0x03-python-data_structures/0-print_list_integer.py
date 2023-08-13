#!/usr/bin/python3

def print_list_integer(my_list=[]):
    """Print ints passed in the list"""
    [print('{:d}'.format(i)) for i in my_list]
