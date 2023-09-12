#!/usr/bin/python3
"""Provides a function that reads from file encoded with utf-8"""


def read_file(filename=""):
    """
    Reads from a file and outputs to stdout

    Args:
        filename (str): The file name to read from
    Returns: nothing
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read())
