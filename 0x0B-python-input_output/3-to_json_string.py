#!/usr/bin/python3
"""Serializes python objects to json string"""


from json import dumps


def to_json_string(my_obj):
    """
    encodes a python object obj to json string

    Args:
        my_obj (any): Python object to encode to json
    Returns:
           str: A json string representation of an object
    """
    json_str = dumps(my_obj)
    return (json_str)
