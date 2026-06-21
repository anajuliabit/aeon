#!/usr/bin/env python3
"""Replicate the bash fingerprint logic from skills/skill-graph/SKILL.md step 1."""
import hashlib, os, re, glob

os.chdir('/home/runner/work/aeon/aeon')

buf = []
for fn in ['aeon.yml', 'skills.json']:
    with open(fn, 'rb') as f:
        digest = hashlib.sha1(f.read()).hexdigest()
    buf.append(f'{digest}  {fn}')

skill_files = sorted(glob.glob('skills/*/SKILL.md'))
mem_re = re.compile(r'memory/(?:topics|state)/[a-zA-Z0-9_.-]+')
grep_re = re.compile(r'(^depends_on:)|(^- skill:)|(consume:)|(parallel:)|(trigger:)', re.M)

for f in skill_files:
    with open(f, 'r', encoding='utf-8', errors='replace') as fp:
        text = fp.read()
    n = 0
    for line in text.split('\n'):
        if line == '---':
            n += 1
            continue
        if n == 1:
            buf.append(f'{f}: {line}')
    for m in grep_re.finditer(text):
        ls = text.rfind('\n', 0, m.start()) + 1
        le = text.find('\n', m.start())
        if le < 0:
            le = len(text)
        buf.append(text[ls:le])
    refs = sorted(set(m.group(0) for m in mem_re.finditer(text)))
    buf.extend(refs)

inner_input = ('\n'.join(buf) + '\n').encode()
inner_sha = hashlib.sha1(inner_input).hexdigest()
print(f'{inner_sha}  -')
