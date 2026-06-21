#!/usr/bin/env python3
import json
from datetime import datetime, timezone
import os
import sys

# Load cron-state
try:
    with open('memory/cron-state.json', 'r') as f:
        cron_state = json.load(f)
except:
    cron_state = {}

# Load last-report
try:
    with open('memory/skill-health/last-report.json', 'r') as f:
        last_report = json.load(f)
except:
    last_report = {}

# Load skill-health data
skill_health_data = {}
for fname in os.listdir('memory/skill-health'):
    if fname.endswith('.json') and fname != 'last-report.json':
        try:
            with open(f'memory/skill-health/{fname}', 'r') as f:
                data = json.load(f)
                skill_name = data.get('skill')
                if skill_name:
                    skill_health_data[skill_name] = data
        except:
            pass

# Simulate enabled skills list from aeon.yml (extracted manually)
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

print("Enabled skills count:", len(enabled_skills))
print("\nChecking cron-state entries...")
for skill in enabled_skills:
    if skill in cron_state:
        state = cron_state[skill]
        print(f"{skill}: status={state.get('last_status')}, success_rate={state.get('success_rate')}, consecutive_failures={state.get('consecutive_failures')}, last_success={state.get('last_success')}")
    else:
        print(f"{skill}: NO DATA in cron-state")
