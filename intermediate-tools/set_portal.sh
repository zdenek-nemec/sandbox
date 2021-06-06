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
    echo "Usage: $(basename $0) [-h] [-s SELECTOR] [-p PATH] [-l LAST] [-n NEXT]"
    echo "Try \`$(basename $0) --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$0" | cut -d ":" -f 1) "$0"
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

echo "Setting up:"
if [[ -z $routing_path  && -z $sequence_last && -z $sequence_next ]]; then
    echo "* nothing, displaying portals only"
fi
if [[ $routing_path ]]; then
    echo "* Routing > Path to $routing_path"
fi
if [[ $sequence_last ]]; then
    echo "* Output > Last Sequence Number to $sequence_last"
fi
if [[ $sequence_next ]]; then
    echo "* Output > Next Sequence Number to $sequence_next"
fi

echo "Selected portals:"
if [[ -z $selector ]]; then
    echo "* no selector specified, apply to all portals"
fi
portals=$(cat cetin_portals.txt | grep -E $selector) # For testing purposes only
for portal in $portals; do
    echo "* $portal"
done

read -p "Please confirm by pressing [Y] or [y]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "* approved"
else
    echo "* cancelled"
    exit 0
fi

query="xxx"
for portal in $portals; do
    if [[ $routing_path ]]; then
        query="${query}\nGET ROUTING FOR $portal"
        query="${query}\nSET PATH FOR $portal $routing_path"
    fi
    if [[ $sequence_last ]]; then
        query="${query}\nGET OUTPUT FOR $portal"
        query="${query}\nSET LAST FOR $portal $sequence_last"
    fi
    if [[ $sequence_next ]]; then
        query="${query}\nGET OUTPUT FOR $portal"
        query="${query}\nSET LAST FOR $portal $sequence_next"
    fi
done

echo $query
