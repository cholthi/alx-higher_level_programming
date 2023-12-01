#!/bin/bash
# Extracts list of supported http methods by a url
curl -sI "$1" | grep -i Allow | awk -F ':' '{print $2}' | head -c -2 | rev | head -c -1 | rev
