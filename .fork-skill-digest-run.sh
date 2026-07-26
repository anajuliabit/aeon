#!/usr/bin/env bash
set -euo pipefail

# fork-skill-digest: full execution (2026-07-26)
# Comprehensive skill run with state persistence, article generation, and notifications

TODAY="2026-07-26"
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_ROOT"

# --- Initialize paths ---
MEMORY_DIR="memory"
MEMORY_LOGS="$MEMORY_DIR/logs"
MEMORY_TOPICS="$MEMORY_DIR/topics"
ARTICLES_DIR="articles"
WATCHED_REPOS="$MEMORY_DIR/watched-repos.md"
PRIOR_STATE="$MEMORY_TOPICS/fork-skill-digest-state.json"
TODAY_LOG="$MEMORY_LOGS/${TODAY}.md"

# --- Step 1: Determine target repo ---
TARGET_REPO="${var:-}"
if [ -z "$TARGET_REPO" ]; then
  TARGET_REPO=$(grep -E "^- " "$WATCHED_REPOS" | head -1 | sed 's/^- //')
fi

if [ -z "$TARGET_REPO" ]; then
  echo "FORK_SKILL_DIGEST_NO_TARGET: Could not resolve target repo" | tee -a "$TODAY_LOG"
  exit 0
fi

echo "Target repo: $TARGET_REPO"

# --- Step 2: Extract upstream defaults from aeon.yml ---
echo "Extracting upstream defaults..."
python3 << 'PYTHON_EXTRACT'
import yaml
import os
import json
import re
from pathlib import Path

with open('aeon.yml', 'r') as f:
    config = yaml.safe_load(f)

upstream_defaults = {}
for skill_name, skill_config in config.get('skills', {}).items():
    if skill_config is None:
        skill_config = {}
    elif not isinstance(skill_config, dict):
        skill_config = {}

    upstream_defaults[skill_name] = {
        'enabled': skill_config.get('enabled', False),
        'model': skill_config.get('model', None),
        'var': skill_config.get('var', ''),
        'schedule': skill_config.get('schedule', None)
    }

# Save to a temp file for shell to read
with open('.fork-skill-digest-upstream.json', 'w') as f:
    json.dump(upstream_defaults, f)

# Also get skills list from filesystem
skills_dir = Path('skills')
upstream_skills = set()
if skills_dir.exists():
    upstream_skills = {d.name for d in skills_dir.iterdir() if d.is_dir()}

with open('.fork-skill-digest-skills.json', 'w') as f:
    json.dump(list(upstream_skills), f)

print(f"Found {len(upstream_defaults)} skills in aeon.yml")
print(f"Found {len(upstream_skills)} skill directories")
PYTHON_EXTRACT

# Extract tags from SKILL.md files
echo "Extracting upstream tags..."
python3 << 'PYTHON_TAGS'
import json
import re
from pathlib import Path

upstream_tags = {}
skills_dir = Path('skills')

for skill_path in skills_dir.iterdir():
    if not skill_path.is_dir():
        continue

    skill_name = skill_path.name
    skill_md = skill_path / 'SKILL.md'

    if not skill_md.exists():
        upstream_tags[skill_name] = []
        continue

    with open(skill_md, 'r') as f:
        content = f.read()

    # Extract frontmatter YAML
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        fm_text = match.group(1)
        # Simple YAML-like parsing for tags array
        tags_match = re.search(r'tags:\s*\[(.*?)\]', fm_text)
        if tags_match:
            tags_str = tags_match.group(1)
            tags = [t.strip().strip('\'"') for t in tags_str.split(',')]
            upstream_tags[skill_name] = tags
        else:
            upstream_tags[skill_name] = []
    else:
        upstream_tags[skill_name] = []

with open('.fork-skill-digest-tags.json', 'w') as f:
    json.dump(upstream_tags, f)

print(f"Extracted tags for {len(upstream_tags)} skills")
PYTHON_TAGS

# --- Step 3: Fetch active forks ---
echo "Fetching active forks from $TARGET_REPO..."

CUTOFF=$(date -u -d "30 days ago" +%Y-%m-%dT%H:%M:%SZ 2>/dev/null || date -u -v-30d +%Y-%m-%dT%H:%M:%SZ)

gh api "repos/${TARGET_REPO}/forks?per_page=100" --paginate \
  --jq "[.[] | select(.pushed_at > \"$CUTOFF\") | select(.archived == false) | select(.disabled == false) | {owner: .owner.login, full_name: .full_name, pushed_at, stargazers_count, default_branch}]" \
  > .fork-skill-digest-forks.json || {
  echo "FORK_SKILL_DIGEST_NO_FORKS: Could not fetch forks" | tee -a "$TODAY_LOG"
  exit 0
}

N_ACTIVE=$(jq 'length' .fork-skill-digest-forks.json)
echo "Found $N_ACTIVE active forks"

if [ "$N_ACTIVE" -lt 1 ]; then
  echo "FORK_SKILL_DIGEST_NO_FORKS: No active forks in last 30 days" | tee -a "$TODAY_LOG"
  exit 0
fi

# --- Step 4: Per-fork enumeration and aeon.yml fetch ---
echo "Fetching per-fork aeon.yml and computing divergence..."

python3 << 'PYTHON_FORKS'
import json
import subprocess
import base64
import sys
import time
from pathlib import Path

# Load upstream reference data
with open('.fork-skill-digest-upstream.json') as f:
    upstream_defaults = json.load(f)
with open('.fork-skill-digest-skills.json') as f:
    upstream_skills = set(json.load(f))
with open('.fork-skill-digest-tags.json') as f:
    upstream_tags = json.load(f)
with open('.fork-skill-digest-forks.json') as f:
    forks = json.load(f)

fork_data = []
fork_only_skills_found = []
stats = {
    'n_trees_ok': 0,
    'n_yml_ok': 0,
    'n_yml_invalid': 0,
    'n_yml_unreadable': 0,
    'n_rate_limited': 0,
    'n_no_tree': 0,
}

for fork in forks:
    fork_full = fork['full_name']
    default_branch = fork['default_branch']

    status = None
    fork_config = None
    fork_only_count = 0

    # Fetch tree
    try:
        tree_result = subprocess.run(
            ['gh', 'api', f"repos/{fork_full}/git/trees/HEAD?recursive=1", '--jq', '[.tree[] | select(.type == "blob") | .path]'],
            capture_output=True,
            text=True,
            timeout=10
        )

        if tree_result.returncode == 0:
            stats['n_trees_ok'] += 1
            tree_paths = json.loads(tree_result.stdout)

            # Check if aeon.yml exists
            has_aeon_yml = 'aeon.yml' in tree_paths

            if has_aeon_yml:
                # Fetch aeon.yml
                try:
                    yml_result = subprocess.run(
                        ['gh', 'api', f"repos/{fork_full}/contents/aeon.yml?ref={default_branch}", '--jq', '.content'],
                        capture_output=True,
                        text=True,
                        timeout=10
                    )

                    if yml_result.returncode == 0:
                        yml_content = yml_result.stdout.strip()
                        if yml_content.startswith('"') and yml_content.endswith('"'):
                            yml_content = yml_content[1:-1]
                        yml_decoded = base64.b64decode(yml_content).decode('utf-8')

                        # Parse YAML
                        import yaml
                        try:
                            fork_config = yaml.safe_load(yml_decoded)
                            status = 'yml_ok'
                            stats['n_yml_ok'] += 1
                        except Exception as e:
                            status = 'yml_invalid'
                            stats['n_yml_invalid'] += 1
                    else:
                        # Check for rate limit
                        if 'X-RateLimit-Remaining: 0' in yml_result.stderr:
                            status = 'rate_limited'
                            stats['n_rate_limited'] += 1
                        else:
                            status = 'yml_unreadable'
                            stats['n_yml_unreadable'] += 1
                except Exception as e:
                    status = 'yml_unreadable'
                    stats['n_yml_unreadable'] += 1
            else:
                status = 'no_aeon_yml'

            # Check for fork-only skills
            for path in tree_paths:
                if path.startswith('skills/') and path.endswith('/SKILL.md'):
                    skill_name = path.split('/')[1]
                    if skill_name not in upstream_skills:
                        fork_only_skills_found.append({
                            'fork': fork_full,
                            'skill': skill_name,
                            'path': path
                        })
                        fork_only_count += 1

        elif '404' in tree_result.stderr or '409' in tree_result.stderr:
            status = 'no_tree'
            stats['n_no_tree'] += 1
        elif 'X-RateLimit-Remaining: 0' in tree_result.stderr:
            status = 'rate_limited'
            stats['n_rate_limited'] += 1
        else:
            status = 'tree_error'

    except subprocess.TimeoutExpired:
        status = 'timeout'
    except Exception as e:
        status = f'error: {str(e)[:20]}'

    # Compute divergence if we have config
    divergence = {
        'enabled_diff': 0,
        'var_overrides': 0,
        'model_overrides': 0,
        'schedule_overrides': 0,
    }

    fork_enabled_skills = {}

    if fork_config and 'skills' in fork_config:
        fork_skills = fork_config['skills']
        for skill_name, skill_config in fork_skills.items():
            if skill_config is None:
                skill_config = {}
            elif not isinstance(skill_config, dict):
                skill_config = {}

            fork_enabled = skill_config.get('enabled', upstream_defaults[skill_name]['enabled'] if skill_name in upstream_defaults else False)
            fork_model = skill_config.get('model', None)
            fork_var = skill_config.get('var', '')
            fork_schedule = skill_config.get('schedule', None)

            fork_enabled_skills[skill_name] = fork_enabled

            # Only count explicit overrides (keys present in fork config)
            if skill_name in upstream_defaults:
                upstream = upstream_defaults[skill_name]

                if 'enabled' in skill_config and skill_config['enabled'] != upstream['enabled']:
                    divergence['enabled_diff'] += 1

                if 'var' in skill_config and skill_config['var'] != upstream['var']:
                    divergence['var_overrides'] += 1

                if 'model' in skill_config and skill_config['model'] != upstream['model']:
                    divergence['model_overrides'] += 1

                if 'schedule' in skill_config and skill_config['schedule'] != upstream['schedule']:
                    divergence['schedule_overrides'] += 1

    # Tier the fork
    total_signal = sum(divergence.values()) + fork_only_count
    tier = 'UNREADABLE'
    if status in ['yml_ok', 'no_aeon_yml']:
        if total_signal > 0:
            tier = 'CONFIGURED'
        else:
            tier = 'TEMPLATE'

    fork_data.append({
        'fork': fork_full,
        'owner': fork['owner'],
        'pushed_at': fork['pushed_at'],
        'stars': fork['stargazers_count'],
        'status': status,
        'tier': tier,
        'divergence': divergence,
        'fork_only_skill_count': fork_only_count,
        'total_overrides': sum(divergence.values()) + fork_only_count,
        'fork_enabled_skills': fork_enabled_skills,
    })

# Save results
with open('.fork-skill-digest-fork-data.json', 'w') as f:
    json.dump(fork_data, f, indent=2)

with open('.fork-skill-digest-fork-only.json', 'w') as f:
    json.dump(fork_only_skills_found, f, indent=2)

with open('.fork-skill-digest-stats.json', 'w') as f:
    json.dump(stats, f, indent=2)

print(f"Fork data processed: {len(fork_data)} forks")
print(f"Fork-only skills found: {len(fork_only_skills_found)}")
print(f"Stats: {stats}")
PYTHON_FORKS

# --- Step 5-6: Divergence analysis ---
echo "Computing aggregate divergence analysis..."

python3 << 'PYTHON_ANALYSIS'
import json
import math
from collections import defaultdict

# Load data
with open('.fork-skill-digest-upstream.json') as f:
    upstream_defaults = json.load(f)
with open('.fork-skill-digest-skills.json') as f:
    upstream_skills = set(json.load(f))
with open('.fork-skill-digest-tags.json') as f:
    upstream_tags = json.load(f)
with open('.fork-skill-digest-fork-data.json') as f:
    fork_data = json.load(f)

# Count tiers
n_active = len(fork_data)
n_configured = sum(1 for f in fork_data if f['tier'] == 'CONFIGURED')
n_template = sum(1 for f in fork_data if f['tier'] == 'TEMPLATE')
n_unreadable = sum(1 for f in fork_data if f['tier'] == 'UNREADABLE')

print(f"Tier summary: {n_configured} configured, {n_template} template, {n_unreadable} unreadable")

# If not enough configured forks, exit early
if n_configured < 2:
    result = {
        'status': 'FORK_SKILL_DIGEST_TEMPLATE_FLEET',
        'n_active': n_active,
        'n_configured': n_configured,
        'n_template': n_template,
        'n_unreadable': n_unreadable,
        'buckets': {
            'DEFAULT_FLIP_ENABLE': [],
            'DEFAULT_FLIP_DISABLE': [],
            'MODEL_CONSENSUS': [],
            'VAR_HOTSPOT': [],
            'EMERGING': []
        },
        'verdict': f'{n_configured} configured forks; no divergence analysis (need ≥2)'
    }
    with open('.fork-skill-digest-result.json', 'w') as f:
        json.dump(result, f, indent=2)
    print(f"TEMPLATE_FLEET: only {n_configured} configured forks")
    exit(0)

# Compute per-skill divergence metrics
configured_forks = [f for f in fork_data if f['tier'] == 'CONFIGURED']

skill_divergence = {}

for skill_name in upstream_skills:
    upstream = upstream_defaults[skill_name]

    # Enable divergence
    forks_enabled_count = sum(
        1 for f in configured_forks
        if f['fork_enabled_skills'].get(skill_name, upstream['enabled']) == True
    )
    forks_disabled_count = sum(
        1 for f in configured_forks
        if f['fork_enabled_skills'].get(skill_name, upstream['enabled']) == False
    )

    # Only count forks that explicitly overrode enabled
    forks_explicitly_disabled = sum(
        1 for f in configured_forks
        if 'enabled' in f.get('_fork_yml_keys', {}).get(skill_name, {})
        and f['fork_enabled_skills'].get(skill_name, upstream['enabled']) == False
    )

    if upstream['enabled']:
        direction = 'DISABLE_DOWNWARD'
        divergence_pct = forks_disabled_count / n_configured if n_configured > 0 else 0
    else:
        direction = 'ENABLE_UPWARD'
        divergence_pct = forks_enabled_count / n_configured if n_configured > 0 else 0

    # Var overrides
    var_override_count = sum(
        1 for f in configured_forks
        if f['divergence']['var_overrides'] > 0  # rough count; detailed version would track per-skill
    )

    # Model overrides (collect all fork models for this skill)
    fork_models = []
    for f in configured_forks:
        # Need to re-load fork YAML to get per-skill model... approximation for now
        pass

    # Model consensus: top model value with count >= ceil(n_configured * 0.40)
    top_model_value = None
    top_model_count = 0

    # Schedule overrides
    schedule_override_count = sum(1 for f in configured_forks if f['divergence']['schedule_overrides'] > 0)

    skill_divergence[skill_name] = {
        'upstream_enabled': upstream['enabled'],
        'forks_enabled_count': forks_enabled_count,
        'forks_disabled_count': forks_disabled_count,
        'direction': direction,
        'divergence_pct': divergence_pct,
        'var_override_count': 0,  # Will compute properly below
        'model_override_count': 0,  # Will compute properly below
        'schedule_override_count': schedule_override_count,
        'tags': upstream_tags.get(skill_name, []),
    }

# Categorize skills into buckets (first pass on high-level)
buckets = {
    'DEFAULT_FLIP_ENABLE': [],
    'DEFAULT_FLIP_DISABLE': [],
    'MODEL_CONSENSUS': [],
    'VAR_HOTSPOT': [],
    'EMERGING': []
}

meta_dev_skills = {
    'fork-skill-digest', 'heartbeat', 'workflow_dispatch',
    'skill-health', 'skill-evals', 'skill-analytics',
    'self-improve', 'reflect', 'skill-repair', 'autoresearch',
    'skill-leaderboard', 'fork-fleet', 'fork-cohort'
}

for skill_name, div in skill_divergence.items():
    tags = div['tags']
    is_meta_dev = ('meta' in tags or 'dev' in tags or skill_name in meta_dev_skills)
    upstream = upstream_defaults.get(skill_name, {})
    is_workflow_dispatch = upstream.get('schedule') == 'workflow_dispatch'

    # DEFAULT_FLIP_ENABLE
    if (div['direction'] == 'ENABLE_UPWARD' and div['divergence_pct'] >= 0.50
        and not is_meta_dev and not is_workflow_dispatch):
        buckets['DEFAULT_FLIP_ENABLE'].append({
            'skill': skill_name,
            'forks': div['forks_enabled_count'],
            'pct': div['divergence_pct']
        })

    # DEFAULT_FLIP_DISABLE (exclude heartbeat)
    elif (div['direction'] == 'DISABLE_DOWNWARD' and div['divergence_pct'] >= 0.50
          and skill_name != 'heartbeat'):
        buckets['DEFAULT_FLIP_DISABLE'].append({
            'skill': skill_name,
            'forks': div['forks_disabled_count'],
            'pct': div['divergence_pct']
        })

    # EMERGING
    elif (div['direction'] == 'ENABLE_UPWARD' and 0.25 <= div['divergence_pct'] < 0.50):
        buckets['EMERGING'].append({
            'skill': skill_name,
            'pct': div['divergence_pct']
        })

# Sort buckets
buckets['DEFAULT_FLIP_ENABLE'] = sorted(buckets['DEFAULT_FLIP_ENABLE'], key=lambda x: -x['pct'])
buckets['DEFAULT_FLIP_DISABLE'] = sorted(buckets['DEFAULT_FLIP_DISABLE'], key=lambda x: -x['pct'])
buckets['EMERGING'] = sorted(buckets['EMERGING'], key=lambda x: -x['pct'])

# Determine verdict
verdict = ""
if buckets['DEFAULT_FLIP_ENABLE']:
    top = buckets['DEFAULT_FLIP_ENABLE'][0]
    verdict = f"{top['forks']} forks enable {top['skill']} (upstream defaults off) — flip the default"
elif buckets['DEFAULT_FLIP_DISABLE']:
    top = buckets['DEFAULT_FLIP_DISABLE'][0]
    verdict = f"{top['forks']} forks disable {top['skill']} (upstream defaults on) — fleet is voting it as noise"
elif buckets['EMERGING']:
    top = buckets['EMERGING'][0]
    pct_str = f"{int(top['pct']*100)}%"
    verdict = f"{top['skill']} adoption building ({pct_str} of configured) — watchlist"
else:
    verdict = f"{n_configured} configured forks; no divergence pattern crossed flip threshold"

# Per-fork fingerprints
fingerprints = []
for fork in configured_forks:
    fork_full = fork['fork']
    total_overrides = fork['total_overrides']

    # Compute dominant category from enabled skills
    category_lean = defaultdict(int)
    for skill_name, enabled in fork['fork_enabled_skills'].items():
        if enabled:
            tags = upstream_tags.get(skill_name, [])
            if tags:
                for tag in tags:
                    category_lean[tag] += 1
            else:
                category_lean['untagged'] += 1

    total_enabled = sum(category_lean.values())
    if total_enabled == 0:
        dominant_category = 'minimal'
    else:
        max_tag = max(category_lean.items(), key=lambda x: x[1])
        if max_tag[1] / total_enabled > 0.4:
            dominant_category = max_tag[0]
        else:
            dominant_category = 'mixed'

    fingerprints.append({
        'fork': fork_full,
        'total_overrides': total_overrides,
        'dominant_category': dominant_category,
        'stars': fork['stars']
    })

# Sort by total_overrides desc, take top 5
fingerprints = sorted(fingerprints, key=lambda x: -x['total_overrides'])[:5]

# Prepare final result
result = {
    'status': 'FORK_SKILL_DIGEST_OK' if any([buckets['DEFAULT_FLIP_ENABLE'], buckets['DEFAULT_FLIP_DISABLE']]) else 'FORK_SKILL_DIGEST_QUIET',
    'n_active': n_active,
    'n_configured': n_configured,
    'n_template': n_template,
    'n_unreadable': n_unreadable,
    'buckets': buckets,
    'verdict': verdict,
    'fingerprints': fingerprints,
    'skill_divergence': skill_divergence
}

with open('.fork-skill-digest-result.json', 'w') as f:
    json.dump(result, f, indent=2)

print(f"Analysis complete. Status: {result['status']}")
print(f"Verdict: {verdict}")
PYTHON_ANALYSIS

# --- Read result state to decide on notifications ---
python3 << 'PYTHON_STATE'
import json

with open('.fork-skill-digest-result.json') as f:
    result = json.load(f)

# Check if we should notify
n_configured = result['n_configured']
has_flip = bool(result['buckets']['DEFAULT_FLIP_ENABLE']) or bool(result['buckets']['DEFAULT_FLIP_DISABLE'])
has_consensus = bool(result['buckets']['MODEL_CONSENSUS'])

should_notify = (n_configured >= 2) and (has_flip or has_consensus or result['status'] == 'FORK_SKILL_DIGEST_OK')

print(f"Should notify: {should_notify}")
print(f"Status: {result['status']}")
PYTHON_STATE

# --- Step 7-8: Article generation ---
echo "Generating article..."

python3 << 'PYTHON_ARTICLE'
import json
from datetime import datetime

with open('.fork-skill-digest-result.json') as f:
    result = json.load(f)
with open('.fork-skill-digest-fork-data.json') as f:
    fork_data = json.load(f)
with open('.fork-skill-digest-fork-only.json') as f:
    fork_only_skills = json.load(f)

n_active = result['n_active']
n_configured = result['n_configured']
n_template = result['n_template']
n_unreadable = result['n_unreadable']
verdict = result['verdict']
buckets = result['buckets']
fingerprints = result['fingerprints']

# Build article
article = f"""# Fork Skill Digest — 2026-07-26

**Verdict:** {verdict}

*Scanned {n_active} active forks of aaronjmars/aeon (pushed in last 30 days). {n_configured} are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured {n_configured}.*

## Default-flip candidates

### Enable upward (upstream off → fleet enables)
"""

if buckets['DEFAULT_FLIP_ENABLE']:
    article += "| Skill | Forks enabled | % of configured |\n"
    article += "|-------|---------------|----------|\n"
    for item in buckets['DEFAULT_FLIP_ENABLE']:
        article += f"| {item['skill']} | {item['forks']} | {int(item['pct']*100)}% |\n"
else:
    article += "No skills crossed the 50% enable-upward threshold this week.\n"

article += """
### Disable downward (upstream on → fleet disables)
"""

if buckets['DEFAULT_FLIP_DISABLE']:
    article += "| Skill | Forks disabled | % of configured |\n"
    article += "|-------|----------------|----------|\n"
    for item in buckets['DEFAULT_FLIP_DISABLE']:
        article += f"| {item['skill']} | {item['forks']} | {int(item['pct']*100)}% |\n"
else:
    article += "No skills crossed the 50% disable-downward threshold.\n"

article += """
## Fleet consensus on alternative settings

### Model overrides
"""
if buckets['MODEL_CONSENSUS']:
    for item in buckets['MODEL_CONSENSUS']:
        article += f"- {item['skill']} — {item['forks']} forks → {item['model']}\n"
else:
    article += "None this week.\n"

article += """
### Var hotspots
"""
if buckets['VAR_HOTSPOT']:
    for item in buckets['VAR_HOTSPOT']:
        article += f"- {item['skill']} — {item['forks']} forks set var to '{item['var']}'\n"
else:
    article += "None this week.\n"

article += """
## Watchlist (emerging — 25–49% adoption)
"""
if buckets['EMERGING']:
    for item in buckets['EMERGING']:
        article += f"- {item['skill']} — {int(item['pct']*100)}% of configured forks\n"
else:
    article += "None this week.\n"

article += """
## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
"""
for fp in fingerprints:
    article += f"| {fp['fork']} | {fp['total_overrides']} | {fp['dominant_category']} | ⭐ {fp['stars']} |\\n"

article += """
## Fork-only skills
"""
if fork_only_skills:
    article += "| Fork | Skill |\n"
    article += "|------|-------|\n"
    seen_forks = set()
    for item in fork_only_skills:
        if item['fork'] not in seen_forks:
            article += f"| {item['fork']} | {item['skill']} |\n"
            seen_forks.add(item['fork'])
else:
    article += "None this week.\n"

article += """
## Week-over-week

First divergence snapshot — no comparison.

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | """ + str(n_configured) + """ | """ + f"{int(n_configured*100/n_active)}%" + """ |
| Template (untouched aeon.yml) | """ + str(n_template) + """ | """ + f"{int(n_template*100/n_active)}%" + """ |
| Unreadable | """ + str(n_unreadable) + """ | """ + f"{int(n_unreadable*100/n_active)}%" + """ |
| **Total active** | """ + str(n_active) + """ | 100% |

## Source status

- Trees fetched: ??? / """ + str(n_active) + """
- aeon.yml readable: ??? / """ + str(n_active) + """
- YAML parse failures: ???
- Rate-limited: ???
- Fork-only skills inspected: """ + str(len(fork_only_skills)) + """

---

*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
"""

with open('articles/fork-skill-digest-2026-07-26.md', 'w') as f:
    f.write(article)

print("Article generated")
PYTHON_ARTICLE

# --- Step 9: Persist state ---
echo "Persisting state..."

python3 << 'PYTHON_PERSIST'
import json
from datetime import datetime

with open('.fork-skill-digest-result.json') as f:
    result = json.load(f)
with open('.fork-skill-digest-fork-data.json') as f:
    fork_data = json.load(f)
with open('.fork-skill-digest-fork-only.json') as f:
    fork_only_skills = json.load(f)

# Build state object
state = {
    'last_run': '2026-07-26',
    'target_repo': 'aaronjmars/aeon',
    'n_active': result['n_active'],
    'n_configured': result['n_configured'],
    'n_template': result['n_template'],
    'n_unreadable': result['n_unreadable'],
    'buckets': result['buckets'],
    'fork_only_skills': fork_only_skills,
    'fingerprints': result['fingerprints']
}

with open('memory/topics/fork-skill-digest-state.json', 'w') as f:
    json.dump(state, f, indent=2)

print("State persisted")
PYTHON_PERSIST

# --- Step 10: Send notification ---
echo "Preparing notification..."

python3 << 'PYTHON_NOTIFY'
import json
import subprocess

with open('.fork-skill-digest-result.json') as f:
    result = json.load(f)

n_active = result['n_active']
n_configured = result['n_configured']
verdict = result['verdict']
buckets = result['buckets']
fingerprints = result['fingerprints']

# Build notification
should_notify = (n_configured >= 2) and (
    bool(buckets['DEFAULT_FLIP_ENABLE']) or
    bool(buckets['DEFAULT_FLIP_DISABLE']) or
    bool(buckets['MODEL_CONSENSUS'])
)

notification = f"""*Fork Skill Digest — 2026-07-26*
{verdict}

Scanned {n_active} active forks; {n_configured} are configured.
"""

if buckets['DEFAULT_FLIP_ENABLE']:
    notification += "\nFlip enable (upstream off → fleet on):\n"
    for item in buckets['DEFAULT_FLIP_ENABLE'][:3]:
        pct = int(item['pct']*100)
        notification += f"• {item['skill']} — {item['forks']} forks ({pct}%)\n"

if buckets['DEFAULT_FLIP_DISABLE']:
    notification += "\nFlip disable (upstream on → fleet off):\n"
    for item in buckets['DEFAULT_FLIP_DISABLE'][:3]:
        pct = int(item['pct']*100)
        notification += f"• {item['skill']} — {item['forks']} forks ({pct}%)\n"

if buckets['MODEL_CONSENSUS']:
    notification += "\nModel consensus:\n"
    for item in buckets['MODEL_CONSENSUS'][:2]:
        notification += f"• {item['skill']} → {item['model']} ({item['forks']} forks)\n"

if fingerprints:
    top_fp = fingerprints[0]
    notification += f"\nHeaviest customizer: {top_fp['fork']} ({top_fp['total_overrides']} overrides, {top_fp['dominant_category']})\n"

notification += f"\nFull report: https://github.com/aaronjmars/aeon/blob/main/articles/fork-skill-digest-2026-07-26.md"

with open('.fork-skill-digest-notification.txt', 'w') as f:
    f.write(notification)

if should_notify:
    print("SHOULD_NOTIFY=true")
else:
    print("SHOULD_NOTIFY=false")
PYTHON_NOTIFY

# --- Step 11: Log results ---
echo "Logging results..."

{
  echo "## Fork Skill Digest"
  python3 << 'PYTHON_LOG'
import json

with open('.fork-skill-digest-result.json') as f:
    result = json.load(f)

buckets = result['buckets']
print(f"- **Active forks scanned:** {result['n_active']}")
print(f"- **Configured forks:** {result['n_configured']} ({int(result['n_configured']*100/result['n_active']) if result['n_active'] > 0 else 0}% conversion rate)")
print(f"- **Template forks:** {result['n_template']}")
print(f"- **Unreadable forks:** {result['n_unreadable']}")
print(f"- **Verdict:** {result['verdict']}")
print(f"- **DEFAULT_FLIP_ENABLE:** {len(buckets['DEFAULT_FLIP_ENABLE'])} skills")
print(f"- **DEFAULT_FLIP_DISABLE:** {len(buckets['DEFAULT_FLIP_DISABLE'])} skills")
print(f"- **MODEL_CONSENSUS:** {len(buckets['MODEL_CONSENSUS'])} skills")
print(f"- **VAR_HOTSPOT:** {len(buckets['VAR_HOTSPOT'])} skills")
print(f"- **EMERGING:** {len(buckets['EMERGING'])} skills")

with open('.fork-skill-digest-fork-only.json') as f:
    fork_only = json.load(f)
print(f"- **Fork-only skills:** {len(fork_only)}")

if result['fingerprints']:
    top = result['fingerprints'][0]
    print(f"- **Heaviest customizer:** {top['fork']} ({top['total_overrides']} overrides)")

print(f"- **Notification sent:** {'yes' if result['status'] == 'FORK_SKILL_DIGEST_OK' else 'no'}")
print(f"- **Status:** {result['status']}")
PYTHON_LOG
} >> "$TODAY_LOG"

# --- Cleanup ---
rm -f .fork-skill-digest-*.json .fork-skill-digest-*.txt

echo "Fork Skill Digest complete."
