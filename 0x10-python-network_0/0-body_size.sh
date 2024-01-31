#!/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL,
#   and displays the size of the body of the response
#   
#   Requirements
# The size must be displayed in bytes
# You have to use curl
# Please test your script in the sandbox provided,
#   using the web server running on port 5000

curl -Is "$1" | awk '/Content-Length/ {print $2}'
