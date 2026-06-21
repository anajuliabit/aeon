#!/bin/bash
set -e
sha1sum aeon.yml skills.json > .skill-graph.raw
for f in skills/*/SKILL.md; do
  awk '/^---$/{n++;next} n==1{print FILENAME": "$0}' "$f" >> .skill-graph.raw
  grep -hE '^depends_on:|^- skill:|consume:|parallel:|trigger:' "$f" >> .skill-graph.raw 2>/dev/null || true
  grep -hoE 'memory/(topics|state)/[a-zA-Z0-9_.-]+' "$f" | sort -u >> .skill-graph.raw
done
sha1sum .skill-graph.raw | awk '{print $1}'
