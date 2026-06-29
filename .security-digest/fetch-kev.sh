#!/usr/bin/env bash
set -u
cd /home/runner/work/aeon/aeon
SINCE=$(date -u -d '7 days ago' '+%Y-%m-%d')
echo "SINCE=$SINCE"
curl -sf --max-time 25 "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json" -o .security-digest/kev.json
RC=$?
echo "curl_rc=$RC"
echo "kev_bytes=$(wc -c < .security-digest/kev.json 2>/dev/null || echo 0)"
if [ -s .security-digest/kev.json ]; then
  jq --arg s "$SINCE" '[.vulnerabilities[] | select(.dateAdded >= $s)]' .security-digest/kev.json > .security-digest/kev_recent.json
  echo "kev_recent_count=$(jq 'length' .security-digest/kev_recent.json)"
  echo "kev_status=ok"
else
  echo "[]" > .security-digest/kev_recent.json
  echo "kev_status=fail"
fi
