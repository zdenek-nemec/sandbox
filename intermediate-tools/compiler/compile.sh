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

# if [[ "$#" == "0" ]]; then
#     python compiler.py
# else
#     python compiler.py --target $1
# fi

list=($(python compiler.py | tr -d '[],' | sed "s/'//g"))
for item in ${list[@]}; do echo "Compile script $item"; done
