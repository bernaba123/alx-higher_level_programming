#!/bin/bash
# size of http response
curl -s "$1" | wc -c
