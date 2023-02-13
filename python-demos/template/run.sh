#!/bin/bash
#
# Name: run.sh
#
# Synopsis:
#     run.sh [-h]
#
# Examples:
#     run.sh
#
# Description:
#     Starts the Python application Lucky Numbers
#
#     -h, --help
#         Show this help message and exit
#

MEDIATION_SERVERS=("avl4658t" "avl4688t" "avl4713p" "avl4715p")
REQUIRED_PYTHONHOME=/dcs/data01/SOFTWARE/Python/Python-3.7.8
REQUIRED_PYTHONPATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/lib
REQUIRED_PATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/bin

print_usage () {
    echo "Usage: $(basename $BASH_SOURCE)"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

print_help () {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

if [[ $# == 1 && ("$1" == "-h" || "$1" == "--help") ]]; then
    print_help
    exit 0
elif [[ $# != 0 ]]; then
    echo "Error: Unexpected arguments" 1>&2
    print_usage
    exit -1
fi

cd $(dirname $BASH_SOURCE)
application_logs_path=./logs
for item in ${MEDIATION_SERVERS[@]}; do
    if [[ "$item" == "$HOSTNAME" ]]; then
        application_logs_path=$MEDIATION_LOGS_PATH
        PYTHONHOME=$REQUIRED_PYTHONHOME
        export PYTHONHOME
        PYTHONPATH=$REQUIRED_PYTHONPATH
        export PYTHONPATH
        PATH=$REQUIRED_PATH:$PATH
        export PATH
        break
    fi
done

if [ ! -d "$application_logs_path" ]; then
    mkdir $application_logs_path
fi
output_log=$application_logs_path/archiving_`date '+%Y-%m-%d'`.log
error_log=$application_logs_path/archiving_errors_`date '+%Y-%m-%d'`.log
echo `date '+%Y-%m-%d %H:%M:%S'` >>$output_log
echo `date '+%Y-%m-%d %H:%M:%S'` >>$error_log

python main.py --log_level INFO 1>>$output_log 2>>$error_log
