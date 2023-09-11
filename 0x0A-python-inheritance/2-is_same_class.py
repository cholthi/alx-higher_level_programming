#!/usr/bin/python3
"""
provides a function that tests if an object is an
instance of a Class cls
"""


def is_same_class(obj, a_class):
    """
    Tests if obj is an instance of the class a_class

    Args:
        obj (any): The object under test
        a_class (type): The class to test for object
    Return: Bool True if an instance of the a_class or False otherwise
    """
    if type(obj) == a_class:
        return (True)
    return (False)
