#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    return (dict(filter(lambda v: v[1] != value, a_dictionary.items())))
