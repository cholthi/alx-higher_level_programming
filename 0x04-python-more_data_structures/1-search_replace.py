#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """replaces search with replace in the input list"""
    return ([replace if search == i else i for i in my_list])
