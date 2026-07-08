#!/usr/bin/env python3
"""Compute skill-graph input fingerprint per skills/skill-graph/SKILL.md step 1."""
import hashlib, glob, re, sys

h = hashlib.sha1()
for f in ["aeon.yml", "skills.json"]:
    with open(f, "rb") as fh:
        h.update(fh.read())

for path in sorted(glob.glob("skills/*/SKILL.md")):
    with open(path) as fh:
        content = fh.read()
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if fm_match:
        h.update((path + ":" + fm_match.group(1)).encode())
    for line in content.splitlines():
        if re.match(r"^(depends_on:|- skill:|consume:|parallel:|trigger:)", line):
            h.update((path + ":" + line + "\n").encode())
    refs = sorted(set(re.findall(r"memory/(?:topics|state)/[a-zA-Z0-9_.-]+", content)))
    for r in refs:
        h.update((path + ":" + r + "\n").encode())

print(h.hexdigest())
