#!/usr/bin/env python3
"""
skill-freshness: Audit enabled skills' upstream file dependencies for staleness.
Minimal implementation of SKILL.md specification.
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, Set, Tuple, List

TODAY = "2026-07-27"
NOW = datetime.now()
NOW_TS = NOW.timestamp()
REPO_ROOT = Path.cwd()
AEON_YML = REPO_ROOT / "aeon.yml"
ARTICLES = REPO_ROOT / "articles"
MEMORY_TOPICS = REPO_ROOT / "memory" / "topics"
MEMORY_LOGS = REPO_ROOT / "memory" / "logs"

THRESHOLDS_HOURS = {
    "articles_daily": 28,
    "articles_weekly": 192,
    "outputs": 4,
    "topics": 168,
    "state": 720,
}

def parse_aeon_yml() -> Tuple[Set[str], Dict[str, str]]:
    """Parse aeon.yml and return (enabled_skills, producer_cadence)."""
    enabled = set()
    cadence = {}

    with open(AEON_YML) as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i]
        # Match skill: { format
        skill_match = re.match(r'^\s*([a-z0-9_-]+):\s*\{', line)
        if skill_match:
            skill = skill_match.group(1)
            # Collect block until closing }
            block = line
            j = i
            while j < len(lines) and '}' not in block:
                j += 1
                block += lines[j]

            # Check enabled
            if re.search(r'enabled:\s*true', block):
                enabled.add(skill)

            # Extract schedule and determine cadence
            sched_match = re.search(r'schedule:\s*"([^"]*)"', block)
            if sched_match:
                schedule = sched_match.group(1)
                if schedule in ("workflow_dispatch", "reactive") or schedule == "":
                    cadence[skill] = "on_demand"
                elif re.search(r'\s[0-6](?:\s|$)', schedule):  # single weekday
                    cadence[skill] = "weekly"
                else:
                    cadence[skill] = "daily"
            else:
                cadence[skill] = "on_demand"
        i += 1

    return enabled, cadence

def extract_file_refs(skill: str) -> List[Tuple[str, str]]:
    """Extract file references from skill SKILL.md.
    Returns list of (path_pattern, class) tuples.
    """
    skill_md = REPO_ROOT / "skills" / skill / "SKILL.md"
    if not skill_md.exists():
        return []

    refs = []
    try:
        with open(skill_md) as f:
            content = f.read()
    except:
        return []

    # Strip fenced code blocks
    lines = content.split('\n')
    in_fence = False
    filtered = []
    for line in lines:
        if line.startswith('```'):
            in_fence = not in_fence
        elif not in_fence:
            filtered.append(line)
    content = '\n'.join(filtered)

    # articles/{name}-*.md (articles)
    for match in re.finditer(r'articles/([a-z0-9_-]+)(?:-\$\{today\}|-\d{4}-\d{2}-\d{2})?\.md', content):
        producer = match.group(1)
        if producer != skill:  # Skip self-refs
            refs.append((f"articles/{producer}-*.md", "articles"))

    # .outputs/{name}.md (outputs)
    for match in re.finditer(r'\.outputs/([a-z0-9_-]+)\.md', content):
        producer = match.group(1)
        if producer != skill:
            refs.append((f".outputs/{producer}.md", "outputs"))

    # memory/topics/{name}.md
    for match in re.finditer(r'memory/topics/([a-z0-9._-]+)\.md', content):
        refs.append((f"memory/topics/{match.group(1)}.md", "topics"))

    # memory/state/{name}.json
    for match in re.finditer(r'memory/state/([a-z0-9._-]+)\.json', content):
        refs.append((f"memory/state/{match.group(1)}.json", "state"))

    return refs

def get_file_age_hours(path: Path) -> float:
    """Get file age in hours, or -1 if missing."""
    if not path.exists():
        return -1
    mtime = path.stat().st_mtime
    return (NOW_TS - mtime) / 3600.0

def resolve_articles(pattern: str, cadence: Dict[str, str]) -> Tuple[float, str]:
    """Resolve articles/{producer}-*.md to actual age and cadence.
    Returns (age_hours, cadence_str) or (-1, "on_demand") if missing.
    """
    match = re.match(r'articles/([a-z0-9_-]+)-\*\.md', pattern)
    if not match:
        return -1, "on_demand"

    producer = match.group(1)
    prod_cadence = cadence.get(producer, "on_demand")

    # Find most recent file
    try:
        files = sorted(ARTICLES.glob(f"{producer}-*.md"), reverse=True)
        if files:
            age = get_file_age_hours(files[0])
            return age, prod_cadence
    except:
        pass

    return -1, prod_cadence

def score_severity(age_hours: float, threshold_hours: float) -> str:
    """Score age as OK/WARN/STALE/MISSING."""
    if age_hours < 0:
        return "MISSING"
    if age_hours <= threshold_hours:
        return "OK"
    if age_hours <= 2 * threshold_hours:
        return "WARN"
    return "STALE"

def format_age(hours: float) -> str:
    """Format hours as human string."""
    if hours < 0:
        return "missing"
    if hours < 1:
        return f"{int(hours * 60)}m"
    if hours < 24:
        return f"{hours:.1f}h"
    days = hours / 24
    return f"{days:.1f}d"

def main():
    # Parse args
    var = os.environ.get("INPUT_VAR", "").strip()
    mode = "execute"
    if var.startswith("dry-run"):
        mode = "dry-run"
        var = var[7:].strip()

    # Load config
    enabled_set, cadence_map = parse_aeon_yml()
    print(f"✓ Parsed aeon.yml: {len(enabled_set)} enabled skills", file=sys.stderr)

    if var and var not in enabled_set:
        print(f"SKILL_FRESHNESS_NO_MATCH: {var} not in enabled skills")
        return

    audit_set = {var} if var else enabled_set

    # Audit each skill
    all_flagged = []
    consumer_status = {}

    for skill in sorted(audit_set):
        refs = extract_file_refs(skill)
        worst_sev = "OK"
        worst_rank = {"OK": 0, "WARN": 1, "STALE": 2, "MISSING": 3}
        worst_entry = None

        for path_pattern, cls in refs:
            if cls == "articles":
                age, prod_cadence = resolve_articles(path_pattern, cadence_map)
                threshold = THRESHOLDS_HOURS["articles_weekly"] if prod_cadence == "weekly" else THRESHOLDS_HOURS["articles_daily"]
            elif cls == "outputs":
                age = get_file_age_hours(REPO_ROOT / path_pattern)
                threshold = THRESHOLDS_HOURS["outputs"]
            elif cls == "topics":
                age = get_file_age_hours(MEMORY_TOPICS / (path_pattern.split("/")[-1]))
                threshold = THRESHOLDS_HOURS["topics"]
            elif cls == "state":
                age = get_file_age_hours(REPO_ROOT / "memory" / "state" / (path_pattern.split("/")[-1]))
                threshold = THRESHOLDS_HOURS["state"]
            else:
                continue

            sev = score_severity(age, threshold)

            if worst_rank.get(sev, 0) > worst_rank.get(worst_sev, 0):
                worst_sev = sev
                worst_entry = (skill, path_pattern, cls, age, threshold, sev)

            if sev != "OK":
                all_flagged.append((skill, path_pattern, cls, age, threshold, sev))

        consumer_status[skill] = worst_sev

    # Determine fleet verdict
    verdict_rank = {"OK": 0, "WARN": 1, "STALE": 2, "MISSING": 3}
    fleet_verdict = max(consumer_status.values(), key=lambda v: verdict_rank.get(v, 0)) if consumer_status else "OK"

    print(f"✓ Fleet verdict: {fleet_verdict}", file=sys.stderr)
    print(f"✓ Flagged: {len(all_flagged)} of {sum(len(extract_file_refs(s)) for s in audit_set)} dependencies", file=sys.stderr)

    # Generate article
    article = f"""# Skill Freshness — {TODAY}

**Verdict:** {fleet_verdict}

*Audited {len(audit_set)} enabled skills · {sum(len(extract_file_refs(s)) for s in audit_set)} dependencies checked · {len(all_flagged)} flagged*
"""

    if all_flagged:
        article += "\n## Flagged dependencies\n\n"
        article += "| Consumer | Dependency | Class | Age | Severity |\n"
        article += "|----------|-----------|-------|-----|----------|\n"

        for skill, path, cls, age, threshold, sev in sorted(all_flagged, key=lambda x: (verdict_rank.get(x[5], 0), x[0]), reverse=True):
            age_str = format_age(age)
            emoji = {"WARN": "⚠️", "STALE": "🔴", "MISSING": "❌"}.get(sev, "")
            article += f"| {skill} | `{path}` | {cls} | {age_str} | {emoji} {sev} |\n"

    # Healthy
    healthy = [s for s in consumer_status if consumer_status[s] == "OK"]
    if healthy:
        article += f"\n## Healthy consumers\n\n"
        for s in sorted(healthy)[:8]:
            article += f"- {s}\n"
        if len(healthy) > 8:
            article += f"+ {len(healthy) - 8} more\n"

    article += f"\n---\n*Skill Freshness audit complete.*"

    # Write article
    article_path = ARTICLES / f"skill-freshness-{TODAY}.md"
    article_path.write_text(article)
    print(f"✓ Wrote {article_path}")

    # Append to log
    log_entry = f"""## Skill Freshness
- **Status**: {fleet_verdict}
- **Audited**: {len(audit_set)} skills · {len(all_flagged)} flagged
- **Article**: articles/skill-freshness-{TODAY}.md"""

    log_path = MEMORY_LOGS / f"{TODAY}.md"
    if log_path.exists():
        with open(log_path, "a") as f:
            f.write("\n" + log_entry)
    else:
        log_path.write_text(log_entry)

    print(f"✓ Logged to {log_path}")

    # Notify if not OK and not dry-run
    if mode != "dry-run" and fleet_verdict != "OK" and all_flagged:
        top_3 = sorted(all_flagged, key=lambda x: (verdict_rank.get(x[5], 0), -x[3] if x[3] >= 0 else 0), reverse=True)[:3]
        msg = f"*Skill Freshness — {TODAY}*\n"
        msg += f"{fleet_verdict} — {len(all_flagged)} flagged\n\nTop issues:\n"
        for skill, path, cls, age, threshold, sev in top_3:
            msg += f"- {skill} ← {path} ({format_age(age)}, {sev})\n"
        msg += f"\nFull: articles/skill-freshness-{TODAY}.md"

        # Call notify
        import subprocess
        subprocess.run(["./notify", msg], check=False)
        print(f"✓ Notification sent")
    else:
        print(f"✓ No notification (mode={mode}, verdict={fleet_verdict})")

if __name__ == "__main__":
    try:
        main()
        print("\n✓ Skill freshness audit complete", file=sys.stderr)
    except Exception as e:
        print(f"\n✗ Error: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)
