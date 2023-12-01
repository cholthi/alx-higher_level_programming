#!/usr/bin/python3
""" Takes a URL as argument and email
Sends a POST request to the URL and reads the response
"""

import requests
from sys import argv

if __name__ == '__main__':
    response = requests.get(argv[1])
    if response.status_code >= requests.codes.bad_request:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
