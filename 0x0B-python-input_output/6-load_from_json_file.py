#!/usr/bin/python3
"""Provides a function that json decodes an object
from a file
"""


from json import load


def load_from_json_file(filename):
    """Decodes a json string from a file `filename`

    Args:
        filename (str): The file to read the encoded json strint from
    """
    with open(filename, "r", encoding="utf-8") as f:
        my_obj = dump(f)
        return (my_obj)
