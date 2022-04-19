#!/bin/bash

INTERMEDIATE9_SERVERS="avl4658t avl4688t avl4713p avl4715p"
INTERMEDIATE9_TOOLS_PATH="/dcs/data01/SOFTWARE/Tools"

contains() {
    [[ $1 =~ (^|[[:space:]])$2($|[[:space:]]) ]] && return 1 || return 0
}

host=$(hostname | awk '{print tolower($0)}')

contains "$INTERMEDIATE9_SERVERS" "$host"
if [[ $? == 1 ]]; then
    application_path=$INTERMEDIATE9_TOOLS_PATH/ConnectivityCheck
    configuration_path=$INTERMEDIATE9_TOOLS_PATH/ConnectivityCheck
else
    application_path="./target"
    configuration_path="."
fi

if [[ $host == "" ]]; then
    configuration_file="targets.csv"
else
    configuration_file="targets_$host.csv"
fi

java -jar $application_path/connectivity-check-1.0-SNAPSHOT.jar $configuration_path/$configuration_file
