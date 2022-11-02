#!/bin/bash
#
# Name: extract.sh
#
# Synopsis:
#     extract.sh [-h]
#
# Examples:
#     extract.sh
#
# Description:
#     Run archive extract application
#

MEDIATION_SERVERS=("avl4658t" "avl4688t" "avl4713p" "avl4715p")
MEDIATION_PYTHONHOME=/dcs/data01/SOFTWARE/Python/Python-3.7.8
MEDIATION_PYTHONPATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/lib
MEDIATION_PATH=/dcs/data01/SOFTWARE/Python/Python-3.7.8/bin
MEDIATION_APPLICATION_PATH=/dcs/data01/SOFTWARE/Tools/Archiving/extract.py

check_host () {
    for item in ${MEDIATION_SERVERS[@]}; do
        if [[ "$item" == "$HOSTNAME" ]]; then
            is_mediation=1
            return
        fi
    done
}

check_host
if [[ $is_mediation ]]; then
    PYTHONHOME=$REQUIRED_PYTHONHOME
    export PYTHONHOME
    PYTHONPATH=$REQUIRED_PYTHONPATH
    export PYTHONPATH
    PATH=$REQUIRED_PATH:$PATH
    export PATH
    python $MEDIATION_APPLICATION_PATH $*
else
    echo "Local"
    python extract.py $*
fi
