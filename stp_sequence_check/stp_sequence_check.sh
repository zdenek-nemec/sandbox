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
#     stp_sequence_check.sh -p ./testing
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

print_usage() {
    echo "Usage: ${BASH_SOURCE[0]##*/} [-h] [-p PATH]"
    echo "Try \`${BASH_SOURCE[0]##*/} --help' for more information."
}

print_help() {
    local rows
    rows=$(grep -n -m 1 -v "^#" "${BASH_SOURCE[0]}")
    head -"${rows%:}" "${BASH_SOURCE[0]}"
}

check_sequence() {
    local seq_start=$1
    local seq_end=$2
    diff --side-by-side --suppress-common-lines \
        <(echo "$seq_nums_sorted") \
        <(seq -w "$seq_start" "$seq_end") \
        | grep ">" | awk '{print "Warning: Missing sequence number " $2}'
}

if [[ $# == 0 ]]; then
    archive_path=$DEFAULT_ARCHIVE_PATH
elif [[ $# == 1 && ($1 == "-h" || $1 == "--help") ]]; then
    print_help
    exit 0
elif [[ $# == 2 && ($1 == "-p" || $1 == "--path") ]]; then
    archive_path=$2
else
    echo "Error: Unexpected arguments" 1>&2
    print_usage
    exit 1
fi

if [[ ! -d $archive_path ]]; then
    echo "Error: Invalid archive path $archive_path" 1>&2
    exit 1
fi

date
yesterday=$(date -d "1 day ago" "+%Y%m%d")
today=$(date "+%Y%m%d")
for source in STP_BO STP_PH; do
    echo -n "$source $yesterday+$today:"
    seq_nums=$(find testing/20230630 testing/20230701 -type f -name "*$source*" -printf "%f\n" | cut -c 37-42)
    seq_nums_sorted=$(echo "$seq_nums" | sort | uniq)
    if [[ $seq_nums ]]; then
        seq_start=${seq_nums%%[[:space:]]*}
        seq_end=${seq_nums##*[[:space:]]}
        echo " checking sequence $seq_start-$seq_end"
        if [[ $seq_start -eq $seq_end ]]; then
            echo "Warning: Both the first and the last sequence numbers are the same ($seq_start)"
        elif [[ $seq_start < $seq_end ]]; then
            check_sequence "$seq_start" "$seq_end"
        elif [[ $seq_start > $seq_end ]]; then
            echo "Warning: Rollover detected"
            check_sequence "$seq_start" 999999
            check_sequence 000000 "$seq_end"
        else
            echo "Error: Unknown error" 1>&2
        fi
    else
        echo " no data"
    fi
done
