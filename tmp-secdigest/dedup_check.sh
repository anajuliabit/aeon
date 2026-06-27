#!/bin/bash
cd "$(dirname "$0")"
jq -r '.[] | .ghsa_id' adv_malware.json | sort > today_malware.txt
grep -hoE "GHSA-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}" ../memory/logs/2026-06-25.md ../memory/logs/2026-06-26.md | sort -u > deduped.txt
comm -23 today_malware.txt deduped.txt > fresh_malware.txt
echo "FRESH MALWARE COUNT: $(wc -l < fresh_malware.txt)"
echo "FRESH MALWARE BY DATE:"
while read ghsa; do
  jq -r --arg g "$ghsa" '.[] | select(.ghsa_id==$g) | "\(.published_at[0:10]) \(.ghsa_id) \(.vulnerabilities[0].package.name)"' adv_malware.json
done < fresh_malware.txt | sort
