#!/bin/bash
# Extracts list of supported http methods by a url
curl -Is "$1" | grep "Allow:" | cut -d ":" -f 2 | cut -c 2- | rev | cut -c 2- | rev
