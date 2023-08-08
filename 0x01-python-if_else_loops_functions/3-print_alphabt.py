#!/usr/bin/python3
for code in range(ord('a'), ord('z') + 1):
    if chr(code) not in 'qe':
        print(chr(code), end="")
