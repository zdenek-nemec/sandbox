#!/bin/bash

echo "Hello, World!"

parent_dir=${PWD##*/}
parent_dir=${parent_dir:-/}
echo "$parent_dir"

if [[ "$parent_dir" != "stp_sequence_check" ]]; then
    echo "Wrong parent directory"
    exit -1
else
    echo "ok"
fi

if [[ -d "./testing" ]]; then
    echo "test dir present, removing"
    rm -rf ./testing
else
    echo "test dir missing, ok"
fi

date_yesterday=$(date -d "1 day ago" "+%Y%m%d")
date_today=$(date "+%Y%m%d")

# 20230628_120202_STP_PH_202306280819-612164.gz
# At least first sequence in the day and latest today's sequence must be correct

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
ls -1 ./testing/tc01/*/*
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
ls -1 ./testing/tc02/*/*
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
ls -1 ./testing/tc03/*/*
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
ls -1 ./testing/tc04/*/*
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
ls -1 ./testing/tc05/*/*
echo ""
