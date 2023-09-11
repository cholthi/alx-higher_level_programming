#!/usr/bin/python3
"""
provides a function that tests if an object is an
instance of a Class cls
"""


def is_kind_of_class(obj, a_class):
    """
    Tests if obj is an instance of the class a_class or
    instance of a derived class from a_class
    """
    return (isinstance(obj, a_class))
