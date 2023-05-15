#!/bin/bash

a=4
if [[ $a == 1 || $a == 2 || $a == 3 ]]; then
    echo "Variable a is 1, 2 or 3"
elif [[ $a == 4 ]]; then
    echo "Variable a is 4"
else
    echo "Variable a is not 1, 2, 3 nor 4"
fi
