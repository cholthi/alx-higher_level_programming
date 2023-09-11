#!/usr/bin/python3
"""Provides a function that returns available attributes and methods
       of an object
"""
def lookup(obj):
    """returns available attributes and methods of the obj"""
    return (dir(obj))
