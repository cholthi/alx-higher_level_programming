#!/usr/bin/python3
""" Takes a URL as argument and email
Sends a POST request to the URL and reads the response
"""

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.post(argv[1], data={'email': argv[2])
    print(response.text)
