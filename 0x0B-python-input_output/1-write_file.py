#!/usr/bin/python3
"""provides a function that writes a string to a file"""


def write_file(filename="", text=""):
    """
    Writes a string text to file filename

    Args:
        filename (str): A file to write to
        text (str): The string/text to write to file
    """
    with open(filename, "w", encoding="utf-8") as f:
        read = f.write(text)
    return (read)
