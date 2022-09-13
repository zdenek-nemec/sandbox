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
#     Bla
#
#     -h, --help
#         Show this help message and exit
#

if [[ "$HOSTNAME" == "N007510" ]]; then
    # PATH_TO_SCRIPTS="./tests"
    # ESCAPED_PATH_TO_SCRIPTS='s/\.\/tests\///g'
    PATH_TO_SCRIPTS="/c/Zdenek/_tmp/IntermediateScripts"
    ESCAPED_PATH_TO_SCRIPTS='s/\/c\/Zdenek\/_tmp\/IntermediateScripts\///g'
    IME_COMPILER='./compile.sh'
else
    PATH_TO_SCRIPTS="/dcs/appl01/var_dcs_9.0_db/cgdc/src"
    ESCAPED_PATH_TO_SCRIPTS='s/\/dcs\/appl01\/var_dcs_9\.0_db\/cgdc\/src\///g'
    IME_COMPILER='/dcs/data01/SOFTWARE/Tools/compile.sh'
fi

alias ime_compile=$IME_COMPILER
list4ime_compile=$(find $PATH_TO_SCRIPTS -maxdepth 1 -type f | sed $ESCAPED_PATH_TO_SCRIPTS); complete -W "$list4ime_compile" ime_compile
