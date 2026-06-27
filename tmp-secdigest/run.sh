#!/bin/bash
set -e
cd "$(dirname "$0")"

SINCE=$(date -u -d '7 days ago' '+%Y-%m-%d')
SINCE48=$(date -u -d '2 days ago' '+%Y-%m-%dT%H:%M:%SZ')
echo "SINCE=$SINCE SINCE48=$SINCE48"

# Filter KEV
jq --arg s "$SINCE" '[.vulnerabilities[] | select(.dateAdded >= $s)]' kev.json > kev_recent.json
echo "kev recent count=$(jq 'length' kev_recent.json)"
jq -r '.[] | "\(.cveID)\t\(.dateAdded)\t\(.vendorProject)\t\(.product)\t\(.vulnerabilityName | .[0:90])"' kev_recent.json
