#!/bin/bash
set -e
cd /home/runner/work/aeon/aeon

# Execute Python skill
python3 skills/skill-freshness/run.py

# Show what was created
echo ""
echo "=== Generated Files ==="
ls -lh articles/skill-freshness-2026-07-27.md 2>/dev/null && echo "✓ Article created"
tail -20 memory/logs/2026-07-27.md 2>/dev/null | grep -A 20 "Skill Freshness" || echo "Log entry pending"
