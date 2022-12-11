#!/usr/bin/env bash

if [ $# -eq 0 ]; then
    echo "No arguments provided"
    exit 1
fi

mkdir -p $1/day_$2
touch $1/day_$2/day_$2.py
touch $1/day_$2/input.txt
touch $1/day_$2/sample.txt
