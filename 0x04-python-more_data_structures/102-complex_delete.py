#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    cached_dict = a_dictionary.copy().items()
    for k, v in cached_dict:
        if v == value:
            del a_dictionary[k]
    return (a_dictionary)
