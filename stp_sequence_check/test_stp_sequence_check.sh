#!/bin/bash
#
# Name: test_stp_sequence_check.sh
#
# Synopsis:
#     test_stp_sequence_check.sh [-h] [-t TEST]
#
# Examples:
#     test_stp_sequence_check.sh -h
#     test_stp_sequence_check.sh
#     test_stp_sequence_check.sh -t 1
#
# Description:
#     Test stp_sequence_check.sh script.
#
#     -h, --help
#         Show this help message and exit
#     -t TEST, --test TEST
#         Run specific test case
#

print_usage() {
    echo "Usage: ${BASH_SOURCE[0]##*/} [-h] [-t TEST]"
    echo "Try \`${BASH_SOURCE[0]##*/} --help' for more information."
}

print_help() {
    local rows
    rows=$(grep -n -m 1 -v "^#" "${BASH_SOURCE[0]}")
    head -"${rows%:}" "${BASH_SOURCE[0]}"
}

if [[ $# == 1 && ($1 == "-h" || $1 == "--help") ]]; then
    print_help
    exit 0
elif [[ $# == 2 && ($1 == "-t" || $1 == "--test") ]]; then
    test_case=$2
elif [[ $# != 0 ]]; then
    echo "Error: Unexpected arguments" 1>&2
    print_usage
    exit 1
fi

parent_directory=${PWD##*/}
parent_directory=${parent_directory:-/}
if [[ $parent_directory != "stp_sequence_check" ]]; then
    echo "Error: This test can be run only from stp_sequence_check root directory" 1>&2
    exit 1
fi

echo "Testing started"
result=""
yesterday=$(date -d "1 day ago" "+%Y%m%d")
today=$(date "+%Y%m%d")
echo ""

if [[ -z $test_case || $test_case == 1 ]]; then
    echo "TC01 - Unbroken sequence - No alarms"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-500001.gz"
    touch "./testing/$yesterday/${yesterday}_020000_STP_PH_${yesterday}hhmm-500002.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_PH_${yesterday}hhmm-500003.gz"
    touch "./testing/$yesterday/${yesterday}_040000_STP_PH_${yesterday}hhmm-500004.gz"
    touch "./testing/$yesterday/${yesterday}_050000_STP_PH_${yesterday}hhmm-500005.gz"
    touch "./testing/$yesterday/${yesterday}_060000_STP_PH_${yesterday}hhmm-500006.gz"
    touch "./testing/$yesterday/${yesterday}_070000_STP_PH_${yesterday}hhmm-500007.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_080000_STP_PH_${today}hhmm-500008.gz"
    touch "./testing/$today/${today}_090000_STP_PH_${today}hhmm-500009.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: no data$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 500001-500009$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 0 ]] && echo "* Failed, warnings" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 2 ]]; then
    echo "TC02 - Broken sequence - Missing sequence numbers"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-500001.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_PH_${yesterday}hhmm-500003.gz"
    touch "./testing/$yesterday/${yesterday}_070000_STP_PH_${yesterday}hhmm-500007.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_080000_STP_PH_${today}hhmm-500008.gz"
    touch "./testing/$today/${today}_090000_STP_PH_${today}hhmm-500009.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: no data$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 500001-500009$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 4 ]] && echo "* Failed, number of warnings" && failed=true
    [[ $(grep "^Warning: Missing sequence number .*$" test_stp_sequence_check.log | cut -d " " -f 5) != "500002"*"500004"*"500005"*"500006" ]] && echo "* Failed, sequence numbers" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 3 ]]; then
    echo "TC03 - Completed broken sequence - No alarms"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-500001.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_PH_${yesterday}hhmm-500003.gz"
    touch "./testing/$yesterday/${yesterday}_070000_STP_PH_${yesterday}hhmm-500007.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_080000_STP_PH_${today}hhmm-500008.gz"
    touch "./testing/$today/${today}_083002_STP_PH_${today}hhmm-500002.gz"
    touch "./testing/$today/${today}_083004_STP_PH_${today}hhmm-500004.gz"
    touch "./testing/$today/${today}_083005_STP_PH_${today}hhmm-500005.gz"
    touch "./testing/$today/${today}_083006_STP_PH_${today}hhmm-500006.gz"
    touch "./testing/$today/${today}_090000_STP_PH_${today}hhmm-500009.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: no data$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 500001-500009$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 0 ]] && echo "* Failed, warnings" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 4 ]]; then
    echo "TC04 - Completed broken sequence day after - No alarms"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_080000_STP_PH_${yesterday}hhmm-500008.gz"
    touch "./testing/$yesterday/${yesterday}_083002_STP_PH_${yesterday}hhmm-500002.gz"
    touch "./testing/$yesterday/${yesterday}_083004_STP_PH_${yesterday}hhmm-500004.gz"
    touch "./testing/$yesterday/${yesterday}_083005_STP_PH_${yesterday}hhmm-500005.gz"
    touch "./testing/$yesterday/${yesterday}_083006_STP_PH_${yesterday}hhmm-500006.gz"
    touch "./testing/$yesterday/${yesterday}_090000_STP_PH_${yesterday}hhmm-500009.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_100000_STP_PH_${today}hhmm-500010.gz"
    touch "./testing/$today/${today}_110000_STP_PH_${today}hhmm-500011.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: no data$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 500008-500011$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 0 ]] && echo "* Failed, warnings" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 5 ]]; then
    echo "TC05 - Unbroken sequence with rollover - Rollover warning"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-999997.gz"
    touch "./testing/$yesterday/${yesterday}_020000_STP_PH_${yesterday}hhmm-999998.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_PH_${yesterday}hhmm-999999.gz"
    touch "./testing/$yesterday/${yesterday}_040000_STP_PH_${yesterday}hhmm-000000.gz"
    touch "./testing/$yesterday/${yesterday}_050000_STP_PH_${yesterday}hhmm-000001.gz"
    touch "./testing/$yesterday/${yesterday}_060000_STP_PH_${yesterday}hhmm-000002.gz"
    touch "./testing/$yesterday/${yesterday}_070000_STP_PH_${yesterday}hhmm-000003.gz"
    touch "./testing/$yesterday/${yesterday}_080000_STP_PH_${yesterday}hhmm-000004.gz"
    touch "./testing/$yesterday/${yesterday}_090000_STP_PH_${yesterday}hhmm-000005.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_100000_STP_PH_${today}hhmm-000006.gz"
    touch "./testing/$today/${today}_110000_STP_PH_${today}hhmm-000007.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: no data$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 999997-000007$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, number of warnings" && failed=true
    [[ $(grep -c "^Warning: Rollover detected$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, rollover warning" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 6 ]]; then
    echo "TC06 - Broken sequence with rollover - Rollover warning and missing sequence numbers"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-999997.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_PH_${yesterday}hhmm-999999.gz"
    touch "./testing/$yesterday/${yesterday}_040000_STP_PH_${yesterday}hhmm-000000.gz"
    touch "./testing/$yesterday/${yesterday}_050000_STP_PH_${yesterday}hhmm-000001.gz"
    touch "./testing/$yesterday/${yesterday}_090000_STP_PH_${yesterday}hhmm-000005.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_100000_STP_PH_${today}hhmm-000006.gz"
    touch "./testing/$today/${today}_110000_STP_PH_${today}hhmm-000007.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: no data$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 999997-000007$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 5 ]] && echo "* Failed, number of warnings" && failed=true
    [[ $(grep -c "^Warning: Rollover detected$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, rollover warning" && failed=true
    [[ $(grep "^Warning: Missing sequence number .*$" test_stp_sequence_check.log | cut -d " " -f 5) != "999998"*"000002"*"000003"*"000004" ]] && echo "* Failed, sequence numbers" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 7 ]]; then
    echo "TC07 - Broken sequence with rollover completed - Rollover warning"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-999997.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_PH_${yesterday}hhmm-999999.gz"
    touch "./testing/$yesterday/${yesterday}_040000_STP_PH_${yesterday}hhmm-000000.gz"
    touch "./testing/$yesterday/${yesterday}_050000_STP_PH_${yesterday}hhmm-000001.gz"
    touch "./testing/$yesterday/${yesterday}_090000_STP_PH_${yesterday}hhmm-000005.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_100000_STP_PH_${today}hhmm-000006.gz"
    touch "./testing/$today/${today}_103001_STP_PH_${today}hhmm-999998.gz"
    touch "./testing/$today/${today}_103002_STP_PH_${today}hhmm-000002.gz"
    touch "./testing/$today/${today}_103003_STP_PH_${today}hhmm-000003.gz"
    touch "./testing/$today/${today}_103004_STP_PH_${today}hhmm-000004.gz"
    touch "./testing/$today/${today}_110000_STP_PH_${today}hhmm-000007.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: no data$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 999997-000007$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, number of warnings" && failed=true
    [[ $(grep -c "^Warning: Rollover detected$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, rollover warning" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 8 ]]; then
    echo "TC08 - Only one file per day - No alarms"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-500001.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_020000_STP_PH_${today}hhmm-500002.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: no data$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 500001-500002$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 0 ]] && echo "* Failed, warnings" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 9 ]]; then
    echo "TC09 - Multiple days with same sequence - Single sequence warning"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-500001.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_010000_STP_PH_${today}hhmm-500001.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: no data$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 500001-500001$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, number of warnings" && failed=true
    [[ $(grep -c "^Warning: Both the first and the last sequence numbers are the same .*$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, same sequence warning" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 10 ]]; then
    echo "TC10 - Unbroken sequences on both sources - No alarms"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_BO_${yesterday}hhmm-500001.gz"
    touch "./testing/$yesterday/${yesterday}_020000_STP_BO_${yesterday}hhmm-500002.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_BO_${yesterday}hhmm-500003.gz"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-500001.gz"
    touch "./testing/$yesterday/${yesterday}_020000_STP_PH_${yesterday}hhmm-500002.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_PH_${yesterday}hhmm-500003.gz"
    touch "./testing/$yesterday/${yesterday}_040000_STP_PH_${yesterday}hhmm-500004.gz"
    touch "./testing/$yesterday/${yesterday}_050000_STP_PH_${yesterday}hhmm-500005.gz"
    touch "./testing/$yesterday/${yesterday}_060000_STP_PH_${yesterday}hhmm-500006.gz"
    touch "./testing/$yesterday/${yesterday}_070000_STP_PH_${yesterday}hhmm-500007.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_080000_STP_PH_${today}hhmm-500008.gz"
    touch "./testing/$today/${today}_090000_STP_PH_${today}hhmm-500009.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: checking sequence 500001-500003$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 500001-500009$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 0 ]] && echo "* Failed, warnings" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 11 ]]; then
    echo "TC11 - Broken sequence on one of the sources - Missing sequence number"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_BO_${yesterday}hhmm-500001.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_BO_${yesterday}hhmm-500003.gz"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-500001.gz"
    touch "./testing/$yesterday/${yesterday}_020000_STP_PH_${yesterday}hhmm-500002.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_PH_${yesterday}hhmm-500003.gz"
    touch "./testing/$yesterday/${yesterday}_040000_STP_PH_${yesterday}hhmm-500004.gz"
    touch "./testing/$yesterday/${yesterday}_050000_STP_PH_${yesterday}hhmm-500005.gz"
    touch "./testing/$yesterday/${yesterday}_060000_STP_PH_${yesterday}hhmm-500006.gz"
    touch "./testing/$yesterday/${yesterday}_070000_STP_PH_${yesterday}hhmm-500007.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_080000_STP_PH_${today}hhmm-500008.gz"
    touch "./testing/$today/${today}_090000_STP_PH_${today}hhmm-500009.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: checking sequence 500001-500003$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 500001-500009$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, number of warnings" && failed=true
    [[ $(grep -c "^Warning: Missing sequence number 500002$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, sequence number" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 12 ]]; then
    echo "TC12 - Broken sequences on both sources - Missing sequence numbers"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_BO_${yesterday}hhmm-500001.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_BO_${yesterday}hhmm-500003.gz"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-500001.gz"
    touch "./testing/$yesterday/${yesterday}_050000_STP_PH_${yesterday}hhmm-500005.gz"
    touch "./testing/$yesterday/${yesterday}_060000_STP_PH_${yesterday}hhmm-500006.gz"
    touch "./testing/$yesterday/${yesterday}_070000_STP_PH_${yesterday}hhmm-500007.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_080000_STP_PH_${today}hhmm-500008.gz"
    touch "./testing/$today/${today}_090000_STP_PH_${today}hhmm-500009.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: checking sequence 500001-500003$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 500001-500009$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 4 ]] && echo "* Failed, number of warnings" && failed=true
    [[ $(grep "^Warning: Missing sequence number .*$" test_stp_sequence_check.log | cut -d " " -f 5) != "500002"*"500002"*"500003"*"500004" ]] && echo "* Failed, sequence numbers" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 13 ]]; then
    echo "TC13 - Unbroken sequences on both sources with rollovers - Rollover warnings"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_BO_${yesterday}hhmm-999999.gz"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-999999.gz"
    touch "./testing/$yesterday/${yesterday}_020000_STP_PH_${yesterday}hhmm-000000.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_010000_STP_BO_${today}hhmm-000000.gz"
    touch "./testing/$today/${today}_010000_STP_PH_${today}hhmm-000001.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: checking sequence 999999-000000$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 999999-000001$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 2 ]] && echo "* Failed, warnings" && failed=true
    [[ $(grep -c "^Warning: Rollover detected$" test_stp_sequence_check.log) != 2 ]] && echo "* Failed, rollover warning" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -z $test_case || $test_case == 14 ]]; then
    echo "TC14 - Broken sequences on both sources with rollovers - Rollover warnings and missing sequence numbers"
    if [[ -d ./testing ]]; then
        rm -rf ./testing
    fi
    mkdir -p "./testing/$yesterday"
    touch "./testing/$yesterday/${yesterday}_010000_STP_BO_${yesterday}hhmm-999999.gz"
    touch "./testing/$yesterday/${yesterday}_010000_STP_PH_${yesterday}hhmm-999999.gz"
    touch "./testing/$yesterday/${yesterday}_030000_STP_PH_${yesterday}hhmm-000002.gz"
    mkdir -p "./testing/$today"
    touch "./testing/$today/${today}_010000_STP_BO_${today}hhmm-000002.gz"
    touch "./testing/$today/${today}_010000_STP_PH_${today}hhmm-000003.gz"
    ./stp_sequence_check.sh --path ./testing | tee test_stp_sequence_check.log
    unset failed
    [[ $(grep -c "^STP_BO .*: checking sequence 999999-000002$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_BO" && failed=true
    [[ $(grep -c "^STP_PH .*: checking sequence 999999-000003$" test_stp_sequence_check.log) != 1 ]] && echo "* Failed, STP_PH" && failed=true
    [[ $(grep -c "^Warning: .*$" test_stp_sequence_check.log) != 6 ]] && echo "* Failed, warnings" && failed=true
    [[ $(grep -c "^Warning: Rollover detected$" test_stp_sequence_check.log) != 2 ]] && echo "* Failed, rollover warning" && failed=true
    [[ $(grep "^Warning: Missing sequence number .*$" test_stp_sequence_check.log | cut -d " " -f 5) != "000000"*"000001"*"000000"*"000001" ]] && echo "* Failed, sequence numbers" && failed=true
    if [[ -z $failed ]]; then
        echo "Test passed"
        result+="."
    else
        echo "Test failed"
        result+="F"
    fi
    echo "Overall result: $result"
    echo ""
fi

if [[ -d ./testing ]]; then
    rm -rf ./testing
fi

if [[ $result == *"F"* ]]; then
    echo "There are failed tests: $result"
else
    echo "All tests passed"
fi
echo "Testing finished"
