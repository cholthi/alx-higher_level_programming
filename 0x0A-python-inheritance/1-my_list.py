#!/usr/bin/python3
"""
Derived list class that provides a method to print
sorted list
"""
class MyList(list):
    """A class that inherits from list and provides print_sorted method"""
    def print_sorted(self):
        print(sorted(self))
