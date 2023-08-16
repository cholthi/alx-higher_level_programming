#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns the key with max value"""
    max = (2 ** 63 - 1) * -1
    if not a_dictionary:
        return (None)
    else:
        for k in a_dictionary:
            if a_dictionary[k] > max:
                key = k
                max = a_dictionary[key]
        return (key)
