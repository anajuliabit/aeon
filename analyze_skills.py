import json
import os
from datetime import datetime, timezone

# Parse aeon.yml manually
with open('aeon.yml', 'r') as f:
    content = f.read()

enabled_skills = []
for line in content.split('\n'):
    line = line.strip()
    if line.startswith('-'):
        continue
    if 'enabled: true' in line:
        # Extract skill name before colon
        if ':' in line:
            skill_name = line.split(':')[0].strip()
            enabled_skills.append(skill_name)

print(f"Enabled skills ({len(enabled_skills)}): {enabled_skills}")

# Load cron-state
try:
    with open('memory/cron-state.json', 'r') as f:
        cron_state = json.load(f)
except Exception as e:
    print(f"Error loading cron-state: {e}")
    cron_state = {}

# Load last-report
try:
    with open('memory/skill-health/last-report.json', 'r') as f:
        last_report = json.load(f)
except Exception as e:
    print(f"Error loading last-report: {e}")
    last_report = {}

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

# Classification
today = datetime.now(timezone.utc).date()

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
            days_since_last_success = (today - last_success_dt.date()).days
        except:
            days_since_last_success = None

    # Check classification rules in order
    if consecutive_failures >= 3 or (last_status == 'failed' and days_since_last_success and days_since_last_success >= 3):
        classifications['CRITICAL'].append(skill)
    elif success_rate < 0.6:
        classifications['DEGRADED'].append(skill)
    elif consecutive_failures >= 1 or success_rate < 0.8:
        classifications['WARNING'].append(skill)
    else:
        # Check for skill-health data
        health = skill_health_data.get(skill)
        if health:
            avg_score = health.get('avg_score', 5)  # default high if missing
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