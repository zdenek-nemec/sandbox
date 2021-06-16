#!/bin/bash
#
# Name: set_shell_prompt.sh
#
# Synopsis:
#     set_shell_prompt.sh [-h] -p {FULL,SHORT}
#
# Examples:
#     set_portal.sh -h
#     set_portal.sh -p FULL
#     set_portal.sh -p SHORT
#
# Description:
#     Set shell prompt (variable PS1).
#
#     Must be run as a sourced script
#         `. ./set_portals.sh'
#
#     -h, --help
#         Show this help message and exit
#     -p {FULL,SHORT}, --path {FULL,SHORT}
#

function print_usage {
    echo "Usage: `basename $0` [-h] -p {FULL,SHORT}"
    echo "Try \``basename $0` --help' for more information."
}

function print_help {
    head -`grep -n -m 1 -v "^#" "$0" | cut -d ":" -f 1` "$0"
}

run_script=1

while [[ $# -gt 0 ]]; do
    option="$1"
    case $option in
        -h|--help)
            print_help
            unset run_script
            shift
            ;;
        -p|--path)
            if [[ -z $2 ]]; then
                echo "Error: Missing path value" 1>&2
                print_usage
                unset run_script
            elif [[ $2 != "FULL" && $2 != "SHORT" ]]; then
                echo "Error: Invalid path value $2" 1>&2
                print_usage
                unset run_script
                shift
            else
                path="$2"
                shift
            fi
            shift
            ;;
        *)
            echo "Error: Unexpected arguments" 1>&2
            print_usage
            unset run_script
            shift
            ;;
    esac
done

default_colour="\033[0m"
if [[ $HOSTNAME == "av2l377p" ]]; then # Production = Red
    colour="\033[1;31m"
elif [[ $HOSTNAME == "avl2783t" ]]; then # Development = Green
    colour="\033[1;32m"
elif [[ $HOSTNAME == "avl2807t" ]]; then # Test = Blue
    colour="\033[1;34m"
elif [[ $HOSTNAME == "av3l378p" ]]; then # Standby = Yellow
    colour="\033[1;33m"
else
    colour=$default_colour
fi

if [[ $run_script ]]; then
    if [[ -z $path ]]; then
        echo "Error: Missing mandatory option path" 1>&2
        print_usage
        unset run_script
    elif [[ $path == "FULL" ]]; then
        PS1="\[${colour}\]\u@\h:\w]\\$\[${default_colour}\] "
    elif [[ $path == "SHORT" ]]; then
        PS1="\[${colour}\]\u@\h \W]\\$\[${default_colour}\] "
    else
        echo "Error: Unexpected option path" 1>&2
        print_usage
        unset run_script
    fi
fi

export PS1
