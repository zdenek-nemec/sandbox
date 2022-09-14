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

INTERMEDIATE=("avl4658t" "avl4688t" "avl4713p" "avl4715p")
REQUIRED_PYTHONHOME=/dcs/data01/SOFTWARE/Python/Python-3.7.8
REQUIRED_PYTHONPATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/lib
REQUIRED_PATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/bin

print_usage () {
    echo "Usage: $(basename $BASH_SOURCE) [--all] [--continue_on_error] [--scripts SCRIPTS]"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

print_help () {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

cd $(dirname $BASH_SOURCE)
unset compile_all
unset continue_on_error
unset scripts
if [[ $# == 0 ]]; then
    echo "Error: Missing arguments" 1>&2 && print_usage && exit -1
fi
while [[ $# -gt 0 ]]; do
    option="$1"
    case $option in
        -h|--help)
            print_help
            shift
            exit 0
            ;;
        --all)
            compile_all=1
            shift
            ;;
        --continue_on_error)
            continue_on_error=1
            shift
            ;;
        --scripts)
            [[ -z $2 ]] && echo "Error: No scripts specified" 1>&2 && print_usage && exit -1
            scripts="$2"
            shift
            shift
            ;;
        *)
            echo "Error: Unexpected arguments" 1>&2 && print_usage && exit -1
            ;;
    esac
done
if [[ $compile_all && $scripts ]]; then
    echo "Error: Invalid arguments, cannot use both --all and --scripts" 1>&2 && print_usage && exit -1
fi

unset is_intermediate
for item in ${INTERMEDIATE[@]}; do
    if [[ "$item" == "$HOSTNAME" ]]; then
        is_intermediate=1
        break
    fi
done

if [[ $is_intermediate ]]; then
    original_PYTHONHOME=$PYTHONHOME
    original_PYTHONPATH=$PYTHONPATH
    original_PATH=$PATH
    PYTHONHOME=$REQUIRED_PYTHONHOME
    export PYTHONHOME
    PYTHONPATH=$REQUIRED_PYTHONPATH
    export PYTHONPATH
    PATH=$REQUIRED_PATH:$PATH
    export PATH
fi

if [[ $compile_all ]]; then
    compile_list=($(python get_compile_list.py | tr -d '[],' | sed "s/'//g"))
else
    compile_list=($(python get_compile_list.py --scripts "$scripts" | tr -d '[],' | sed "s/'//g"))
fi
if [[ "$compile_list" == "-1" ]]; then
    echo -e "\033[1;31mCompilation aborted\033[0m"
    exit -1
fi

if [[ $is_intermediate ]]; then
    PYTHONHOME=$original_PYTHONHOME
    export PYTHONHOME
    PYTHONPATH=$original_PYTHONPATH
    export PYTHONPATH
    PATH=$original_PATH
    export PATH
fi

compilation_failures=0
for item in ${compile_list[@]}; do
    echo "Compile script $item"
    if [[ $is_intermediate ]]; then
        cgdc_compile_script.sh $item
    else
        echo "Simulating compilation"
    fi
    compilation_result="$?"
    if [[ "$compilation_result" != "0" ]]; then
        echo -e "\033[1;33mScript $item failed\033[0m"
        ((compilation_failures=compilation_failures+1))
        if [[ $continue_on_error ]]; then
            echo -e "\033[1;33mContinuing\033[0m"
        else
            echo -e "\033[1;31mAborting\033[0m"
            break
        fi
    fi
done

if [[ $compilation_failures == 0 ]]; then
    echo -e "\033[1;32mCompilation finished successfully, scripts compiled: ${#compile_list[@]}\033[0m"
elif [[ $continue_on_error ]]; then
    echo -e "\033[1;33mCompilation finished with errors, failed scripts: $compilation_failures\033[0m"
else
    echo -e "\033[1;31mCompilation aborted\033[0m"
    exit -1
fi
