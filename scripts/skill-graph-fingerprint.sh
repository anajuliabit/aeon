#!/bin/bash
# Compute input fingerprint for skill-graph skill
set -e
cd "$(dirname "$0")/.."
sha1sum aeon.yml skills.json > /tmp/sg.raw
for f in skills/*/SKILL.md; do
  awk '/^---$/{n++;next} n==1{print FILENAME": "$0}' "$f" >> /tmp/sg.raw
  grep -hE '^depends_on:|^- skill:|consume:|parallel:|trigger:' "$f" >> /tmp/sg.raw 2>/dev/null || true
  grep -hoE 'memory/(topics|state)/[a-zA-Z0-9_.-]+' "$f" | sort -u >> /tmp/sg.raw
done
sha1sum /tmp/sg.raw | awk '{print $1}'
