#!/usr/bin/python3
import requests
from requests.auth import HTTPBasicAuth
from sys import argv


if __name__ == "__main__":
    auth = HTTPBasicAuth
    req = requests.get("http:///api.github.com/user", auth=auth)

    print(req.json().get("id"))
