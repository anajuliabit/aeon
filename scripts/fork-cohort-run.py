#!/usr/bin/env python3
"""Fork cohort skill runner — processes forks via gh CLI calls."""
import json
import subprocess
import sys
from datetime import datetime, timezone

TODAY = "2026-07-05"
PARENT_REPO = "aaronjmars/aeon"
STATE_FILE = "memory/topics/fork-cohort-state.json"
BOT_ALLOWLIST = {"dependabot[bot]", "github-actions[bot]", "aeonframework[bot]"}
MAX_FORKS = 80


def gh_api(path, jq=None, allow_errors=True):
    cmd = ["gh", "api", path]
    if jq:
        cmd += ["--jq", jq]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
    if result.returncode != 0:
        if allow_errors:
            return None, result.returncode
        raise RuntimeError(result.stderr)
    return result.stdout.strip(), 0


def parse_dt(s):
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except Exception:
        return None


def days_since(dt_str):
    dt = parse_dt(dt_str)
    if dt is None:
        return float("inf")
    now = datetime.now(timezone.utc)
    return (now - dt).total_seconds() / 86400


def get_forks():
    cmd = [
        "gh", "api", "repos/aaronjmars/aeon/forks",
        "--paginate",
        "--jq", '[.[] | select(.archived != true and .disabled != true) | {full_name, owner: .owner.login, default_branch, pushed_at, stargazers_count, created_at}]'
    ]
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    if result.returncode != 0:
        return None
    raw = result.stdout.strip()
    try:
        data = json.loads(raw)
        # If paginated, might be list of lists
        if data and isinstance(data[0], list):
            flat = [item for page in data for item in page]
        else:
            flat = data
        return flat
    except Exception as e:
        print(f"JSON parse error: {e}", file=sys.stderr)
        return None


def get_last_run(fork_full_name, default_branch):
    """Returns (last_run_iso, status_code)"""
    out, code = gh_api(
        f"repos/{fork_full_name}/actions/runs?per_page=1",
        jq=".workflow_runs[0].updated_at // empty"
    )
    if code == 404:
        return None, 404
    if code in (403, 500, 502, 503):
        # Retry once
        import time
        wait = 60 if code == 403 else 10
        time.sleep(wait)
        out, code = gh_api(
            f"repos/{fork_full_name}/actions/runs?per_page=1",
            jq=".workflow_runs[0].updated_at // empty"
        )
        if code != 0:
            return None, code
    if code != 0:
        return None, code
    return out if out else None, 0


def get_enabled_count(fork_full_name, default_branch):
    out, code = gh_api(
        f"repos/{fork_full_name}/contents/aeon.yml?ref={default_branch}",
        jq=".content"
    )
    if code != 0 or not out:
        return 0
    # Decode base64
    import base64
    content_b64 = out.strip().replace("\\n", "").replace("\n", "")
    try:
        content = base64.b64decode(content_b64).decode("utf-8")
    except Exception:
        return 0
    count = 0
    for line in content.split("\n"):
        stripped = line.strip()
        if stripped.startswith("#"):
            continue
        if "enabled: true" in stripped or "enabled:true" in stripped:
            count += 1
    return count


def classify(last_run_iso, days, enabled_count, was_404):
    if was_404 or (days is not None and days > 365):
        return "COLD"
    if days is None:
        return "COLD"
    if days < 7 and enabled_count >= 5:
        return "POWER"
    if days < 7:
        return "ACTIVE"
    if days >= 7:
        return "STALE"
    return "UNREADABLE"


def bucket_transition(old_bucket, new_bucket, old_data):
    if old_bucket is None:
        if new_bucket in ("ACTIVE", "POWER"):
            return "NEW_ACTIVE"
        return "NEW_FORK"
    if new_bucket == "POWER" and old_bucket != "POWER":
        return "LEVELED_UP"
    if old_bucket == "POWER" and new_bucket == "ACTIVE":
        return "DROPPED_FROM_POWER"
    if old_bucket in ("ACTIVE", "POWER") and new_bucket == "STALE":
        return "WENT_STALE"
    if old_bucket == "STALE" and new_bucket in ("ACTIVE", "POWER"):
        return "REVIVED"
    if old_bucket in ("ACTIVE", "POWER") and new_bucket == "COLD":
        return "WENT_COLD"
    return None


def main():
    # Load prior state
    try:
        with open(STATE_FILE) as f:
            prior_state = json.load(f)
    except Exception:
        prior_state = {"forks": {}, "last_run": None}

    prior_forks = prior_state.get("forks", {})
    is_first_run = not prior_state.get("last_run")

    print(f"Prior run: {prior_state.get('last_run')} — {len(prior_forks)} prior forks tracked")

    # Fetch forks
    print("Fetching fork list...")
    forks = get_forks()
    if forks is None:
        print("FORK_COHORT_API_FAIL: could not fetch fork list")
        return

    total_available = len(forks)
    print(f"Total forks fetched: {total_available}")

    # Sort by pushed_at desc and cap at 80
    def push_key(f):
        return f.get("pushed_at") or "1970-01-01T00:00:00Z"

    forks.sort(key=push_key, reverse=True)
    truncated = total_available > MAX_FORKS
    if truncated:
        print(f"Truncating to {MAX_FORKS} (total={total_available})")
        forks = forks[:MAX_FORKS]

    # Process each fork
    results = {}
    runs_ok = 0
    runs_total = 0
    aeon_ok = 0
    aeon_total = 0
    unreadable_count = 0

    for i, fork in enumerate(forks):
        full_name = fork["full_name"]
        owner = fork["owner"]
        default_branch = fork.get("default_branch") or "main"
        stars = fork.get("stargazers_count", 0)

        # Skip bot owners from rendering but still track
        is_bot = owner in BOT_ALLOWLIST or owner.endswith("[bot]")

        print(f"  [{i+1}/{len(forks)}] {full_name}...", end=" ", flush=True)

        # Get last run
        runs_total += 1
        last_run, code = get_last_run(full_name, default_branch)
        was_404 = (code == 404)
        if code not in (0, 404):
            print(f"UNREADABLE (code={code})")
            results[full_name] = {
                "bucket": "UNREADABLE",
                "last_run": None,
                "days_since_run": None,
                "enabled_count": 0,
                "stargazers": stars,
                "default_branch": default_branch,
                "owner": owner,
                "is_bot": is_bot,
                "created_at": fork.get("created_at"),
            }
            unreadable_count += 1
            continue

        runs_ok += 1
        d = days_since(last_run) if last_run else float("inf")
        if d == float("inf"):
            d_display = None
        else:
            d_display = round(d, 1)

        # Get enabled count only for ACTIVE candidates
        enabled_count = 0
        if last_run and d < 7:
            aeon_total += 1
            enabled_count = get_enabled_count(full_name, default_branch)
            if enabled_count > 0:
                aeon_ok += 1

        bucket = classify(last_run, d if last_run else None, enabled_count, was_404)
        print(f"{bucket} (last={last_run[:10] if last_run else 'never'}, enabled={enabled_count})")

        results[full_name] = {
            "bucket": bucket,
            "last_run": last_run,
            "days_since_run": d_display,
            "enabled_count": enabled_count,
            "stargazers": stars,
            "default_branch": default_branch,
            "owner": owner,
            "is_bot": is_bot,
            "created_at": fork.get("created_at"),
        }

    # Count totals (non-bot)
    non_bot = {k: v for k, v in results.items() if not v.get("is_bot")}
    counts = {"POWER": 0, "ACTIVE": 0, "STALE": 0, "COLD": 0, "UNREADABLE": 0}
    for v in non_bot.values():
        b = v["bucket"]
        counts[b] = counts.get(b, 0) + 1

    n_total = len(non_bot)
    n_running = counts["POWER"] + counts["ACTIVE"]

    # Week-over-week transitions
    transitions = {}
    for full_name, data in results.items():
        if data.get("is_bot"):
            continue
        old = prior_forks.get(full_name)
        old_bucket = old["bucket"] if old else None
        new_bucket = data["bucket"]
        tag = bucket_transition(old_bucket, new_bucket, old)
        if tag:
            transitions[full_name] = {
                "tag": tag,
                "old_bucket": old_bucket,
                "new_bucket": new_bucket,
                "data": data,
            }

    # Prior totals for delta
    prior_totals = prior_state.get("totals", {})

    def delta_str(new_val, key):
        old_val = prior_totals.get(key, 0)
        diff = new_val - old_val
        if diff > 0:
            return f"+{diff}"
        elif diff < 0:
            return str(diff)
        return "0"

    # Group transitions
    leveled_up = [(k, v) for k, v in transitions.items() if v["tag"] == "LEVELED_UP"]
    revived = [(k, v) for k, v in transitions.items() if v["tag"] == "REVIVED"]
    went_stale = [(k, v) for k, v in transitions.items() if v["tag"] == "WENT_STALE"]
    new_active = [(k, v) for k, v in transitions.items() if v["tag"] == "NEW_ACTIVE"]
    went_cold = [(k, v) for k, v in transitions.items() if v["tag"] == "WENT_COLD"]
    dropped = [(k, v) for k, v in transitions.items() if v["tag"] == "DROPPED_FROM_POWER"]

    # Pick verdict
    if is_first_run:
        verdict = f"COLD START: {n_total} forks, {n_running} running"
    elif leveled_up:
        verdict = f"LEVELED_UP: {len(leveled_up)} fork(s) crossed POWER threshold"
    elif revived:
        verdict = f"REVIVED: {len(revived)} stale fork(s) running again"
    elif went_stale:
        verdict = f"WENT_STALE: {len(went_stale)} active fork(s) went quiet"
    elif transitions:
        verdict = f"MOVEMENT: {len(transitions)} bucket changes this week"
    else:
        verdict = f"STEADY: {n_running} of {n_total} running"

    pct = round(n_running / n_total * 100) if n_total > 0 else 0
    print(f"\nVerdict: {verdict}")
    print(f"Totals: POWER={counts['POWER']} ACTIVE={counts['ACTIVE']} STALE={counts['STALE']} COLD={counts['COLD']} UNREADABLE={counts['UNREADABLE']}")

    # Build article
    lines = []
    lines.append(f"# Fork Activation Cohort — {TODAY}")
    lines.append("")
    lines.append(f"**Verdict:** {verdict}")
    lines.append("")
    lines.append(f"**Parent:** {PARENT_REPO}")
    lines.append(f"**Total forks:** {n_total} · **Running (last 7d):** {n_running} ({pct}%)")
    if truncated:
        lines.append(f"_Note: Scanned top {MAX_FORKS} of {total_available} forks by recent push activity (truncated)._")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Cohort breakdown")
    lines.append("")
    lines.append("| Cohort | Count | Δ vs last week |")
    lines.append("|--------|-------|----------------|")
    lines.append(f"| POWER | {counts['POWER']} | {delta_str(counts['POWER'], 'power')} |")
    lines.append(f"| ACTIVE | {counts['ACTIVE']} | {delta_str(counts['ACTIVE'], 'active')} |")
    lines.append(f"| STALE | {counts['STALE']} | {delta_str(counts['STALE'], 'stale')} |")
    lines.append(f"| COLD | {counts['COLD']} | {delta_str(counts['COLD'], 'cold')} |")
    if counts["UNREADABLE"] > 0:
        lines.append(f"| UNREADABLE | {counts['UNREADABLE']} | {delta_str(counts['UNREADABLE'], 'unreadable')} |")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## Movement this week")
    lines.append("")

    has_movement = any([leveled_up, revived, went_stale, new_active, went_cold, dropped])
    if not has_movement:
        lines.append("_No bucket changes this week._")
    else:
        if leveled_up:
            lines.append("### Leveled up to POWER")
            for k, v in leveled_up:
                d = v["data"]
                dsr = d.get("days_since_run")
                days_str = f"{dsr}d" if dsr is not None else "0d"
                lines.append(f"- @{d['owner']} — `{k}` (+{d['enabled_count']} skills enabled, last run {days_str} ago)")
            lines.append("")

        if revived:
            lines.append("### Revived (stale → running)")
            for k, v in revived:
                d = v["data"]
                old = prior_forks.get(k, {})
                old_last = old.get("last_run", "unknown")
                old_date = old_last[:10] if old_last else "unknown"
                dsr = d.get("days_since_run")
                days_str = f"{dsr}d" if dsr is not None else "0d"
                lines.append(f"- @{d['owner']} — `{k}` (last run {days_str} ago, was last seen {old_date})")
            lines.append("")

        if went_stale:
            lines.append("### Went stale (active → quiet)")
            for k, v in went_stale:
                d = v["data"]
                dsr = d.get("days_since_run")
                days_str = f"{dsr}d" if dsr is not None else "?"
                lines.append(f"- @{d['owner']} — `{k}` (last run {days_str} ago, dropped from {v['old_bucket']})")
            lines.append("")

        if new_active:
            lines.append("### New forks running")
            for k, v in new_active:
                d = v["data"]
                created = d.get("created_at", "")
                created_date = created[:10] if created else "unknown"
                dsr = d.get("days_since_run")
                days_str = f"{dsr}d" if dsr is not None else "0d"
                lines.append(f"- @{d['owner']} — `{k}` (created {created_date}, last run {days_str} ago)")
            lines.append("")

        if went_cold:
            lines.append("### Newly cold (was running, now silent >365d)")
            for k, v in went_cold:
                d = v["data"]
                lr = d.get("last_run")
                lr_date = lr[:10] if lr else "unknown"
                lines.append(f"- @{d['owner']} — `{k}` (last run {lr_date})")
            lines.append("")

        if dropped:
            lines.append("### Dropped from POWER")
            for k, v in dropped:
                d = v["data"]
                dsr = d.get("days_since_run")
                days_str = f"{dsr}d" if dsr is not None else "?"
                lines.append(f"- @{d['owner']} — `{k}` (now ACTIVE, {d['enabled_count']} skills enabled, last run {days_str} ago)")
            lines.append("")

    lines.append("---")
    lines.append("")

    # POWER roster
    power_forks = [(k, v) for k, v in non_bot.items() if v["bucket"] == "POWER"]
    power_forks.sort(key=lambda x: x[1].get("enabled_count", 0), reverse=True)
    if power_forks:
        lines.append("## POWER cohort roster")
        lines.append("")
        lines.append("| Fork | Owner | Enabled skills | Last run | Stars |")
        lines.append("|------|-------|----------------|----------|-------|")
        display = power_forks[:30]
        for k, v in display:
            lr = v.get("last_run")
            dsr = v.get("days_since_run")
            if dsr is not None and dsr < 1:
                lr_display = f"{round(dsr*24)}h ago"
            elif dsr is not None:
                lr_display = f"{dsr}d ago"
            else:
                lr_display = "unknown"
            lines.append(f"| {k} | @{v['owner']} | {v['enabled_count']} | {lr_display} | {v['stargazers']} |")
        if len(power_forks) > 30:
            lines.append(f"_... and {len(power_forks) - 30} more_")
        lines.append("")
        lines.append("---")
        lines.append("")

    # Source status
    unreadable_n = counts["UNREADABLE"]
    trunc_str = "true" if truncated else "false"
    lines.append("## Source status")
    lines.append("")
    lines.append(f"`forks_list=ok · runs_lookup={runs_ok}/{runs_total} · aeon_yml_lookup={aeon_ok}/{aeon_total} · unreadable={unreadable_n} · truncated={trunc_str}`")

    article_content = "\n".join(lines)

    # Write article
    article_path = f"articles/fork-cohort-{TODAY}.md"
    with open(article_path, "w") as f:
        f.write(article_content)
    print(f"Article written: {article_path}")

    # Build new state
    state_forks = {}
    for k, v in results.items():
        state_forks[k] = {
            "bucket": v["bucket"],
            "last_run": v.get("last_run"),
            "days_since_run": v.get("days_since_run"),
            "enabled_count": v.get("enabled_count", 0),
            "stargazers": v.get("stargazers", 0),
            "default_branch": v.get("default_branch", "main"),
        }

    new_state = {
        "last_run": TODAY,
        "last_status": "FORK_COHORT_OK",
        "parent_repo": PARENT_REPO,
        "totals": {
            "total": n_total,
            "scanned": len(forks),
            "truncated": truncated,
            "power": counts["POWER"],
            "active": counts["ACTIVE"],
            "stale": counts["STALE"],
            "cold": counts["COLD"],
            "unreadable": counts["UNREADABLE"],
        },
        "forks": state_forks,
    }

    with open(STATE_FILE, "w") as f:
        json.dump(new_state, f, indent=2)
    print(f"State written: {STATE_FILE}")

    # Determine exit status
    if is_first_run:
        exit_status = "FORK_COHORT_OK"
    elif verdict.startswith("STEADY") and not transitions:
        exit_status = "FORK_COHORT_QUIET"
    else:
        exit_status = "FORK_COHORT_OK"

    # Print summary info for notify
    print(f"\nEXIT_STATUS={exit_status}")
    print(f"VERDICT={verdict}")
    print(f"N_TOTAL={n_total} N_RUNNING={n_running} PCT={pct}")
    print(f"POWER={counts['POWER']} ACTIVE={counts['ACTIVE']} STALE={counts['STALE']} COLD={counts['COLD']}")
    print(f"LEVELED_UP={len(leveled_up)} REVIVED={len(revived)} WENT_STALE={len(went_stale)} NEW_ACTIVE={len(new_active)} WENT_COLD={len(went_cold)}")

    # Save summary for shell consumption
    summary = {
        "exit_status": exit_status,
        "verdict": verdict,
        "n_total": n_total,
        "n_running": n_running,
        "pct": pct,
        "counts": counts,
        "leveled_up": [(k, v["data"]["owner"], v["data"].get("enabled_count", 0)) for k, v in leveled_up],
        "revived": [(k, v["data"]["owner"]) for k, v in revived],
        "went_stale": [(k, v["data"]["owner"], v["data"].get("days_since_run")) for k, v in went_stale],
        "new_active": [(k, v["data"]["owner"]) for k, v in new_active],
        "went_cold": [(k, v["data"]["owner"]) for k, v in went_cold],
        "article_path": article_path,
    }
    with open(".fork-cohort-summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print("Summary written: .fork-cohort-summary.json")


if __name__ == "__main__":
    main()
