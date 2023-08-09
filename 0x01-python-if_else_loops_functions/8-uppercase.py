#!/usr/bin/python3
def uppercase(str):
    lst = [chr(ord(c)-32) if ord(c) >= ord('a') and
              ord(c) <= ord('z') else c  for c in str]
    print('{}'.format(''.join(lst)))
