#!/bin/bash
F=/home/runner/work/aeon/aeon/.skg-fp.txt
> "$F"
sha1sum aeon.yml skills.json >> "$F"
for f in skills/*/SKILL.md; do
  awk '/^---$/{n++;next} n==1{print FILENAME": "$0}' "$f" >> "$F"
  grep -hE '^depends_on:|^- skill:|consume:|parallel:|trigger:' "$f" >> "$F" 2>/dev/null || true
  grep -hoE 'memory/(topics|state)/[a-zA-Z0-9_.-]+' "$f" | sort -u >> "$F"
done
sha1sum "$F"
