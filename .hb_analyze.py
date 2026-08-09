import re
import json
from datetime import datetime, timezone

with open('memory/cron-state.json') as f:
    state = json.load(f)
state_skills = set(state.keys())

with open('aeon.yml') as f:
    text = f.read()

enabled = {}
for line in text.split('\n'):
    m = re.match(r'^\s+([a-z][a-z0-9-]+)\s*:\s*\{', line)
    if m and 'enabled: true' in line:
        sched_m = re.search(r'schedule:\s*"([^"]+)"', line)
        enabled[m.group(1)] = sched_m.group(1) if sched_m else None

for m in re.finditer(r'^(\s+)([a-z][a-z0-9-]+):\s*\n((?:\s+[^\n]+\n)*?)\s+enabled:\s*true', text, re.MULTILINE):
    key = m.group(2)
    block = m.group(0)
    sched_m = re.search(r'schedule:\s*"([^"]+)"', block)
    enabled[key] = sched_m.group(1) if sched_m else None

print('Enabled skills:', len(enabled))
missing = set(enabled) - state_skills
print('Enabled MISSING from state:', sorted(missing))

now = datetime(2026, 8, 5, 20, 50, tzinfo=timezone.utc)

def hours_ago(ts):
    if not ts:
        return None
    dt = datetime.fromisoformat(ts.replace('Z', '+00:00'))
    return (now - dt).total_seconds() / 3600

print()
print('=== Chronic failures (sr < 0.5, runs >= 5) ===')
for k, v in state.items():
    if v.get('total_runs', 0) >= 5 and v.get('success_rate', 1) < 0.5:
        en = 'enabled' if k in enabled else 'disabled'
        print(f'  {k}: sr={v["success_rate"]:.2f} runs={v["total_runs"]} consec={v.get("consecutive_failures", 0)} [{en}]')

print()
print('=== Consecutive failures >= 3 ===')
for k, v in state.items():
    if v.get('consecutive_failures', 0) >= 3:
        print(f'  {k}: consec={v["consecutive_failures"]}')

print()
print('=== Stuck (dispatched >45min) ===')
for k, v in state.items():
    if v.get('last_status') == 'dispatched':
        h = hours_ago(v.get('last_dispatch'))
        if h is not None and h > 0.75:
            print(f'  {k}: dispatched {h:.1f}h ago')

print()
print('=== Failed skills ===')
for k, v in state.items():
    if v.get('last_status') == 'failed':
        print(f'  {k}: last_failed={v.get("last_failed")}')

print()
print('=== Enabled skills: last_success > 2x schedule interval ===')
def cron_interval_hours(cron):
    if not cron:
        return None
    parts = cron.split()
    if len(parts) < 5:
        return None
    minute, hour, dom, month, dow = parts[:5]
    if dow != '*' and dow != '?':
        return 24 * 7
    if hour == '*':
        return 1
    if '*/' in hour:
        try:
            return int(hour.split('*/')[1])
        except:
            return 24
    if ',' in hour:
        n = len(hour.split(','))
        return 24 / n
    if dom != '*':
        if '1/' in dom:
            try:
                return int(dom.split('1/')[1]) * 24
            except:
                return 24
        return 24
    return 24

for k, v in enabled.items():
    if k not in state:
        continue
    ls = state[k].get('last_success')
    if not ls:
        continue
    h = hours_ago(ls)
    intv = cron_interval_hours(v)
    if intv and h and h > 2 * intv:
        print(f'  {k}: sched="{v}" intv={intv:.1f}h last_success={h:.1f}h ago ({h/intv:.1f}x)')

print()
print('=== Heartbeat self ===')
h = state.get('heartbeat', {})
print(f'  last_success: {h.get("last_success")} ({hours_ago(h.get("last_success")):.1f}h ago)')

print()
print('=== All enabled skills last_success ===')
rows = []
for k in sorted(enabled):
    sched = enabled.get(k)
    v = state.get(k, {})
    ls = v.get('last_success')
    ha = hours_ago(ls) if ls else None
    rows.append((k, sched, ls, ha, v.get('last_status'), v.get('success_rate'), v.get('total_runs'), v.get('total_successes'), v.get('last_dispatch')))
rows.sort(key=lambda r: r[3] if r[3] is not None else 999999)
for r in rows:
    print(r)
