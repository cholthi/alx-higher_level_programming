#!/usr/bin/python3
"""Provides a function that encodes an object 
as json and writes to a file
"""


from json import dump


def save_to_json_file(my_obj, filename):
    """Encodes `my_obj` to json and writes it to file `filename`

    Args:
        my_obj (object): The person object to serialize to json
        filename (str): The file to write the encoded json strint to
    """
    with open(filename, "w", encoding="utf-8") as f:
        json_str = dump(my_obj, f)
