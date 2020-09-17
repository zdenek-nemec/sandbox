#!/bin/bash

echo "Hello, World!"

STREAMS="DPG IN MSC"
for stream in $STREAMS
do
    printf "$stream\nIN---OUT\n" > $stream.txt.tmp
    mv $stream.txt.tmp $stream.txt
done
