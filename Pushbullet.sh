#!/bin/bash

API="VsiRoSNwa4BHCYOw74wr2AMYFBkciJB2"
MSG="$1"

curl -u $API: https://api.pushbullet.com/v2/pushes -d type=note -d title="Interactive Monitor" -d channel_tag="interactivemonitor" -d body="$MSG"
