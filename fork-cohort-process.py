#!/usr/bin/env python3
"""Fork cohort processor — fetches forks, queries runs, classifies, outputs JSON."""
import json, subprocess, sys, re, base64, time
from datetime import datetime, timezone

TODAY = "2026-08-16"
PARENT_REPO = "aaronjmars/aeon"
BOT_OWNERS = {"dependabot[bot]", "github-actions[bot]", "aeonframework[bot]"}

def gh_api(path, jq=None, paginate=False):
    cmd = ['gh', 'api', path]
    if paginate:
        cmd.append('--paginate')
    if jq:
        cmd += ['--jq', jq]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            stderr = r.stderr.strip()
            if 'HTTP 404' in stderr or '404' in stderr:
                return None, 404
            if 'HTTP 403' in stderr or '403' in stderr:
                return None, 403
            return None, r.returncode
        return r.stdout.strip(), 0
    except subprocess.TimeoutExpired:
        return None, -1
    except Exception:
        return None, -1

# Step 2: Fetch forks list (paginated)
print("Fetching forks list...", file=sys.stderr)
forks_raw, rc = gh_api(
    f"repos/{PARENT_REPO}/forks?per_page=100",
    jq='[.[] | select(.archived != true and .disabled != true) | {full_name, owner: .owner.login, default_branch, pushed_at, stargazers_count, created_at}]',
    paginate=True
)
if rc != 0 or not forks_raw:
    print(json.dumps({"error": "FORK_COHORT_API_FAIL", "rc": rc}))
    sys.exit(1)

# paginate produces multiple JSON arrays (one per page), merge them
forks = []
seen_names = set()
# Split on top-level JSON array boundaries
for m in re.finditer(r'\[.*?\]', forks_raw, re.DOTALL):
    try:
        arr = json.loads(m.group())
        for f in arr:
            if f['full_name'] not in seen_names:
                seen_names.add(f['full_name'])
                forks.append(f)
    except json.JSONDecodeError:
        pass

n_total = len(forks)
print(f"Total forks: {n_total}", file=sys.stderr)

# Sort by pushed_at desc and cap at 80
forks.sort(key=lambda x: x.get('pushed_at',''), reverse=True)
truncated = n_total > 80
scan_forks = forks[:80]
print(f"Scanning {len(scan_forks)}, truncated={truncated}", file=sys.stderr)

now = datetime.now(timezone.utc)

def days_since(iso):
    if not iso:
        return float('inf')
    try:
        dt = datetime.fromisoformat(iso.replace('Z', '+00:00'))
        return (now - dt).total_seconds() / 86400
    except Exception:
        return float('inf')

results = {}
runs_ok = 0
runs_fail = 0
aeon_yml_ok = 0
aeon_yml_fail = 0

for i, fork in enumerate(scan_forks):
    fn = fork['full_name']
    owner = fork['owner']
    branch = fork.get('default_branch', 'main')

    print(f"[{i+1}/{len(scan_forks)}] {fn}", file=sys.stderr)

    # Step 3: get last workflow run
    out, rc = gh_api(f"repos/{fn}/actions/runs?per_page=1", '.workflow_runs[0].updated_at // empty')

    if rc == 404:
        bucket = 'COLD'
        last_run = None
        dsr = float('inf')
        runs_ok += 1
    elif rc == 403:
        # Rate limited — retry once after 60s
        time.sleep(60)
        out, rc = gh_api(f"repos/{fn}/actions/runs?per_page=1", '.workflow_runs[0].updated_at // empty')
        if rc != 0:
            bucket = 'UNREADABLE'
            last_run = None
            dsr = float('inf')
            runs_fail += 1
            results[fn] = {'bucket': bucket, 'last_run': last_run, 'days_since_run': None,
                           'enabled_count': 0, 'stargazers': fork.get('stargazers_count', 0),
                           'default_branch': branch, 'owner': owner}
            continue
        else:
            last_run = out if out else None
            dsr = days_since(last_run)
            runs_ok += 1
    elif rc != 0:
        # Retry once after 10s
        time.sleep(10)
        out, rc = gh_api(f"repos/{fn}/actions/runs?per_page=1", '.workflow_runs[0].updated_at // empty')
        if rc != 0:
            bucket = 'UNREADABLE'
            last_run = None
            dsr = float('inf')
            runs_fail += 1
            results[fn] = {'bucket': bucket, 'last_run': last_run, 'days_since_run': None,
                           'enabled_count': 0, 'stargazers': fork.get('stargazers_count', 0),
                           'default_branch': branch, 'owner': owner}
            continue
        else:
            last_run = out if out else None
            dsr = days_since(last_run)
            runs_ok += 1
    else:
        last_run = out if out else None
        dsr = days_since(last_run)
        runs_ok += 1

    # Step 4: enabled count for ACTIVE/POWER candidates
    enabled_count = 0
    if dsr < 7:
        yml_b64, yml_rc = gh_api(f"repos/{fn}/contents/aeon.yml?ref={branch}", '.content')
        if yml_b64 and yml_rc == 0:
            try:
                # base64 may be split across lines
                content = base64.b64decode(yml_b64.replace('\n', '')).decode('utf-8', errors='replace')
                enabled_count = sum(
                    1 for line in content.splitlines()
                    if re.search(r'enabled:\s*true', line) and not line.strip().startswith('#')
                )
                aeon_yml_ok += 1
            except Exception:
                aeon_yml_fail += 1
        else:
            aeon_yml_fail += 1

    # Step 5: classify
    if rc == 404 or dsr > 365:
        bucket = 'COLD'
    elif dsr < 7 and enabled_count >= 5:
        bucket = 'POWER'
    elif dsr < 7:
        bucket = 'ACTIVE'
    elif dsr >= 7:
        bucket = 'STALE'
    else:
        bucket = 'UNREADABLE'

    dsr_out = round(dsr, 1) if dsr != float('inf') else None
    results[fn] = {
        'bucket': bucket,
        'last_run': last_run,
        'days_since_run': dsr_out,
        'enabled_count': enabled_count,
        'stargazers': fork.get('stargazers_count', 0),
        'default_branch': branch,
        'owner': owner,
        'created_at': fork.get('created_at', '')
    }
    print(f"  -> {bucket} (dsr={dsr_out}, enabled={enabled_count})", file=sys.stderr)

# Tally
counts = {'POWER': 0, 'ACTIVE': 0, 'STALE': 0, 'COLD': 0, 'UNREADABLE': 0}
for v in results.values():
    counts[v['bucket']] = counts.get(v['bucket'], 0) + 1

output = {
    'n_total': n_total,
    'truncated': truncated,
    'runs_ok': runs_ok,
    'runs_fail': runs_fail,
    'aeon_yml_ok': aeon_yml_ok,
    'aeon_yml_fail': aeon_yml_fail,
    'counts': counts,
    'forks': results
}
print(json.dumps(output))
