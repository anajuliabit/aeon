#!/usr/bin/env bash
set -u
SD=/home/runner/work/aeon/aeon/.security-digest
SINCE=$(date -u -d '7 days ago' '+%Y-%m-%d')
echo "SINCE=$SINCE"
jq --arg s "$SINCE" '[.vulnerabilities[] | select(.dateAdded >= $s)]' "$SD/kev.json" > "$SD/kev_recent.json"
echo "recent_count=$(jq length "$SD/kev_recent.json")"
jq -r '.[] | "\(.cveID) | added=\(.dateAdded) | due=\(.dueDate) | ransomware=\(.knownRansomwareCampaignUse) | vendor=\(.vendorProject) | product=\(.product)\n  short: \(.shortDescription)"' "$SD/kev_recent.json"
