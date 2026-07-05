#!/usr/bin/env node
/**
 * Fork Skill Digest analysis script (Node.js port of fork_analysis.py)
 * Reads .fork_results_tmp.json and produces fork_analysis_output.json
 */

const fs = require('fs');
const path = require('path');

// ========== UPSTREAM DEFAULTS ==========
const UPSTREAM_ENABLED = new Set([
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
]);

const UPSTREAM_MODELS = {
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
  "competitor-launch-radar": "claude-sonnet-4-6",
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
};

const UPSTREAM_VARS = {
  "list-digest": "1642770456720683008",
  "thought-review": "24",
};

const UPSTREAM_SCHEDULES = {
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
};

const UPSTREAM_SKILLS = new Set([
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
]);

const SKILL_TAGS = {
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
  // note: agent-buzz appears twice in py (content + social); keep content
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
};

function getUpstreamDefault(skillName) {
  return {
    enabled: UPSTREAM_ENABLED.has(skillName),
    model: UPSTREAM_MODELS[skillName] || null,
    var: UPSTREAM_VARS[skillName] || "",
    schedule: UPSTREAM_SCHEDULES[skillName] || null,
  };
}

function normalizeModel(m) {
  if (m === null || m === undefined) return null;
  return String(m).trim();
}

function normalizeVar(v) {
  if (v === null || v === undefined) return "";
  return String(v).trim();
}

function normalizeSchedule(s) {
  if (s === null || s === undefined) return null;
  return String(s).trim();
}

function topValue(lst, minCount = 2) {
  if (!lst || lst.length === 0) return [null, 0];
  const counts = {};
  for (const x of lst) counts[x] = (counts[x] || 0) + 1;
  let topItem = null, topCount = 0;
  for (const [k, v] of Object.entries(counts)) {
    if (v > topCount) { topItem = k; topCount = v; }
  }
  if (topCount >= minCount) return [topItem, topCount];
  return [null, 0];
}

// ========== LOAD FORK DATA ==========
const scriptDir = path.dirname(path.resolve(__filename));
const resultsPath = path.join(scriptDir, '.fork_results_tmp.json');
const fork_data = JSON.parse(fs.readFileSync(resultsPath, 'utf8'));

const n_active = fork_data.length;
process.stderr.write(`Total active forks: ${n_active}\n`);

// ========== TIER EACH FORK ==========
const configured_forks = [];
const template_forks = [];
const unreadable_forks = [];

for (const fd of fork_data) {
  const status = fd.status || "";
  const fn = fd.full_name;

  if (status !== "ok") {
    unreadable_forks.push(fn);
    continue;
  }

  const skills = fd.skills || {};

  let enabled_diff = 0, var_overrides = 0, model_overrides = 0, schedule_overrides = 0;

  for (const [skill_name, fork_skill] of Object.entries(skills)) {
    if (!UPSTREAM_SKILLS.has(skill_name)) continue;
    const up = getUpstreamDefault(skill_name);

    const fe = fork_skill.enabled;
    if (fe !== null && fe !== undefined && fe !== up.enabled) enabled_diff++;

    const fv = normalizeVar(fork_skill.var);
    const uv = up.var;
    if (fv && fv !== uv) var_overrides++;

    const fm = normalizeModel(fork_skill.model);
    const um = up.model;
    if (fm !== null && fm !== um) model_overrides++;

    const fs_ = normalizeSchedule(fork_skill.schedule);
    const us = up.schedule;
    if (fs_ !== null && fs_ !== us) schedule_overrides++;
  }

  const total_signal = enabled_diff + var_overrides + model_overrides + schedule_overrides;

  if (total_signal > 0) {
    configured_forks.push({ full_name: fn, skills, enabled_diff, var_overrides, model_overrides, schedule_overrides });
  } else {
    template_forks.push(fn);
  }
}

const n_configured = configured_forks.length;
const n_template = template_forks.length;
const n_unreadable = unreadable_forks.length;

process.stderr.write(`Configured: ${n_configured}, Template: ${n_template}, Unreadable: ${n_unreadable}\n`);

// ========== EARLY EXIT IF NOT ENOUGH CONFIGURED ==========
if (n_configured < 2) {
  const result = {
    status: "FORK_SKILL_DIGEST_TEMPLATE_FLEET",
    n_active, n_configured, n_template, n_unreadable,
  };
  console.log(JSON.stringify(result, null, 2));
  process.exit(0);
}

// ========== AGGREGATE DIVERGENCE ==========
const skill_divergence = {};

for (const skill_name of UPSTREAM_SKILLS) {
  const up = getUpstreamDefault(skill_name);

  let forks_enabled_count = 0, forks_disabled_count = 0;
  let var_override_count = 0, model_override_count = 0, schedule_override_count = 0;
  const fork_models = [], fork_vars = [], fork_schedules = [];

  for (const cf of configured_forks) {
    const fork_skills = cf.skills;
    if (!(skill_name in fork_skills)) continue;
    const fskill = fork_skills[skill_name];

    const fe = fskill.enabled;
    if (fe === true) forks_enabled_count++;
    else if (fe === false) forks_disabled_count++;

    const fv = normalizeVar(fskill.var);
    const uv = up.var;
    if (fv && fv !== uv) { var_override_count++; fork_vars.push(fv); }

    const fm = normalizeModel(fskill.model);
    const um = up.model;
    if (fm !== null && fm !== um) { model_override_count++; fork_models.push(fm); }

    const fs_ = normalizeSchedule(fskill.schedule);
    const us = up.schedule;
    if (fs_ !== null && fs_ !== us) { schedule_override_count++; fork_schedules.push(fs_); }
  }

  const upstream_enabled = up.enabled;
  let divergence_pct, direction;
  if (!upstream_enabled) {
    divergence_pct = forks_enabled_count / n_configured;
    direction = "ENABLE_UPWARD";
  } else {
    divergence_pct = forks_disabled_count / n_configured;
    direction = "DISABLE_DOWNWARD";
  }

  const [top_model, top_model_count] = topValue(fork_models);
  const [top_var, top_var_count] = topValue(fork_vars);
  const [top_schedule, top_schedule_count] = topValue(fork_schedules);

  if (forks_enabled_count > 0 || forks_disabled_count > 0 ||
      var_override_count > 0 || model_override_count > 0 || schedule_override_count > 0) {
    skill_divergence[skill_name] = {
      forks_enabled_count, forks_disabled_count, upstream_enabled,
      divergence_pct, direction,
      var_override_count, model_override_count, schedule_override_count,
      top_model, top_model_count, top_var, top_var_count, top_schedule, top_schedule_count,
    };
  }
}

// ========== CATEGORIZE ==========
const buckets = {
  DEFAULT_FLIP_ENABLE: [],
  DEFAULT_FLIP_DISABLE: [],
  MODEL_CONSENSUS: [],
  VAR_HOTSPOT: [],
  EMERGING: [],
};

const categorized = new Set();
const model_threshold = Math.max(2, Math.ceil(n_configured * 0.40));
const var_threshold = Math.max(2, Math.ceil(n_configured * 0.30));
const EXCLUDE_TAGS = new Set(["meta", "dev"]);

const WD_SKILLS = new Set();
for (const skill_name of UPSTREAM_SKILLS) {
  const up = getUpstreamDefault(skill_name);
  if (up.schedule === "workflow_dispatch") WD_SKILLS.add(skill_name);
}

for (const [skill_name, sd] of Object.entries(skill_divergence)) {
  if (categorized.has(skill_name)) continue;

  const tags = SKILL_TAGS[skill_name] || [];
  const is_meta_or_dev = tags.some(t => EXCLUDE_TAGS.has(t));
  const is_wd = WD_SKILLS.has(skill_name);

  if (sd.direction === "ENABLE_UPWARD" && sd.divergence_pct >= 0.50 && !is_wd && !is_meta_or_dev) {
    buckets.DEFAULT_FLIP_ENABLE.push({ skill: skill_name, forks: sd.forks_enabled_count, pct: Math.round(sd.divergence_pct * 100) / 100 });
    categorized.add(skill_name);
    continue;
  }

  if (sd.direction === "DISABLE_DOWNWARD" && sd.divergence_pct >= 0.50 && skill_name !== "heartbeat") {
    buckets.DEFAULT_FLIP_DISABLE.push({ skill: skill_name, forks: sd.forks_disabled_count, pct: Math.round(sd.divergence_pct * 100) / 100 });
    categorized.add(skill_name);
    continue;
  }

  if (sd.top_model && sd.top_model_count >= model_threshold) {
    buckets.MODEL_CONSENSUS.push({ skill: skill_name, model: sd.top_model, forks: sd.top_model_count });
    categorized.add(skill_name);
    continue;
  }

  if (sd.var_override_count >= var_threshold && sd.top_var) {
    buckets.VAR_HOTSPOT.push({ skill: skill_name, var: sd.top_var, forks: sd.top_var_count });
    categorized.add(skill_name);
    continue;
  }

  if (sd.direction === "ENABLE_UPWARD" && sd.divergence_pct >= 0.25 && sd.divergence_pct < 0.50) {
    buckets.EMERGING.push({ skill: skill_name, pct: Math.round(sd.divergence_pct * 100) / 100 });
    categorized.add(skill_name);
  }
}

// Sort
buckets.DEFAULT_FLIP_ENABLE.sort((a, b) => b.pct - a.pct);
buckets.DEFAULT_FLIP_DISABLE.sort((a, b) => b.pct - a.pct);
buckets.MODEL_CONSENSUS.sort((a, b) => b.forks - a.forks);
buckets.VAR_HOTSPOT.sort((a, b) => b.forks - a.forks);
buckets.EMERGING.sort((a, b) => b.pct - a.pct);

// ========== PER-FORK FINGERPRINT ==========
const fork_fingerprints = [];
for (const cf of configured_forks) {
  const total_overrides = cf.enabled_diff + cf.var_overrides + cf.model_overrides + cf.schedule_overrides;

  const tag_counts = {};
  for (const [skill_name, fskill] of Object.entries(cf.skills)) {
    const fe = fskill.enabled;
    if (fe === true) {
      const tags = SKILL_TAGS[skill_name] || ["other"];
      for (const t of tags) tag_counts[t] = (tag_counts[t] || 0) + 1;
    }
  }

  const total_enabled = Object.values(tag_counts).reduce((a, b) => a + b, 0);
  let dominant = "mixed";
  if (total_enabled > 0) {
    let topTag = "mixed", topCount = 0;
    for (const [t, c] of Object.entries(tag_counts)) {
      if (c > topCount) { topTag = t; topCount = c; }
    }
    if (topCount > total_enabled * 0.40) dominant = topTag;
  }

  fork_fingerprints.push({
    fork: cf.full_name,
    total_overrides,
    dominant_category: dominant,
    enabled_diff: cf.enabled_diff,
    var_overrides: cf.var_overrides,
    model_overrides: cf.model_overrides,
    schedule_overrides: cf.schedule_overrides,
  });
}

fork_fingerprints.sort((a, b) => b.total_overrides - a.total_overrides);
const top_5_fingerprints = fork_fingerprints.slice(0, 5);

// ========== APPENDIX TABLE ==========
const appendix_rows = [];
for (const [skill_name, sd] of Object.entries(skill_divergence)) {
  const total = sd.forks_enabled_count + sd.forks_disabled_count +
    sd.var_override_count + sd.model_override_count + sd.schedule_override_count;
  appendix_rows.push({
    skill: skill_name,
    direction: sd.direction,
    enable_diff: sd.direction === "ENABLE_UPWARD" ? sd.forks_enabled_count : sd.forks_disabled_count,
    var_overrides: sd.var_override_count,
    model_overrides: sd.model_override_count,
    schedule_overrides: sd.schedule_override_count,
    pct: Math.round(sd.divergence_pct * 100) / 100,
    total,
  });
}
appendix_rows.sort((a, b) => b.total - a.total);

// ========== OUTPUT ==========
const result = {
  n_active, n_configured, n_template, n_unreadable,
  unreadable_forks, template_forks,
  buckets,
  fork_only_skills: [],
  fingerprints: top_5_fingerprints,
  appendix: appendix_rows.slice(0, 30),
  skill_divergence: Object.fromEntries(Object.entries(skill_divergence).slice(0, 50)),
};

const out_path = path.join(scriptDir, 'fork_analysis_output.json');
fs.writeFileSync(out_path, JSON.stringify(result, null, 2));

process.stderr.write(`Analysis written to ${out_path}\n`);
console.log(JSON.stringify(result, null, 2));
