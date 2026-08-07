#!/bin/bash
#
# Name: get_youtube_rss_feed.sh
#
# Synopsis:
#     get_youtube_rss_feed.sh --url {YOUTUBE_CHANNEL_URL}
#
# Examples:
#     get_youtube_rss_feed.sh
#     get_youtube_rss_feed.sh --url "https://www.youtube.com/@thewitcher"
#
# Description:
#     Obtain URL to RSS feed of given YouTube channel
#
#     -h, --help
#         Show this help message and exit
#     --url {YOUTUBE_CHANNEL_URL}
#         URL of the channel
#

function print_usage {
    echo "Usage: $(basename $BASH_SOURCE) --url {YOUTUBE_CHANNEL_URL}"
    echo "Try \`$(basename $BASH_SOURCE) --help' for more information."
}

function print_help {
    head -$(grep -n -m 1 -v "^#" "$BASH_SOURCE" | cut -d ":" -f 1) "$BASH_SOURCE"
}

if [[ "$#" == "1" && ("$1" == "-h" || "$1" == "--help") ]]; then
    print_help
    exit 0
elif [[ "$#" == "2" && "$1" == "--url" ]]; then
    url="$2"
else
    print_usage
    exit -1
fi

html="$(curl -sL --fail -A "Mozilla/5.0 (compatible; rss-fetcher/1.0)" "$url")" || {
    echo "Error: failed to fetch $url" >&2
    exit 2
}

rss_url="$(printf '%s' "$html" \
    | grep -oE '<link[^>]+application/rss\+xml[^>]*>' \
    | grep -oE 'href="[^"]+"' \
    | head -n1 \
    | sed -E 's/^href="(.+)"$/\1/')"

if [[ -z "$rss_url" ]]; then
    echo "Error: no RSS link found on page: $url" >&2
    exit 3
fi

echo "$rss_url"
