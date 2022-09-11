#!/bin/bash
#
# Name: compile.sh
#
# Synopsis:
#     compile.sh
#
# Examples:
#     compile.sh
#
# Description:
#     Bla
#
#     -h, --help
#         Show this help message and exit
#

list=($(python compiler.py | tr -d '[],' | sed "s/'//g"))
for item in ${list[@]}; do echo "Compile script $item"; done
