#!/bin/bash
#
# Name: set_aliases.sh
#
# Synopsis:
#     set_aliases.sh
#
# Examples:
#     set_aliases.sh
#
# Description:
#     Set aliases for Intermediate compiler.
#     Run for the parent shell with `. ./set_aliases.sh'.
#
#     -h, --help
#         Show this help message and exit
#

set_environment () {
    is_intermediate
    if [[ $IS_INTERMEDIATE ]]; then
        echo "Intermediate Environment $HOSTNAME"
        SCRIPTS_PATH="/dcs/appl01/var_dcs_9.0_db/cgdc/src"
        SCRIPTS_PATH_REMOVE="s/\/dcs\/appl01\/var_dcs_9\.0_db\/cgdc\/src\///"
        INTERMEDIATE_COMPILER="/dcs/data01/SOFTWARE/Tools/IntermediateCompiler/compile.sh"
    else
        echo "Unknown Environment $HOSTNAME"
        SCRIPTS_PATH="./tests"
        SCRIPTS_PATH_REMOVE="s/\.\/tests\///g"
        INTERMEDIATE_COMPILER="./compile.sh"
    fi
}

cd $(dirname $BASH_SOURCE)
source ./functions.sh

check_help $# $1 $BASH_SOURCE

if [[ "$#" == "0" ]]; then
    :
else
    print_usage $BASH_SOURCE
    exit -1
fi

set_environment

alias ime_compile=$IME_COMPILER
list4ime_compile=$(find $SCRIPTS_PATH -maxdepth 1 -type f | sed $SCRIPTS_PATH_REMOVE | grep .scr$ | sed "s/\.scr//"); complete -W "$list4ime_compile" ime_compile
