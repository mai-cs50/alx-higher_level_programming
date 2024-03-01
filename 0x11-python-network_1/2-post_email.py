#!/usr/bin/python3
import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")
    req = Request(url, data=data)

    with urlopen(req) as response:
        print(response.read().decode("utf-8"))
