#!/bin/bash
set -e
SINCE48=$(date -u -d '2 days ago' '+%Y-%m-%dT%H:%M:%SZ')
echo "SINCE48=$SINCE48"
gh api "/advisories?type=reviewed&severity=critical&published=${SINCE48}.." > adv-critical.json
echo "critical bytes: $(wc -c < adv-critical.json), count: $(jq 'length' adv-critical.json)"
gh api "/advisories?type=reviewed&severity=high&published=${SINCE48}.." > adv-high.json
echo "high bytes: $(wc -c < adv-high.json), count: $(jq 'length' adv-high.json)"
gh api "/advisories?type=malware&published=${SINCE48}.." > adv-malware.json 2>/dev/null || echo "[]" > adv-malware.json
echo "malware bytes: $(wc -c < adv-malware.json), count: $(jq 'length' adv-malware.json 2>/dev/null || echo 0)"
