#!/bin/bash
#
# Name: run.sh
#
# Synopsis:
#     run.sh CONFIGURATION
#
# Examples:
#     hello.sh zdenek_2g3g.ini
#     hello.sh zdenek_4g5g.ini
#
# Description:
#     Script for running Python Roaming Pre-Processor application.
#
#     CONFIGURATION
#         Configuration file
#

PYTHON=python

function print_usage {
    echo "Usage: $(basename $BASH_SOURCE) CONFIGURATION"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

if [[ "$#" == "1" && ("$1" == "-h" || "$1" == "--help") ]]; then
    print_help
    exit 0
elif [[ "$#" == "1" ]]; then
    configuration_file=$1
else
    print_usage
    exit -1
fi

cd "$(dirname "$0")"

if [[ ! -f $configuration_file ]]; then
    echo "Error: Configuration file does not exist" 1>&2
    exit -1
fi

$PYTHON main.py --log_level DEBUG --config $configuration_file >>${configuration_file%.*}.log
