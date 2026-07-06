#!/usr/bin/env python3
"""
Fork Skill Digest analysis script.
Reads .fork_results_tmp.json and produces fork_analysis_output.json
"""

import json
import math
import os
import sys
from collections import defaultdict, Counter

# ========== UPSTREAM DEFAULTS (from local aeon.yml) ==========
# enabled: true skills from upstream
UPSTREAM_ENABLED = {
    "morning-brief", "daily-routine", "github-trending", "token-alert",
    "token-movers", "on-chain-monitor", "defi-monitor", "defi-overview",
    "market-context-refresh", "btc-levels", "narrative-tracker", "unlock-monitor",
    "aixbt-pulse", "search-skill", "security-digest", "deal-flow", "reg-monitor",
    "list-digest", "agent-buzz", "goal-tracker", "skill-health", "skill-analytics",
    "self-improve", "reflect", "action-converter", "evening-recap", "thought-review",
    "fork-cohort", "skill-evals", "skill-update-check", "weekly-review",
    "weekly-shiplog", "operator-scorecard", "fork-skill-digest", "fork-skill-gap",
    "skill-graph", "skill-freshness", "skill-security-scan", "vuln-scanner",
    "autoresearch", "cost-report", "heartbeat", "token-pick"
}

# model overrides from upstream
UPSTREAM_MODELS = {
    "token-movers": "claude-haiku-4-5-20251001",
    "on-chain-monitor": "claude-haiku-4-5-20251001",
    "defi-monitor": "claude-haiku-4-5-20251001",
    "defi-overview": "claude-haiku-4-5-20251001",
    "token-pick": "claude-haiku-4-5-20251001",
    "market-context-refresh": "claude-sonnet-4-6",
    "btc-levels": "claude-sonnet-4-6",
    "aixbt-pulse": "claude-sonnet-4-6",
    "skill-analytics": "claude-sonnet-4-6",
    "evening-recap": "claude-sonnet-4-6",
    "cost-report": "claude-sonnet-4-6",
    "fork-cohort": "claude-sonnet-4-6",
    "skill-evals": "claude-sonnet-4-6",
    "skill-update-check": "claude-sonnet-4-6",
    "operator-scorecard": "claude-sonnet-4-6",
    "fork-skill-digest": "claude-sonnet-4-6",
    "fork-skill-gap": "claude-sonnet-4-6",
    "skill-freshness": "claude-sonnet-4-6",
    "monitor-polymarket": "claude-sonnet-4-6",
    "monitor-kalshi": "claude-sonnet-4-6",
    "price-threshold-alert": "claude-sonnet-4-6",
    "token-report": "claude-sonnet-4-6",
    "star-momentum-alert": "claude-sonnet-4-6",
    "syndicate-article": "claude-sonnet-4-6",
    "vercel-projects": "claude-sonnet-4-6",
    "ai-framework-watch": "claude-sonnet-4-6",
    "competitor-launch-radar": "claude-sonnet-4-6",  # MODEL_CONSENSUS from prior run
    "fleet-state": "claude-sonnet-4-6",
    "fork-release-tracker": "claude-sonnet-4-6",
    "contributor-spotlight": "claude-sonnet-4-6",
    "fork-first-run-alert": "claude-sonnet-4-6",
    "repo-scanner": "claude-sonnet-4-6",
    "skill-leaderboard": "claude-sonnet-4-6",
    "fork-contributor-leaderboard": "claude-sonnet-4-6",
    "contributor-reward": "claude-sonnet-4-6",
    "v4-readiness": "claude-sonnet-4-6",
    "schedule-ads": "claude-sonnet-4-6",
    "telegram-digest": "claude-sonnet-4-6",
    "huggingface-trending": "claude-sonnet-4-6",
}

# var overrides from upstream
UPSTREAM_VARS = {
    "list-digest": "1642770456720683008",
    "thought-review": "24",
}

# schedule from upstream (only list skills that have non-default schedules; for divergence checking)
UPSTREAM_SCHEDULES = {
    "morning-brief": "0 7 * * *",
    "daily-routine": "0 7 * * *",
    "rss-digest": "0 7 * * *",
    "hacker-news-digest": "0 7 * * *",
    "paper-digest": "0 7 * * *",
    "reddit-digest": "0 7 * * *",
    "telegram-digest": "30 7 * * *",
    "issue-triage": "0 9 * * *",
    "pr-triage": "30 9 * * *",
    "pr-review": "0 9 * * *",
    "auto-merge": "0 14 * * *",
    "github-monitor": "0 9 * * *",
    "github-issues": "0 9 * * *",
    "github-trending": "0 9 * * *",
    "github-releases": "30 9 * * *",
    "huggingface-trending": "30 9 * * *",
    "token-alert": "0 12 * * *",
    "token-movers": "10 12 * * *",
    "on-chain-monitor": "20 12 * * *",
    "defi-monitor": "40 12 * * *",
    "defi-overview": "0 12 * * *",
    "monitor-polymarket": "30 12 * * *",
    "monitor-kalshi": "0 13 * * *",
    "token-pick": "0 12 * * *",
    "price-threshold-alert": "*/30 * * * *",
    "market-context-refresh": "0 13 * * *",
    "btc-levels": "15 */4 * * *",
    "narrative-tracker": "30 13 * * *",
    "unlock-monitor": "0 10 * * 1",
    "aixbt-pulse": "0 9,21 * * *",
    "article": "0 14 * * *",
    "search-skill": "0 14 * * *",
    "security-digest": "0 14 * * *",
    "deal-flow": "0 14 * * 1",
    "reg-monitor": "0 14 * * 3",
    "list-digest": "0 17 * * *",
    "agent-buzz": "30 17 * * *",
    "skill-security-scan": "0 16 * * 1",
    "vuln-scanner": "0 16 * * 6",
    "autoresearch": "workflow_dispatch",
    "goal-tracker": "0 18 * * *",
    "skill-health": "0 18 * * *",
    "skill-analytics": "30 18 * * 3",
    "self-improve": "0 18 1/2 * *",
    "reflect": "0 18 * * *",
    "action-converter": "0 18 * * *",
    "evening-recap": "0 21 * * *",
    "thought-review": "0 7,21 * * *",
    "cost-report": "0 7 * * 1",
    "fork-cohort": "0 19 * * 0",
    "skill-evals": "0 22 * * 0",
    "skill-update-check": "0 19 * * 0",
    "weekly-review": "0 19 * * 1",
    "weekly-shiplog": "0 9 * * 1",
    "operator-scorecard": "30 10 * * 1",
    "fork-skill-digest": "30 18 * * 0",
    "fork-skill-gap": "0 21 * * 0",
    "skill-graph": "0 17 * * 0",
    "skill-freshness": "0 8 * * *",
    "heartbeat": "0 8,14,20 * * *",
}

# All skills in upstream (from ls skills/)
UPSTREAM_SKILLS = {
    "action-converter", "agent-buzz", "agent-displacement", "ai-framework-watch",
    "aixbt-pulse", "api-health", "approval-audit", "article", "article-queue",
    "atrium-watch", "auto-merge", "auto-workflow", "autoresearch", "base-mcp",
    "batch-health", "beamr-route", "beat-tracker", "btc-levels", "builder-map",
    "capabilities-map", "changelog", "channel-recap", "code-health",
    "competitor-launch-radar", "compute-pulse", "config-validator",
    "content-performance", "contract-audit", "contributor-reward",
    "contributor-spotlight", "cost-report", "create-campaign", "create-skill",
    "ctrl", "daily-routine", "deal-flow", "deep-research", "defi-monitor",
    "defi-overview", "deploy-prototype", "deployer-trace", "digest",
    "disclosure-tracker", "distribute-tokens", "ecosystem-links", "ecosystem-pulse",
    "engagement-act", "evening-recap", "external-feature", "farcaster-digest",
    "fear-divergence", "fetch-tweets", "fleet-control", "fleet-scorecard",
    "fleet-state", "followup-patrol", "fork-cohort", "fork-contributor-leaderboard",
    "fork-first-run-alert", "fork-fleet", "fork-health", "fork-release-tracker",
    "fork-skill-digest", "fork-skill-gap", "frequency-guard", "fund-flow",
    "github-issues", "github-monitor", "github-releases", "github-trending",
    "goal-tracker", "hacker-news-digest", "heartbeat", "holder-concentration",
    "honeypot-check", "huggingface-trending", "idea-capture", "idea-pipeline",
    "idea-validator", "install-skill", "investigation-report", "issue-triage",
    "janitor", "last30", "linked-wallets", "liquidpad-launch", "list-digest",
    "lp-lock", "market-context-refresh", "mcp-pulse", "memory-dedupe",
    "mention-radar", "milestone-tracker", "monitor-kalshi", "monitor-polymarket",
    "monitor-runners", "morning-brief", "narrative-convergence", "narrative-tracker",
    "on-chain-monitor", "onboard", "operator-scorecard", "paper-digest",
    "paper-pick", "pm-manipulation", "pm-pulse", "polymarket-comments", "pr-merge",
    "pr-review", "pr-tracker", "pr-triage", "price-threshold-alert",
    "product-hunt-launch", "project-lens", "push-recap", "pvr-triage",
    "pvr-watchlist", "reddit-digest", "reflect", "refresh-x", "reg-monitor",
    "remix-tweets", "reply-maker", "repo-actions", "repo-article", "repo-pulse",
    "repo-revive", "repo-scanner", "research-brief", "rss-digest", "rss-feed",
    "rug-scan", "rwa-pulse", "schedule-ads", "search-skill", "security",
    "security-digest", "self-improve", "show-hn-draft", "signal-verdict",
    "skill-adoption", "skill-analytics", "skill-enabler", "skill-evals",
    "skill-freshness", "skill-graph", "skill-health", "skill-leaderboard",
    "skill-repair", "skill-security-scan", "skill-spotlight", "skill-triage",
    "skill-update-check", "smithery-manifest", "soul-builder", "sparkleware-catalog",
    "spawn-instance", "spend-monitor", "star-milestone", "star-momentum-alert",
    "startup-idea", "strategy-builder", "syndicate-article", "technical-explainer",
    "telegram-digest", "thought-review", "thread-formatter", "token-alert",
    "token-movers", "token-pick", "token-report", "tool-builder", "topic-momentum",
    "treasury-info", "tweet-roundup", "tx-explain", "unlock-monitor",
    "update-gallery", "v4-readiness", "vercel-projects", "vibecoding-digest",
    "vigil", "vigil-revoke", "vuln-scanner", "vuln-tracker", "wallet-profile",
    "wallet-risk", "weekly-review", "weekly-shiplog", "workflow-security-audit",
    "write-tweet", "x402-monitor",
}

# Tags per skill (best-effort from SKILL.md frontmatter knowledge)
# meta/dev tags matter for exclusion from DEFAULT_FLIP_ENABLE
SKILL_TAGS = {
    "heartbeat": ["meta"],
    "skill-health": ["meta"],
    "skill-evals": ["meta"],
    "skill-analytics": ["meta"],
    "skill-repair": ["meta"],
    "skill-triage": ["meta"],
    "skill-update-check": ["meta"],
    "skill-freshness": ["meta"],
    "skill-graph": ["meta"],
    "skill-security-scan": ["meta"],
    "skill-leaderboard": ["meta"],
    "fork-cohort": ["meta"],
    "fork-fleet": ["meta"],
    "fork-skill-digest": ["meta"],
    "fork-skill-gap": ["meta"],
    "fork-skill-gap": ["meta"],
    "fork-health": ["meta"],
    "fork-release-tracker": ["meta"],
    "fork-first-run-alert": ["meta"],
    "fork-contributor-leaderboard": ["meta"],
    "contributor-spotlight": ["meta"],
    "contributor-reward": ["meta"],
    "fleet-state": ["meta"],
    "fleet-control": ["meta"],
    "fleet-scorecard": ["meta"],
    "operator-scorecard": ["meta"],
    "action-converter": ["meta"],
    "self-improve": ["meta"],
    "autoresearch": ["meta"],
    "create-skill": ["dev"],
    "install-skill": ["dev"],
    "skill-enabler": ["dev"],
    "config-validator": ["dev"],
    "auto-workflow": ["dev"],
    "onboard": ["dev"],
    "deploy-prototype": ["dev"],
    "spawn-instance": ["dev"],
    "weekly-review": ["meta"],
    "weekly-shiplog": ["meta"],
    "reflect": ["meta"],
    "goal-tracker": ["meta"],
    "batch-health": ["meta"],
    "frequency-guard": ["meta"],
    "signal-verdict": ["meta"],
    "skill-spotlight": ["meta"],
    "api-health": ["meta"],
    "cost-report": ["meta"],
    "vuln-scanner": ["security"],
    "security-digest": ["security"],
    "security": ["security"],
    "pvr-triage": ["security"],
    "pvr-watchlist": ["security"],
    "vuln-tracker": ["security"],
    "workflow-security-audit": ["security"],
    "disclosure-tracker": ["security"],
    "github-trending": ["content"],
    "agent-buzz": ["content"],
    "narrative-tracker": ["content"],
    "search-skill": ["content"],
    "deal-flow": ["content"],
    "reg-monitor": ["content"],
    "mcp-pulse": ["content"],
    "ai-framework-watch": ["content"],
    "compute-pulse": ["content"],
    "rwa-pulse": ["content"],
    "paper-pick": ["content"],
    "hacker-news-digest": ["content"],
    "list-digest": ["social"],
    "tweet-roundup": ["social"],
    "write-tweet": ["social"],
    "agent-buzz": ["social"],
    "token-alert": ["crypto"],
    "token-movers": ["crypto"],
    "token-pick": ["crypto"],
    "defi-overview": ["crypto"],
    "defi-monitor": ["crypto"],
    "on-chain-monitor": ["crypto"],
    "market-context-refresh": ["crypto"],
    "btc-levels": ["crypto"],
    "narrative-tracker": ["crypto"],
    "aixbt-pulse": ["crypto"],
}

def get_upstream_default(skill_name):
    return {
        "enabled": skill_name in UPSTREAM_ENABLED,
        "model": UPSTREAM_MODELS.get(skill_name),
        "var": UPSTREAM_VARS.get(skill_name, ""),
        "schedule": UPSTREAM_SCHEDULES.get(skill_name),
    }

def normalize_model(m):
    if m is None:
        return None
    return str(m).strip()

def normalize_var(v):
    if v is None:
        return ""
    return str(v).strip()

def normalize_schedule(s):
    if s is None:
        return None
    return str(s).strip()

# ========== LOAD FORK DATA ==========
script_dir = os.path.dirname(os.path.abspath(__file__))
results_path = os.path.join(script_dir, ".fork_results_tmp.json")

with open(results_path) as f:
    fork_data = json.load(f)

n_active = len(fork_data)
print(f"Total active forks: {n_active}", file=sys.stderr)

# ========== TIER EACH FORK ==========
configured_forks = []
template_forks = []
unreadable_forks = []

for fd in fork_data:
    status = fd.get("status", "")
    fn = fd["full_name"]

    if status not in ("ok",):
        unreadable_forks.append(fn)
        continue

    skills = fd.get("skills", {})

    # Compute divergence signals
    enabled_diff = 0
    var_overrides = 0
    model_overrides = 0
    schedule_overrides = 0

    for skill_name, fork_skill in skills.items():
        if skill_name not in UPSTREAM_SKILLS:
            continue
        up = get_upstream_default(skill_name)

        # enabled diff: only count if fork explicitly set it differently
        fe = fork_skill.get("enabled")
        if fe is not None and fe != up["enabled"]:
            enabled_diff += 1

        # var override: fork sets a different non-empty var
        fv = normalize_var(fork_skill.get("var"))
        uv = up["var"]
        if fv and fv != uv:
            var_overrides += 1

        # model override
        fm = normalize_model(fork_skill.get("model"))
        um = up["model"]
        if fm is not None and fm != um:
            model_overrides += 1

        # schedule override
        fs = normalize_schedule(fork_skill.get("schedule"))
        us = up["schedule"]
        if fs is not None and fs != us:
            schedule_overrides += 1

    total_signal = enabled_diff + var_overrides + model_overrides + schedule_overrides

    if total_signal > 0:
        configured_forks.append({
            "full_name": fn,
            "skills": skills,
            "enabled_diff": enabled_diff,
            "var_overrides": var_overrides,
            "model_overrides": model_overrides,
            "schedule_overrides": schedule_overrides,
        })
    else:
        template_forks.append(fn)

n_configured = len(configured_forks)
n_template = len(template_forks)
n_unreadable = len(unreadable_forks)

print(f"Configured: {n_configured}, Template: {n_template}, Unreadable: {n_unreadable}", file=sys.stderr)

# ========== AGGREGATE DIVERGENCE ==========
if n_configured < 2:
    result = {
        "status": "FORK_SKILL_DIGEST_TEMPLATE_FLEET",
        "n_active": n_active,
        "n_configured": n_configured,
        "n_template": n_template,
        "n_unreadable": n_unreadable,
    }
    print(json.dumps(result))
    sys.exit(0)

# For each skill, compute divergence dimensions
skill_divergence = {}

for skill_name in UPSTREAM_SKILLS:
    up = get_upstream_default(skill_name)

    forks_enabled_count = 0   # forks where enabled=true
    forks_disabled_count = 0  # forks where enabled=false (explicitly)
    var_override_count = 0
    model_override_count = 0
    schedule_override_count = 0
    fork_models = []
    fork_vars = []
    fork_schedules = []

    for cf in configured_forks:
        fork_skills = cf["skills"]
        if skill_name not in fork_skills:
            continue
        fskill = fork_skills[skill_name]

        fe = fskill.get("enabled")
        if fe is True:
            forks_enabled_count += 1
        elif fe is False:
            forks_disabled_count += 1
        # else: None = inherits, don't count

        fv = normalize_var(fskill.get("var"))
        uv = up["var"]
        if fv and fv != uv:
            var_override_count += 1
            fork_vars.append(fv)

        fm = normalize_model(fskill.get("model"))
        um = up["model"]
        if fm is not None and fm != um:
            model_override_count += 1
            fork_models.append(fm)

        fs = normalize_schedule(fskill.get("schedule"))
        us = up["schedule"]
        if fs is not None and fs != us:
            schedule_override_count += 1
            fork_schedules.append(fs)

    # Compute divergence_pct
    upstream_enabled = up["enabled"]
    if not upstream_enabled:
        divergence_pct = forks_enabled_count / n_configured
        direction = "ENABLE_UPWARD"
    else:
        divergence_pct = forks_disabled_count / n_configured
        direction = "DISABLE_DOWNWARD"

    # Top values
    def top_value(lst, min_count=2):
        if not lst:
            return None, 0
        c = Counter(lst)
        top, count = c.most_common(1)[0]
        if count >= min_count:
            return top, count
        return None, 0

    top_model, top_model_count = top_value(fork_models)
    top_var, top_var_count = top_value(fork_vars)
    top_schedule, top_schedule_count = top_value(fork_schedules)

    if (forks_enabled_count > 0 or forks_disabled_count > 0 or
        var_override_count > 0 or model_override_count > 0 or schedule_override_count > 0):
        skill_divergence[skill_name] = {
            "forks_enabled_count": forks_enabled_count,
            "forks_disabled_count": forks_disabled_count,
            "upstream_enabled": upstream_enabled,
            "divergence_pct": divergence_pct,
            "direction": direction,
            "var_override_count": var_override_count,
            "model_override_count": model_override_count,
            "schedule_override_count": schedule_override_count,
            "top_model": top_model,
            "top_model_count": top_model_count,
            "top_var": top_var,
            "top_var_count": top_var_count,
            "top_schedule": top_schedule,
            "top_schedule_count": top_schedule_count,
        }

# ========== CATEGORIZE DIVERGENT SKILLS ==========
buckets = {
    "DEFAULT_FLIP_ENABLE": [],
    "DEFAULT_FLIP_DISABLE": [],
    "MODEL_CONSENSUS": [],
    "VAR_HOTSPOT": [],
    "EMERGING": [],
}

categorized = set()

# Thresholds
model_threshold = max(2, math.ceil(n_configured * 0.40))
var_threshold = max(2, math.ceil(n_configured * 0.30))

# Tags to exclude from DEFAULT_FLIP_ENABLE
EXCLUDE_TAGS = {"meta", "dev"}

WD_SKILLS = set()  # skills with workflow_dispatch schedule
for skill_name in UPSTREAM_SKILLS:
    up = get_upstream_default(skill_name)
    if up.get("schedule") == "workflow_dispatch":
        WD_SKILLS.add(skill_name)

for skill_name, sd in skill_divergence.items():
    if skill_name in categorized:
        continue

    tags = SKILL_TAGS.get(skill_name, [])
    is_meta_or_dev = any(t in EXCLUDE_TAGS for t in tags)
    is_wd = skill_name in WD_SKILLS

    # DEFAULT_FLIP_ENABLE
    if (sd["direction"] == "ENABLE_UPWARD" and
        sd["divergence_pct"] >= 0.50 and
        not is_wd and
        not is_meta_or_dev):
        buckets["DEFAULT_FLIP_ENABLE"].append({
            "skill": skill_name,
            "forks": sd["forks_enabled_count"],
            "pct": round(sd["divergence_pct"], 2)
        })
        categorized.add(skill_name)
        continue

    # DEFAULT_FLIP_DISABLE
    if (sd["direction"] == "DISABLE_DOWNWARD" and
        sd["divergence_pct"] >= 0.50 and
        skill_name != "heartbeat"):
        buckets["DEFAULT_FLIP_DISABLE"].append({
            "skill": skill_name,
            "forks": sd["forks_disabled_count"],
            "pct": round(sd["divergence_pct"], 2)
        })
        categorized.add(skill_name)
        continue

    # MODEL_CONSENSUS
    if sd["top_model"] and sd["top_model_count"] >= model_threshold:
        buckets["MODEL_CONSENSUS"].append({
            "skill": skill_name,
            "model": sd["top_model"],
            "forks": sd["top_model_count"]
        })
        categorized.add(skill_name)
        continue

    # VAR_HOTSPOT
    if sd["var_override_count"] >= var_threshold and sd["top_var"]:
        buckets["VAR_HOTSPOT"].append({
            "skill": skill_name,
            "var": sd["top_var"],
            "forks": sd["top_var_count"]
        })
        categorized.add(skill_name)
        continue

    # EMERGING
    if (sd["direction"] == "ENABLE_UPWARD" and
        0.25 <= sd["divergence_pct"] < 0.50):
        buckets["EMERGING"].append({
            "skill": skill_name,
            "pct": round(sd["divergence_pct"], 2)
        })
        categorized.add(skill_name)

# Sort buckets by pct/forks desc
for key in ["DEFAULT_FLIP_ENABLE", "DEFAULT_FLIP_DISABLE"]:
    buckets[key].sort(key=lambda x: x["pct"], reverse=True)
buckets["MODEL_CONSENSUS"].sort(key=lambda x: x["forks"], reverse=True)
buckets["VAR_HOTSPOT"].sort(key=lambda x: x["forks"], reverse=True)
buckets["EMERGING"].sort(key=lambda x: x["pct"], reverse=True)

# ========== FORK-ONLY SKILLS ==========
# We'd need tree calls per fork; skip for now - use prior known data + any new ones
# For this run, note that tree calls weren't made, so fork-only detection is limited
fork_only_skills = []  # would need tree calls

# ========== PER-FORK FINGERPRINT ==========
fork_fingerprints = []
for cf in configured_forks:
    total_overrides = (cf["enabled_diff"] + cf["var_overrides"] +
                      cf["model_overrides"] + cf["schedule_overrides"])

    # Category lean: count enabled skills by tag
    tag_counts = defaultdict(int)
    for skill_name, fskill in cf["skills"].items():
        fe = fskill.get("enabled")
        if fe is True:
            tags = SKILL_TAGS.get(skill_name, ["other"])
            for t in tags:
                tag_counts[t] += 1

    total_enabled = sum(tag_counts.values())
    if total_enabled == 0:
        dominant = "mixed"
    else:
        top_tag, top_count = max(tag_counts.items(), key=lambda x: x[1], default=("mixed", 0))
        if top_count > total_enabled * 0.40:
            dominant = top_tag
        else:
            dominant = "mixed"

    fork_fingerprints.append({
        "fork": cf["full_name"],
        "total_overrides": total_overrides,
        "dominant_category": dominant,
        "enabled_diff": cf["enabled_diff"],
        "var_overrides": cf["var_overrides"],
        "model_overrides": cf["model_overrides"],
        "schedule_overrides": cf["schedule_overrides"],
    })

fork_fingerprints.sort(key=lambda x: x["total_overrides"], reverse=True)
top_5_fingerprints = fork_fingerprints[:5]

# ========== APPENDIX TABLE ==========
appendix_rows = []
for skill_name, sd in skill_divergence.items():
    total = (sd["forks_enabled_count"] + sd["forks_disabled_count"] +
             sd["var_override_count"] + sd["model_override_count"] +
             sd["schedule_override_count"])
    appendix_rows.append({
        "skill": skill_name,
        "direction": sd["direction"],
        "enable_diff": sd["forks_enabled_count"] if sd["direction"] == "ENABLE_UPWARD" else sd["forks_disabled_count"],
        "var_overrides": sd["var_override_count"],
        "model_overrides": sd["model_override_count"],
        "schedule_overrides": sd["schedule_override_count"],
        "pct": round(sd["divergence_pct"], 2),
        "total": total,
    })
appendix_rows.sort(key=lambda x: x["total"], reverse=True)

# ========== OUTPUT ==========
result = {
    "n_active": n_active,
    "n_configured": n_configured,
    "n_template": n_template,
    "n_unreadable": n_unreadable,
    "unreadable_forks": unreadable_forks,
    "template_forks": template_forks,
    "buckets": buckets,
    "fork_only_skills": fork_only_skills,
    "fingerprints": top_5_fingerprints,
    "appendix": appendix_rows[:30],
    "skill_divergence": {k: v for k, v in list(skill_divergence.items())[:50]},
}

out_path = os.path.join(script_dir, "fork_analysis_output.json")
with open(out_path, "w") as f:
    json.dump(result, f, indent=2)

print(f"Analysis written to {out_path}", file=sys.stderr)
print(json.dumps(result, indent=2))
