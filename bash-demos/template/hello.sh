#!/bin/bash
#
# Name: hello.sh
#
# Synopsis:
#     hello.sh [-h] [-n NAME] [-g {Hello,Hi}]
#
# Examples:
#     hello.sh
#     hello.sh -n Arcifrajer
#
# Description:
#     Hello, Arcifrajer!
#
#     -h, --help
#         Show this help message and exit
#     -n NAME, --name NAME
#         User's name
#     -g {Hello,Hi}, --greeting {Hello,Hi}
#         Specific greeting
#

DEFAULT_NAME="Frajer"
DEFAULT_GREETING="Hello"

function print_usage {
    echo "Usage: $(basename $BASH_SOURCE) [-h] [-n NAME] [-g {Hello,Hi}]"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

name=$DEFAULT_NAME
greeting=$DEFAULT_GREETING
while [[ $# -gt 0 ]]; do
    option="$1"
    case $option in
        -h|--help)
            print_help
            shift
            exit 0
            ;;
        -n|--name)
            [[ -z $2 ]] && echo "Error: Missing name value" 1>&2 && print_usage && exit -1
            name="$2"
            shift
            shift
            ;;
        -g|--greeting)
            [[ -z $2 ]] && echo "Error: Missing greeintg value" 1>&2 && print_usage && exit -1
            [[ $2 != "Hello" && $2 != "Hi" ]] && echo "Error: Invalid greeting value $2" 1>&2 && print_usage && exit -1
            greeting="$2"
            shift
            shift
            ;;
        *)
            echo "Error: Unexpected arguments" 1>&2
            print_usage
            shift
            exit -1
            ;;
    esac
done

echo "${greeting}, ${name}!"
