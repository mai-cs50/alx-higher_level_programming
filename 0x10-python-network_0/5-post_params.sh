#!/bin/bash
# takes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
