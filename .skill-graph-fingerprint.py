#!/usr/bin/env python3
"""Compute skill-graph input fingerprint deterministically."""
import hashlib
import glob
import os
import re
import sys
import json

REPO = "/home/runner/work/aeon/aeon"
os.chdir(REPO)

buf = []

# Top-level files
for path in ("aeon.yml", "skills.json"):
    with open(path, "rb") as fh:
        h = hashlib.sha1(fh.read()).hexdigest()
    buf.append(f"{h}  {path}")

# All SKILL.md files
for skill_md in sorted(glob.glob("skills/*/SKILL.md")):
    with open(skill_md, "r", encoding="utf-8", errors="replace") as fh:
        text = fh.read()

    # frontmatter (between first two --- lines)
    fm_lines = []
    in_fm = False
    frontmatter_seen = 0
    for line in text.splitlines():
        if line.strip() == "---":
            frontmatter_seen += 1
            if frontmatter_seen == 1:
                in_fm = True
                continue
            if frontmatter_seen == 2:
                in_fm = False
                break
        elif in_fm:
            fm_lines.append(f"{skill_md}: {line}")
    buf.extend(fm_lines)

    # depends_on:, - skill:, consume:, parallel:, trigger: matches
    for line in text.splitlines():
        if re.match(r'^(depends_on:|- skill:|consume:|parallel:|trigger:)', line):
            buf.append(line)

    # memory/{topics,state}/... references
    mem_refs = sorted(set(re.findall(r'memory/(?:topics|state)/[a-zA-Z0-9_.-]+', text)))
    buf.extend(mem_refs)

content = "\n".join(buf).encode()
digest = hashlib.sha1(content).hexdigest()
print(digest)
