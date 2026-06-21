#!/usr/bin/env python3
"""Replicate the bash fingerprint logic from skills/skill-graph/SKILL.md step 1."""
import hashlib, os, re, glob, subprocess

os.chdir('/home/runner/work/aeon/aeon')

# Stream the same lines the bash pipe would produce, then sha1 them.
buf = []

# 1) sha1sum aeon.yml skills.json (exact bash output format)
for fn in ['aeon.yml', 'skills.json']:
    with open(fn, 'rb') as f:
        digest = hashlib.sha1(f.read()).hexdigest()
    buf.append(f'{digest}  {fn}')

# 2) per-skill processing in sorted order (shell glob expands sorted on most systems; force it)
skill_files = sorted(glob.glob('skills/*/SKILL.md'))

edge_re = re.compile(r'^(depends_on:|- skill:|consume:|parallel:|trigger:)')
mem_re = re.compile(r'memory/(topics|state)/[a-zA-Z0-9_.-]+')

for f in skill_files:
    with open(f, 'r', encoding='utf-8', errors='replace') as fp:
        text = fp.read()
    # awk: emit lines inside the first --- ... --- block, prefixed with 'FILENAME: '
    n = 0
    for line in text.split('\n'):
        if line == '---':
            n += 1
            continue
        if n == 1:
            buf.append(f'{f}: {line}')
    # grep -hE '^depends_on:|^- skill:|consume:|parallel:|trigger:' (anchored on the OR'd alternatives — grep regex actually only anchors the first)
    # The bash command grep '^depends_on:|^- skill:|consume:|parallel:|trigger:' matches if any alternative appears (not all anchored).
    grep_re = re.compile(r'(^depends_on:)|(^- skill:)|(consume:)|(parallel:)|(trigger:)', re.M)
    for m in grep_re.finditer(text):
        # emit the whole line containing the match
        ls = text.rfind('\n', 0, m.start()) + 1
        le = text.find('\n', m.start())
        if le < 0:
            le = len(text)
        buf.append(text[ls:le])
    # grep -hoE 'memory/(topics|state)/...' | sort -u
    refs = sorted(set(m.group(0) for m in mem_re.finditer(text)))
    buf.extend(refs)

inner_input = ('\n'.join(buf) + '\n').encode()
inner_sha = hashlib.sha1(inner_input).hexdigest()
print(f'{inner_sha}  -')
