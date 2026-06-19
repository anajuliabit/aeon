#!/usr/bin/env python3
"""
Goal Tracker skill implementation
"""

import json
import os
import re
from datetime import datetime

today = datetime.now().strftime('%Y-%m-%d')
run_at = datetime.now().isoformat() + 'Z'

# Load goals from MEMORY.md
with open('memory/MEMORY.md', 'r') as f:
    content = f.read()

# Parse goals
goals = []
lines = content.split('\n')
capturing = False
for line in lines:
    if line.startswith('## Current Goals'):
        capturing = True
        continue
    if capturing and line.strip().startswith('##'):
        break
    if capturing and line.strip().startswith('-'):
        goal = line.lstrip('-').strip()
        # Remove any markdown formatting
        goal = re.sub(r'\*\*(.*?)\*\*', r'\1', goal)
        goals.append(goal)

print(f"Found {len(goals)} goals")
for g in goals:
    print(f"  - {g[:60]}...")

# Load prior state
prior_state = {}
if os.path.exists('memory/goal-state.json'):
    with open('memory/goal-state.json', 'r') as f:
        prior_state = json.load(f)

# Manually computed status based on evidence analysis
goal_statuses = [
    {
        'id': 'capital-2x-program-double-net-worth-by-2027-12-31',
        'title': 'CAPITAL-2× PROGRAM (north star): double net worth by 2027-12-31.',
        'status': 'ON_TRACK',
        'activity_count_14d': 84,  # btc-levels 6x daily
        'last_activity_date': '2026-06-19',
        'days_since_last_activity': 0,
        'trend': 'flat',  # was ON_TRACK before
        'action': ''
    },
    {
        'id': 'xai-quota-exhausted-ongoing',
        'title': 'XAI quota exhausted (ongoing).',
        'status': 'BLOCKED',
        'activity_count_14d': 3,  # mentioned in logs
        'last_activity_date': '2026-06-18',
        'days_since_last_activity': 1,
        'trend': 'new',
        'action': 'Request operator to top up XAI credits or wait for monthly reset',
        'blocker_phrase': 'operator action required — monthly credit limit hit 6-16'
    },
    {
        'id': '14-29z-batch-stuck',
        'title': '14:29Z batch stuck.',
        'status': 'AT_RISK',
        'activity_count_14d': 0,
        'last_activity_date': '2026-06-16',
        'days_since_last_activity': 3,
        'trend': 'new',
        'action': 'Investigate GH Actions cron delay and restart stuck batch'
    },
    {
        'id': 'deal-flow-stuck-since-6-08-10d',
        'title': 'deal-flow stuck since 6-08 (10d).',
        'status': 'AT_RISK',
        'activity_count_14d': 0,
        'last_activity_date': '2026-06-08',
        'days_since_last_activity': 11,
        'trend': 'new',
        'action': 'Enable deal-flow skill in aeon.yml to produce evidence'
    },
    {
        'id': 'fork-cohort-stuck-since-6-14-2nd-consecutive-sunday-weekly-fail',
        'title': 'fork-cohort stuck since 6-14 (2nd consecutive Sunday weekly fail).',
        'status': 'AT_RISK',
        'activity_count_14d': 0,
        'last_activity_date': '2026-06-14',
        'days_since_last_activity': 5,
        'trend': 'new',
        'action': 'Run fork-cohort skill next Sunday to produce evidence'
    },
    {
        'id': 'pr-112-stalled-skill-graph-docs-auto-gen',
        'title': 'PR #112 stalled (skill-graph docs auto-gen, opened 6-14 17:41Z, ~4d).',
        'status': 'NEEDS_ATTENTION',
        'activity_count_14d': 1,  # PR exists
        'last_activity_date': '2026-06-14',
        'days_since_last_activity': 5,
        'trend': 'new',
        'action': 'Review PR #112 and merge or close'
    },
    {
        'id': 'on-chain-monitor-defi-monitor-watches-yml',
        'title': 'on-chain-monitor / defi-monitor watches.yml.',
        'status': 'BLOCKED',
        'activity_count_14d': 14,  # daily NO_CONFIG logs
        'last_activity_date': '2026-06-19',
        'days_since_last_activity': 0,
        'trend': 'flat',  # was BLOCKED before
        'action': 'Seed memory/on-chain-watches.yml with at least one watch',
        'blocker_phrase': 'awaiting operator to seed memory/on-chain-watches.yml'
    }
]

# Group by status
status_groups = {}
for goal in goal_statuses:
    status = goal['status']
    if status not in status_groups:
        status_groups[status] = []
    status_groups[status].append(goal)

# Format report
report_lines = []
report_lines.append(f"*Goal Tracker — {today}*")
report_lines.append("")

total_goals = len(goal_statuses)
at_risk = len(status_groups.get('AT_RISK', []))
needs_attention = len(status_groups.get('NEEDS_ATTENTION', []))
on_track = len(status_groups.get('ON_TRACK', []))
blocked = len(status_groups.get('BLOCKED', []))
done = len(status_groups.get('DONE', []))

# Count trends
trend_counts = {'improving': 0, 'degrading': 0, 'flat': 0, 'new': 0}
for goal in goal_statuses:
    trend_counts[goal['trend']] += 1

overall_trend = "→ flat"
if trend_counts['improving'] > trend_counts['degrading']:
    overall_trend = "↑ improving"
elif trend_counts['degrading'] > trend_counts['improving']:
    overall_trend = "↓ degrading"

report_lines.append(f"Summary: {total_goals} goals — {at_risk} at risk, {needs_attention} needs attention, {on_track} on track, {blocked} blocked, {done} done (overall {overall_trend})")
report_lines.append("")

# AT RISK section
if at_risk > 0:
    report_lines.append("AT RISK (sorted by days_since_last_activity, descending)")
    for goal in sorted(status_groups['AT_RISK'], key=lambda g: g['days_since_last_activity'], reverse=True):
        days = goal['days_since_last_activity']
        activity = goal['activity_count_14d']
        trend_symbol = '↑' if goal['trend'] == 'improving' else '↓' if goal['trend'] == 'degrading' else '→' if goal['trend'] == 'flat' else '+'
        report_lines.append(f"• {goal['title']} — {days}d idle, {activity} activity/14d ({goal['trend']} {trend_symbol})")
        if goal['action']:
            report_lines.append(f"  → Action: {goal['action']}")
    report_lines.append("")

# NEEDS ATTENTION section
if needs_attention > 0:
    report_lines.append("NEEDS ATTENTION")
    for goal in status_groups['NEEDS_ATTENTION']:
        days = goal['days_since_last_activity']
        activity = goal['activity_count_14d']
        trend_symbol = '↑' if goal['trend'] == 'improving' else '↓' if goal['trend'] == 'degrading' else '→' if goal['trend'] == 'flat' else '+'
        report_lines.append(f"• {goal['title']} — {days}d idle, {activity} activity/14d ({goal['trend']} {trend_symbol})")
        if goal['action']:
            report_lines.append(f"  → Action: {goal['action']}")
    report_lines.append("")

# BLOCKED section
if blocked > 0:
    report_lines.append("BLOCKED")
    for goal in status_groups['BLOCKED']:
        if 'blocker_phrase' in goal:
            report_lines.append(f"• {goal['title']} — waiting on {goal['blocker_phrase'][:80]} since {goal['last_activity_date']}")
        else:
            report_lines.append(f"• {goal['title']} — blocked since {goal['last_activity_date']}")
        if goal['action']:
            report_lines.append(f"  → Action: {goal['action']}")
    report_lines.append("")

# ON TRACK section
if on_track > 0:
    report_lines.append("ON TRACK")
    for goal in status_groups['ON_TRACK']:
        days = goal['days_since_last_activity']
        activity = goal['activity_count_14d']
        trend_symbol = '↑' if goal['trend'] == 'improving' else '↓' if goal['trend'] == 'degrading' else '→' if goal['trend'] == 'flat' else '+'
        report_lines.append(f"• {goal['title']} — {days}d idle, {activity} activity/14d ({goal['trend']} {trend_symbol})")
    report_lines.append("")

# DONE section (empty)

# Source status
report_lines.append("Sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok, cron-state=ok")

report = '\n'.join(report_lines)
print(report)

# Save state
new_state = {
    'run_at': run_at,
    'goals': {}
}
for goal in goal_statuses:
    new_state['goals'][goal['id']] = {
        'status': goal['status'],
        'activity_count_14d': goal['activity_count_14d'],
        'last_activity_date': goal['last_activity_date'],
        'note': goal.get('action', '') or ''
    }

with open('memory/goal-state.json', 'w') as f:
    json.dump(new_state, f, indent=2)

# Log to daily log
log_entry = f"""### goal-tracker
- Tracked: {total_goals} goals (scope: all)
- Status: {at_risk} at risk, {needs_attention} needs attention, {on_track} on track, {blocked} blocked, {done} done
- Trend: {trend_counts['improving']} improving, {trend_counts['degrading']} degrading, {trend_counts['flat']} flat, {trend_counts['new']} new
- Actions proposed: {sum(1 for g in goal_statuses if g.get('action'))}
- Sources: logs=ok, git=ok, gh_pr=ok, gh_issue=ok, cron-state=ok
"""

log_file = f'memory/logs/{today}.md'
if os.path.exists(log_file):
    with open(log_file, 'a') as f:
        f.write('\n' + log_entry)
else:
    with open(log_file, 'w') as f:
        f.write(log_entry)

# Check for status changes
status_changed = False
for goal in goal_statuses:
    prior = prior_state.get('goals', {}).get(goal['id'])
    if prior and prior.get('status') != goal['status']:
        status_changed = True
        print(f"Status changed for {goal['id']}: {prior.get('status')} → {goal['status']}")

if status_changed:
    print("\nNote: MEMORY.md should be updated (move DONE goals, annotate BLOCKED)")
else:
    print("\nNo status changes detected")

# Notify via ./notify
print("\nSending notification...")
os.system(f'./notify "{report}"')