#!/bin/bash
#
# Name: archive.sh
#
# Synopsis:
#     archive.sh
#
# Examples:
#     archive.sh
#
# Description:
#     Create and distribute TAR archives of input files collected by Mediation.
#
#     -h, --help
#         Show this help message and exit
#

INTERMEDIATE=("avl4658t" "avl4688t" "avl4713p" "avl4715p")
REQUIRED_PYTHONHOME=/dcs/data01/SOFTWARE/Python/Python-3.7.8
REQUIRED_PYTHONPATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/lib
REQUIRED_PATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/bin

print_usage () {
    echo "Usage: $(basename $BASH_SOURCE)"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

print_help () {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

cd $(dirname $BASH_SOURCE)
if [[ $# == 1 && ("$1" == "-h" || "$1" == "--help") ]]; then
    print_help
    exit 0
elif [[ $# != 0 ]]; then
    echo "Error: Unexpected arguments" 1>&2
    print_usage
    exit -1
fi

for item in ${INTERMEDIATE[@]}; do
    if [[ "$item" == "$HOSTNAME" ]]; then
        PYTHONHOME=$REQUIRED_PYTHONHOME
        export PYTHONHOME
        PYTHONPATH=$REQUIRED_PYTHONPATH
        export PYTHONPATH
        PATH=$REQUIRED_PATH:$PATH
        export PATH
        break
    fi
done

python archive.py
