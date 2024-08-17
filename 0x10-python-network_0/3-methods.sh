#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI -X OPTIONS "$1" | grep -i "Allow:" | cut -d " " -f2- | tr ' ' ',' | sed 's/,$//'
