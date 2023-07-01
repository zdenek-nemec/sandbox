#!/bin/bash
#
# Name: stp_sequence_check.sh
#
# Synopsis:
#     stp_sequence_check.sh [-h] [-p PATH]
#
# Examples:
#     stp_sequence_check.sh -h
#     stp_sequence_check.sh
#     stp_sequence_check.sh -p ./testing/tc01
#
# Description:
#     Sequence number check in STP archive from today and yesterday. Default
#     path to archive is /cdr_archive/INPUT/A_RR/RR.
#
#     -h, --help
#         Show this help message and exit
#     -p PATH, --path PATH
#         Use provided path to archive instead of the default one
#

DEFAULT_ARCHIVE_PATH=/cdr_archive/INPUT/A_RR/RR

function print_usage {
    echo "Usage: ${BASH_SOURCE##*/} [-h] [-p PATH]"
    echo "Try \`${BASH_SOURCE##*/} --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

if [[ $# == 1 && ($1 == "-h" || $1 == "--help") ]]; then
    print_help
    exit 0
elif [[ $# == 0 ]]; then
    archive_path=$DEFAULT_ARCHIVE_PATH
elif [[ $# == 2 && ($1 == "-p" || $1 == "--path") ]]; then
    archive_path=$2
else
    echo "ERROR: Invalid arguments"
    print_usage
    exit -1
fi

if [ ! -d $archive_path ]; then
    echo "ERROR: Invalid archive path $archive_path"
    exit -1
fi

date
archive_date_yesterday=$(date -d "1 day ago" "+%Y%m%d")
archive_date_today=$(date "+%Y%m%d")
for source in STP_BO STP_PH; do
    echo -n "$source $archive_date_yesterday+$archive_date_today:"
    seq_numbers=$(ls $archive_path/$archive_date_yesterday $archive_path/$archive_date_today | grep $source | cut -c 37-42)
    seq_numbers_sorted=$(echo "$seq_numbers" | sort | uniq)
    if [[ $seq_numbers ]]; then
        seq_start=$(echo "$seq_numbers" | head -1)
        seq_end=$(echo "$seq_numbers" | tail -1)
        echo " checking sequence $seq_start-$seq_end"
        diff --side-by-side --suppress-common-lines <(echo "$seq_numbers_sorted") <(seq  $seq_start $seq_end) | grep ">" | awk '{print "WARNING, missing sequence number: " $2}'
    else
        echo " no data"
    fi
done
