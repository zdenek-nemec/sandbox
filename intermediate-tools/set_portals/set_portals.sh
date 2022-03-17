#!/bin/bash
#
# Name: set_portals.sh
#
# Synopsis:
#     set_portals.sh [-h] [-p PORTALS] [-s SELECTOR] [--status {ENABLE,DISABLE}] [--dispatch {ENABLE,DISABLE}] [--node NODE] [--user USER] [--password PASSWORD] [--path PATH] [--last LAST] [--next NEXT]
#
# Examples:
#     set_portals.sh
#     set_portals.sh -s "ZDENEK"
#     set_portals.sh -p "portals.txt" -s "ZDENEK"
#     set_portals.sh -s "ZDENEK7|ZDENEK8"
#     set_portals.sh -s "ZDENEK[78]"
#     set_portals.sh -s "ZDENEK\|.*_DATA"
#     set_portals.sh -s "ZDENEK\|.*_DATA" --status "ENABLE" --dispatch "ENABLE"
#     set_portals.sh -s "ZDENEK\|.*_DATA" --node "localhost" --user "zdenek" --password "tajne" --path "/tmp"
#     set_portals.sh -s "ZDENEK\|.*_DATA" --last 0 --next 1
#
# Description:
#     Shell script for setting up CSG Intermediate portals.
#
#     Depending on Intermediate version, some options may not be supported.
#
#     | Intermediate | 7 | 8 | 9 |
#     | ------------ | - | - | - |
#     | status       | Y | Y | Y |
#     | dispatch     | Y | Y | Y |
#     | node         | - | Y | Y |
#     | user         | - | Y | Y |
#     | password     | - | Y | Y |
#     | path         | - | Y | Y |
#     | last         | Y | Y | Y |
#     | next         | Y | Y | Y |
#
#     -h, --help
#         Show this help message and exit
#     -p PORTALS, --portals PORTALS
#         List of portals, if missing, dcs_db_config_report is used
#     -s SELECTOR, --selector SELECTOR
#         Grep expression for selecting the portal(s)
#     --status {ENABLE,DISABLE}
#         Enable or disable the portal(s)
#     --dispatch {ENABLE,DISABLE}
#         Enable or disable the dispatch
#     --node NODE
#         Node to be setup on the primary route
#     --user USER
#         User to be setup on the primary route
#     --password PASSWORD
#         Password to be setup on the primary route
#     --path PATH
#         Path to be setup on the primary route
#     --last LAST
#         Set last sequence number
#     --next NEXT
#         Set next sequence number
#

function print_usage {
    echo "Usage: $(basename $0) [-h] [-p PORTALS] [-s SELECTOR] [--status {ENABLE,DISABLE}] [--dispatch {ENABLE,DISABLE}] [--node NODE] [--user USER] [--password PASSWORD] [--path PATH] [--last LAST] [--next NEXT]"
    echo "Try \`$(basename $0) --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$0" | cut -d ":" -f 1) "$0"
}

while [[ $# -gt 0 ]]; do
    option="$1"
    case $option in
        -h|--help)
            shift
            print_help
            exit 0
            ;;
        -p|--portals)
            [ -z $2 ] && echo "Error: Missing list of portals" 1>&2 && print_usage && exit -1
            [ ! -f $2 ] && echo "Error: Invalid list of portals" 1>&2 && print_usage && exit -1
            portal_list="$2"
            shift
            shift
            ;;
        -s|--selector)
            [ -z $2 ] && echo "Error: Missing selector" 1>&2 && print_usage && exit -1
            selector="$2"
            shift
            shift
            ;;
        --status)
            [ -z $2 ] && echo "Error: Missing portal status" 1>&2 && print_usage && exit -1
            [[ $2 != "ENABLE" && $2 != "DISABLE" ]] && echo "Error: Invalid portal status $2" 1>&2 && print_usage && exit -1
            portal_status="$2"
            shift
            shift
            ;;
        --dispatch)
            [ -z $2 ] && echo "Error: Missing portal dispatch status" 1>&2 && print_usage && exit -1
            [[ $2 != "ENABLE" && $2 != "DISABLE" ]] && echo "Error: Invalid portal dispatch status $2" 1>&2 && print_usage && exit -1
            dispatch_status="$2"
            shift
            shift
            ;;
        --node)
            [ -z $2 ] && echo "Error: Missing route node" 1>&2 && print_usage && exit -1
            routing_node="$2"
            shift
            shift
            ;;
        --user)
            [ -z $2 ] && echo "Error: Missing route user" 1>&2 && print_usage && exit -1
            routing_user="$2"
            shift
            shift
            ;;
        --password)
            [ -z $2 ] && echo "Error: Missing route password" 1>&2 && print_usage && exit -1
            routing_password="$2"
            shift
            shift
            ;;
        --path)
            [ -z $2 ] && echo "Error: Missing route path" 1>&2 && print_usage && exit -1
            routing_path="$2"
            shift
            shift
            ;;
        --last)
            [ -z $2 ] && echo "Error: Missing last sequence" 1>&2 && print_usage && exit -1
            sequence_last="$2"
            shift
            shift
            ;;
        --next)
            [ -z $2 ] && echo "Error: Missing next sequence" 1>&2 && print_usage && exit -1
            sequence_next="$2"
            shift
            shift
            ;;
        *)
            shift
            echo "Error: Unexpected arguments" 1>&2
            print_usage
            exit -1
            ;;
    esac
done

intermediate_version=$(cgi_status | grep "DCS Release" | sed 's/^\t//g')
if [[ ${intermediate_version:12:2} == "7." ]]; then
    if [[ $routing_node || $routing_user || $routing_password || $routing_path ]]; then
        echo "Error: Unsupported options on Intermediate 7" 1>&2
        exit -1
    fi
fi

echo "Setting up:"
if [[ -z $portal_status && -z $dispatch_status && -z $routing_node && -z $routing_user && -z $routing_password && -z $routing_path && -z $sequence_last && -z $sequence_next ]]; then
    echo "* Nothing, displaying portals only"
fi
if [[ $portal_status ]]; then
    echo "* Root > Portal Status to $portal_status"
fi
if [[ $dispatch_status ]]; then
    echo "* Root > Dispatch Status to $dispatch_status"
fi
if [[ $routing_node ]]; then
    echo "* Routing > Node to $routing_node"
fi
if [[ $routing_user ]]; then
    echo "* Routing > User to $routing_user"
fi
if [[ $routing_password ]]; then
    echo "* Routing > Password to $routing_password"
fi
if [[ $routing_path ]]; then
    echo "* Routing > Path to $routing_path"
fi
if [[ $sequence_last ]]; then
    echo "* Output > Last Sequence Number to $sequence_last"
fi
if [[ $sequence_next ]]; then
    echo "* Output > Next Sequence Number to $sequence_next"
fi

if [[ $portal_list ]]; then
    portals=$(cat $portal_list | sort | uniq)
else
    portals=$(dcs_db_config_report -report_type dportal -stdout | grep "Portal Record: " | sed 's/Portal Record: //' | sort | uniq)
fi

echo "Selected portals:"
if [[ -z $selector ]]; then
    echo "* No selector specified, apply to all portals"
    selected_portals=$(echo "$portals")
else
    selected_portals=$(echo "$portals" | grep -E $selector)
fi
for portal in $selected_portals; do
    echo "* $portal"
done

read -p "Please confirm by pressing [Y] or [y]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "* Approved"
else
    echo "* Cancelled"
    exit 0
fi

query=""
for portal in $selected_portals; do
    s=$(echo $portal | cut -d "|" -f 1)
    p=$(echo $portal | cut -d "|" -f 2)
    if [[ $portal_status == "ENABLE" ]]; then
        query="${query}ACTIVATE $s $p\n"
    elif [[ $portal_status == "DISABLE" ]]; then
        query="${query}SUSPEND $s $p\n"
    fi
    if [[ $routing_node ]]; then
        query="${query}GET ROUTING FOR $s $p\n"
        query="${query}UPDATE ROUTING FOR $s $p -DATA_TGT_NAME=$routing_node\n"
        query="${query}UPDATE ROUTING FOR $s $p -SFTP_HOSTNAME=$routing_node\n"
        query="${query}UPDATE ROUTING FOR $s $p -DATA_ROUTE_STATUS=ENABLED\n"
    fi
    if [[ $routing_user ]]; then
        query="${query}GET ROUTING FOR $s $p\n"
        query="${query}UPDATE ROUTING FOR $s $p -DATA_TGT_LOGIN=$routing_user\n"
        query="${query}UPDATE ROUTING FOR $s $p -SFTP_USERNAME=$routing_user\n"
        query="${query}UPDATE ROUTING FOR $s $p -DATA_ROUTE_STATUS=ENABLED\n"
    fi
    if [[ $routing_password ]]; then
        query="${query}GET ROUTING FOR $s $p\n"
        query="${query}UPDATE ROUTING FOR $s $p -DATA_TGT_SECURITY=$routing_password\n"
        query="${query}UPDATE ROUTING FOR $s $p -SFTP_PASSWORD=$routing_password\n"
        query="${query}UPDATE ROUTING FOR $s $p -DATA_ROUTE_STATUS=ENABLED\n"
    fi
    if [[ $routing_path ]]; then
        query="${query}GET ROUTING FOR $s $p\n"
        query="${query}UPDATE ROUTING FOR $s $p -DATA_TGT_PATH=$routing_path\n"
        query="${query}UPDATE ROUTING FOR $s $p -SFTP_DIR=$routing_path\n"
        query="${query}UPDATE ROUTING FOR $s $p -DATA_ROUTE_STATUS=ENABLED\n"
    fi
    if [[ $sequence_last ]]; then
        query="${query}GET_INFO $s $p -OUT_BATCH_LAST_SEQ\n"
        query="${query}SET_INFO $s $p -OUT_BATCH_LAST_SEQ=$sequence_last\n"
    fi
    if [[ $sequence_next ]]; then
        query="${query}GET_INFO $s $p -OUT_BATCH_NEXT_SEQ\n"
        query="${query}SET_INFO $s $p -OUT_BATCH_NEXT_SEQ=$sequence_next\n"
    fi
done
dcs_dportal_utl <<- EOF
`echo -e $query`
EOF

query=""
for portal in $selected_portals; do
    s=$(echo $portal | cut -d "|" -f 1)
    p=$(echo $portal | cut -d "|" -f 2)
    if [[ $dispatch_status == "ENABLE" ]]; then
        query="${query}ENABLE -OWNER=$s -PORTAL=$p\n"
    elif [[ $dispatch_status == "DISABLE" ]]; then
        query="${query}DISABLE -OWNER=$s -PORTAL=$p\n"
    fi
done
dcs_dispatch_utl <<- EOF
`echo -e $query`
EOF
