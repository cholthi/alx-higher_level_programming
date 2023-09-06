#!/usr/bin/python3
"""provides a function that outputs a name"""


def say_my_name(first_name, last_name=""):
    """concatenetae first_name and last_name in a string

    Args:
      first_name (str): First name
      last_name: (str): Last name
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
