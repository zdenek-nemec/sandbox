#!/bin/bash
#
# Name: compile.sh
#
# Synopsis:
#     compile.sh [--scripts SCRIPTS]
#
# Examples:
#     compile.sh
#     compile.sh --scripts "ics_2_dwh"
#     compile.sh --scripts "ics_library"
#     compile.sh --scripts "ics_library ics_2_dwh"
#
# Description:
#     Compile Intermediate scripts.
#
#     -h, --help
#         Show this help message and exit
#     --scripts SCRIPTS
#         Altered scripts which will be compiled along with scripts that are
#         dependent on them
#

function print_usage {
    echo "Usage: $(basename $BASH_SOURCE) [-h]"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

if [[ "$#" == "1" && ("$1" == "-h" || "$1" == "-help" || "$1" == "--help") ]]; then
    print_help
    exit 0
fi

. ./set_environment.sh

cd $(dirname "$IME_COMPILER")

if [[ "$#" == "0" ]]; then
    compile_list=($(python compiler.py | tr -d '[],' | sed "s/'//g"))
else
    compile_list=($(python compiler.py --scripts $1 | tr -d '[],' | sed "s/'//g"))
fi

for item in ${compile_list[@]}; do
    echo "Compile script $item"
    if [[ $IS_INTERMEDIATE ]]; then
        cgdc_compile_script.sh $item
    else
        echo "Simulating compilation"
    fi
    compilation_result="$?"
    if [[ "$compilation_result" != "0" ]]; then
        echo -e "\033[1;31mFailed, aborting\033[0m"
        break
    fi
done

if [[ "$compilation_result" == "0" ]]; then
    echo -e "\033[1;32mSuccess\033[0m"
fi
