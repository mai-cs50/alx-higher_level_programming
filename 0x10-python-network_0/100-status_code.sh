#!/bin/bash
# takes n a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -L -X HEAD -w "%{http_code}" "$1"
