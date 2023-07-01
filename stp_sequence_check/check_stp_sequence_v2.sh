#!/bin/bash
#
# Name: check_stp_sequence.sh
#
# Synopsis:
#     check_stp_sequence.sh [ALTERNATIVE_PATH]
#
# Examples:
#     check_stp_sequence.sh
#     check_stp_sequence.sh /appl/cgi/dcs/data01_loc/tmp/x0562300/check_stp_sequence/testing/tc01_match
#
# Description:
#     Sequence number check in STP archive from today and yesterday. Default
#     archive path is /cdr_archive/INPUT/A_RR/RR.
#
#     ALTERNATIVE_PATH
#         Alternative archive path to use instead of default
#

function print_usage {
    echo "Usage: $(basename $BASH_SOURCE) [ALTERNATIVE_PATH]"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

if [[ "$#" == "1" && ("$1" == "-h" || "$1" == "--help") ]]; then
    print_help
    exit 0
elif [[ "$#" == "1" ]]; then
    rr_archive_path=$1
elif [[ "$#" == "0" ]]; then
    rr_archive_path=/cdr_archive/INPUT/A_RR/RR
else
    print_usage
    exit -1
fi

date
archive_date_yesterday=$(date -d "1 day ago" "+%Y%m%d")
archive_date_today=$(date "+%Y%m%d")
for source in STP_BO STP_PH; do
    echo -n "$source $archive_date_yesterday+$archive_date_today:"
    seq_numbers=$(ls $rr_archive_path/$archive_date_yesterday $rr_archive_path/$archive_date_today | grep $source | cut -c 37-42)
    seq_numbers_sorted=$(echo "$seq_numbers" | sort | uniq)
    if [[ $seq_numbers ]]; then
        seq_start=$(echo "$seq_numbers" | head -1)
        seq_end=$(echo "$seq_numbers" | tail -1)
        echo " checking sequence $seq_start--$seq_end"
        diff --side-by-side --suppress-common-lines <(echo "$seq_numbers_sorted") <(seq  $seq_start $seq_end) | grep ">" | awk '{print "WARNING, missing sequence number: " $2}'
    else echo " no data"
    fi
done
