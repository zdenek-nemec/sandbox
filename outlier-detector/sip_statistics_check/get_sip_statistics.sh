#!/bin/bash
#
# Name: get_sip_statistics.sh
#
# Synopsis:
#     get_sip_statistics.sh [-h]
#
# Examples:
#     get_sip_statistics.sh
#
# Description:
#     Get SIP statistics data from archived files
#
#     -h, --help
#         Show this help message and exit
#

ARCHIVE_PATH=/cdr_archive/INPUT/A_SIP
STATISTICS_PATH=/appl/cgi/dcs/data01/TOOLS/sip_statistics_check/data
HOURS_TO_CHECK=3

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

for i in $(seq 0 $HOURS_TO_CHECK); do
    timestamp=$(date +%Y%m%d_%H -d "$i hour ago")
    day=${timestamp:0:8}
    hour=${timestamp:9:2}
    statistics_file=$STATISTICS_PATH/sip_${day}_${hour}.csv
    echo "#Records,Hour,Month,Day,Year" > $statistics_file
    zcat \
        $ARCHIVE_PATH/${day}_$hour*.gz \
        $ARCHIVE_PATH/$day/${day}_$hour*.gz \
        $ARCHIVE_PATH/$day/$day/${day}_$hour*.gz \
        2>/dev/null \
        | cut -d "," -f 12 \
        | fgrep -v "00:00:00.000 UTC Jan 01 1970" \
        | cut -c 1-3,19- \
        | sort \
        | uniq -c \
        | sed '/^\ *$/d; s/"//g; s/^ *//g; s/ /,/g' \
        >> $statistics_file
done
