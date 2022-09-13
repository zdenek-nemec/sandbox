#!/bin/bash
#
# Name: compile.sh
#
# Synopsis:
#     compile.sh [SCRIPTS]
#
# Examples:
#     compile.sh
#     compile.sh ics_2_dwh
#     compile.sh ics_library
#     compile.sh "ics_library ics_2_dwh"
#
# Description:
#     Compile Intermediate scripts with dependencies.
#
#     -h, --help
#         Show this help message and exit
#     SCRIPTS
#         Scripts which will be compiled along with scripts that are dependent
#         on them
#

source ./functions.sh

check_help $# $1 $BASH_SOURCE

if [[ "$#" == "0" ]]; then
    :
elif [[ "$#" == "1" ]]; then
    scripts=$1
else
    print_usage $BASH_SOURCE
    exit -1
fi

set_environment

cd $(dirname $IME_COMPILER)

if [[ "$#" == "0" ]]; then
    compile_list=($(python get_compile_list.py | tr -d '[],' | sed "s/'//g"))
else
    compile_list=($(python get_compile_list.py --scripts "$scripts" | tr -d '[],' | sed "s/'//g"))
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
        echo -e "\033[1;31mFailed, aborting compilation\033[0m"
        break
    fi
done

if [[ "$compilation_result" == "0" ]]; then
    echo -e "\033[1;32mSuccess\033[0m"
fi
