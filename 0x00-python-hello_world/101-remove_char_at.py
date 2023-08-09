#!/usr/bin/python3
def remove_char_at(str, n):
    list_str = list(str)
    del list_str[n]
    return ''.join(list_str)
