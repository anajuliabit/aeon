import os
import re

enabled_skills = [
    'morning-brief', 'daily-routine', 'github-trending', 'token-alert', 'token-movers',
    'on-chain-monitor', 'defi-monitor', 'defi-overview', 'token-pick', 'market-context-refresh',
    'btc-levels', 'narrative-tracker', 'aixbt-pulse', 'security-digest', 'list-digest',
    'agent-buzz', 'goal-tracker', 'skill-health', 'self-improve', 'reflect', 'action-converter',
    'evening-recap', 'thought-review', 'skill-freshness', 'heartbeat',
    'unlock-monitor', 'skill-security-scan', 'deal-flow', 'reg-monitor', 'search-skill',
    'skill-analytics', 'skill-evals', 'skill-update-check', 'weekly-review', 'weekly-shiplog',
    'operator-scorecard', 'fork-skill-digest', 'fork-skill-gap', 'fork-cohort', 'skill-graph',
    'vuln-scanner', 'cost-report', 'autoresearch'
]

art_pat = re.compile(r'articles/([a-zA-Z0-9_-]+)(?:-\\\$\{today\}|-[0-9]{4}-[0-9]{2}-[0-9]{2})?\.md')
out_pat = re.compile(r'\.outputs/([a-zA-Z0-9_-]+)\.md')
top_pat = re.compile(r'memory/topics/([a-zA-Z0-9_.-]+)\.md')
sta_pat = re.compile(r'memory/state/([a-zA-Z0-9_.-]+)\.json')

deps = {}

for skill in enabled_skills:
    skill_path = f'skills/{skill}/SKILL.md'
    if not os.path.exists(skill_path):
        continue
    with open(skill_path) as f:
        content = f.read()

    content_filtered = re.sub(r'```(?:bash|text|sh|shell)[^`]*?```', '', content, flags=re.DOTALL)

    found = set()
    for m in art_pat.finditer(content_filtered):
        p = m.group(0)
        prod = m.group(1)
        if prod == skill or prod.startswith(skill) or skill.startswith(prod):
            continue
        found.add(('articles', p))
    for m in out_pat.finditer(content_filtered):
        p = m.group(0)
        prod = m.group(1)
        if prod == skill or prod.startswith(skill) or skill.startswith(prod):
            continue
        found.add(('outputs', p))
    for m in top_pat.finditer(content_filtered):
        p = m.group(0)
        found.add(('topics', p))
    for m in sta_pat.finditer(content_filtered):
        p = m.group(0)
        fname = m.group(1)
        if fname == skill or fname.startswith(skill) or skill.startswith(fname):
            continue
        found.add(('state', p))

    if found:
        deps[skill] = sorted(found)

for skill, items in sorted(deps.items()):
    for cls, path in items:
        print(f'{skill} -> [{cls}] {path}')
