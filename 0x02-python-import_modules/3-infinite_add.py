#!/usr/bin/python3

from sys import argv

argv_int = map(lambda x: int(x), argv[1:])

if __name__ == '__main__':
    print('{}'.format(sum(argv_int)))
