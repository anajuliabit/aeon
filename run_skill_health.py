import json
import os
import hashlib
from datetime import datetime, timezone, timedelta

# 1. Gather state

# Parse enabled skills from aeon.yml
with open('aeon.yml', 'r') as f:
    lines = f.readlines()

enabled_skills = []
in_skills_section = False
for line in lines:
    stripped = line.strip()
    if stripped.startswith('skills:'):
        in_skills_section = True
        continue
    if in_skills_section and ':' in line and '#' not in line.split(':')[0]:
        # End of skills section
        if stripped.startswith('#'):
            continue
        if not stripped or stripped.startswith('reactive:') or stripped.startswith('chains:') or stripped.startswith('model:'):
            break

        # Extract skill name (before colon)
        skill_name = line.split(':')[0].strip()
        # Check if enabled: true appears on same line or next lines
        if 'enabled: true' in line:
            enabled_skills.append(skill_name)
        else:
            # Check next few lines for enabled: true
            line_idx = lines.index(line)
            for next_line in lines[line_idx:line_idx+3]:
                if 'enabled: true' in next_line:
                    enabled_skills.append(skill_name)
                    break

print(f"Found {len(enabled_skills)} enabled skills")
print(enabled_skills)

# Load cron-state
try:
    with open('memory/cron-state.json', 'r') as f:
        cron_state = json.load(f)
except Exception as e:
    print(f"Error loading cron-state: {e}")
    cron_state = {}

# Load skill-health data
skill_health_data = {}
skill_health_dir = 'memory/skill-health'
if os.path.exists(skill_health_dir):
    for fname in os.listdir(skill_health_dir):
        if fname.endswith('.json') and fname != 'last-report.json':
            try:
                with open(os.path.join(skill_health_dir, fname), 'r') as f:
                    data = json.load(f)
                    skill_name = data.get('skill')
                    if skill_name:
                        skill_health_data[skill_name] = data
            except Exception as e:
                print(f"Error loading {fname}: {e}")

# Load last report
try:
    with open('memory/skill-health/last-report.json', 'r') as f:
        last_report = json.load(f)
except Exception as e:
    print(f"Error loading last-report: {e}")
    last_report = {}

# 2. Classify each enabled skill
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

    # Calculate days since last success
    days_since_last_success = None
    if last_success:
        try:
            last_success_dt = datetime.fromisoformat(last_success.replace('Z', '+00:00'))
            days_since_last_success = (today.date() - last_success_dt.date()).days
        except:
            days_since_last_success = None

    # Apply classification rules in order
    if consecutive_failures >= 3 or (last_status == 'failed' and days_since_last_success and days_since_last_success >= 3):
        classifications['CRITICAL'].append(skill)
    elif success_rate < 0.6:
        classifications['DEGRADED'].append(skill)
    elif consecutive_failures >= 1 or success_rate < 0.8:
        classifications['WARNING'].append(skill)
    else:
        # Check skill-health data
        health = skill_health_data.get(skill)
        if health:
            avg_score = health.get('avg_score', 5)
            if avg_score >= 3:
                classifications['HEALTHY'].append(skill)
            else:
                classifications['DEGRADED'].append(skill)
        else:
            classifications['HEALTHY'].append(skill)

print("\nClassification results:")
for category, skills in classifications.items():
    if skills:
        print(f"{category} ({len(skills)}): {skills}")

# 3. Check issues (skip for now per precondition guard)
if not os.path.exists('memory/issues/INDEX.md'):
    print("\nIssue tracker missing - skipping issue reconciliation per precondition guard")
    # Log to memory/logs
    today_str = today.strftime('%Y-%m-%d')
    log_file = f'memory/logs/{today_str}.md'
    log_entry = f"\n### skill-health\n- SKILL_HEALTH_ISSUE_TRACKER_MISSING — skipping issue reconciliation (INDEX.md missing)\n"

    try:
        with open(log_file, 'a') as f:
            f.write(log_entry)
        print(f"Logged to {log_file}")
    except Exception as e:
        print(f"Error logging: {e}")

# 5. Decide whether to notify
# Build hash signature
current_hash_input = []
current_hash_input.extend(classifications['CRITICAL'])
current_hash_input.extend(classifications['FLAPPING'])
current_hash_input.extend(classifications['DEGRADED'])
current_hash_input.sort()

current_hash = hashlib.sha256(json.dumps(current_hash_input).encode()).hexdigest()

print(f"\nCurrent hash: {current_hash}")
print(f"Last report hash: {last_report.get('hash', 'none')}")

# Check if we should notify
should_notify = False
last_notified_at = last_report.get('last_notified_at')
if last_notified_at:
    try:
        last_notified_dt = datetime.fromisoformat(last_notified_at.replace('Z', '+00:00'))
        hours_since_notify = (today - last_notified_dt).total_seconds() / 3600
        if current_hash != last_report.get('hash') or hours_since_notify >= 24:
            should_notify = True
    except:
        should_notify = True
else:
    should_notify = True

print(f"Should notify: {should_notify}")

# 6. Format the report
# Determine overall health
if classifications['CRITICAL']:
    overall_health = 'CRITICAL'
elif classifications['DEGRADED'] or classifications['FLAPPING']:
    overall_health = 'DEGRADED'
elif classifications['WARNING']:
    overall_health = 'WARNING'
else:
    overall_health = 'OK'

# Format message
message_lines = []
message_lines.append(f"*Skill Health — {today.strftime('%Y-%m-%d')}*")

health_label = f"HEALTH: {overall_health}"
if overall_health == 'CRITICAL':
    health_label += f"({len(classifications['CRITICAL'])})"
elif overall_health == 'DEGRADED':
    health_label += f"({len(classifications['DEGRADED']) + len(classifications['FLAPPING'])})"
elif overall_health == 'WARNING':
    health_label += f"({len(classifications['WARNING'])})"

message_lines.append(health_label)

# Add sections if needed
if classifications['CRITICAL']:
    message_lines.append("\n🔴 CRITICAL")
    for skill in classifications['CRITICAL'][:5]:
        state = cron_state[skill]
        cons_fails = state.get('consecutive_failures', 0)
        days_down = state.get('days_since_last_success', '?')
        error = state.get('last_error', 'unknown')
        # Extract API host if possible
        api_host = 'unknown'
        if 'api.coingecko.com' in error:
            api_host = 'api.coingecko.com'
        elif 'api.github.com' in error:
            api_host = 'api.github.com'
        action = 'INVESTIGATE'
        if api_host != 'unknown':
            action = 'WAIT-API'
        message_lines.append(f"- {skill} — {cons_fails} fails, {days_down}d down — {action} ({api_host})")

if classifications['DEGRADED']:
    message_lines.append("\n🟡 DEGRADED")
    for skill in classifications['DEGRADED'][:5]:
        state = cron_state[skill]
        success_rate = state.get('success_rate', 0) * 100
        message_lines.append(f"- {skill} — {success_rate:.0f}% success")

if classifications['FLAPPING']:
    message_lines.append("\n🟡 FLAPPING")
    for skill in classifications['FLAPPING'][:5]:
        state = cron_state[skill]
        success_rate = state.get('success_rate', 0) * 100
        message_lines.append(f"- {skill} — {success_rate:.0f}% success")

if classifications['WARNING']:
    message_lines.append("\n🟠 WARNING")
    for skill in classifications['WARNING'][:5]:
        state = cron_state[skill]
        cons_fails = state.get('consecutive_failures', 0)
        success_rate = state.get('success_rate', 0) * 100
        message_lines.append(f"- {skill} — {cons_fails} fails, {success_rate:.0f}% success")

if classifications['NO_DATA']:
    message_lines.append(f"\n⚪ NO DATA ({len(classifications['NO_DATA'])}): {', '.join(classifications['NO_DATA'][:5])}")
    if len(classifications['NO_DATA']) > 5:
        message_lines.append(f"  +{len(classifications['NO_DATA']) - 5} more")

message_lines.append(f"\n🟢 HEALTHY: {len(classifications['HEALTHY'])}")

# If all healthy and no issues, simplify
if overall_health == 'OK' and len(classifications['WARNING']) == 0 and len(classifications['NO_DATA']) == 0:
    message = f"*Skill Health — {today.strftime('%Y-%m-%d')}*\nHEALTH: OK — {len(classifications['HEALTHY'])} skills healthy"
else:
    message = '\n'.join(message_lines)

print("\nFormatted message:")
print(message)

# 7. Save last report
last_report_data = {
    "hash": current_hash,
    "last_notified_at": last_report.get('last_notified_at') if not should_notify else today.isoformat(),
    "last_run_at": today.isoformat(),
    "classification": {
        "critical": classifications['CRITICAL'],
        "degraded": classifications['DEGRADED'],
        "flapping": classifications['FLAPPING'],
        "warning": classifications['WARNING'],
        "healthy_count": len(classifications['HEALTHY']),
        "no_data": classifications['NO_DATA']
    }
}

# Write last report
try:
    with open('memory/skill-health/last-report.json', 'w') as f:
        json.dump(last_report_data, f, indent=2)
    print(f"\nSaved last-report.json")
except Exception as e:
    print(f"Error saving last-report: {e}")

# 8. Log to memory/logs
today_str = today.strftime('%Y-%m-%d')
log_file = f'memory/logs/{today_str}.md'
log_entry = f"\n### skill-health\n"
if should_notify:
    log_entry += f"- HEALTH: {overall_health}\n"
    log_entry += f"- notified: true\n"
    log_entry += f"- open issues: 0 (tracker missing)\n"
    log_entry += f"- systemic: none\n"
else:
    log_entry += f"- SKILL_HEALTH_NOOP — state unchanged since {last_report.get('last_run_at', 'unknown')}, hash={current_hash[:8]}\n"

try:
    with open(log_file, 'a') as f:
        f.write(log_entry)
    print(f"Logged to {log_file}")
except Exception as e:
    print(f"Error logging: {e}")

print(f"\nAnalysis complete. Notification {'should be sent' if should_notify else 'skipped (no change or <24h)'}")