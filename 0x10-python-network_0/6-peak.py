#!/usr/bin/python3
""" Provides find_peak function that takes a list of int
and returns the first peak number in a list
"""


def find_peak(list_of_integers):
    start, end = 0, len(list_of_integers) - 1
    while start < end:
        mid = start + (end - start) // 2

        if (list_of_integers[mid] > list_of_integers[mid - 1]) and (
                list_of_integers[mid] > list_of_integers[mid + 1]):
            return list_of_integers[mid]
        if list_of_integers[mid - 1] > list_of_integers[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_of_integers[start]
