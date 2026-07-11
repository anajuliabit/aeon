#!/usr/bin/env bash
set -u
cd /home/runner/work/aeon/aeon
SINCE=$(date -u -d '7 days ago' '+%Y-%m-%d')
echo "SINCE=$SINCE"
jq --arg s "$SINCE" '[.vulnerabilities[] | select(.dateAdded >= $s)]' .security-digest/kev.json > .security-digest/kev_recent.json
echo "kev_recent_count=$(jq 'length' .security-digest/kev_recent.json)"
jq -r '.[] | "\(.cveID) | added=\(.dateAdded) | ransomware=\(.knownRansomwareCampaignUse) | vendor=\(.vendorProject) | product=\(.product)\n  short: \(.shortDescription | .[0:200])"' .security-digest/kev_recent.json
