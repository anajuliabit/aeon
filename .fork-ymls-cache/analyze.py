#!/usr/bin/env python3
"""Fork skill digest analysis script."""

import json
import os
import subprocess
import base64
import sys
import re
from collections import defaultdict

CACHE_DIR = "/home/runner/work/aeon/aeon/.fork-ymls-cache"
UPSTREAM_YML = "/home/runner/work/aeon/aeon/aeon.yml"
SKILLS_DIR = "/home/runner/work/aeon/aeon/skills"
TODAY = "2026-07-19"
TARGET_REPO = "aaronjmars/aeon"

ACTIVE_FORKS = [
    {"full_name": "Sauken-69/aeon", "default_branch": "main"},
    {"full_name": "enuno/noesis-aeon", "default_branch": "main"},
    {"full_name": "aeonbookai/aeonTemplate", "default_branch": "main"},
    {"full_name": "kriptoburak/aeon-xquik", "default_branch": "main"},
    {"full_name": "ostrov9878/aeon", "default_branch": "main"},
    {"full_name": "techdigger/aeon", "default_branch": "main"},
    {"full_name": "Aluma/aeon", "default_branch": "main"},
    {"full_name": "KingKaonix/aeon", "default_branch": "main"},
    {"full_name": "mattsegura/aeon", "default_branch": "main"},
    {"full_name": "Svector-anu/svectors-lab", "default_branch": "main"},
    {"full_name": "nigelon11/aeon", "default_branch": "main"},
    {"full_name": "webguy-cloud/aeon", "default_branch": "main"},
    {"full_name": "s97472091-pixel/aeon", "default_branch": "main"},
    {"full_name": "usepaxterapp/aeon", "default_branch": "main"},
    {"full_name": "penguinxbt/aeon", "default_branch": "main"},
    {"full_name": "freezerboi/aeon", "default_branch": "main"},
    {"full_name": "anajuliabit/aeon-fork", "default_branch": "main"},
    {"full_name": "madmystic/aeon", "default_branch": "main"},
    {"full_name": "SamsShow/aeon", "default_branch": "main"},
    {"full_name": "Marr554/aeon", "default_branch": "main"},
    {"full_name": "alpenflow/aeon", "default_branch": "main"},
    {"full_name": "stefrogovskyi/aeon", "default_branch": "main"},
    {"full_name": "usephylax/aeon", "default_branch": "main"},
    {"full_name": "saivarmadpr/aeon", "default_branch": "main"},
    {"full_name": "Tholynceus/aeon", "default_branch": "main"},
    {"full_name": "maredek-bot/aeon", "default_branch": "main"},
    {"full_name": "CharonAI-code/aeon", "default_branch": "main"},
    {"full_name": "clawhunter/add-clawhunter-pack", "default_branch": "main"},
    {"full_name": "zszkey/aeon-1", "default_branch": "main"},
    {"full_name": "sinfronterasai/aeon", "default_branch": "main"},
    {"full_name": "gitlumen-team/aeon", "default_branch": "main"},
    {"full_name": "ashneil12/aeon-upstream", "default_branch": "main"},
    {"full_name": "chxoky/aeon", "default_branch": "main"},
    {"full_name": "aeoncity-hub/aeon", "default_branch": "main"},
    {"full_name": "beijiangqukuailian/aeon", "default_branch": "main"},
    {"full_name": "vigilcodes/aeon", "default_branch": "main"},
    {"full_name": "yindaqiu/aeon", "default_branch": "main"},
    {"full_name": "BBridgeers/aeon", "default_branch": "main"},
    {"full_name": "swarm-ai-research/aeon-atlas", "default_branch": "main"},
    {"full_name": "TakamiyaZee/aeon", "default_branch": "main"},
    {"full_name": "xBalbinus/aeon", "default_branch": "main"},
    {"full_name": "sparkleware/aeon", "default_branch": "main"},
    {"full_name": "UIZorrot/aeon", "default_branch": "main"},
    {"full_name": "lawbworld-tech/aeon", "default_branch": "main"},
    {"full_name": "gitlawbounty/aeon", "default_branch": "main"},
    {"full_name": "taekwonv89/aeon", "default_branch": "main"},
    {"full_name": "0xMal0u/aeon", "default_branch": "main"},
    {"full_name": "youpsla/aeon", "default_branch": "main"},
    {"full_name": "antfleet-ops/aeon", "default_branch": "main"},
    {"full_name": "damo-nu11/aeon-minebean", "default_branch": "main"},
    {"full_name": "abhirajprasad/aeon", "default_branch": "main"},
    {"full_name": "enzoonchain/aeon", "default_branch": "main"},
    {"full_name": "AntFleet/aeon-template", "default_branch": "main"},
    {"full_name": "takanafur/aeon", "default_branch": "main"},
    {"full_name": "madebyshun/blueagent-aeon", "default_branch": "main"},
    {"full_name": "Da6hkin/aeon", "default_branch": "main"},
    {"full_name": "Boodszw/Boodszw_Bread", "default_branch": "main"},
    {"full_name": "ether-btc/aeon", "default_branch": "main"},
    {"full_name": "yugo-engineer/aeon", "default_branch": "main"},
    {"full_name": "pezetel/aeon", "default_branch": "main"},
    {"full_name": "AmithKumar1/aeon", "default_branch": "main"},
]


def safe_name(full_name):
    return full_name.replace("/", "_")


def run_gh(args, timeout=30):
    try:
        result = subprocess.run(
            ["gh"] + args,
            capture_output=True, text=True, timeout=timeout
        )
        return result.returncode, result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return -1, "", "timeout"


def fetch_fork_yml(fork):
    full_name = fork["full_name"]
    branch = fork["default_branch"]
    cache_path = os.path.join(CACHE_DIR, safe_name(full_name) + ".yml")
    status_path = os.path.join(CACHE_DIR, safe_name(full_name) + ".status")

    # Check cache
    if os.path.exists(cache_path):
        print(f"  {full_name}: cached")
        return "ok", cache_path
    if os.path.exists(status_path):
        with open(status_path) as f:
            return f.read().strip(), None

    print(f"  Fetching {full_name}...", end=" ", flush=True)
    rc, out, err = run_gh([
        "api",
        f"repos/{full_name}/contents/aeon.yml?ref={branch}",
        "--jq", ".content"
    ])

    if rc != 0 or "Not Found" in err or "HTTP 404" in err or "404" in out:
        print("NO_AEON_YML")
        with open(status_path, "w") as f:
            f.write("no_aeon_yml")
        return "no_aeon_yml", None

    try:
        # out is base64 content (possibly multi-line)
        content = base64.b64decode(out.strip())
        with open(cache_path, "wb") as f:
            f.write(content)
        print("OK")
        return "ok", cache_path
    except Exception as e:
        print(f"DECODE_FAIL: {e}")
        with open(status_path, "w") as f:
            f.write("yml_invalid")
        return "yml_invalid", None


def parse_skills_from_yml(text):
    """
    Minimal YAML parser for aeon.yml skills section.
    Returns dict: skill_name -> {enabled, model, var, schedule}
    """
    skills = {}
    in_skills = False
    in_skill = None

    lines = text.split("\n")
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.rstrip()

        # Detect skills: block
        if re.match(r'^skills\s*:', stripped):
            in_skills = True
            in_skill = None
            i += 1
            continue

        # Leave skills block if we hit a top-level key
        if in_skills and re.match(r'^[a-zA-Z]', stripped) and not stripped.startswith(' ') and not stripped.startswith('#'):
            if not re.match(r'^skills\s*:', stripped):
                in_skills = False
                in_skill = None
                i += 1
                continue

        if not in_skills:
            i += 1
            continue

        # Skip comment lines and empty lines
        if not stripped or stripped.lstrip().startswith('#'):
            i += 1
            continue

        # Match a skill entry (2-space indent)
        # Pattern: "  skill-name: { ... }" or "  skill-name:" (bare)
        m = re.match(r'^  ([a-zA-Z0-9_-]+)\s*:', stripped)
        if m:
            skill_name = m.group(1)
            in_skill = skill_name
            rest = stripped[m.end():].strip()

            # Initialize with None (will inherit upstream defaults)
            skill_data = {"enabled": None, "model": None, "var": None, "schedule": None}

            # Inline single-line dict: { enabled: true, ... }
            if rest.startswith('{') and '}' in rest:
                inline = rest
                # Multi-line inline: check following lines for continuation
                j = i + 1
                while j < len(lines) and '}' not in inline:
                    inline += " " + lines[j].strip()
                    j += 1

                inline_content = re.sub(r'^\{|\}.*$', '', inline).strip()
                skill_data = parse_inline_props(inline_content, skill_data)
                skills[skill_name] = skill_data
                i = j if '}' not in rest else i + 1
                continue
            elif rest == '' or rest.startswith('#'):
                # Bare entry — multi-line block form follows
                skills[skill_name] = skill_data
                i += 1
                # Look ahead for sub-keys
                while i < len(lines):
                    sub = lines[i].rstrip()
                    if not sub or sub.lstrip().startswith('#'):
                        i += 1
                        continue
                    # 4-space indent = sub-key of current skill
                    sm = re.match(r'^    ([a-zA-Z_]+)\s*:\s*(.*)', sub)
                    if sm:
                        k, v = sm.group(1), sm.group(2).strip()
                        v = v.split('#')[0].strip().strip('"').strip("'")
                        if k == 'enabled':
                            skill_data['enabled'] = v.lower() == 'true'
                        elif k == 'model':
                            skill_data['model'] = v if v else None
                        elif k == 'var':
                            skill_data['var'] = v
                        elif k == 'schedule':
                            skill_data['schedule'] = v if v else None
                        i += 1
                    else:
                        break
                skills[skill_name] = skill_data
                continue
            else:
                skills[skill_name] = skill_data
                i += 1
                continue
        i += 1

    return skills


def parse_inline_props(text, skill_data):
    """Parse inline YAML properties like: enabled: true, model: "x", var: "", schedule: "0 7 * * *" """
    # Remove trailing comments
    text = re.sub(r'#.*$', '', text).strip()

    # Split on commas (careful with schedule which has spaces)
    # Use a simple state machine
    props = {}
    # Match key: value pairs
    for m in re.finditer(r'([a-zA-Z_]+)\s*:\s*("(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|[^,}]+)', text):
        k = m.group(1).strip()
        v = m.group(2).strip().strip('"').strip("'").strip()
        props[k] = v

    if 'enabled' in props:
        skill_data['enabled'] = props['enabled'].lower() == 'true'
    if 'model' in props:
        skill_data['model'] = props['model'] if props['model'] else None
    if 'var' in props:
        skill_data['var'] = props['var']
    if 'schedule' in props:
        skill_data['schedule'] = props['schedule'] if props['schedule'] else None

    return skill_data


def get_upstream_defaults():
    """Parse the local aeon.yml for upstream defaults."""
    with open(UPSTREAM_YML) as f:
        text = f.read()
    return parse_skills_from_yml(text)


def get_upstream_skills():
    """Get set of skill directory names."""
    if not os.path.isdir(SKILLS_DIR):
        return set()
    return set(d for d in os.listdir(SKILLS_DIR)
               if os.path.isdir(os.path.join(SKILLS_DIR, d))
               and os.path.exists(os.path.join(SKILLS_DIR, d, "SKILL.md")))


def get_upstream_tags():
    """Parse tags from each skill's SKILL.md frontmatter."""
    tags = {}
    skills_dir = SKILLS_DIR
    for skill_name in os.listdir(skills_dir):
        skill_md = os.path.join(skills_dir, skill_name, "SKILL.md")
        if not os.path.exists(skill_md):
            continue
        try:
            with open(skill_md) as f:
                content = f.read()
            # Extract frontmatter
            fm_match = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
            if fm_match:
                fm = fm_match.group(1)
                tag_m = re.search(r'tags\s*:\s*\[([^\]]*)\]', fm)
                if tag_m:
                    raw_tags = tag_m.group(1)
                    tag_list = [t.strip().strip('"').strip("'") for t in raw_tags.split(',') if t.strip()]
                    tags[skill_name] = tag_list
                else:
                    tags[skill_name] = []
            else:
                tags[skill_name] = []
        except Exception:
            tags[skill_name] = []
    return tags


def get_fork_only_skills(fork_full, fork_text):
    """Find skills in fork tree that aren't in upstream."""
    upstream_skills = get_upstream_skills()
    fork_skills = set()
    # Find skills/<name>/SKILL.md patterns in fork aeon.yml or fetch tree
    # For efficiency, parse the fork aeon.yml for any skill keys, then check against upstream
    fork_parsed = parse_skills_from_yml(fork_text)
    # Fork-only skills would need tree enumeration; skip for now
    return []


def normalize_model(model_str):
    """Normalize model strings."""
    if not model_str:
        return None
    s = model_str.strip().strip('"').strip("'")
    return s if s else None


def main():
    print("=== Step 1: Fetching upstream defaults ===")
    upstream_defaults = get_upstream_defaults()
    upstream_skills = get_upstream_skills()
    upstream_tags = get_upstream_tags()
    print(f"Upstream skills: {len(upstream_skills)}, skills in aeon.yml: {len(upstream_defaults)}")

    print("\n=== Step 2: Fetching fork aeon.ymls ===")
    fork_results = []
    for fork in ACTIVE_FORKS:
        status, path = fetch_fork_yml(fork)
        fork_results.append({
            "fork": fork,
            "status": status,
            "path": path
        })

    n_ok = sum(1 for r in fork_results if r["status"] == "ok")
    n_no_yml = sum(1 for r in fork_results if r["status"] == "no_aeon_yml")
    n_invalid = sum(1 for r in fork_results if r["status"] in ("yml_invalid", "yml_decode_fail"))
    print(f"\nFetched: {n_ok} OK, {n_no_yml} no aeon.yml, {n_invalid} invalid")

    print("\n=== Step 3: Parsing fork aeon.ymls ===")
    # For each fork with a readable aeon.yml, parse it and compute divergence
    fork_data = []
    for r in fork_results:
        if r["status"] != "ok" or not r["path"]:
            fork_data.append({
                "fork": r["fork"]["full_name"],
                "tier": "UNREADABLE",
                "status": r["status"],
                "skills": {},
                "enabled_diff": 0, "var_overrides": 0, "model_overrides": 0,
                "schedule_overrides": 0, "fork_only_skill_count": 0
            })
            continue

        try:
            with open(r["path"]) as f:
                text = f.read()
        except Exception as e:
            fork_data.append({
                "fork": r["fork"]["full_name"],
                "tier": "UNREADABLE",
                "status": "read_error",
                "skills": {},
                "enabled_diff": 0, "var_overrides": 0, "model_overrides": 0,
                "schedule_overrides": 0, "fork_only_skill_count": 0
            })
            continue

        fork_skills = parse_skills_from_yml(text)

        # Compute divergence vs upstream_defaults
        enabled_diff = 0
        var_overrides = 0
        model_overrides = 0
        schedule_overrides = 0

        for skill_name, up in upstream_defaults.items():
            fk = fork_skills.get(skill_name, {})

            # enabled: compare only if fork explicitly sets it
            fk_enabled = fk.get("enabled") if fk else None
            up_enabled = up.get("enabled")
            if fk_enabled is not None and up_enabled is not None and fk_enabled != up_enabled:
                enabled_diff += 1

            # var: compare only if fork sets non-empty var where upstream is empty (or different)
            fk_var = fk.get("var") if fk else None
            up_var = up.get("var", "")
            if fk_var is not None and fk_var != "" and fk_var != up_var:
                var_overrides += 1

            # model: compare only if fork sets a model different from upstream
            fk_model = normalize_model(fk.get("model") if fk else None)
            up_model = normalize_model(up.get("model"))
            if fk_model is not None and fk_model != up_model:
                model_overrides += 1

            # schedule: compare only if fork sets a different schedule
            fk_schedule = fk.get("schedule") if fk else None
            up_schedule = up.get("schedule")
            if fk_schedule is not None and fk_schedule != up_schedule:
                schedule_overrides += 1

        total_diff = enabled_diff + var_overrides + model_overrides + schedule_overrides

        tier = "CONFIGURED" if total_diff >= 1 else "TEMPLATE"

        fork_data.append({
            "fork": r["fork"]["full_name"],
            "tier": tier,
            "status": "ok",
            "skills": fork_skills,
            "enabled_diff": enabled_diff,
            "var_overrides": var_overrides,
            "model_overrides": model_overrides,
            "schedule_overrides": schedule_overrides,
            "fork_only_skill_count": 0
        })

    # Print tier summary
    n_configured = sum(1 for d in fork_data if d["tier"] == "CONFIGURED")
    n_template = sum(1 for d in fork_data if d["tier"] == "TEMPLATE")
    n_unreadable = sum(1 for d in fork_data if d["tier"] == "UNREADABLE")
    print(f"Tiers: {n_configured} CONFIGURED, {n_template} TEMPLATE, {n_unreadable} UNREADABLE")

    print("\n=== Step 4: Aggregate divergence ===")
    configured_forks = [d for d in fork_data if d["tier"] == "CONFIGURED"]
    N = len(configured_forks)
    print(f"N_CONFIGURED = {N}")

    if N < 2:
        print("FORK_SKILL_DIGEST_TEMPLATE_FLEET — fewer than 2 configured forks")
        result = {
            "status": "FORK_SKILL_DIGEST_TEMPLATE_FLEET",
            "n_active": len(ACTIVE_FORKS),
            "n_configured": N,
            "n_template": n_template,
            "n_unreadable": n_unreadable,
            "fork_data": fork_data
        }
        with open(os.path.join(CACHE_DIR, "result.json"), "w") as f:
            json.dump(result, f, indent=2)
        return

    # For each upstream skill, compute divergence across configured forks
    skill_divergence = {}

    for skill_name, up in upstream_defaults.items():
        up_enabled = up.get("enabled", False)
        up_model = normalize_model(up.get("model"))
        up_var = up.get("var", "") or ""
        up_schedule = up.get("schedule")

        forks_enabled_count = 0
        forks_disabled_count = 0
        model_counts = defaultdict(int)
        var_counts = defaultdict(int)
        schedule_counts = defaultdict(int)
        var_override_count = 0
        model_override_count = 0
        schedule_override_count = 0

        for fd in configured_forks:
            fk = fd["skills"].get(skill_name, {})
            fk_enabled = fk.get("enabled") if fk else None
            fk_model = normalize_model(fk.get("model") if fk else None)
            fk_var = fk.get("var") if fk else None
            fk_schedule = fk.get("schedule") if fk else None

            if fk_enabled is True:
                forks_enabled_count += 1
            elif fk_enabled is False:
                forks_disabled_count += 1

            if fk_model is not None and fk_model != up_model:
                model_override_count += 1
                model_counts[fk_model] += 1

            if fk_var is not None and fk_var != "" and fk_var != up_var:
                var_override_count += 1
                var_counts[fk_var] += 1

            if fk_schedule is not None and fk_schedule != up_schedule:
                schedule_override_count += 1
                schedule_counts[fk_schedule] += 1

        # Compute divergence_pct
        if not up_enabled:
            divergence_pct = forks_enabled_count / N
            direction = "ENABLE_UPWARD"
        else:
            divergence_pct = forks_disabled_count / N
            direction = "DISABLE_DOWNWARD"

        top_model = None
        if model_counts:
            best_model = max(model_counts, key=model_counts.get)
            if model_counts[best_model] >= 2:
                top_model = {"value": best_model, "count": model_counts[best_model]}

        top_var = None
        if var_counts:
            best_var = max(var_counts, key=var_counts.get)
            if var_counts[best_var] >= 2:
                top_var = {"value": best_var, "count": var_counts[best_var]}

        top_schedule = None
        if schedule_counts:
            best_schedule = max(schedule_counts, key=schedule_counts.get)
            if schedule_counts[best_schedule] >= 2:
                top_schedule = {"value": best_schedule, "count": schedule_counts[best_schedule]}

        total_signal = (forks_enabled_count if direction == "ENABLE_UPWARD" else forks_disabled_count) + var_override_count + model_override_count + schedule_override_count

        if total_signal > 0:
            skill_divergence[skill_name] = {
                "up_enabled": up_enabled,
                "direction": direction,
                "forks_enabled_count": forks_enabled_count,
                "forks_disabled_count": forks_disabled_count,
                "divergence_pct": divergence_pct,
                "var_override_count": var_override_count,
                "top_var": top_var,
                "model_override_count": model_override_count,
                "top_model": top_model,
                "schedule_override_count": schedule_override_count,
                "top_schedule": top_schedule,
                "total_signal": total_signal
            }

    print(f"Skills with divergence signal: {len(skill_divergence)}")

    print("\n=== Step 5: Categorize ===")
    buckets = {
        "DEFAULT_FLIP_ENABLE": [],
        "DEFAULT_FLIP_DISABLE": [],
        "MODEL_CONSENSUS": [],
        "VAR_HOTSPOT": [],
        "EMERGING": []
    }

    # Excluded skills from flip buckets
    EXCLUDE_FROM_ENABLE_FLIP = set()  # skills tagged meta or dev
    for sname, tags_list in upstream_tags.items():
        if "meta" in tags_list or "dev" in tags_list:
            EXCLUDE_FROM_ENABLE_FLIP.add(sname)

    # Get workflow_dispatch skills
    WD_SKILLS = set(s for s, v in upstream_defaults.items() if v.get("schedule") == "workflow_dispatch")
    EXCLUDE_FROM_DISABLE = {"heartbeat"}

    for skill_name, div in skill_divergence.items():
        tags_list = upstream_tags.get(skill_name, [])
        is_meta_dev = "meta" in tags_list or "dev" in tags_list
        is_wd = upstream_defaults.get(skill_name, {}).get("schedule") == "workflow_dispatch"

        assigned = False

        # DEFAULT_FLIP_ENABLE
        if (div["direction"] == "ENABLE_UPWARD"
                and div["divergence_pct"] >= 0.50
                and not is_wd
                and skill_name not in EXCLUDE_FROM_ENABLE_FLIP):
            buckets["DEFAULT_FLIP_ENABLE"].append({
                "skill": skill_name,
                "forks": div["forks_enabled_count"],
                "pct": div["divergence_pct"]
            })
            assigned = True

        # DEFAULT_FLIP_DISABLE
        if not assigned and (div["direction"] == "DISABLE_DOWNWARD"
                and div["divergence_pct"] >= 0.50
                and skill_name not in EXCLUDE_FROM_DISABLE):
            buckets["DEFAULT_FLIP_DISABLE"].append({
                "skill": skill_name,
                "forks": div["forks_disabled_count"],
                "pct": div["divergence_pct"]
            })
            assigned = True

        # MODEL_CONSENSUS
        if not assigned and div["top_model"] is not None:
            min_count = max(2, -(-N * 40 // 100))  # ceil(N * 0.40)
            if div["top_model"]["count"] >= min_count:
                buckets["MODEL_CONSENSUS"].append({
                    "skill": skill_name,
                    "model": div["top_model"]["value"],
                    "forks": div["top_model"]["count"]
                })
                assigned = True

        # VAR_HOTSPOT
        if not assigned and div["top_var"] is not None:
            min_count = max(2, -(-N * 30 // 100))  # ceil(N * 0.30)
            if div["var_override_count"] >= min_count and div["top_var"]["count"] >= 2:
                buckets["VAR_HOTSPOT"].append({
                    "skill": skill_name,
                    "var": div["top_var"]["value"],
                    "forks": div["var_override_count"]
                })
                assigned = True

        # EMERGING
        if not assigned and (div["direction"] == "ENABLE_UPWARD"
                and 0.25 <= div["divergence_pct"] < 0.50):
            buckets["EMERGING"].append({
                "skill": skill_name,
                "pct": div["divergence_pct"],
                "forks": div["forks_enabled_count"]
            })

    # Sort buckets by pct/forks desc
    for key in ["DEFAULT_FLIP_ENABLE", "DEFAULT_FLIP_DISABLE", "EMERGING"]:
        buckets[key].sort(key=lambda x: x.get("pct", 0), reverse=True)
    buckets["MODEL_CONSENSUS"].sort(key=lambda x: x["forks"], reverse=True)
    buckets["VAR_HOTSPOT"].sort(key=lambda x: x["forks"], reverse=True)

    print("DEFAULT_FLIP_ENABLE:", len(buckets["DEFAULT_FLIP_ENABLE"]))
    print("DEFAULT_FLIP_DISABLE:", len(buckets["DEFAULT_FLIP_DISABLE"]))
    print("MODEL_CONSENSUS:", len(buckets["MODEL_CONSENSUS"]))
    print("VAR_HOTSPOT:", len(buckets["VAR_HOTSPOT"]))
    print("EMERGING:", len(buckets["EMERGING"]))

    print("\n=== Step 6: Fork fingerprints ===")
    fingerprints = []
    for fd in configured_forks:
        total_overrides = (fd["enabled_diff"] + fd["var_overrides"] +
                          fd["model_overrides"] + fd["schedule_overrides"] +
                          fd["fork_only_skill_count"])

        # Category lean: count enabled skills per tag
        tag_counts = defaultdict(int)
        for skill_name, skill_vals in fd["skills"].items():
            if skill_vals.get("enabled") is True:
                tags_list = upstream_tags.get(skill_name, [])
                if tags_list:
                    for t in tags_list:
                        tag_counts[t] += 1
                else:
                    tag_counts["untagged"] += 1

        total_enabled = sum(tag_counts.values())
        dominant = "mixed"
        if tag_counts:
            best_tag = max(tag_counts, key=tag_counts.get)
            if total_enabled > 0 and tag_counts[best_tag] / total_enabled > 0.40:
                dominant = best_tag

        fingerprints.append({
            "fork": fd["fork"],
            "total_overrides": total_overrides,
            "dominant_category": dominant,
            "tag_breakdown": dict(tag_counts),
            "enabled_diff": fd["enabled_diff"],
            "model_overrides": fd["model_overrides"],
            "var_overrides": fd["var_overrides"],
        })

    fingerprints.sort(key=lambda x: x["total_overrides"], reverse=True)
    top5 = fingerprints[:5]
    print("Top 5 heaviest customizers:")
    for fp in top5:
        print(f"  {fp['fork']}: {fp['total_overrides']} overrides, dominant={fp['dominant_category']}")

    # Fork-only skills (via tree enumeration — skipped for efficiency; use cached if available)
    fork_only_skills = []
    for r in fork_results:
        if r["status"] != "ok" or not r["path"]:
            continue
        # Check if tree has any skills/<name>/SKILL.md not in upstream
        # This would require a tree call; for now we'll check known ones
        pass

    # Check swarm-ai-research/aeon-atlas specifically (known from last run)
    # Will check their tree
    print("\n=== Step 7: Check fork-only skills for known heavy forks ===")
    for fp in top5:
        fork_full = fp["fork"]
        print(f"  Checking tree for {fork_full}...")
        rc, out, err = run_gh([
            "api",
            f"repos/{fork_full}/git/trees/HEAD?recursive=1",
            "--jq", '[.tree[] | select(.type == "blob") | .path] | map(select(startswith("skills/"))) | map(select(endswith("SKILL.md")))'
        ], timeout=30)
        if rc == 0:
            try:
                paths = json.loads(out)
                for path in paths:
                    m = re.match(r'skills/([^/]+)/SKILL\.md', path)
                    if m:
                        skill_name = m.group(1)
                        if skill_name not in upstream_skills:
                            fork_only_skills.append({"fork": fork_full, "skill": skill_name})
                            print(f"    Fork-only: {skill_name}")
            except Exception:
                pass

    result = {
        "status": "ok",
        "n_active": len(ACTIVE_FORKS),
        "n_configured": N,
        "n_template": n_template,
        "n_unreadable": n_unreadable,
        "buckets": buckets,
        "skill_divergence": skill_divergence,
        "fingerprints": top5,
        "fork_only_skills": fork_only_skills,
        "fork_data": [
            {"fork": d["fork"], "tier": d["tier"], "status": d["status"],
             "enabled_diff": d["enabled_diff"], "var_overrides": d["var_overrides"],
             "model_overrides": d["model_overrides"], "schedule_overrides": d["schedule_overrides"]}
            for d in fork_data
        ]
    }

    with open(os.path.join(CACHE_DIR, "result.json"), "w") as f:
        json.dump(result, f, indent=2)

    print("\n=== DONE ===")
    print(f"Result written to {os.path.join(CACHE_DIR, 'result.json')}")


if __name__ == "__main__":
    main()
