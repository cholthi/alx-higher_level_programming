#!/usr/bin/python3
""" Receives a username and password for use with GithubAPI
Retrives the github user information
"""

import requests
from sys import argv

user = argv[1]
passwd = argv[2]
endpoint = 'https://api.github.com/user'

response = requests.get(endpoint, auth=(user, passwd))

if response.status_code == requests.codes.ok:
    try:
        data = response.json()
        print(data['id'])
    except Exception as e:
        raise e
else:
    print(None)
