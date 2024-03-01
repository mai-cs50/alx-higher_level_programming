#!/usr/bin/python3
import urllib.request
import sys


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    with urlopen(req) as response:
        print(dict(response.headers).get('X-Request-Id'))
