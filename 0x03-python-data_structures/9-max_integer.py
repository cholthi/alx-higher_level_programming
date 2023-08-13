#!/usr/bin/python3

def max_integer(my_list=[]):
    """Finds max value in a list of ints"""
    if len(my_list) == 0:
        return (None)
    max = (2 ** 63 -1) * -1
    for i in my_list:
        if i > max:
            max = i
    return (max)
