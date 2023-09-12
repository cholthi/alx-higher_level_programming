#!/usr/bin/python3
"""
provides a function that tests if an object is an
instance of a Class cls
"""


def inherits_from(obj, a_class):
    """
    Tests if obj is an instance of the class a_class or
    instance of a derived class from a_class

    Args:
        obj (any): The object under  test
        a_class (type): The class to test for
    Return:
         Bool True if obj is a subclass of a_class or False otherwise
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
