#!/usr/bin/python3
for i in range(0, 10):
    for p in range(i + 1, 10):
        if i == 8 and p == 9:
            print('{}{}'.format(i, p))
        else:
            print(f'{}{}'.format(i, p), end=", ")
