import re
import json
from datetime import datetime, timedelta
import os

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
        # Remove bullet point and extra whitespace
        goal_text = line.lstrip('-').strip()
        goals.append(goal_text)
    elif capturing and line.strip().startswith('*'):
        goal_text = line.lstrip('*').strip()
        goals.append(goal_text)

print(f'Found {len(goals)} goals:')
for i, g in enumerate(goals):
    print(f'  {i+1}. {g}')

# Derive IDs and keywords
goal_objs = []
for goal in goals:
    # Create ID: slugified title
    id_str = re.sub(r'[^a-z0-9]+', '-', goal.lower()).strip('-')
    id_str = re.sub(r'-+', '-', id_str)

    # Extract keywords: remove stopwords
    stopwords = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'shall', 'should', 'can', 'could', 'may', 'might', 'must', 'this', 'that', 'these', 'those', 'by', 'as', 'it', 'its', 'it\'s', 'we', 'you', 'they', 'them', 'their', 'our', 'your', 'my', 'mine', 'his', 'her', 'hers'}
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

print('\nGoal objects:')
for obj in goal_objs:
    print(f"  {obj['id']}: {obj['title'][:50]}...")
    print(f"    keywords: {obj['keywords']}")

# Save goals for later
with open('/tmp/goals.json', 'w') as f:
    json.dump(goal_objs, f, indent=2)