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

alias ime_compile=$IME_COMPILER
list4ime_compile=$(find $SCRIPTS_PATH -maxdepth 1 -type f | sed $SCRIPTS_PATH_REMOVE | sed "s/\.scr//"); complete -W "$list4ime_compile" ime_compile
