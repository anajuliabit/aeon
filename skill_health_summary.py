#!/usr/bin/env python3
import json
import hashlib
from datetime import datetime, timezone

# Load cron-state
with open('memory/cron-state.json', 'r') as f:
    cron_state = json.load(f)

# Manually extracted enabled skills from aeon.yml
enabled_skills = [
    "morning-brief",
    "daily-routine",
    "github-trending",
    "token-alert",
    "token-movers",
    "on-chain-monitor",
    "defi-monitor",
    "defi-overview",
    "token-pick",
    "market-context-refresh",
    "btc-levels",
    "narrative-tracker",
    "unlock-monitor",
    "aixbt-pulse",
    "search-skill",
    "security-digest",
    "deal-flow",
    "reg-monitor",
    "skill-security-scan",
    "vuln-scanner",
    "autoresearch",
    "list-digest",
    "agent-buzz",
    "goal-tracker",
    "skill-health",
    "skill-analytics",
    "self-improve",
    "reflect",
    "action-converter",
    "evening-recap",
    "cost-report",
    "fork-cohort",
    "skill-evals",
    "skill-update-check",
    "fleet-control",
    "weekly-review",
    "weekly-shiplog",
    "operator-scorecard",
    "fork-skill-digest",
    "fork-skill-gap",
    "skill-graph",
    "skill-freshness",
    "heartbeat"
]

print(f"Analyzing {len(enabled_skills)} enabled skills")

# Classification
today = datetime.now(timezone.utc)

classifications = {
    'CRITICAL': [],
    'DEGRADED': [],
    'FLAPPING': [],
    'WARNING': [],
    'HEALTHY': [],
    'NO_DATA': []
}

for skill in enabled_skills:
    state = cron_state.get(skill)

    if not state:
        classifications['NO_DATA'].append(skill)
        continue

    last_status = state.get('last_status')
    consecutive_failures = state.get('consecutive_failures', 0)
    success_rate = state.get('success_rate', 1.0)
    last_success = state.get('last_success')

    # Apply classification rules in order
    if consecutive_failures >= 3:
        classifications['CRITICAL'].append(skill)
    elif success_rate < 0.6:
        classifications['DEGRADED'].append(skill)
    elif consecutive_failures >= 1 or success_rate < 0.8:
        classifications['WARNING'].append(skill)
    else:
        classifications['HEALTHY'].append(skill)

print("\n=== SKILL HEALTH REPORT ===")
print(f"Date: {today.strftime('%Y-%m-%d %H:%M UTC')}")
print()

for category, skills in classifications.items():
    if skills:
        print(f"{category} ({len(skills)}):")
        for skill in skills:
            state = cron_state[skill]
            fails = state.get('consecutive_failures', 0)
            rate = state.get('success_rate', 1.0)
            last_status = state.get('last_status', 'unknown')
            print(f"  - {skill}: {fails} consecutive fails, {rate:.1%} success, last={last_status}")

# Build hash for notification decision
critical_degraded = classifications['CRITICAL'] + classifications['DEGRADED'] + classifications['FLAPPING']
critical_degraded.sort()
current_hash = hashlib.sha256(json.dumps(critical_degraded).encode()).hexdigest()

print(f"\nHash signature: {current_hash[:16]}...")

# Check against last report
try:
    with open('memory/skill-health/last-report.json', 'r') as f:
        last_report = json.load(f)
    last_hash = last_report.get('hash', '')
    last_notified = last_report.get('last_notified_at', '')
    print(f"Last report hash: {last_hash[:16]}...")
    print(f"Last notified: {last_notified}")

    if current_hash == last_hash:
        print("Status unchanged since last report")
    else:
        print("Status CHANGED - notification needed")
except:
    print("No last report found")

# Determine overall health
if classifications['CRITICAL']:
    overall = 'CRITICAL'
elif classifications['DEGRADED'] or classifications['FLAPPING']:
    overall = 'DEGRADED'
elif classifications['WARNING']:
    overall = 'WARNING'
else:
    overall = 'OK'

print(f"\nOverall health: {overall}")

# Format notification
msg_lines = []
msg_lines.append(f"*Skill Health — {today.strftime('%Y-%m-%d')}*")

if overall == 'CRITICAL':
    msg_lines.append(f"HEALTH: CRITICAL({len(classifications['CRITICAL'])})")
elif overall == 'DEGRADED':
    msg_lines.append(f"HEALTH: DEGRADED({len(classifications['DEGRADED']) + len(classifications['FLAPPING'])})")
elif overall == 'WARNING':
    msg_lines.append(f"HEALTH: WARNING({len(classifications['WARNING'])})")
else:
    msg_lines.append(f"HEALTH: OK")

# Add critical section
if classifications['CRITICAL']:
    msg_lines.append("\n🔴 CRITICAL")
    for skill in classifications['CRITICAL']:
        state = cron_state[skill]
        fails = state.get('consecutive_failures', 0)
        msg_lines.append(f"- {skill} — {fails} fails")

# Add degraded section
if classifications['DEGRADED']:
    msg_lines.append("\n🟡 DEGRADED")
    for skill in classifications['DEGRADED']:
        state = cron_state[skill]
        rate = state.get('success_rate', 0) * 100
        msg_lines.append(f"- {skill} — {rate:.0f}% success")

# Add warning section
if classifications['WARNING']:
    msg_lines.append("\n🟠 WARNING")
    for skill in classifications['WARNING']:
        state = cron_state[skill]
        fails = state.get('consecutive_failures', 0)
        rate = state.get('success_rate', 0) * 100
        msg_lines.append(f"- {skill} — {fails} fails, {rate:.0f}% success")

if classifications['NO_DATA']:
    msg_lines.append(f"\n⚪ NO DATA ({len(classifications['NO_DATA'])}): {', '.join(classifications['NO_DATA'])}")

msg_lines.append(f"\n🟢 HEALTHY: {len(classifications['HEALTHY'])}")

message = '\n'.join(msg_lines)
print("\n=== NOTIFICATION MESSAGE ===")
print(message)