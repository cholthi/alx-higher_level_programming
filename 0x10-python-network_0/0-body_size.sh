#!/bin/bash
# Get the size of the remote url contents
curl -s "$1" | wc -c
