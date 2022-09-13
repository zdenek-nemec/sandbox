#!/bin/bash
#
# Name: functions.sh
#
# Synopsis:
#     functions.sh
#
# Examples:
#     functions.sh
#
# Description:
#     Collection of Bash functions intended for use by Intermediate compiler.
#     Import, do not run directly.
#

INTERMEDIATE=("avl4658t" "avl4688t" "avl4713p" "avl4715p")

print_usage () {
    invoker=$1
    echo "Usage: $(basename $invoker)"
    echo "Try \`$(basename $invoker) --help' for more information."
}

print_help () {
    invoker=$1
    head -$(grep -n -m 1 -v "^#" "$invoker" | cut -d ":" -f 1) "$invoker"
}

check_help () {
    parameters=$1
    first=$2
    invoker=$3
    if [[ "$parameters" == "1" && ("$first" == "-h" || "$first" == "-help" || "$first" == "--help") ]]; then
        print_help $invoker
        exit 0
    fi
}

is_intermediate () {
    unset IS_INTERMEDIATE
    for item in ${INTERMEDIATE[@]}; do
        if [[ "$item" == "$HOSTNAME" ]]; then
            IS_INTERMEDIATE=1
            break
        fi
    done
}

set_environment () {
    is_intermediate
    if [[ $IS_INTERMEDIATE ]]; then
        echo "Intermediate Environment $HOSTNAME"
        SCRIPTS_PATH="/dcs/appl01/var_dcs_9.0_db/cgdc/src"
        SCRIPTS_PATH_REMOVE="s/\/dcs\/appl01\/var_dcs_9\.0_db\/cgdc\/src\///"
        IME_COMPILER="/dcs/data01/SOFTWARE/Tools/IntermediateCompiler/compile.sh"
    else
        echo "Unknown Environment $HOSTNAME"
        SCRIPTS_PATH="./tests"
        SCRIPTS_PATH_REMOVE="s/\.\/tests\///g"
        IME_COMPILER="./compile.sh"
    fi
}
