#!/usr/bin/python3
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -sI "$URL" | grep -i "allow" | cut -d " " -f2-
