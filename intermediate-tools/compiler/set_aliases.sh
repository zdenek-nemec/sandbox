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
list4ime_compile=$(find $SCRIPTS_PATH -maxdepth 1 -type f | sed $SCRIPTS_PATH_REMOVE | sed "s/\.scr//"); complete -W "$list4ime_compile" ime_compile
