#!/bin/bash

date; archive_date_yesterday=$(date -d "1 day ago" "+%Y%m%d"); archive_date_today=$(date "+%Y%m%d"); for source in STP_BO STP_PH; do echo -n "$source $archive_date_yesterday+$archive_date_today:"; seq_numbers=$(ls /cdr_archive/INPUT/A_RR/RR/$archive_date_yesterday /cdr_archive/INPUT/A_RR/RR/$archive_date_today | grep $source | cut -c 37-42 | sort | uniq); if [[ $seq_numbers ]]; then seq_start=$(echo "$seq_numbers" | head -1); seq_end=$(echo "$seq_numbers" | tail -1); echo " checking sequence $seq_start--$seq_end"; diff --side-by-side --suppress-common-lines <(echo "$seq_numbers") <(seq  $seq_start $seq_end) | awk '{print "WARNING, missing sequence number: " $2}'; else echo " no data"; fi; done

