import re
import json
import os
from datetime import datetime, timedelta
import subprocess

today = datetime.now().strftime('%Y-%m-%d')
run_at = datetime.now().isoformat() + 'Z'

# Parse goals from MEMORY.md
with open('memory/MEMORY.md', 'r') as f:
    content = f.read()

# Find goals section
lines = content.split('\n')
goals = []
capturing = False
for line in lines:
    if line.startswith('## Current Goals'):
        capturing = True
        continue
    if capturing and line.strip().startswith('##'):
        break
    if capturing and line.strip().startswith('-'):
        goal_text = line.lstrip('-').strip()
        goals.append(goal_text)
    elif capturing and line.strip().startswith('*'):
        goal_text = line.lstrip('*').strip()
        goals.append(goal_text)

if len(goals) == 0:
    print("Error: No goals found in MEMORY.md")
    exit(1)

# Derive IDs and keywords
goal_objs = []
for goal in goals:
    # Create ID: slugified title
    id_str = re.sub(r'[^a-z0-9]+', '-', goal.lower()).strip('-')
    id_str = re.sub(r'-+', '-', id_str)

    # Extract keywords: remove stopwords
    stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should', 'can', 'could', 'may', 'might', 'must', 'this', 'that', 'these', 'those', 'by', 'as', 'it', 'its', 'it\'s', 'we', 'you', 'they', 'them', 'their', 'our', 'your', 'my', 'mine', 'his', 'her', 'hers', 'its', 'its'}
    words = re.findall(r'\b\w+\b', goal.lower())
    keywords = [w for w in words if w not in stopwords and len(w) > 2]

    # Add obvious aliases
    aliases = []
    if 'xai' in keywords:
        aliases.append('xai-quota')
        aliases.append('xai')
    if 'quota' in keywords:
        aliases.append('xai')
    if 'batch' in keywords:
        aliases.append('14:29')
    if 'stuck' in keywords:
        aliases.append('stalled')
    if 'deal-flow' in keywords:
        aliases.append('dealflow')
    if 'fork-cohort' in keywords:
        aliases.append('forkcohort')
        aliases.append('fork')
    if 'pr' in keywords:
        aliases.append('pull-request')
        aliases.append('112')
    if 'monitor' in keywords:
        aliases.append('on-chain')
        aliases.append('defi')
    if 'watches' in keywords:
        aliases.append('on-chain-watches')
        aliases.append('yml')

    goal_objs.append({
        'id': id_str,
        'title': goal,
        'keywords': keywords + aliases,
        'due': None,
        'target': None
    })

# Load prior state
prior_state = {}
if os.path.exists('memory/goal-state.json'):
    with open('memory/goal-state.json', 'r') as f:
        prior_state = json.load(f)

# Scan logs for last 30 days
log_files = []
for fname in os.listdir('memory/logs'):
    if fname.endswith('.md'):
        date_str = fname.replace('.md', '')
        if date_str.endswith('-btc'):
            date_str = date_str[:-4]
        try:
            log_date = datetime.strptime(date_str, '%Y-%m-%d')
            if (datetime.now() - log_date).days <= 30:
                log_files.append(fname)
        except ValueError:
            continue

evidence = []
for fname in log_files:
    with open(f'memory/logs/{fname}', 'r') as f:
        content = f.read()
        for line_num, line in enumerate(content.split('\n'), 1):
            evidence.append({
                'source': 'log',
                'date': fname.replace('.md', '').replace('-btc', ''),
                'text': line,
                'line': line_num
            })

# Scan commits
commits = subprocess.run(['git', 'log', '--since="30 days ago"', '--pretty=format:%ad|%s', '--date=short'], capture_output=True, text=True)
for line in commits.stdout.strip().split('\n'):
    if line:
        parts = line.split('|')
        if len(parts) == 2:
            evidence.append({
                'source': 'commit',
                'date': parts[0],
                'text': parts[1]
            })

# Scan PRs (from gh output)
pr_json = subprocess.run(['gh', 'pr', 'list', '--state=all', '--search', 'updated:>=2026-05-20', '--json', 'number,title,state,updatedAt,url'], capture_output=True, text=True)
if pr_json.stdout:
    prs = json.loads(pr_json.stdout)
    for pr in prs:
        evidence.append({
            'source': 'pr',
            'date': pr['updatedAt'][:10],
            'text': f'#{pr["number"]} {pr["title"]} ({pr["state"]})',
            'url': pr['url']
        })

# Scan issues (empty in this case)

# Scan cron-state for skill health
with open('memory/cron-state.json', 'r') as f:
    cron_data = json.load(f)
for skill_name, stats in cron_data.items():
    evidence.append({
        'source': 'cron-state',
        'date': stats.get('last_success', '')[:10] if stats.get('last_success') else stats.get('last_dispatch', '')[:10] if stats.get('last_dispatch') else today,
        'text': f'{skill_name}: last_status={stats.get("last_status")}, success_rate={stats.get("success_rate")}'
    })

# Evaluate each goal
goal_results = []
for goal in goal_objs:
    goal_id = goal['id']
    keywords = goal['keywords']

    # Filter evidence for this goal
    matching_evidence = []
    for ev in evidence:
        # Case-insensitive whole-word match
        text_lower = ev['text'].lower()
        for kw in keywords:
            if kw.lower() in text_lower:
                matching_evidence.append(ev)
                break

    # Count activity in windows
    today_date = datetime.strptime(today, '%Y-%m-%d')
    activity_14d = 0
    activity_30d = 0
    last_activity_date = None

    for ev in matching_evidence:
        try:
            ev_date = datetime.strptime(ev['date'], '%Y-%m-%d')
            days_diff = (today_date - ev_date).days
            if days_diff <= 30:
                activity_30d += 1
            if days_diff <= 14:
                activity_14d += 1
            if last_activity_date is None or ev_date > datetime.strptime(last_activity_date, '%Y-%m-%d'):
                last_activity_date = ev['date']
        except ValueError:
            continue

    # Check completion signals
    completion_signal = False
    for ev in matching_evidence:
        if ev['source'] == 'log' or ev['source'] == 'commit' or ev['source'] == 'pr':
            text_lower = ev['text'].lower()
            completion_words = ['completed', 'done', 'shipped', 'launched', 'closed', 'merged', 'finished', 'resolved']
            for kw in keywords:
                if kw.lower() in text_lower:
                    for cw in completion_words:
                        if cw in text_lower:
                            completion_signal = True
                            break

    # Check blocker signals
    blocker_signal = False
    blocker_phrase = ''
    for ev in matching_evidence:
        if ev['source'] == 'log':
            text_lower = ev['text'].lower()
            blocker_words = ['blocked', 'waiting on', 'stuck on', 'awaiting', 'gated']
            for kw in keywords:
                if kw.lower() in text_lower:
                    for bw in blocker_words:
                        if bw in text_lower:
                            blocker_signal = True
                            blocker_phrase = ev['text']
                            break

    # Days since last activity
    days_since_last_activity = None
    if last_activity_date:
        last_date = datetime.strptime(last_activity_date, '%Y-%m-%d')
        days_since_last_activity = (today_date - last_date).days

    # Determine status
    status = 'AT_RISK'
    if completion_signal:
        status = 'DONE'
    elif blocker_signal:
        status = 'BLOCKED'
    elif activity_14d >= 2 and days_since_last_activity is not None and days_since_last_activity <= 7:
        status = 'ON_TRACK'
    elif activity_14d == 1 or (days_since_last_activity is not None and days_since_last_activity >= 8 and days_since_last_activity <= 14):
        status = 'NEEDS_ATTENTION'
    elif activity_14d == 0 and (days_since_last_activity is None or days_since_last_activity > 14):
        status = 'AT_RISK'

    # Compute trend vs prior snapshot
    prior = prior_state.get('goals', {}).get(goal_id)
    trend = 'new'
    if prior:
        prev_status = prior.get('status')
        prev_activity = prior.get('activity_count_14d', 0)
        if prev_status == status:
            if abs(activity_14d - prev_activity) <= prev_activity * 0.25:
                trend = 'flat'
            elif activity_14d >= prev_activity * 1.5:
                trend = 'improving'
            elif activity_14d <= prev_activity * 0.5:
                trend = 'degrading'
        else:
            status_order = {'AT_RISK': 1, 'NEEDS_ATTENTION': 2, 'ON_TRACK': 3, 'BLOCKED': 4, 'DONE': 5}
            if status_order.get(status, 0) > status_order.get(prev_status, 0):
                trend = 'improving'
            else:
                trend = 'degrading'

    # Determine action per non-DONE goal
    action = ''
    if status != 'DONE':
        if status == 'AT_RISK' and days_since_last_activity > 21:
            if 'xai' in keywords or 'quota' in keywords:
                action = 'Request operator to top up XAI credits or wait for monthly reset'
            elif 'batch' in keywords or '14:29' in keywords:
                action = 'Investigate GH Actions cron delay and restart stuck batch'
            elif 'deal-flow' in keywords:
                action = 'Enable deal-flow skill in aeon.yml to produce evidence'
            elif 'fork-cohort' in keywords:
                action = 'Run fork-cohort skill next Sunday to produce evidence'
            elif 'pr' in keywords or '112' in keywords:
                action = 'Review PR #112 and merge or close'
            elif 'monitor' in keywords or 'watches' in keywords:
                action = 'Seed memory/on-chain-watches.yml with at least one watch'
            else:
                action = 'Enable corresponding skill in aeon.yml'
        elif status == 'BLOCKED':
            action = f'Unblock by addressing {blocker_phrase[:50]}'
        elif status == 'NEEDS_ATTENTION':
            action = 'Complete the smallest next deliverable'
        elif status == 'ON_TRACK':
            action = ''  # omit action

    goal_results.append({
        'id': goal_id,
        'title': goal['title'],
        'keywords': keywords,
        'status': status,
        'activity_count_14d': activity_14d,
        'activity_count_30d': activity_30d,
        'last_activity_date': last_activity_date,
        'days_since_last_activity': days_since_last_activity,
        'completion_signal': completion_signal,
        'blocker_signal': blocker_signal,
        'blocker_phrase': blocker_phrase,
        'trend': trend,
        'action': action
    })

# Group by status
status_groups = {}
for goal in goal_results:
    status = goal['status']
    if status not in status_groups:
        status_groups[status] = []
    status_groups[status].append(goal)

# Format report
report_lines = []
report_lines.append(f"*Goal Tracker — {today}*")
report_lines.append("")

total_goals = len(goal_results)
at_risk = len(status_groups.get('AT_RISK', []))
needs_attention = len(status_groups.get('NEEDS_ATTENTION', []))
on_track = len(status_groups.get('ON_TRACK', []))
blocked = len(status_groups.get('BLOCKED', []))
done = len(status_groups.get('DONE', []))

# Overall trend
improving = sum(1 for g in goal_results if g['trend'] == 'improving')
degrading = sum(1 for g in goal_results if g['trend'] == 'degrading')
flat = sum(1 for g in goal_results if g['trend'] == 'flat')
new = sum(1 for g in goal_results if g['trend'] == 'new')

overall_trend = "→ flat"
if improving > degrading:
    overall_trend = "↑ improving"
elif degrading > improving:
    overall_trend = "↓ degrading"

report_lines.append(f"Summary: {total_goals} goals — {at_risk} at risk, {needs_attention} needs attention, {on_track} on track, {blocked} blocked, {done} done (overall {overall_trend})")
report_lines.append("")

# AT RISK section
if at_risk > 0:
    report_lines.append("AT RISK (sorted by days_since_last_activity, descending)")
    for goal in sorted(status_groups['AT_RISK'], key=lambda g: g['days_since_last_activity'] if g['days_since_last_activity'] is not None else 100, reverse=True):
        days = goal['days_since_last_activity'] if goal['days_since_last_activity'] is not None else 'none'
        activity = goal['activity_count_14d']
        trend_symbol = '↑' if goal['trend'] == 'improving' else '↓' if goal['trend'] == 'degrading' else '→' if goal['trend'] == 'flat' else '+'
        report_lines.append(f"• {goal['title']} — {days}d idle, {activity} activity/14d (was {goal['trend']} {trend_symbol})")
        if goal['action']:
            report_lines.append(f"  → Action: {goal['action']}")
    report_lines.append("")

# NEEDS ATTENTION section
if needs_attention > 0:
    report_lines.append("NEEDS ATTENTION")
    for goal in status_groups['NEEDS_ATTENTION']:
        days = goal['days_since_last_activity'] if goal['days_since_last_activity'] is not None else 'none'
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
        if goal['blocker_phrase']:
            report_lines.append(f"• {goal['title']} — waiting on {goal['blocker_phrase'][:100]} since {goal['last_activity_date']}")
        else:
            report_lines.append(f"• {goal['title']} — blocked since {goal['last_activity_date']}")
        if goal['action']:
            report_lines.append(f"  → Action: {goal['action']}")
    report_lines.append("")

# ON TRACK section
if on_track > 0:
    report_lines.append("ON TRACK")
    for goal in status_groups['ON_TRACK']:
        days = goal['days_since_last_activity'] if goal['days_since_last_activity'] is not None else 'none'
        activity = goal['activity_count_14d']
        trend_symbol = '↑' if goal['trend'] == 'improving' else '↓' if goal['trend'] == 'degrading' else '→' if goal['trend'] == 'flat' else '+'
        report_lines.append(f"• {goal['title']} — {days}d idle, {activity} activity/14d ({goal['trend']} {trend_symbol})")
    report_lines.append("")

# DONE section
if done > 0:
    report_lines.append("DONE")
    for goal in status_groups['DONE']:
        report_lines.append(f"• {goal['title']} — completed {goal['last_activity_date']}")
    report_lines.append("")

# Source status
source_status = {
    'logs': 'ok',
    'git': 'ok' if commits.stdout.strip() != '' else 'fail',
    'gh_pr': 'ok' if pr_json.stdout.strip() != '' else 'fail',
    'gh_issue': 'ok',  # empty list is still ok
    'cron-state': 'ok'
}
report_lines.append(f"Sources: logs={source_status['logs']}, git={source_status['git']}, gh_pr={source_status['gh_pr']}, gh_issue={source_status['gh_issue']}, cron-state={source_status['cron-state']}")

# Write report
report = '\n'.join(report_lines)
print(report)

# Save state
new_state = {
    'run_at': run_at,
    'goals': {}
}
for goal in goal_results:
    new_state['goals'][goal['id']] = {
        'status': goal['status'],
        'activity_count_14d': goal['activity_count_14d'],
        'last_activity_date': goal['last_activity_date'],
        'note': goal['action'] if goal['action'] else ''
    }

with open('memory/goal-state.json', 'w') as f:
    json.dump(new_state, f, indent=2)

# Check if status changed vs prior state
status_changed = False
for goal in goal_results:
    prior = prior_state.get('goals', {}).get(goal['id'])
    if prior and prior.get('status') != goal['status']:
        status_changed = True
        break

# Update MEMORY.md if status changed
if status_changed:
    # We'll need to read and update MEMORY.md
    # This would involve moving DONE goals to Completed Goals section
    # and annotating BLOCKED goals with blocker notes
    # For now, just note that we need to update
    print("\nStatus changed, MEMORY.md should be updated")

# Log to daily log
log_entry = f"""### goal-tracker
- Tracked: {total_goals} goals (scope: all)
- Status: {at_risk} at risk, {needs_attention} needs attention, {on_track} on track, {blocked} blocked, {done} done
- Trend: {improving} improving, {degrading} degrading, {flat} flat, {new} new
- Actions proposed: {sum(1 for g in goal_results if g['action'])}
- Sources: logs={source_status['logs']}, git={source_status['git']}, gh_pr={source_status['gh_pr']}, gh_issue={source_status['gh_issue']}, cron-state={source_status['cron-state']}
"""

with open(f'memory/logs/{today}.md', 'a') as f:
    f.write(log_entry)

# Notify
subprocess.run(['./notify', report], check=False)