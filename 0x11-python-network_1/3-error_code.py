#!/usr/bin/python3
'''script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)'''


import urllib.request
import urllib.parse
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = Request(url)

    try:
        with urlopen(req) as response:
            print(response.read().decode("ascii"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
