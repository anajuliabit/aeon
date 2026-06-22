import subprocess, json, sys
from datetime import datetime, timezone

TODAY = "2026-06-21"
NOW = datetime(2026, 6, 21, 19, 30, 0, tzinfo=timezone.utc)
PARENT = "aaronjmars/aeon"

# Fetch all forks
result = subprocess.run(
    ["gh", "api", f"repos/{PARENT}/forks", "--paginate",
     "--jq", '.[] | select(.archived != true and .disabled != true) | {full_name, owner: .owner.login, default_branch, pushed_at, stargazers_count, created_at}'],
    capture_output=True, text=True
)
lines = [l.strip() for l in result.stdout.strip().split('\n') if l.strip()]
forks = []
seen = set()
for l in lines:
    try:
        f = json.loads(l)
        if f['full_name'] not in seen:
            seen.add(f['full_name'])
            forks.append(f)
    except: pass

forks.sort(key=lambda x: x['pushed_at'], reverse=True)
total_forks = len(forks)
truncated = total_forks > 80
top80 = forks[:80]
print(f"TOTAL_FORKS={total_forks} PROCESSING={len(top80)} TRUNCATED={truncated}", flush=True)

BOT_ALLOWLIST = {"dependabot[bot]", "github-actions[bot]", "aeonframework[bot]"}

results = []
runs_ok = 0
runs_fail = 0
aeon_ok = 0
aeon_fail = 0

for i, fork in enumerate(top80):
    fn = fork['full_name']
    owner = fork['owner']
    branch = fork['default_branch']

    # Skip bot owners from rendering but count in totals
    is_bot = owner in BOT_ALLOWLIST

    # Step 3: Get last workflow run
    last_run = None
    bucket = None
    runs_status = 200

    r = subprocess.run(
        ["gh", "api", f"repos/{fn}/actions/runs?per_page=1",
         "--jq", ".workflow_runs[0].updated_at // empty"],
        capture_output=True, text=True
    )

    if r.returncode == 0:
        runs_ok += 1
        last_run_raw = r.stdout.strip()
        last_run = last_run_raw if last_run_raw else None
    else:
        stderr = r.stderr.strip()
        if "404" in stderr or "Not Found" in stderr:
            bucket = "COLD"
            last_run = None
            runs_ok += 1  # 404 = treat as COLD, not a real failure
        elif "403" in stderr:
            # Retry once
            import time; time.sleep(2)
            r2 = subprocess.run(
                ["gh", "api", f"repos/{fn}/actions/runs?per_page=1",
                 "--jq", ".workflow_runs[0].updated_at // empty"],
                capture_output=True, text=True
            )
            if r2.returncode == 0:
                runs_ok += 1
                last_run_raw = r2.stdout.strip()
                last_run = last_run_raw if last_run_raw else None
            else:
                bucket = "UNREADABLE"
                runs_fail += 1
        else:
            # 5xx or other
            bucket = "UNREADABLE"
            runs_fail += 1

    # Compute days_since_run
    days_since_run = float('inf')
    if last_run:
        try:
            dt = datetime.fromisoformat(last_run.replace('Z', '+00:00'))
            days_since_run = (NOW - dt).total_seconds() / 86400
        except: pass

    # Step 4: enabled count (only for ACTIVE candidates)
    enabled_count = 0

    # Step 5: Classify
    if bucket is None:  # not already COLD or UNREADABLE from API errors
        if last_run is None:
            bucket = "COLD"
        elif days_since_run > 365:
            bucket = "COLD"
        elif days_since_run < 7:
            # Need to check enabled count for POWER
            r2 = subprocess.run(
                ["gh", "api", f"repos/{fn}/contents/aeon.yml?ref={branch}",
                 "--jq", ".content"],
                capture_output=True, text=True
            )
            if r2.returncode == 0 and r2.stdout.strip():
                import base64
                try:
                    content = base64.b64decode(r2.stdout.strip()).decode('utf-8', errors='replace')
                    # Count enabled: true (not in comments)
                    count = 0
                    for line in content.split('\n'):
                        stripped = line.strip()
                        if stripped.startswith('#'):
                            continue
                        import re
                        if re.search(r'enabled:\s*true', stripped):
                            count += 1
                    enabled_count = count
                    aeon_ok += 1
                except:
                    aeon_fail += 1
            else:
                aeon_fail += 1

            if enabled_count >= 5:
                bucket = "POWER"
            else:
                bucket = "ACTIVE"
        else:
            bucket = "STALE"

    results.append({
        "full_name": fn,
        "owner": owner,
        "is_bot": is_bot,
        "bucket": bucket,
        "last_run": last_run,
        "days_since_run": round(days_since_run, 1) if days_since_run != float('inf') else None,
        "enabled_count": enabled_count,
        "stargazers_count": fork['stargazers_count'],
        "default_branch": branch,
        "created_at": fork['created_at'],
        "pushed_at": fork['pushed_at'],
    })

    print(f"[{i+1}/{len(top80)}] {fn} → {bucket} (last_run: {last_run}, days: {round(days_since_run,1) if days_since_run != float('inf') else 'inf'}, enabled: {enabled_count})", flush=True)

# Write results
output = {
    "total_forks": total_forks,
    "processed": len(top80),
    "truncated": truncated,
    "runs_ok": runs_ok,
    "runs_fail": runs_fail,
    "aeon_ok": aeon_ok,
    "aeon_fail": aeon_fail,
    "results": results
}
with open("memory/topics/fork-cohort-results.json", "w") as f:
    json.dump(output, f, indent=2)
print(f"\nDone. Results written to memory/topics/fork-cohort-results.json", flush=True)
