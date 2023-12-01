#!/bin/bash
# Receives a URL and makes a request a GET to it
curl -s "$1" | cat - ; echo ""
