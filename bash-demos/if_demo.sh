#!/bin/bash

a=3
if [[ $a == 1 || $a == 2 ]]; then
    echo "Variable a is 1 or 2"
else
    echo "Variable a is not 1 nor 2"
fi
