#!/usr/bin/python3
'''Write a Python script that takes your GitHub credentials (username and password) and
uses the GitHub API to display your id'''


import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    auth = HTTPBasicAuth
    req = requests.get("http:///api.github.com/user", auth=auth)

    print(req.json().get("id"))
