#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Prints a dict sorted by keys"""
    sorted_keys = sorted(a_dictionary.items(), key=lambda i: i[0])
    for key, val in sorted_keys:
        print('{}: {}'.format(key, val))
