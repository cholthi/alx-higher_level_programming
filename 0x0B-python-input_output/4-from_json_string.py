#!/usr/bin/python3
"""Unserializes json string python objects"""


from json import loads


def from_json_string(my_str):
    """
    decodes a json string to python object

    Args:
        my_str (any): A json string to unmarshal
    Returns:
           object: A python object decoded from json string
    """
    my_obj = loads(my_str)
    return (my_obj)
