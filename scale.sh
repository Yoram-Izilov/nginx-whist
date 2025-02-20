#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <scale-number>"
    exit 1
fi

SCALE=$1

docker-compose up -d --scale app=$SCALE