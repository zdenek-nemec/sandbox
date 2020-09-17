#!/bin/bash

echo "Hello, World!"

STREAMS="TABLE_A TABLE_B TABLE_C"
for stream in $STREAMS
do
    printf "$stream\nIN---OUT\n" > $stream.csv.tmp
    mv $stream.csv.tmp $stream.csv
done
