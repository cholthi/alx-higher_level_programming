#!/bin/bash
# Extracts list of supported http methods by a url
curl -sI "$1" | grep -i allow | awk -F ':'
