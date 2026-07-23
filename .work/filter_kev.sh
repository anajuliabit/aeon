#!/usr/bin/env bash
set -euo pipefail
SINCE=$(date -u -d "7 days ago" "+%Y-%m-%d" 2>/dev/null || date -u -v-7d "+%Y-%m-%d")
echo "SINCE=$SINCE"
jq --arg s "$SINCE" '[.vulnerabilities[] | select(.dateAdded >= $s)]' /home/runner/work/aeon/aeon/.work/kev.json > /home/runner/work/aeon/aeon/.work/kev_recent.json
COUNT=$(jq -r 'length' /home/runner/work/aeon/aeon/.work/kev_recent.json)
echo "COUNT=$COUNT"
jq -r '.[] | [.cveID, .dateAdded, .vendorProject, .product, .knownRansomwareCampaignUse] | @tsv' /home/runner/work/aeon/aeon/.work/kev_recent.json
