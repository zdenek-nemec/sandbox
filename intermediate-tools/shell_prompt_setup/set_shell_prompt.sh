#!/bin/bash
#
# Name: set_shell_prompt.sh
#
# Synopsis:
#     set_shell_prompt.sh [-h] [-p {FULL,SHORT}] [-c {DEFAULT,RED,GREEN,YELLOW,BLUE,PURPLE}]
#
# Examples:
#     set_shell_prompt.sh -p FULL
#     set_shell_prompt.sh -p SHORT
#     set_shell_prompt.sh -c DEFAULT
#     set_shell_prompt.sh -c RED
#     set_shell_prompt.sh -p SHORT -c RED
#
# Description:
#     Set shell prompt (variable PS1).
#
#     Must be run as a sourced script
#         `. ./set_shell_prompt.sh'
#
#     -h, --help
#         Show this help message and exit
#     -p {FULL,SHORT}, --path {FULL,SHORT}
#         Show full/short path in the shell prompt
#     -c {RED,GREEN,YELLOW,BLUE,PURPLE}, --colour {RED,GREEN,YELLOW,BLUE,PURPLE}
#         Display shell prompt in specific colour
#

function print_usage {
    echo "Usage: set_shell_prompt.sh [-h] [-p {FULL,SHORT}] [-c {DEFAULT,RED,GREEN,YELLOW,BLUE,PURPLE}]"
    echo "Try \`set_shell_prompt.sh --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

ssp_run_script=1

while [[ $# -gt 0 ]]; do
    ssp_option="$1"
    case $ssp_option in
        -h|--help)
            print_help
            unset ssp_run_script
            shift
            ;;
        -p|--path)
            if [[ -z $2 ]]; then
                echo "Error: Missing path value" 1>&2
                print_usage
                unset ssp_run_script
            elif [[ $2 != "FULL" && $2 != "SHORT" ]]; then
                echo "Error: Invalid path value $2" 1>&2
                print_usage
                unset ssp_run_script
                shift
            else
                ssp_path="$2"
                shift
            fi
            shift
            ;;
        -c|--colour)
            if [[ -z $2 ]]; then
                echo "Error: Missing colour value" 1>&2
                print_usage
                unset ssp_run_script
            elif [[ $2 != "DEFAULT" && $2 != "RED" && $2 != "GREEN" && $2 != "YELLOW" && $2 != "BLUE" && $2 != "PURPLE" ]]; then
                echo "Error: Invalid colour value $2" 1>&2
                print_usage
                unset ssp_run_script
                shift
            else
                ssp_colour="$2"
                shift
            fi
            shift
            ;;
        *)
            echo "Error: Unexpected arguments" 1>&2
            print_usage
            unset ssp_run_script
            shift
            ;;
    esac
done

ssp_default_colour_code="\033[0m"
if [[ $ssp_colour == "RED" ]]; then
    ssp_colour_code="\033[1;31m"
elif [[ $ssp_colour == "GREEN" ]]; then
    ssp_colour_code="\033[1;32m"
elif [[ $ssp_colour == "YELLOW" ]]; then
    ssp_colour_code="\033[1;33m"
elif [[ $ssp_colour == "BLUE" ]]; then
    ssp_colour_code="\033[1;34m"
elif [[ $ssp_colour == "PURPLE" ]]; then
    ssp_colour_code="\033[1;35m"
else
    ssp_colour_code=$ssp_default_colour_code
fi

if [[ $ssp_run_script ]]; then
    if [[ -z $ssp_path && -z $ssp_colour ]]; then
        echo "No changes"
        unset ssp_run_script
    elif [[ -z $ssp_path ]]; then
        PS1=$(echo $PS1 | sed 's/\\\[\\033\[.;..m\\\]//g' | sed 's/\\\[\\033\[0m\\\]//g')
        PS1="\[${ssp_colour_code}\]$PS1\[${ssp_default_colour_code}\] "
    elif [[ $ssp_path == "FULL" ]]; then
        PS1="\[${ssp_colour_code}\][\u@\h:\w]\\$\[${ssp_default_colour_code}\] "
    elif [[ $ssp_path == "SHORT" ]]; then
        PS1="\[${ssp_colour_code}\][\u@\h \W]\\$\[${ssp_default_colour_code}\] "
    else
        echo "Error: Unexpected options" 1>&2
        print_usage
        unset ssp_run_script
    fi
fi

if [[ $ssp_run_script ]]; then
    export PS1
fi

[[ $ssp_run_script ]] && unset ssp_run_script
[[ $ssp_option ]] && unset ssp_option
[[ $ssp_path ]] && unset ssp_path
[[ $ssp_colour ]] && unset ssp_colour
[[ $ssp_default_colour_code ]] && unset ssp_default_colour_code
[[ $ssp_colour_code ]] && unset ssp_colour_code
