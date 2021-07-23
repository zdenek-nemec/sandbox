#!/bin/bash
for i in {0..3}; do
    timestamp=$(date +%Y%m%d_%H -d "$i hour ago")
    day=${timestamp:0:8}
    hour=${timestamp:9:2}
    statistics_file="/appl/cgi/dcs/data01/TOOLS/sip_statistics_check/data/sip_${day}_${hour}.csv"
    echo "#Records,Hour,Month,Day,Year" > $statistics_file
    zcat /cdr_archive/INPUT/A_SIP/$day/$day/${day}_$hour*.gz 2>/dev/null | cut -d "," -f 12 | fgrep -v "00:00:00.000 UTC Jan 01 1970" | cut -c 1-3,19- | sort | uniq -c | sed '/^\ *$/d; s/"//g; s/^ *//g; s/ /,/g' >> $statistics_file
    zcat /cdr_archive/INPUT/A_SIP/$day/${day}_$hour*.gz 2>/dev/null | cut -d "," -f 12 | fgrep -v "00:00:00.000 UTC Jan 01 1970" | cut -c 1-3,19- | sort | uniq -c | sed '/^\ *$/d; s/"//g; s/^ *//g; s/ /,/g' >> $statistics_file
    zcat /cdr_archive/INPUT/A_SIP/${day}_$hour*.gz 2>/dev/null | cut -d "," -f 12 | fgrep -v "00:00:00.000 UTC Jan 01 1970" | cut -c 1-3,19- | sort | uniq -c | sed '/^\ *$/d; s/"//g; s/^ *//g; s/ /,/g' >> $statistics_file
done

