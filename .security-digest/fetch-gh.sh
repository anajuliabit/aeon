#!/usr/bin/env bash
set -u
cd /home/runner/work/aeon/aeon
SINCE48=$(date -u -d '2 days ago' '+%Y-%m-%dT%H:%M:%SZ')
echo "SINCE48=$SINCE48"
gh api "/advisories?type=reviewed&severity=critical&published=${SINCE48}.." --paginate > .security-digest/adv_critical.json 2>.security-digest/err_critical
echo "critical_rc=$? count=$(jq 'if type==\"array\" then length else 0 end' .security-digest/adv_critical.json 2>/dev/null)"
gh api "/advisories?type=reviewed&severity=high&published=${SINCE48}.." --paginate > .security-digest/adv_high.json 2>.security-digest/err_high
echo "high_rc=$? count=$(jq 'if type==\"array\" then length else 0 end' .security-digest/adv_high.json 2>/dev/null)"
gh api "/advisories?type=malware&published=${SINCE48}.." --paginate > .security-digest/adv_malware.json 2>.security-digest/err_malware
echo "malware_rc=$? count=$(jq 'if type==\"array\" then length else 0 end' .security-digest/adv_malware.json 2>/dev/null)"
