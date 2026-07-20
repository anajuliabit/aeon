#!/usr/bin/env python3
"""Fetch forks from GitHub API, classify by run activity, compute deltas."""
import subprocess, json, datetime, sys, os

TODAY = "2026-07-19"
PARENT_REPO = "aaronjmars/aeon"
BOT_ALLOWLIST = {"dependabot[bot]", "github-actions[bot]", "aeonframework[bot]"}

def gh_api(path, paginate=False):
    cmd = ["gh", "api", path]
    if paginate:
        cmd.append("--paginate")
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        return None, result.stderr
    return result.stdout, None

def parse_iso(s):
    if not s:
        return None
    s = s.replace('Z', '+00:00')
    try:
        return datetime.datetime.fromisoformat(s).replace(tzinfo=datetime.timezone.utc)
    except:
        return None

def days_since(iso_str):
    if not iso_str:
        return float('inf')
    dt = parse_iso(iso_str)
    if not dt:
        return float('inf')
    now = datetime.datetime(2026, 7, 19, 20, 0, 0, tzinfo=datetime.timezone.utc)
    diff = (now - dt).total_seconds() / 86400
    return diff

# Step 1: fetch forks
print("Fetching forks...", file=sys.stderr)
raw, err = gh_api(f"repos/{PARENT_REPO}/forks?per_page=100&sort=newest", paginate=True)
if err or not raw:
    print(json.dumps({"error": f"API fail: {err}"}))
    sys.exit(1)

# Parse - may be multiple pages concatenated
raw = raw.strip()
try:
    if raw.startswith('[['):
        pages = json.loads('[' + raw.replace('][', '],[') + ']')
        all_forks = []
        for p in pages:
            all_forks.extend(p)
    else:
        all_forks = json.loads(raw)
except json.JSONDecodeError as e:
    # Try line by line
    all_forks = []
    for line in raw.split('\n'):
        line = line.strip()
        if line.startswith('[') and line.endswith(']'):
            try:
                all_forks.extend(json.loads(line))
            except:
                pass

# Filter archived/disabled, deduplicate
seen = set()
forks = []
for f in all_forks:
    if f.get('archived') or f.get('disabled'):
        continue
    fn = f['full_name']
    if fn not in seen:
        seen.add(fn)
        forks.append(f)

total_forks = len(forks)
print(f"Total unique forks: {total_forks}", file=sys.stderr)

# Sort by pushed_at desc, cap at 80
forks.sort(key=lambda x: x.get('pushed_at', ''), reverse=True)
truncated = total_forks > 80
if truncated:
    forks = forks[:80]
    print(f"Truncated to 80 (truncated_at=80)", file=sys.stderr)

# Step 2: load prior state
prior_path = "memory/topics/fork-cohort-state.json"
prior = {"forks": {}, "last_run": None}
if os.path.exists(prior_path):
    with open(prior_path) as fp:
        prior = json.load(fp)
prior_forks = prior.get("forks", {})

# Step 3 & 4 & 5: per-fork runs + classify
results = {}
run_success = 0
run_total = 0
aeon_yml_success = 0
aeon_yml_total = 0
unreadable_count = 0

for fork in forks:
    fn = fork['full_name']
    owner = fork['owner']['login'] if isinstance(fork.get('owner'), dict) else fork.get('owner', fn.split('/')[0])
    default_branch = fork.get('default_branch', 'main')
    stars = fork.get('stargazers_count', 0)
    created_at = fork.get('created_at', '')

    # Skip bot forks from classification but count in totals
    is_bot = owner in BOT_ALLOWLIST

    # Get last workflow run
    run_total += 1
    last_run = None
    bucket = None

    raw_run, err_run = gh_api(f"repos/{fn}/actions/runs?per_page=1")
    if err_run:
        # Check for 404
        if '404' in (err_run or ''):
            bucket = "COLD"
            last_run = None
        elif '403' in (err_run or ''):
            # retry once
            import time; time.sleep(60)
            raw_run2, err_run2 = gh_api(f"repos/{fn}/actions/runs?per_page=1")
            if err_run2:
                bucket = "UNREADABLE"
                unreadable_count += 1
            else:
                try:
                    data = json.loads(raw_run2)
                    runs = data.get('workflow_runs', [])
                    last_run = runs[0]['updated_at'] if runs else None
                    run_success += 1
                except:
                    bucket = "UNREADABLE"
                    unreadable_count += 1
        else:
            bucket = "UNREADABLE"
            unreadable_count += 1
    else:
        try:
            data = json.loads(raw_run)
            runs = data.get('workflow_runs', [])
            last_run = runs[0]['updated_at'] if runs else None
            run_success += 1
        except:
            bucket = "UNREADABLE"
            unreadable_count += 1

    if bucket is None:
        dsr = days_since(last_run)
        if dsr > 365 or last_run is None:
            bucket = "COLD"
        elif dsr < 7:
            # Need to check enabled count for POWER
            bucket = "_ACTIVE_CANDIDATE"
        else:
            bucket = "STALE"

    enabled_count = 0
    if bucket == "_ACTIVE_CANDIDATE":
        # Fetch aeon.yml
        aeon_yml_total += 1
        raw_yml, err_yml = gh_api(f"repos/{fn}/contents/aeon.yml?ref={default_branch}")
        if raw_yml and not err_yml:
            try:
                yml_data = json.loads(raw_yml)
                import base64
                content_b64 = yml_data.get('content', '')
                content = base64.b64decode(content_b64.replace('\n', '')).decode('utf-8', errors='replace')
                import re
                matches = re.findall(r'enabled:\s*true', content)
                # Don't count commented lines
                enabled_count = sum(1 for m in re.finditer(r'(?m)^(?!\s*#).*enabled:\s*true', content))
                aeon_yml_success += 1
            except:
                enabled_count = 0
        else:
            enabled_count = 0

        if enabled_count >= 5:
            bucket = "POWER"
        else:
            bucket = "ACTIVE"

    dsr = days_since(last_run)
    results[fn] = {
        "bucket": bucket,
        "last_run": last_run,
        "days_since_run": round(dsr, 1) if dsr != float('inf') else None,
        "enabled_count": enabled_count,
        "stargazers": stars,
        "default_branch": default_branch,
        "owner": owner,
        "created_at": created_at,
        "is_bot": is_bot
    }
    print(f"  {fn}: {bucket} (dsr={dsr:.1f if dsr != float('inf') else 'inf'}, enabled={enabled_count})", file=sys.stderr)

# Step 6: compute deltas
transitions = []
for fn, cur in results.items():
    prev = prior_forks.get(fn)
    cur_bucket = cur['bucket']
    if cur_bucket == "UNREADABLE":
        continue
    if prev is None:
        if cur_bucket in ("ACTIVE", "POWER"):
            tag = "NEW_ACTIVE"
        else:
            tag = "NEW_FORK"
        transitions.append({"fork": fn, "tag": tag, "owner": cur['owner'], "cur_bucket": cur_bucket, "prev_bucket": None})
    else:
        prev_bucket = prev.get('bucket', 'COLD')
        if prev_bucket == cur_bucket:
            continue
        if cur_bucket == "POWER":
            tag = "LEVELED_UP"
        elif prev_bucket in ("ACTIVE", "POWER") and cur_bucket == "STALE":
            tag = "WENT_STALE"
        elif prev_bucket in ("ACTIVE", "POWER") and cur_bucket == "COLD":
            tag = "WENT_COLD"
        elif prev_bucket == "STALE" and cur_bucket in ("ACTIVE", "POWER"):
            tag = "REVIVED"
        elif prev_bucket == "POWER" and cur_bucket == "ACTIVE":
            tag = "DROPPED_FROM_POWER"
        elif cur_bucket in ("ACTIVE", "POWER") and prev_bucket not in ("ACTIVE", "POWER"):
            tag = "NEW_ACTIVE"
        else:
            tag = None
        if tag:
            transitions.append({
                "fork": fn,
                "tag": tag,
                "owner": cur['owner'],
                "cur_bucket": cur_bucket,
                "prev_bucket": prev_bucket,
                "enabled_count": cur.get('enabled_count', 0),
                "days_since_run": cur.get('days_since_run')
            })

# Count buckets
counts = {"POWER": 0, "ACTIVE": 0, "STALE": 0, "COLD": 0, "UNREADABLE": 0}
for fn, r in results.items():
    b = r['bucket']
    if b in counts:
        counts[b] += 1

n_running = counts['POWER'] + counts['ACTIVE']

# Step 7: verdict
leveled_up = [t for t in transitions if t['tag'] == 'LEVELED_UP']
revived = [t for t in transitions if t['tag'] == 'REVIVED']
went_stale = [t for t in transitions if t['tag'] == 'WENT_STALE']
new_active = [t for t in transitions if t['tag'] == 'NEW_ACTIVE']
went_cold = [t for t in transitions if t['tag'] == 'WENT_COLD']
dropped = [t for t in transitions if t['tag'] == 'DROPPED_FROM_POWER']

has_prior = bool(prior.get('last_run'))

if leveled_up:
    verdict = f"LEVELED_UP: {len(leveled_up)} forks crossed POWER threshold"
elif revived:
    verdict = f"REVIVED: {len(revived)} stale forks running again"
elif went_stale:
    verdict = f"WENT_STALE: {len(went_stale)} active forks went quiet"
elif not transitions and has_prior:
    verdict = f"STEADY: {n_running} of {len(results)} running"
else:
    verdict = f"COLD START: {len(results)} forks, {n_running} running"

# Delta vs prior totals
prior_totals = prior.get('totals', {})
def delta(key, cur):
    prev = prior_totals.get(key, 0)
    diff = cur - prev
    return f"+{diff}" if diff >= 0 else str(diff)

output = {
    "today": TODAY,
    "parent_repo": PARENT_REPO,
    "total_forks": total_forks,
    "scanned": len(results),
    "truncated": truncated,
    "counts": counts,
    "n_running": n_running,
    "verdict": verdict,
    "transitions": transitions,
    "results": results,
    "prior_totals": prior_totals,
    "source_status": {
        "forks_list": "ok",
        "runs_lookup": f"{run_success}/{run_total}",
        "aeon_yml_lookup": f"{aeon_yml_success}/{aeon_yml_total}",
        "unreadable": unreadable_count,
        "truncated": truncated
    }
}

print(json.dumps(output, indent=2))
