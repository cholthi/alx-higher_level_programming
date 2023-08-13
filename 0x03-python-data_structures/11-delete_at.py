#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Removes element at index idx from the list"""
    if idx > len(my_list) - 1 or idx < 0:
        return (my_list)
    del my_list[idx]
    return (my_list)
