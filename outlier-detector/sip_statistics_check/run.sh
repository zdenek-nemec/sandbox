#!/bin/bash

timestamp=`date '+%Y-%m-%d %H:%M:%S'`
echo $timestamp >> /appl/cgi/dcs/data01/TOOLS/sip_statistics_check/run.log
cd /appl/cgi/dcs/data01/TOOLS/sip_statistics_check
python3 sip_statistics_check.py >> /appl/cgi/dcs/data01/TOOLS/sip_statistics_check/run.log
