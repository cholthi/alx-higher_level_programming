#!/usr/bin/python3
""" Takes a URL as argument and sends a request to it
Retrives the value of X-Request-Id from the response
"""

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    print(response.headers.get('X-Request-Id'))
