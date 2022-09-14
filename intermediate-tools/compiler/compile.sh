#!/bin/bash
#
# Name: compile.sh
#
# Synopsis:
#     compile.sh [--all] [--continue_on_error] [--scripts SCRIPTS]
#
# Examples:
#     compile.sh --all
#     compile.sh --all --continue_on_error
#     compile.sh --scripts ics_2_dwh
#     compile.sh --scripts ics_library
#     compile.sh --scripts "ics_library ics_2_dwh"
#
# Description:
#     Compile Intermediate scripts with dependencies.
#
#     -h, --help
#         Show this help message and exit
#     --all
#         Compile all scripts
#     --continue_on_error
#         Continue compiling even if some scripts fail
#     --scripts SCRIPTS
#         Scripts which will be compiled along with scripts that are dependent
#         on them
#

cd $(dirname $BASH_SOURCE)
source ./functions.sh

unset COMPILE_ALL
unset CONTINUE_ON_ERROR
unset SCRIPTS
if [[ $# == 0 ]]; then
    echo "Error: Missing arguments" 1>&2 && print_usage $BASH_SOURCE && exit -1
fi
while [[ $# -gt 0 ]]; do
    option="$1"
    case $option in
        -h|--help)
            print_help $BASH_SOURCE
            shift
            exit 0
            ;;
        --all)
            COMPILE_ALL=1
            shift
            ;;
        --continue_on_error)
            CONTINUE_ON_ERROR=1
            shift
            ;;
        --scripts)
            [[ -z $2 ]] && echo "Error: No scripts specified" 1>&2 && print_usage $BASH_SOURCE && exit -1
            SCRIPTS="$2"
            shift
            shift
            ;;
        *)
            echo "Error: Unexpected arguments" 1>&2 && print_usage $BASH_SOURCE && exit -1
            ;;
    esac
done
if [[ $COMPILE_ALL && $SCRIPTS ]]; then
    echo "Error: Invalid arguments, cannot use both --all and --scripts" 1>&2 && print_usage $BASH_SOURCE && exit -1
fi

is_intermediate
if [[ $IS_INTERMEDIATE ]]; then
    original_python_home=$PYTHONHOME
    original_python_path=$PYTHONPATH
    original_path=$PATH
    PYTHONHOME=/dcs/data01/SOFTWARE/Python/Python-3.7.8
    export PYTHONHOME
    PYTHONPATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/lib
    export PYTHONPATH
    PATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/bin:$PATH
    export PATH
fi

if [[ $COMPILE_ALL ]]; then
    compile_list=($(python get_compile_list.py | tr -d '[],' | sed "s/'//g"))
else
    compile_list=($(python get_compile_list.py --scripts "$SCRIPTS" | tr -d '[],' | sed "s/'//g"))
fi

if [[ $IS_INTERMEDIATE ]]; then
    PYTHONHOME=$original_python_home
    export PYTHONHOME
    PYTHONPATH=$original_python_path
    export PYTHONPATH
    PATH=$original_path
    export PATH
fi

compilation_failures=0
for item in ${compile_list[@]}; do
    echo "Compile script $item"
    if [[ $IS_INTERMEDIATE ]]; then
        cgdc_compile_script.sh $item
    else
        echo "Simulating compilation"
    fi
    compilation_result="$?"
    if [[ "$compilation_result" != "0" ]]; then
        echo -e "\033[1;33mScript $item failed\033[0m"
        ((compilation_failures=compilation_failures+1))
        if [[ $CONTINUE_ON_ERROR ]]; then
            echo -e "\033[1;33mContinuing\033[0m"
        else
            echo -e "\033[1;31mAborting the compilation\033[0m"
            break
        fi
    fi
done

if [[ $compilation_failures == 0 ]]; then
    echo -e "\033[1;32mSuccess, scripts compiled: ${#compile_list[@]}\033[0m"
else
    if [[ $CONTINUE_ON_ERROR ]]; then
        echo -e "\033[1;33mCompilation finished, failed scripts: $compilation_failures\033[0m"
    else
        echo -e "\033[1;31mCompilation aborted\033[0m"
    fi
fi
