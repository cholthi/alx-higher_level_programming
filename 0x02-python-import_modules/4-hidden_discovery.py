#!/usr/bin/python3

import hidden_4

if __name__ == '__main__':
    defined_names = dir(hidden_4)
    [print(name) for name in sorted((name for name in defined_names if not name.startswith('__')))]
