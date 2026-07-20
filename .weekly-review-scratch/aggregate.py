import sys, json, re
from collections import Counter
raw = sys.stdin.read()
objs = re.split(r'(?<=\})\{(?=\"total_count\")', raw)
if len(objs) > 1:
    for i in range(1, len(objs)):
        objs[i] = '{' + objs[i]
totals = Counter()
by_conclusion = Counter()
by_name_fail = Counter()
by_name_cancel = Counter()
by_name = Counter()
fail_details = []
cancel_details = []
for obj in objs:
    try:
        d = json.loads(obj)
    except Exception:
        continue
    for r in d.get('workflow_runs', []):
        totals['total'] += 1
        c = r.get('conclusion') or r.get('status')
        n = r.get('name', '?')
        ts = r.get('created_at', '')
        by_conclusion[c] += 1
        by_name[n] += 1
        if c == 'failure':
            by_name_fail[n] += 1
            fail_details.append((ts, n))
        elif c == 'cancelled':
            by_name_cancel[n] += 1
            cancel_details.append((ts, n))
print('TOTAL:', totals['total'])
print('BY CONCLUSION:', dict(by_conclusion))
print('--FAIL BY WF--')
for n, c in by_name_fail.most_common(30):
    print(f'  {n}: {c}')
print('--CANCEL BY WF--')
for n, c in by_name_cancel.most_common(30):
    print(f'  {n}: {c}')
print('--FAIL DETAILS--')
for ts, n in sorted(fail_details):
    print(f'  {ts}  {n}')
print('--CANCEL DETAILS--')
for ts, n in sorted(cancel_details):
    print(f'  {ts}  {n}')
