#!/bin/bash
#
# Name: run.sh
#
# Synopsis:
#     run.sh [-h]
#
# Examples:
#     run.sh
#
# Description:
#     Run SIP statistics check application
#
#     -h, --help
#         Show this help message and exit
#

WORK_PATH=/appl/cgi/dcs/data01/TOOLS/sip_statistics_check

function print_usage {
    echo "Usage: $(basename $BASH_SOURCE) [-h]"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

if [[ "$#" == "1" && ("$1" == "-h" || "$1" == "--help") ]]; then
    print_help
    exit 0
elif [[ "$#" != "0" ]]; then
    print_usage
    exit -1
fi

cd $WORK_PATH
echo "$(date '+%Y-%m-%d %H:%M:%S') - SIP statistics check started" >> run.log
python3 sip_statistics_check.py >> run.log
echo "$(date '+%Y-%m-%d %H:%M:%S') - SIP statistics check finished" >> run.log
