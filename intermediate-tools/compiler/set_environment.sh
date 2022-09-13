#!/bin/bash
#
# Name: set_environment.sh
#
# Synopsis:
#     set_environment.sh
#
# Examples:
#     set_environment.sh
#
# Description:
#     Set the environment for Intermediate compiler.
#     Run for the parent shell with `. ./set_environment.sh'.
#
#     -h, --help
#         Show this help message and exit
#

INTERMEDIATE=("avl4688t" "avl4715p" "avl4713p" "avl4658t")
# INTERMEDIATE=("avl4688t" "avl4715p" "avl4713p" "avl4658t" "N007510" "JISKRA")

function print_usage {
    echo "Usage: $(basename $BASH_SOURCE) [-h]"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

function is_intermediate () {
    for item in ${INTERMEDIATE[@]}; do
        if [[ "$item" == "$HOSTNAME" ]]; then
            IS_INTERMEDIATE="1"
        fi
    done
}

if [[ "$#" == "1" && ("$1" == "-h" || "$1" == "-help" || "$1" == "--help") ]]; then
    print_help
    exit 0
fi

is_intermediate

if [[ $IS_INTERMEDIATE ]]; then
    echo "Intermediate Environment"
    SCRIPTS_PATH="/dcs/appl01/var_dcs_9.0_db/cgdc/src"
    SCRIPTS_PATH_REMOVE="s/\/dcs\/appl01\/var_dcs_9\.0_db\/cgdc\/src\///"
    IME_COMPILER="/dcs/data01/SOFTWARE/Tools/IntermediateCompiler/compile.sh"
else
    echo "Unknown Environment"
    SCRIPTS_PATH="./tests"
    SCRIPTS_PATH_REMOVE="s/\.\/tests\///g"
    IME_COMPILER="./compile.sh"
fi
