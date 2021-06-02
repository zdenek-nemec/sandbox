#!/bin/bash
#
# Name: script.sh
#
# Synopsis:
#     script.sh [-h] [-n NAME]
#
# Examples:
#     script.sh
#     script.sh -n Arcifrajer
#     script.sh -h
#
# Description:
#     Shell script for the Arcifrajer.
#
#     -h, --help
#         Show this help message and exit
#     -n NAME, --name NAME
#         User's name
#

DEFAULT_NAME="Frajer"

function print_usage {
    echo "Usage: `basename $0` [-h] [-n NAME]"
    echo "Try \``basename $0` --help' for more information."
}

function print_help {
    head -`grep -n -m 1 -v "^#" "$0" | cut -d ":" -f 1` "$0"
}

# # Help
# if [[ "$#" == "1" && ("$1" == "-h" || "$1" == "--help") ]]; then
#     print_help
#     exit 0
# fi

# # Arguments
# if [[ "$#" == "0" ]]; then
#     name=$DEFAULT_NAME
# elif [[ "$#" == "2" && ("$1" == "-n" || "$1" == "--name") ]]; then
#     name=$2
# else
#     echo "Error: Unexpected arguments" 1>&2
#     print_usage
#     exit -1
# fi


name=$DEFAULT_NAME
while [[ $# -gt 0 ]]; do
    option="$1"
    case $option in
        -h|--help)
            shift
            print_help
            exit 0
            ;;
        -n|--name)
            [ -z $2 ] && echo "error"; exit -1
            name="$2"
            shift
            shift
            ;;
        *)
            shift
            echo "Error: Unexpected arguments" 1>&2
            print_usage
            exit -1
            ;;
    esac
done



# Execute

echo "Hello, ${name}!"
