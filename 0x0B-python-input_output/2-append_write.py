#!/usr/bin/python3
"""provides a function that appends a string to a file"""


def write_file(filename="", text=""):
    """
    Appends a string text to file filename

    Args:
        filename (str): A file to write to
        text (str): The string/text to write to file
    """
    with open(filename, "a", encoding="utf-8") as f:
        read = f.write(text)
    return (read)
