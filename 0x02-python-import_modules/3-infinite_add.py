#!/usr/bin/python3

if __name__ == '__main__':
    """ Sums its agruments"""
    import sys

    argv_int = map(lambda x: int(x), argv[1:])
    print('{}'.format(sum(argv_int)))
