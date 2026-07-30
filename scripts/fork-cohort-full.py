#!/usr/bin/env python3
"""
fork-cohort: Weekly fork activation cohort tracker.
Buckets every fork by recent run activity (COLD / STALE / ACTIVE / POWER).
"""

import json
import subprocess
import os
from datetime import datetime, timedelta

TODAY = datetime.utcnow().strftime("%Y-%m-%d")
PARENT_REPO = "aaronjmars/aeon"  # Original parent
STATE_FILE = "memory/topics/fork-cohort-state.json"
ARTICLE_FILE = f"articles/fork-cohort-{TODAY}.md"

print("=== Fork Cohort Tracker ===")
print(f"Date: {TODAY}")
print(f"Parent: {PARENT_REPO}")

# Step 2: List forks
print("\nFetching forks list...")
try:
    result = subprocess.run(
        ["gh", "api", f"repos/{PARENT_REPO}/forks", "--paginate",
         "--jq", "[.[] | select(.archived != true and .disabled != true) | {full_name, owner: .owner.login, default_branch, pushed_at, stargazers_count, created_at}]"],
        capture_output=True, text=True, timeout=30
    )

    if result.returncode != 0:
        print(f"Error: {result.stderr}")
        print("FORK_COHORT_API_FAIL")
        exit(1)

    fork_list = json.loads(result.stdout)
except Exception as e:
    print(f"Exception: {e}")
    print("FORK_COHORT_API_FAIL")
    exit(1)

fork_count = len(fork_list)
print(f"Found {fork_count} active forks")

if fork_count == 0:
    print("FORK_COHORT_NO_FORKS")
    exit(0)

# Load previous state
prev_state = {}
try:
    with open(STATE_FILE, 'r') as f:
        prev_state = json.load(f).get('forks', {})
except:
    prev_state = {}

print(f"Previous state has {len(prev_state)} forks")

# Process forks
print("\nProcessing forks (max 80)...")
forks_data = {}
bucket_counts = {"POWER": 0, "ACTIVE": 0, "STALE": 0, "COLD": 0, "UNREADABLE": 0}
runs_checked = 0
aeon_checked = 0
unreadable_count = 0

NOW = datetime.utcnow()

for idx, fork in enumerate(fork_list[:80]):
    full_name = fork["full_name"]
    owner = fork["owner"]
    default_branch = fork["default_branch"]
    stars = fork["stargazers_count"]

    # Get last run
    last_run = None
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{full_name}/actions/runs?per_page=1", "--jq", ".workflow_runs[0].updated_at // empty"],
            capture_output=True, text=True, timeout=10
        )

        if result.returncode == 0 and result.stdout.strip():
            last_run = result.stdout.strip()
            runs_checked += 1
    except Exception as e:
        runs_checked += 1

    # Calculate days since run
    if last_run:
        try:
            last_run_dt = datetime.fromisoformat(last_run.replace("Z", "+00:00"))
            days_since_run = (NOW - last_run_dt).days
        except:
            days_since_run = 999
    else:
        days_since_run = 999

    # Classify bucket
    bucket = "UNKNOWN"
    enabled_count = 0

    if days_since_run > 365:
        bucket = "COLD"
    elif days_since_run < 7:
        bucket = "ACTIVE"

        # Check aeon.yml for enabled skills (only for ACTIVE candidates)
        try:
            result = subprocess.run(
                ["gh", "api", f"repos/{full_name}/contents/aeon.yml?ref={default_branch}", "--jq", ".content"],
                capture_output=True, text=True, timeout=10
            )

            if result.returncode == 0 and result.stdout.strip():
                import base64
                aeon_content = base64.b64decode(result.stdout.strip()).decode()
                enabled_count = len([line for line in aeon_content.split('\n') if 'enabled:' in line and 'true' in line])
                aeon_checked += 1
                if enabled_count >= 5:
                    bucket = "POWER"
        except:
            pass
    elif days_since_run >= 7:
        bucket = "STALE"

    if bucket != "UNREADABLE":
        bucket_counts[bucket] += 1
    else:
        unreadable_count += 1

    forks_data[full_name] = {
        "bucket": bucket,
        "last_run": last_run,
        "days_since_run": days_since_run,
        "enabled_count": enabled_count,
        "owner": owner,
        "stargazers": stars,
        "default_branch": default_branch
    }

# Count bucket changes
transitions = {
    "LEVELED_UP": [],
    "REVIVED": [],
    "WENT_STALE": [],
    "NEW_ACTIVE": [],
    "WENT_COLD": [],
    "NEW_FORK": [],
    "DROPPED_FROM_POWER": []
}

for full_name, current in forks_data.items():
    prev = prev_state.get(full_name, {})
    prev_bucket = prev.get("bucket")
    curr_bucket = current["bucket"]

    if not prev_bucket:
        # New fork
        if curr_bucket in ["ACTIVE", "POWER"]:
            transitions["NEW_ACTIVE"].append(full_name)
        else:
            transitions["NEW_FORK"].append(full_name)
    else:
        # Existing fork - check transitions
        if curr_bucket == "POWER":
            transitions["LEVELED_UP"].append(full_name)
        elif prev_bucket == "STALE" and curr_bucket in ["ACTIVE", "POWER"]:
            transitions["REVIVED"].append(full_name)
        elif prev_bucket == "ACTIVE" and curr_bucket == "STALE":
            transitions["WENT_STALE"].append(full_name)
        elif prev_bucket in ["ACTIVE", "POWER"] and curr_bucket == "COLD":
            transitions["WENT_COLD"].append(full_name)
        elif prev_bucket == "POWER" and curr_bucket == "ACTIVE":
            transitions["DROPPED_FROM_POWER"].append(full_name)

# Pick verdict
power_count = bucket_counts["POWER"]
active_count = bucket_counts["ACTIVE"]
stale_count = bucket_counts["STALE"]
cold_count = bucket_counts["COLD"]
total_count = power_count + active_count + stale_count + cold_count
running_count = power_count + active_count

verdict = "STEADY"
if transitions["LEVELED_UP"]:
    verdict = f"LEVELED_UP: {len(transitions['LEVELED_UP'])} forks crossed POWER threshold"
elif transitions["REVIVED"]:
    verdict = f"REVIVED: {len(transitions['REVIVED'])} stale forks running again"
elif transitions["WENT_STALE"]:
    verdict = f"WENT_STALE: {len(transitions['WENT_STALE'])} active forks went quiet"
elif not prev_state:
    verdict = f"COLD START: {total_count} forks, {running_count} running"
else:
    verdict = f"STEADY: {running_count} of {total_count} running"

pct = round(100.0 * running_count / total_count) if total_count > 0 else 0

print("")
print(f"=== Results for {TODAY} ===")
print(f"Verdict: {verdict}")
print(f"Total: {total_count} · POWER: {power_count} · ACTIVE: {active_count} · STALE: {stale_count} · COLD: {cold_count}")
print(f"Running (last 7d): {running_count} ({pct}%)")
print(f"\nTransitions:")
for t_type, forks in transitions.items():
    if forks:
        print(f"  {t_type}: {len(forks)}")

# Build article content
article = f"""# Fork Activation Cohort — {TODAY}

**Verdict:** {verdict}

**Parent:** {PARENT_REPO}
**Total forks:** {total_count} · **Running (last 7d):** {running_count} ({pct}%)

---

## Cohort breakdown

| Cohort | Count | Δ vs last week |
|--------|-------|----------------|
| POWER | {power_count} | {'+' if power_count > bucket_counts.get('POWER', 0) else ''}{power_count - len(prev_state.get('forks', {}).values())} |
| ACTIVE | {active_count} | {'+' if active_count > bucket_counts.get('ACTIVE', 0) else ''}{active_count - len(prev_state.get('forks', {}).values())} |
| STALE | {stale_count} | {'+' if stale_count > bucket_counts.get('STALE', 0) else ''}{stale_count - len(prev_state.get('forks', {}).values())} |
| COLD | {cold_count} | {'+' if cold_count > bucket_counts.get('COLD', 0) else ''}{cold_count - len(prev_state.get('forks', {}).values())} |
| UNREADABLE | {unreadable_count} | |

---

## Movement this week

"""

if not any(transitions.values()):
    article += "_No bucket changes this week._\n"
else:
    if transitions["LEVELED_UP"]:
        article += "### Leveled up to POWER\n"
        for full_name in transitions["LEVELED_UP"][:5]:
            data = forks_data[full_name]
            article += f"- @{data['owner']} — `{full_name}` (+{data['enabled_count']} skills enabled, last run {data['days_since_run']}d ago)\n"
        if len(transitions["LEVELED_UP"]) > 5:
            article += f"- ... and {len(transitions['LEVELED_UP']) - 5} more\n"
        article += "\n"

    if transitions["REVIVED"]:
        article += "### Revived (stale → running)\n"
        for full_name in transitions["REVIVED"][:5]:
            data = forks_data[full_name]
            article += f"- @{data['owner']} — `{full_name}` (last run {data['days_since_run']}d ago)\n"
        if len(transitions["REVIVED"]) > 5:
            article += f"- ... and {len(transitions['REVIVED']) - 5} more\n"
        article += "\n"

    if transitions["WENT_STALE"]:
        article += "### Went stale (active → quiet)\n"
        for full_name in transitions["WENT_STALE"][:5]:
            data = forks_data[full_name]
            article += f"- @{data['owner']} — `{full_name}` (last run {data['days_since_run']}d ago)\n"
        if len(transitions["WENT_STALE"]) > 5:
            article += f"- ... and {len(transitions['WENT_STALE']) - 5} more\n"
        article += "\n"

    if transitions["NEW_ACTIVE"]:
        article += "### New forks running\n"
        for full_name in transitions["NEW_ACTIVE"][:5]:
            data = forks_data[full_name]
            article += f"- @{data['owner']} — `{full_name}` (last run {data['days_since_run']}d ago)\n"
        if len(transitions["NEW_ACTIVE"]) > 5:
            article += f"- ... and {len(transitions['NEW_ACTIVE']) - 5} more\n"
        article += "\n"

    if transitions["WENT_COLD"]:
        article += "### Newly cold (was running, now silent >365d)\n"
        for full_name in transitions["WENT_COLD"][:5]:
            data = forks_data[full_name]
            article += f"- @{data['owner']} — `{full_name}`\n"
        if len(transitions["WENT_COLD"]) > 5:
            article += f"- ... and {len(transitions['WENT_COLD']) - 5} more\n"
        article += "\n"

# POWER roster (top 30 by enabled_count)
power_forks = sorted(
    [(name, data) for name, data in forks_data.items() if data["bucket"] == "POWER"],
    key=lambda x: x[1]["enabled_count"],
    reverse=True
)

if power_forks:
    article += "---\n\n## POWER cohort roster\n\n"
    article += "| Fork | Owner | Enabled skills | Last run | Stars |\n"
    article += "|------|-------|----------------|----------|-------|\n"

    for full_name, data in power_forks[:30]:
        last_run_str = f"{data['days_since_run']}d" if data['last_run'] else "never"
        article += f"| {full_name} | @{data['owner']} | {data['enabled_count']} | {last_run_str} ago | {data['stargazers']} |\n"

    if len(power_forks) > 30:
        article += f"\n... and {len(power_forks) - 30} more\n"

article += f"""

---

## Source status

`forks_list=ok · runs_lookup={runs_checked}/{total_count} · aeon_yml_lookup={aeon_checked}/{active_count} · unreadable={unreadable_count} · truncated={'true' if len(fork_list) > 80 else 'false'}`
"""

print("\nWriting article...")
with open(ARTICLE_FILE, 'w') as f:
    f.write(article)

print(f"Article written to {ARTICLE_FILE}")

# Update state
new_state = {
    "last_run": TODAY,
    "last_status": "FORK_COHORT_OK",
    "parent_repo": PARENT_REPO,
    "totals": {
        "total": total_count,
        "power": power_count,
        "active": active_count,
        "stale": stale_count,
        "cold": cold_count,
        "unreadable": unreadable_count
    },
    "forks": forks_data
}

with open(STATE_FILE, 'w') as f:
    json.dump(new_state, f, indent=2)

print(f"State updated to {STATE_FILE}")

# Determine if we should notify
should_notify = True
if not transitions["LEVELED_UP"] and not transitions["REVIVED"] and not transitions["WENT_STALE"] and not transitions["NEW_ACTIVE"]:
    if prev_state and verdict.startswith("STEADY"):
        should_notify = False

print(f"\nNotify? {should_notify}")
print(f"Status: FORK_COHORT_OK")
print(f"Verdict: {verdict}")

if should_notify:
    # Build notification
    notify_msg = f"*Fork Cohort — {TODAY} — {PARENT_REPO}*\n"
    notify_msg += f"{verdict}\n\n"
    notify_msg += f"Of {total_count} forks, {running_count} ran in the last 7 days ({pct}%). "
    notify_msg += f"POWER {power_count} · ACTIVE {active_count} · STALE {stale_count} · COLD {cold_count}.\n"

    if transitions["LEVELED_UP"]:
        notify_msg += f"\nLeveled up to POWER:\n"
        for full_name in transitions["LEVELED_UP"][:3]:
            data = forks_data[full_name]
            notify_msg += f"- @{data['owner']} — {full_name.split('/')[-1]} ({data['enabled_count']} skills)\n"
        if len(transitions["LEVELED_UP"]) > 3:
            notify_msg += f"- ... and {len(transitions['LEVELED_UP']) - 3} more\n"

    if transitions["REVIVED"]:
        names = ", ".join([forks_data[f]["owner"] for f in transitions["REVIVED"][:3]])
        notify_msg += f"\nRevived: @{names}"
        if len(transitions["REVIVED"]) > 3:
            notify_msg += f", ... and {len(transitions['REVIVED']) - 3} more"
        notify_msg += "\n"

    if transitions["WENT_STALE"]:
        notify_msg += f"\nWent stale (worth a check-in):\n"
        for full_name in transitions["WENT_STALE"][:3]:
            data = forks_data[full_name]
            notify_msg += f"- @{data['owner']} — last run {data['days_since_run']}d ago\n"
        if len(transitions["WENT_STALE"]) > 3:
            notify_msg += f"- ... and {len(transitions['WENT_STALE']) - 3} more\n"

    notify_msg += f"\nFull report: articles/fork-cohort-{TODAY}.md"

    print(f"\n=== NOTIFICATION ===\n{notify_msg}")

    # Save notification for ./notify
    with open(".pending-notify/fork-cohort.txt", "w") as f:
        f.write(notify_msg)
