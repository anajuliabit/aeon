#!/usr/bin/env python3
"""Compute skill-graph input fingerprint per skills/skill-graph/SKILL.md step 1."""
import os, glob, hashlib, re

os.chdir('/home/runner/work/aeon/aeon')
parts = []

for f in ('aeon.yml', 'skills.json'):
    with open(f, 'rb') as h:
        parts.append(hashlib.sha1(h.read()).hexdigest() + '  ' + f)

for f in sorted(glob.glob('skills/*/SKILL.md')):
    with open(f) as h:
        text = h.read()
    lines = text.split('\n')
    n = 0
    for line in lines:
        if line == '---':
            n += 1
            continue
        if n == 1:
            parts.append(f + ': ' + line)
    for line in lines:
        if re.match(r'^(depends_on:|- skill:|consume:|parallel:|trigger:)', line):
            parts.append(line)
    refs = set(re.findall(r'memory/(?:topics|state)/[a-zA-Z0-9_.-]+', text))
    for r in sorted(refs):
        parts.append(r)

blob = '\n'.join(parts) + '\n'
h = hashlib.sha1(blob.encode()).hexdigest()
print(h)
print('lines:', len(parts))
