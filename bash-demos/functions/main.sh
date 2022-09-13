#!/bin/bash
#
# Name: main.sh
#
# Synopsis:
#     main.sh
#
# Examples:
#     main.sh
#
# Description:
#     Shell script for demonstration of Bash functions.
#

local_function_a () {
    echo "Local function A"
}

echo "Hello, World!"

local_function_a

source ./functions.sh
function_a
function_c
