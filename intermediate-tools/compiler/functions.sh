#!/bin/bash
#
# Name: functions.sh
#
# Synopsis:
#     functions.sh
#
# Examples:
#     functions.sh
#
# Description:
#     Collection of Bash functions intended for use by Intermediate compiler.
#     Import, do not run directly.
#

INTERMEDIATE=("avl4658t" "avl4688t" "avl4713p" "avl4715p")

print_usage () {
    invoker=$1
    echo "Usage: $(basename $invoker)"
    echo "Try \`$(basename $invoker) --help' for more information."
}

print_help () {
    invoker=$1
    head -$(grep -n -m 1 -v "^#" "$invoker" | cut -d ":" -f 1) "$invoker"
}

is_intermediate () {
    unset IS_INTERMEDIATE
    for item in ${INTERMEDIATE[@]}; do
        if [[ "$item" == "$HOSTNAME" ]]; then
            IS_INTERMEDIATE=1
            break
        fi
    done
}
