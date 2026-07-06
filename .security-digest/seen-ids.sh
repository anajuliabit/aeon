#!/usr/bin/env bash
set -u
cd /home/runner/work/aeon/aeon
grep -hoE "(GHSA-[a-z0-9]+-[a-z0-9]+-[a-z0-9]+|CVE-[0-9]{4}-[0-9]+)" memory/logs/2026-06-27.md memory/logs/2026-06-28.md memory/logs/2026-06-29.md 2>/dev/null | sort -u > .security-digest/seen_ids.txt
echo "seen_count=$(wc -l < .security-digest/seen_ids.txt)"
head -30 .security-digest/seen_ids.txt
