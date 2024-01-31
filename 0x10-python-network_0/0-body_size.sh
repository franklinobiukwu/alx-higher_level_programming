#!/bin/bash
# Write a Bash script that takes in a URL, sends a request to that URL,
curl -Is "$1" | awk '/Content-Length/ {print $2}'
