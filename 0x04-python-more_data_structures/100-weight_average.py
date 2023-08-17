#!/usr/bin/python3
def weight_average(my_list=[]):
    """Returns weighted average of the input list"""
    if len(my_list) == 0:
        return (0)

    res = (sum([a * b for a, b in my_list])) / (sum(dict(my_list).values()))
    return (res)
