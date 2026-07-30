#!/usr/bin/env python3
import json
import subprocess
import os
from datetime import datetime, timedelta
import base64

TODAY = datetime.utcnow().strftime("%Y-%m-%d")
PARENT_REPO = "anajuliabit/aeon"
STATE_FILE = "memory/topics/fork-cohort-state.json"

print("=== Fork Cohort Tracker ===")
print(f"Date: {TODAY}")
print(f"Parent: {PARENT_REPO}")

# Step 2: List forks
print("Fetching forks list...")
result = subprocess.run(
    ["gh", "api", f"repos/{PARENT_REPO}/forks", "--paginate",
     "--jq", "[.[] | select(.archived != true and .disabled != true) | {full_name, owner: .owner.login, default_branch, pushed_at, stargazers_count, created_at}]"],
    capture_output=True, text=True
)

if result.returncode != 0:
    print(f"Failed to fetch forks: {result.stderr}")
    with open("/tmp/fork-cohort-status.txt", "w") as f:
        f.write("FORK_COHORT_API_FAIL")
    exit(1)

fork_list = json.loads(result.stdout)
fork_count = len(fork_list)
print(f"Found {fork_count} active forks")

if fork_count == 0:
    with open("/tmp/fork-cohort-status.txt", "w") as f:
        f.write("FORK_COHORT_NO_FORKS")
    exit(0)

# Process forks
print("Processing forks (max 80)...")
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

    print(f"  [{idx+1}/{min(fork_count, 80)}] {full_name}...", end="", flush=True)

    # Get last run
    last_run = None
    result = subprocess.run(
        ["gh", "api", f"repos/{full_name}/actions/runs?per_page=1", "--jq", ".workflow_runs[0].updated_at // empty"],
        capture_output=True, text=True, timeout=10
    )

    if result.returncode == 0 and result.stdout.strip():
        last_run = result.stdout.strip()
        runs_checked += 1
        print(f" last_run={last_run[:10]}", flush=True)
    else:
        print(f" (no runs or API error)", flush=True)
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

        # Check aeon.yml for enabled skills
        result = subprocess.run(
            ["gh", "api", f"repos/{full_name}/contents/aeon.yml?ref={default_branch}", "--jq", ".content"],
            capture_output=True, text=True, timeout=10
        )

        if result.returncode == 0 and result.stdout.strip():
            try:
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

print("")
print("=== Bucketing Results ===")
print(f"POWER: {bucket_counts['POWER']}")
print(f"ACTIVE: {bucket_counts['ACTIVE']}")
print(f"STALE: {bucket_counts['STALE']}")
print(f"COLD: {bucket_counts['COLD']}")
print(f"UNREADABLE: {bucket_counts['UNREADABLE']}")

# Save processing data
with open("/tmp/fork-cohort-data.json", "w") as f:
    json.dump({
        "date": TODAY,
        "parent": PARENT_REPO,
        "forks_data": forks_data,
        "bucket_counts": bucket_counts,
        "stats": {
            "total_forks": len(forks_data),
            "runs_checked": runs_checked,
            "aeon_checked": aeon_checked,
            "unreadable": unreadable_count
        }
    }, f, indent=2)

print(f"\nData saved to /tmp/fork-cohort-data.json")
print(f"Total processed: {len(forks_data)}")
print(f"Runs checked: {runs_checked}")
print(f"Aeon.yml checked: {aeon_checked}")
