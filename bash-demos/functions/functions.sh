#!/bin/bash
#
# Name: functions.sh
#
# Usage:
#     Import, do not run directly
#
# Description:
#     Collection of Bash functions intended for use by other scripts.
#

CONSTANT_C="This is C"

function_a () {
    echo "Function A"
}

function_b () {
    echo "Function B"
}

function_c () {
    echo "$CONSTANT_C"
}
