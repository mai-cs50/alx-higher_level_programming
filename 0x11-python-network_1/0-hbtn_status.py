#!/usr/bin/python3
'''script that fetches https://alx-intranet.hbtn.io/status'''
from urllib.request import Request, urlopen

if __name__ == "__main__":
    url = "http://0.0.0.0:5050/status"
    req = requests.get(url)
    with urlopen(req) as response:
        body = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(req.text)))
        print('\t- content: {}' .format(req.text))
        #print('\t- utf8 content: {}'.format(body.decode("utf-8")))
