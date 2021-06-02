#!/bin/bash
#
# Name: set_portal.sh
#
# Synopsis:
#     set_portal.sh [-h]
#
# Examples:
#     set_portal.sh
#     set_portal.sh -h
#
# Description:
#     Shell script for setting up Intermediate portals.
#
#     -h, --help
#         Show this help message and exit
#

function print_usage {
    echo "Usage: `basename $0` [-h]"
    echo "Try \``basename $0` --help' for more information."
}

function print_help {
    head -`grep -n -m 1 -v "^#" "$0" | cut -d ":" -f 1` "$0"
}

while [[ $# -gt 0 ]]; do
    option="$1"
    case $option in
        -h|--help)
            shift
            print_help
            exit 0
            ;;
        -s|--system)
            [ -z $2 ] && echo "Error: Missing system" && print_usage && exit -1
            system="$2"
            shift
            shift
            ;;
        --portal)
            [ -z $2 ] && echo "Error: Missing portal" && print_usage && exit -1
            portal="$2"
            shift
            shift
            ;;
        --path)
            [ -z $2 ] && echo "Error: Missing routing path" && print_usage && exit -1
            routing_path="$2"
            shift
            shift
            ;;
        --last)
            [ -z $2 ] && echo "Error: Missing last sequence" && print_usage && exit -1
            sequence_last="$2"
            shift
            shift
            ;;
        --next)
            [ -z $2 ] && echo "Error: Missing next sequence" && print_usage && exit -1
            sequence_next="$2"
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

echo "System: $system"
echo "Portal: $portal"
echo "Routing Path: $routing_path"
echo "Last Sequence: $sequence_last"
echo "Next Sequence: $sequence_next"
