#!/bin/bash
cd /home/runner/work/aeon/aeon
{
  sha1sum aeon.yml skills.json
  for f in skills/*/SKILL.md; do
    awk '/^---$/{n++;next} n==1{print FILENAME": "$0}' "$f"
    grep -hE '^depends_on:|^- skill:|consume:|parallel:|trigger:' "$f" 2>/dev/null || true
    grep -hoE 'memory/(topics|state)/[a-zA-Z0-9_.-]+' "$f" | sort -u
  done | sha1sum
} > .skill-graph-tmp/fingerprint.txt
cat .skill-graph-tmp/fingerprint.txt
