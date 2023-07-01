#!/bin/bash
#
# Name: test_stp_sequence_check.sh
#
# Synopsis:
#     test_stp_sequence_check.sh [-h]
#
# Examples:
#     test_stp_sequence_check.sh -h
#     test_stp_sequence_check.sh
#
# Description:
#     Test stp_sequence_check.sh script.
#
#     -h, --help
#         Show this help message and exit
#

function print_usage {
    echo "Usage: ${BASH_SOURCE##*/} [-h]"
    echo "Try \`${BASH_SOURCE##*/} --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

if [[ $# == 1 && ($1 == "-h" || $1 == "--help") ]]; then
    print_help
    exit 0
elif [[ ! $# == 0 ]]; then
    echo "ERROR: Invalid arguments"
    print_usage
    exit -1
fi

parent_directory=${PWD##*/}
parent_directory=${parent_directory:-/}
if [ $parent_directory != "stp_sequence_check" ]; then
    echo "ERROR: This test can be run only from stp_sequence_check root directory"
    exit -1
fi

if [[ -d "./testing" ]]; then
    echo "Testing directory exists already, removing"
    rm -rf ./testing
fi

date_yesterday=$(date -d "1 day ago" "+%Y%m%d")
date_today=$(date "+%Y%m%d")

echo "Testing started"
exit 0
echo "TC01 - Unbroken sequence"
mkdir -p ./testing/tc01/$date_yesterday
touch ./testing/tc01/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/tc01/$date_yesterday/${date_yesterday}_020000_STP_PH_${date_yesterday}hhmm-500002.gz
touch ./testing/tc01/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-500003.gz
touch ./testing/tc01/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-500004.gz
touch ./testing/tc01/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-500005.gz
touch ./testing/tc01/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-500006.gz
mkdir -p ./testing/tc01/$date_today
touch ./testing/tc01/$date_today/${date_today}_070000_STP_PH_${date_today}hhmm-500007.gz
touch ./testing/tc01/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/tc01/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing/tc01
echo ""

echo "TC02 - Broken sequence"
mkdir -p ./testing/tc02/$date_yesterday
touch ./testing/tc02/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/tc02/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-500003.gz
touch ./testing/tc02/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-500006.gz
mkdir -p ./testing/tc02/$date_today
touch ./testing/tc02/$date_today/${date_today}_070000_STP_PH_${date_today}hhmm-500007.gz
touch ./testing/tc02/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/tc02/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing/tc02
echo ""

echo "TC03 - Broken sequence completed"
mkdir -p ./testing/tc03/$date_yesterday
touch ./testing/tc03/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/tc03/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-500003.gz
touch ./testing/tc03/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-500006.gz
mkdir -p ./testing/tc03/$date_today
touch ./testing/tc03/$date_today/${date_today}_070000_STP_PH_${date_today}hhmm-500007.gz
touch ./testing/tc03/$date_today/${date_today}_073002_STP_PH_${date_today}hhmm-500002.gz
touch ./testing/tc03/$date_today/${date_today}_073004_STP_PH_${date_today}hhmm-500004.gz
touch ./testing/tc03/$date_today/${date_today}_073005_STP_PH_${date_today}hhmm-500005.gz
touch ./testing/tc03/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/tc03/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing/tc03
echo ""

echo "TC04 - Unbroken sequence and more"
mkdir -p ./testing/tc04/$date_yesterday
touch ./testing/tc04/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/tc04/$date_yesterday/${date_yesterday}_020000_STP_PH_${date_yesterday}hhmm-500002.gz
touch ./testing/tc04/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-500003.gz
touch ./testing/tc04/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-500004.gz
touch ./testing/tc04/$date_yesterday/${date_yesterday}_043000_STP_PH_${date_yesterday}hhmm-666001.gz
touch ./testing/tc04/$date_yesterday/${date_yesterday}_043000_STP_PH_${date_yesterday}hhmm-666002.gz
touch ./testing/tc04/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-500005.gz
touch ./testing/tc04/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-500006.gz
mkdir -p ./testing/tc04/$date_today
touch ./testing/tc04/$date_today/${date_today}_070000_STP_PH_${date_today}hhmm-500007.gz
touch ./testing/tc04/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/tc04/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing/tc04
echo ""

echo "TC05 - Unbroken sequence with rollover"
mkdir -p ./testing/tc05/$date_yesterday
touch ./testing/tc05/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-999997.gz
touch ./testing/tc05/$date_yesterday/${date_yesterday}_020000_STP_PH_${date_yesterday}hhmm-999998.gz
touch ./testing/tc05/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-999999.gz
touch ./testing/tc05/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-000000.gz
touch ./testing/tc05/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-000001.gz
touch ./testing/tc05/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-000002.gz
mkdir -p ./testing/tc05/$date_today
touch ./testing/tc05/$date_today/${date_today}_070000_STP_PH_${date_today}hhmm-000003.gz
touch ./testing/tc05/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-000004.gz
touch ./testing/tc05/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-000005.gz
./stp_sequence_check.sh --path ./testing/tc05
echo ""

echo "TC06 - Broken sequence with rollover"
mkdir -p ./testing/tc06/$date_yesterday
touch ./testing/tc06/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-999997.gz
touch ./testing/tc06/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-999999.gz
touch ./testing/tc06/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-000000.gz
touch ./testing/tc06/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-000001.gz
touch ./testing/tc06/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-000002.gz
mkdir -p ./testing/tc06/$date_today
touch ./testing/tc06/$date_today/${date_today}_070000_STP_PH_${date_today}hhmm-000003.gz
touch ./testing/tc06/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-000004.gz
touch ./testing/tc06/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-000005.gz
./stp_sequence_check.sh --path ./testing/tc06
echo ""

echo "Testing finished"
