#!/bin/bash
#
# Name: run_fft.sh
#
# Synopsis:
#     run_fft.sh <config>
#
# Examples:
#     run_fft.sh u1_ama
#
# Description:
#     Run Fast File Transfer application with specific configuration for
#     avl2572p/avl2573p.
#
# Options:
#     <config>
#         Reference to FFT configuration file, base name.
#
#


function print_error_message {
    echo "Usage: `basename $0` <config>"
    echo "Try \``basename $0` --help' for more information."
}


environment="production"
if [[ `hostname` == "ubuntu" ]]; then
    environment="test"
fi

if [[ $environment == "test" ]]; then
    python=/home/zdenek/.pyenv/shims/python
    bin_path=/home/zdenek/fast-file-transfer/bin
    config_path=/home/zdenek/fast-file-transfer/config
    log_path=/home/zdenek/fast-file-transfer/logs
    log_level=DEBUG
else
    python=/opt/rh/rh-python36/root/usr/bin/python3.6
    bin_path=/appl/fastfile/fast-file-transfer/bin
    config_path=/appl/fastfile/fast-file-transfer/config
    log_path=/appl/fastfile/logs
    log_level=DEBUG
fi

# Help
if [[ "$#" == "1"
        && ("$1" == "-h" || "$1" == "-help" || "$1" == "--help") ]]; then
    head -`grep -n -m 1 -v "^#" "$0" | cut -d ":" -f 1` "$0"
    exit 0
fi

# Check the arguments
if [[ "$#" == "1" ]]; then
    config=$1
else
    echo "Error: Unexpected number of arguments" 1>&2
    print_error_message
    exit -1
fi

# Check the paths
if [[ ! -d "$bin_path" ]]; then
    echo "Error: Invalid bin-path $bin_path"
    print_error_message
    exit -1
elif [[ ! -d "$config_path" ]]; then
    echo "Error: Invalid config-path $config_path"
    print_error_message
    exit -1
elif [[ ! -d "$log_path" ]]; then
    echo "Error: Invalid logs-path $log_path"
    print_error_message
    exit -1
fi

timestamp=`date '+%Y-%m-%d %H:%M:%S'`
echo $timestamp >> ${log_path}/${config}_stdout.log
echo $timestamp >> ${log_path}/${config}_stderr.log
if [[ $environment == "test" ]]; then
    $python ${bin_path}/fast_file_transfer.py \
        --config ${config_path}/${config}.cfg \
        --log_file ${log_path}/${config}.log \
        --log_level $log_level \
        --skip_site_commands \
        1>>${log_path}/${config}_stdout.log \
        2>>${log_path}/${config}_stderr.log
else
    $python ${bin_path}/fast_file_transfer.py \
        --config ${config_path}/${config}.cfg \
        --log_file ${log_path}/${config}.log \
        --log_level $log_level \
        1>>${log_path}/${config}_stdout.log \
        2>>${log_path}/${config}_stderr.log
fi
