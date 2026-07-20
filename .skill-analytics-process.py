#!/usr/bin/env python3
import subprocess, json, sys
from collections import defaultdict

# Fetch raw runs data
result = subprocess.run(
    ['gh', 'api',
     'repos/{owner}/{repo}/actions/runs?created>=2026-07-08&per_page=100',
     '--paginate',
     '-q', '[.workflow_runs[] | select(.created_at >= "2026-07-08T19:25:57Z") | select(.name | startswith("skill:"))| {skill: (.name | ltrimstr("skill: ")), conclusion: (.conclusion // "pending"), status, created: .created_at}] | .[]'],
    capture_output=True, text=True
)

records = []
for line in result.stdout.strip().split('\n'):
    line = line.strip()
    if not line:
        continue
    try:
        records.append(json.loads(line))
    except:
        pass

print(f"Total raw records: {len(records)}", file=sys.stderr)

skills = defaultdict(lambda: {'total':0,'success':0,'failure':0,'cancelled':0,'in_progress':0,'last_run':'','last_conclusion':''})
for r in records:
    sk = r['skill']
    # Normalize thought-review (24) -> thought-review, list-digest (...) -> list-digest
    if sk.startswith('thought-review'):
        sk = 'thought-review'
    elif sk.startswith('list-digest'):
        sk = 'list-digest'
    skills[sk]['total'] += 1
    c = r['conclusion']
    s = r['status']
    if c == 'success':
        skills[sk]['success'] += 1
        skills[sk]['last_conclusion'] = 'success'
    elif c == 'failure':
        skills[sk]['failure'] += 1
        skills[sk]['last_conclusion'] = 'failure'
    elif c == 'cancelled':
        skills[sk]['cancelled'] += 1
        skills[sk]['last_conclusion'] = 'cancelled'
    elif s == 'in_progress':
        skills[sk]['in_progress'] += 1
        skills[sk]['last_conclusion'] = 'in_progress'
    if r['created'] > skills[sk]['last_run']:
        skills[sk]['last_run'] = r['created']

total_runs = sum(v['total'] for v in skills.values())
total_success = sum(v['success'] for v in skills.values())
total_failure = sum(v['failure'] for v in skills.values())
total_cancelled = sum(v['cancelled'] for v in skills.values())
total_in_progress = sum(v['in_progress'] for v in skills.values())
distinct = len(skills)

overall_pct = round(total_success / (total_success + total_failure) * 100) if (total_success + total_failure) > 0 else 0

print(f"TOTALS: runs={total_runs} success={total_success} failure={total_failure} cancelled={total_cancelled} in_progress={total_in_progress} distinct={distinct} pct={overall_pct}")

sorted_skills = sorted(skills.items(), key=lambda x: -x[1]['total'])
for sk, v in sorted_skills:
    sr = round(v['success']/v['total']*100) if v['total'] > 0 else 0
    print(f"SKILL|{sk}|{v['total']}|{v['success']}|{v['failure']}|{v['cancelled']}|{v['in_progress']}|{sr}%|{v['last_conclusion']}")
