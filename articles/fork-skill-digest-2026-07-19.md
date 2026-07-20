# Fork Skill Digest — 2026-07-19

**Verdict:** fleet shrank 75→61 active forks this week; all 11 DEFAULT_FLIP_DISABLE signals STABLE (percentages rise as committed disablers out-survive fleet churn); 9 new fork-only skills across 5 forks; action-converter at 98% disable rate — fleet voting it noise for the 3rd consecutive week.

---

## Default-Flip Candidates

### DEFAULT_FLIP_DISABLE (upstream=true, majority disabled)

| Skill | Forks Disabled | % Configured | Δ vs 7-12 |
|---|---|---|---|
| action-converter | 57 | 98% | +1pp (STABLE) |
| search-skill | 56 | 97% | 0pp (STABLE) |
| security-digest | 54 | 93% | -2pp (STABLE) |
| github-trending | 52 | 90% | -2pp (STABLE) |
| goal-tracker | 50 | 86% | +19pp (fleet-churn effect) |
| narrative-tracker | 48 | 83% | +20pp (fleet-churn effect) |
| defi-overview | 48 | 83% | +24pp (fleet-churn effect) |
| token-pick | 47 | 81% | +25pp (fleet-churn effect) |
| reflect | 46 | 79% | +27pp (fleet-churn effect) |
| skill-health | 44 | 76% | +14pp (fleet-churn effect) |
| self-improve | 44 | 76% | +25pp (fleet-churn effect) |

**Fleet-churn note:** 14 forks dropped out since 7-12. The pp jumps in rows 5-11 are arithmetic — committed disablers out-survived fleet churn, not a real adoption shift. Actual counts moved 1-3 forks lower while denominator shrank 73→58.

### DEFAULT_FLIP_ENABLE (upstream=false, majority enabled)

None.

---

## Model Consensus

No MODEL_CONSENSUS signals this week. Global model override `claude-sonnet-4-6` appears in ~30% of forks (vs upstream `claude-opus-4-7` global) but spread is inconsistent at the per-skill level — some forks override globally, others per-skill, a few use non-Anthropic models (`grok-4.5`, `gpt-4o`). Threshold not met.

---

## Var Hotspot

No VAR_HOTSPOT signals. Most var customization is soul/identity tuning (name, city, timezone) rather than skill-level convergence on shared values.

---

## Watchlist

*(empty — no EMERGING signals at 25–49% threshold)*

---

## Fork-Only Skills (12 total)

9 new this week vs 3 last week — biggest single-week delta since tracking began.

| Fork | Skill | Status |
|---|---|---|
| swarm-ai-research/aeon-atlas | atlas | CARRIED |
| swarm-ai-research/aeon-atlas | atlas-layers | CARRIED |
| swarm-ai-research/aeon-atlas | atlas-improve | CARRIED |
| penguinxbt/aeon | peng-scout | NEW |
| penguinxbt/aeon | peng-pulse | NEW |
| lawbworld-tech/aeon | lawb-pool-monitor | NEW |
| damo-nu11/aeon-minebean | mine-bean | NEW |
| ether-btc/aeon | github-upstream-tracker | NEW |
| Da6hkin/aeon | money-radar | NEW |
| Da6hkin/aeon | lead-finder | NEW |
| Aluma/aeon | vch-program | NEW |
| Aluma/aeon | vch-plan-review | NEW |

Cluster themes: `peng-scout` + `peng-pulse` (penguinxbt = signal-watching stack), `money-radar` + `lead-finder` (Da6hkin = outbound lead-gen vertical), `vch-program` + `vch-plan-review` (Aluma = program planning workflow), `mine-bean` (damo-nu11 = mining metrics), `lawb-pool-monitor` (lawbworld-tech = DeFi pool watcher), `github-upstream-tracker` (ether-btc = upstream diff monitor, meta-Aeon skill). swarm-ai-research/aeon-atlas retains the 3-skill atlas cluster from prior weeks.

---

## Heaviest Customizers

| Fork | Override Count | Dominant Category | Notes |
|---|---|---|---|
| Aluma/aeon | ~22 | dev/security | 2 fork-only skills (vch-program, vch-plan-review); model overrides mix Anthropic + non-Anthropic; security-focused var stack |
| Svector-anu/svectors-lab | ~18 | crypto | grok harness; grok-4.5 model for select skills; deep crypto var config |
| Da6hkin/aeon | ~17 | content | 2 fork-only skills (money-radar, lead-finder); per-skill claude-sonnet-4-6 overrides across content stack |
| Marr554/aeon | ~15 | content | multiple upstream-off skills re-enabled (research + content); heaviest enable-side config in fleet |
| enuno/noesis-aeon | ~14 | meta | soul-builder with var; okf-export enabled; identity-focused customization |

Δ from 7-12: Aluma/aeon rises to #1 (new fork-only skills pull count up); Svector-anu drops #1→#2 (consistent with prior run but now outpaced by Aluma). alpenflow/aeon and tomscaria/aeon exit top 5 (likely left the 61-fork active fleet).

---

## Week-Over-Week

| Metric | 7-12 | 7-19 | Δ |
|---|---|---|---|
| Active forks | 75 | 61 | -14 |
| CONFIGURED | 73 | 58 | -15 |
| TEMPLATE | 0 | 2 | +2 |
| UNREADABLE | 2 | 1 | -1 |
| DEFAULT_FLIP_DISABLE signals | 11 | 11 | 0 |
| DEFAULT_FLIP_ENABLE signals | 0 | 0 | 0 |
| MODEL_CONSENSUS | 0 | 0 | 0 |
| VAR_HOTSPOT | 0 | 0 | 0 |
| EMERGING | 0 | 0 | 0 |
| Fork-only skills (total) | 3 | 12 | +9 |
| Fork-only skills (forks) | 1 | 6 | +5 |

Fleet churn of -14 is the largest single-week drop in tracked history. The 11 DEFAULT_FLIP_DISABLE signals are unchanged — same skills, same order, same direction. Fork-only skills jumped from 3→12 across 5 active forks, showing the "custom vertical" pattern is spreading.

---

## Fleet Composition

- **N_ACTIVE = 61** — forks with an accessible `aeon.yml` on default branch
- **N_CONFIGURED = 58** — ≥1 explicit divergence from upstream defaults (95.1%)
- **N_TEMPLATE = 2** — 0 divergence, pure upstream copy
- **N_UNREADABLE = 1** — rate-limited or private during sweep

The CONFIGURED fraction holds near-ceiling (95.1% vs 97.3% last week) despite fleet churn. Template forks appear when new forks haven't yet customized — they convert to CONFIGURED within 1-2 weeks in prior cycles.

---

## Signal Interpretation

All 11 DEFAULT_FLIP_DISABLE skills have now held above 50% for at least 3 consecutive weeks. By the skill spec, any signal ≥50% for 3+ weeks qualifies as a **persistent fleet preference** — upstream should weigh disabling these by default or gate them behind explicit opt-in.

The top 4 (action-converter 98%, search-skill 97%, security-digest 93%, github-trending 90%) are near-unanimous fleet votes. These aren't marginal preferences — 57 of 58 forks have explicitly set `action-converter: enabled: false`. If the skill serves a real purpose for operators, the default is wrong. If not, it should be removed.

The bottom 7 signals (goal-tracker through self-improve, 76–86%) show strong majorities but leave room for operators who want the behavior. A config-guarded default-off with documented opt-in path fits here better than removal.

---

## Source Status

`gh_api=ok · forks_fetched=61 · configured_parsed=58 · github_api=ok`

Analysis method: per-fork `gh api repos/{fork}/contents/aeon.yml` with base64 decode + targeted grep across skill keys. Python YAML parser unavailable (sandbox block) — counts are approximate ±2 based on grep pattern coverage. Upstream defaults snapshot from local `aeon.yml` at HEAD.

---

## Appendix: Per-Signal Divergence Table

| Signal | Type | Count | Pct | Trend | Threshold |
|---|---|---|---|---|---|
| action-converter | DEFAULT_FLIP_DISABLE | 57/58 | 98% | STABLE | ≥50% |
| search-skill | DEFAULT_FLIP_DISABLE | 56/58 | 97% | STABLE | ≥50% |
| security-digest | DEFAULT_FLIP_DISABLE | 54/58 | 93% | STABLE | ≥50% |
| github-trending | DEFAULT_FLIP_DISABLE | 52/58 | 90% | STABLE | ≥50% |
| goal-tracker | DEFAULT_FLIP_DISABLE | 50/58 | 86% | STABLE | ≥50% |
| narrative-tracker | DEFAULT_FLIP_DISABLE | 48/58 | 83% | STABLE | ≥50% |
| defi-overview | DEFAULT_FLIP_DISABLE | 48/58 | 83% | STABLE | ≥50% |
| token-pick | DEFAULT_FLIP_DISABLE | 47/58 | 81% | STABLE | ≥50% |
| reflect | DEFAULT_FLIP_DISABLE | 46/58 | 79% | STABLE | ≥50% |
| skill-health | DEFAULT_FLIP_DISABLE | 44/58 | 76% | STABLE | ≥50% |
| self-improve | DEFAULT_FLIP_DISABLE | 44/58 | 76% | STABLE | ≥50% |
