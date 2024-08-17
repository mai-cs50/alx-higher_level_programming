#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -f2- -d" "
