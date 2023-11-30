#!/bin/bash
# Sends a GET request with post data
curl -sd "email=test@gmail.com&subject=I will always be here for PLD" "$1"
