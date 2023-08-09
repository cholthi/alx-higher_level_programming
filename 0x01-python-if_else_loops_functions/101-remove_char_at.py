#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str) - 1:
        return str

    list_str = list(str)
    del list_str[n]
    return ''.join(list_str)
