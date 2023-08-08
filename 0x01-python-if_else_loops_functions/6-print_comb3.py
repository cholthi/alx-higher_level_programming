#!/usr/bin/python3
for i in range(0, 10):
    for p in range(i + 1, 10):
        if i == 8 and p == 9:
            print(f'{i:d}{p:d}')
        else:
            print(f'{i:d}{p:d}', end=", ")
