#!/bin/bash
#
# Name: set_portal.sh
#
# Synopsis:
#     set_portal.sh [-h] [-s SELECTOR] [-p PATH] [-l LAST] [-n NEXT]
#
# Examples:
#     set_portal.sh
#     set_portal.sh -s ZDENEK
#     set_portal.sh -s ZDENEK[78]
#     set_portal.sh -s "ZDENEK[78]\|.*PUT|ZDENEK\|"
#     set_portal.sh -s O_OCSR -l 0 -n 0
#     set_portal.sh -s O_OCSR -p /some/path
#     set_portal.sh -h
#
# Description:
#     Shell script for setting up Intermediate portals.
#
#     -h, --help
#         Show this help message and exit
#     -s SELECTOR, --selector SELECTOR
#         Grep expression for selecting the portals
#     -p PATH, --path PATH
#         Set primary routing path
#     -l LAST, --last LAST
#         Set last sequence number
#     -n NEXT, --next NEXT
#         Set next sequence number
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
        -s|--selector)
            [ -z $2 ] && echo "Error: Missing selector" 1>&2 && print_usage && exit -1
            selector="$2"
            shift
            shift
            ;;
        -p|--path)
            [ -z $2 ] && echo "Error: Missing routing path" 1>&2 && print_usage && exit -1
            routing_path="$2"
            shift
            shift
            ;;
        -l|--last)
            [ -z $2 ] && echo "Error: Missing last sequence" 1>&2 && print_usage && exit -1
            sequence_last="$2"
            shift
            shift
            ;;
        -n|--next)
            [ -z $2 ] && echo "Error: Missing next sequence" 1>&2 && print_usage && exit -1
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

echo "Selector: $selector"
echo "Routing Path: $routing_path"
echo "Last Sequence: $sequence_last"
echo "Next Sequence: $sequence_next"

if [[ -z $selector ]]; then
    echo "All portals"
fi

if [[ -z $routing_path  && -z $sequence_last && -z $sequence_next ]]; then
    echo "Nothing to setup"
fi

portals=$(cat cetin_portals.txt | grep -E $selector)
for portal in $portals; do
    echo $portal;
done
