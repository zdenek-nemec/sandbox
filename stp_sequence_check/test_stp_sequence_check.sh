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
    echo "Error: Invalid arguments"
    print_usage
    exit -1
fi

parent_directory=${PWD##*/}
parent_directory=${parent_directory:-/}
if [ $parent_directory != "stp_sequence_check" ]; then
    echo "Error: This test can be run only from stp_sequence_check root directory"
    exit -1
fi

date_yesterday=$(date -d "1 day ago" "+%Y%m%d")
date_today=$(date "+%Y%m%d")

echo "Testing started"

echo "TC01 - Unbroken sequence: No alarms"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/$date_yesterday/${date_yesterday}_020000_STP_PH_${date_yesterday}hhmm-500002.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-500003.gz
touch ./testing/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-500004.gz
touch ./testing/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-500005.gz
touch ./testing/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-500006.gz
touch ./testing/$date_yesterday/${date_yesterday}_070000_STP_PH_${date_yesterday}hhmm-500007.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC02 - Broken sequence: Missing 500002, 500004, 500005 and 500006"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-500003.gz
touch ./testing/$date_yesterday/${date_yesterday}_070000_STP_PH_${date_yesterday}hhmm-500007.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC03 - Completed broken sequence: No alarms"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-500003.gz
touch ./testing/$date_yesterday/${date_yesterday}_070000_STP_PH_${date_yesterday}hhmm-500007.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/$date_today/${date_today}_083002_STP_PH_${date_today}hhmm-500002.gz
touch ./testing/$date_today/${date_today}_083004_STP_PH_${date_today}hhmm-500004.gz
touch ./testing/$date_today/${date_today}_083005_STP_PH_${date_today}hhmm-500005.gz
touch ./testing/$date_today/${date_today}_083006_STP_PH_${date_today}hhmm-500006.gz
touch ./testing/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC04 - Completed broken sequence day after: No alarms"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_080000_STP_PH_${date_yesterday}hhmm-500008.gz
touch ./testing/$date_yesterday/${date_yesterday}_083002_STP_PH_${date_yesterday}hhmm-500002.gz
touch ./testing/$date_yesterday/${date_yesterday}_083004_STP_PH_${date_yesterday}hhmm-500004.gz
touch ./testing/$date_yesterday/${date_yesterday}_083005_STP_PH_${date_yesterday}hhmm-500005.gz
touch ./testing/$date_yesterday/${date_yesterday}_083006_STP_PH_${date_yesterday}hhmm-500006.gz
touch ./testing/$date_yesterday/${date_yesterday}_090000_STP_PH_${date_yesterday}hhmm-500009.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_100000_STP_PH_${date_today}hhmm-500010.gz
touch ./testing/$date_today/${date_today}_110000_STP_PH_${date_today}hhmm-500011.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC05 - Unbroken sequence with rollover: Rollover warning"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-999997.gz
touch ./testing/$date_yesterday/${date_yesterday}_020000_STP_PH_${date_yesterday}hhmm-999998.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-999999.gz
touch ./testing/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-000000.gz
touch ./testing/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-000001.gz
touch ./testing/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-000002.gz
touch ./testing/$date_yesterday/${date_yesterday}_070000_STP_PH_${date_yesterday}hhmm-000003.gz
touch ./testing/$date_yesterday/${date_yesterday}_080000_STP_PH_${date_yesterday}hhmm-000004.gz
touch ./testing/$date_yesterday/${date_yesterday}_090000_STP_PH_${date_yesterday}hhmm-000005.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_100000_STP_PH_${date_today}hhmm-000006.gz
touch ./testing/$date_today/${date_today}_110000_STP_PH_${date_today}hhmm-000007.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC06 - Broken sequence with rollover: Rollover warning and missing 999998, 000002, 000003 and 000004"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-999997.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-999999.gz
touch ./testing/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-000000.gz
touch ./testing/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-000001.gz
touch ./testing/$date_yesterday/${date_yesterday}_090000_STP_PH_${date_yesterday}hhmm-000005.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_100000_STP_PH_${date_today}hhmm-000006.gz
touch ./testing/$date_today/${date_today}_110000_STP_PH_${date_today}hhmm-000007.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC07 - Broken sequence with rollover completed: Rollover warning"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-999997.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-999999.gz
touch ./testing/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-000000.gz
touch ./testing/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-000001.gz
touch ./testing/$date_yesterday/${date_yesterday}_090000_STP_PH_${date_yesterday}hhmm-000005.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_100000_STP_PH_${date_today}hhmm-000006.gz
touch ./testing/$date_today/${date_today}_103001_STP_PH_${date_today}hhmm-999998.gz
touch ./testing/$date_today/${date_today}_103002_STP_PH_${date_today}hhmm-000002.gz
touch ./testing/$date_today/${date_today}_103003_STP_PH_${date_today}hhmm-000003.gz
touch ./testing/$date_today/${date_today}_103004_STP_PH_${date_today}hhmm-000004.gz
touch ./testing/$date_today/${date_today}_110000_STP_PH_${date_today}hhmm-000007.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC08 - Only one file per day: No alarms"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_yesterday/${date_yesterday}_020000_STP_PH_${date_yesterday}hhmm-500002.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC09 - Multiple days with same sequence: Single sequence warning"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_010000_STP_PH_${date_today}hhmm-500001.gz
./stp_sequence_check.sh --path ./testing
rm -rf ./testing/*
echo ""

echo "TC10 - Unbroken sequences on both sources: No alarms"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_BO_${date_yesterday}hhmm-500001.gz
touch ./testing/$date_yesterday/${date_yesterday}_020000_STP_BO_${date_yesterday}hhmm-500002.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_BO_${date_yesterday}hhmm-500003.gz
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/$date_yesterday/${date_yesterday}_020000_STP_PH_${date_yesterday}hhmm-500002.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-500003.gz
touch ./testing/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-500004.gz
touch ./testing/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-500005.gz
touch ./testing/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-500006.gz
touch ./testing/$date_yesterday/${date_yesterday}_070000_STP_PH_${date_yesterday}hhmm-500007.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC11 - Broken sequence on one of the sources: Missing BO 500002"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_BO_${date_yesterday}hhmm-500001.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_BO_${date_yesterday}hhmm-500003.gz
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/$date_yesterday/${date_yesterday}_020000_STP_PH_${date_yesterday}hhmm-500002.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_PH_${date_yesterday}hhmm-500003.gz
touch ./testing/$date_yesterday/${date_yesterday}_040000_STP_PH_${date_yesterday}hhmm-500004.gz
touch ./testing/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-500005.gz
touch ./testing/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-500006.gz
touch ./testing/$date_yesterday/${date_yesterday}_070000_STP_PH_${date_yesterday}hhmm-500007.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing
echo ""

echo "TC12 - Broken sequences on both sources: Missing BO 500002, PH 500002, 500003 and 500004"
if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi
mkdir -p ./testing/$date_yesterday
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_BO_${date_yesterday}hhmm-500001.gz
touch ./testing/$date_yesterday/${date_yesterday}_030000_STP_BO_${date_yesterday}hhmm-500003.gz
touch ./testing/$date_yesterday/${date_yesterday}_010000_STP_PH_${date_yesterday}hhmm-500001.gz
touch ./testing/$date_yesterday/${date_yesterday}_050000_STP_PH_${date_yesterday}hhmm-500005.gz
touch ./testing/$date_yesterday/${date_yesterday}_060000_STP_PH_${date_yesterday}hhmm-500006.gz
touch ./testing/$date_yesterday/${date_yesterday}_070000_STP_PH_${date_yesterday}hhmm-500007.gz
mkdir -p ./testing/$date_today
touch ./testing/$date_today/${date_today}_080000_STP_PH_${date_today}hhmm-500008.gz
touch ./testing/$date_today/${date_today}_090000_STP_PH_${date_today}hhmm-500009.gz
./stp_sequence_check.sh --path ./testing
echo ""

if [[ -d "./testing" ]]; then
    rm -rf ./testing
fi

echo "Testing finished"
