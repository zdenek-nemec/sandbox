# YouTube RSS

## Goal

Goal of this project is to create command line application that scans pre-configured Youtube
channels for new videos.

* Only new videos since the last check will be reported
* Sources can be grouped - multiple sources reduced to single channel
* Output is CSV or HTML page with author, name, link, date

## How to get XML

1. Go to YouTube channel, e.g. [The Critical Drinker](https://www.youtube.com/@TheCriticalDrinker)
2. Check the source code and search for `externalId`
3. Paste externalId to `https://www.youtube.com/feeds/videos.xml?channel_id=THE_CHANNEL_ID_HERE`

Sources

* [StackOverflow](https://stackoverflow.com/questions/14366648/how-can-i-get-a-channel-id-from-youtube)
