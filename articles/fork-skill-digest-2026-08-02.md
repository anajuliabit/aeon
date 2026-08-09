# Fork Skill Digest — 2026-08-02

**Verdict:** 40 forks disable action-converter (upstream defaults on) — fleet is voting it as noise

*Scanned 50 active forks of aaronjmars/aeon (pushed in last 30 days). 49 are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured 49.*

---

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

| Skill | Forks disabled | % of configured | Δ vs last week |
|-------|----------------|-----------------|----------------|
| action-converter | 40 | 82% | — |
| search-skill | 38 | 78% | — |
| self-improve | 36 | 73% | — |
| autoresearch | 36 | 73% | — |
| github-trending | 34 | 69% | — |
| skill-health | 33 | 67% | — |
| security-digest | 32 | 65% | — |
| token-pick | 32 | 65% | — |
| vuln-scanner | 31 | 63% | — |
| defi-overview | 31 | 63% | — |
| token-movers | 31 | 63% | — |
| narrative-tracker | 30 | 61% | — |
| unlock-monitor | 30 | 61% | — |
| reflect | 28 | 57% | — |
| deal-flow | 28 | 57% | — |
| list-digest | 27 | 55% | — |
| goal-tracker | 27 | 55% | — |
| agent-buzz | 26 | 53% | — |

**Note:** Counts are based on explicit `enabled: false` entries in each fork's `aeon.yml`. Skills absent from a fork's config inherit the upstream default (not counted as divergence). Two template families are present in this fleet: the v4 template (heartbeat `0 8 * * *`, ~13 forks) and the full template (heartbeat `0 8,14,20 * * *`, ~21 forks). The full template explicitly lists more skills, so security-digest/deal-flow/list-digest/goal-tracker/agent-buzz counts reflect the larger template footprint.

Skills that **dropped out** vs last week: `token-alert` (last: 56%) and `defi-monitor` (last: 62%) — neither appears in the new fleet's primary template schema, so they inherit the upstream default rather than being explicitly disabled. `defi-monitor` and `token-alert` are stable in upstream; these are template-gap fades, not operator preferences.

---

## Fleet consensus on alternative settings

### Model overrides

No model crossed the fleet-consensus threshold (≥40% of configured forks) this week.

Notable individual overrides:
- `Da6hkin/aeon` — `heartbeat` → `claude-sonnet-4-6`; `defi-overview`, `unlock-monitor` → `claude-sonnet-4-6` (upstream: `claude-haiku-4-5-20251001` / none)
- `Aluma/aeon` — `pr-triage` → `gpt-luna`; `pr-review` → `claude-opus-4-8` (non-standard / different tier)
- `0xMal0u/aeon` — `on-chain-monitor`, `narrative-tracker`, `morning-brief` → `claude-sonnet-4-6` (upstream: `claude-haiku-4-5-20251001` / none)

Last week's MODEL_CONSENSUS (`smithery-manifest → claude-sonnet-4-6`, 34 forks): **FADED** — entirely new fleet, no fork in this cohort has smithery-manifest enabled.

### Var hotspots

None this week.

### Schedule overrides

| Skill | Forks | Alternative schedule | Note |
|-------|-------|----------------------|------|
| heartbeat | 13 | `0 8 * * *` | 1×/day vs upstream 3×/day (`0 8,14,20 * * *`). All 13 use the v4 template. Systematic operator preference for lighter heartbeat cadence. |
| defi-overview | 1 | `0 */6 * * *` | Svector-anu; 6×/day vs upstream 1×/day |
| narrative-tracker | 1 | `30 */6 * * *` | Svector-anu; 6×/day vs upstream 1×/day |
| enzoonchain/heartbeat | 1 | `0 7,13,19 * * *` | Shifted 1h earlier than upstream |

---

## Watchlist (emerging — 25–49% adoption)

None this week. No skill in the 25–49% enable-upward band.

---

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| stefrogovskyi/aeon | ~30 | meta | Old-template disabler: 24+ upstream-enabled skills explicitly set false; no custom enables. Highest enabled_diff in fleet. |
| nigelon11/aeon | ~25 | meta | Similar full-template disabler pattern. 101 explicit `enabled: false` entries; uses v4 naming (`hn-digest`, `onchain-monitor`). |
| Svector-anu/svectors-lab | ~15 | fork-only | Active operator: 4 upstream-disabled skills enabled (digest, auto-workflow, x402-monitor, fear-divergence) + 3 fork-only skills (verdikta-hunter, hunter-22, picks-tracker) + 2 schedule overrides. |
| Marr554/aeon | ~10 | dev | 6 upstream-disabled skills enabled (pr-review, github-monitor, research-brief, deep-research, external-feature, strategy-builder) + fork-only skill (priority-brief). |
| Aluma/aeon | ~8 | dev | 2 enables (pr-triage, pr-review), 2 model overrides (gpt-luna on pr-triage, claude-opus-4-8 on pr-review), 2 fork-only skills (vch-program, vch-plan-review). First fleet instance of non-Claude model keys on upstream skills. |

---

## Fork-only skills

| Fork | Skill | Note |
|------|-------|------|
| swarm-ai-research/aeon-atlas | atlas | Sunday 04:00 UTC — fetch all forks, parse aeon.yml, regenerate atlas.{json,md,html} |
| swarm-ai-research/aeon-atlas | atlas-layers | Sunday 05:00 UTC — render 7-layer categorical view from atlas.json |
| swarm-ai-research/aeon-atlas | atlas-improve | Monthly — diff 30d atlas.json, open one improvement PR |
| enuno/noesis-aeon | okf-export | OKF type-frontmatter backfill on memory/topics notes |
| enuno/noesis-aeon | memory-flush | Daily 23:30 UTC — promote important log entries into MEMORY.md |
| Aluma/aeon | vch-program | Custom role skill for Aluma/vybose-context-hub auditing |
| Aluma/aeon | vch-plan-review | Independent plan gate using gpt-terra model |
| Svector-anu/svectors-lab | verdikta-hunter | Verdikta AI-judged bounties on Base |
| Svector-anu/svectors-lab | hunter-22 | Daily bounty scan against ClawHunter free discovery API |
| Svector-anu/svectors-lab | picks-tracker | Sunday — 30-day retrospective scoring of picks |
| freezerboi/aeon | hunter-22 | ClawHunter bounty scan (shared with Svector-anu) |
| freezerboi/aeon | picks-tracker | Picks retrospective |
| damo-nu11/aeon-minebean | mine-bean | 10-min cron — custom scheduled task |
| lawbworld-tech/aeon | lawb-pool-monitor | Hourly — LawbFishing prize pool health on Base mainnet |
| ether-btc/aeon | github-upstream-tracker | 30-min — sync upstream PR state |
| Marr554/aeon | priority-brief | Morning priority brief (7:00 UTC) |

These skills exist as `skills/<name>/SKILL.md` in a fork but not in upstream. Surfaces fork experiments worth reviewing for upstreaming.

---

## Week-over-week

**Fleet composition shift** — prior snapshot (2026-07-26) captured 79 active forks; this run captured 50. The 30d activity window has rotated to a newer cohort: the forks from last week's bulk of old-template heavy disablers (SahilParikh03, mnemedb, NASTYZUNI, dannysrod, daxaur) have aged out. The new fleet is split between v4-template operators (heartbeat 1×/day) and full-template operators (heartbeat 3×/day, 182 explicit disabled entries).

| Delta type | Skills |
|------------|--------|
| FADED (DEFAULT_FLIP_DISABLE → not in bucket) | `token-alert` (was 56%), `defi-monitor` (was 62%), `aixbt-pulse` (was 87%) |
| FADED (MODEL_CONSENSUS) | `smithery-manifest → claude-sonnet-4-6` (was 34 forks) |
| STABLE (DEFAULT_FLIP_DISABLE) | action-converter, search-skill, self-improve, autoresearch, security-digest, deal-flow, github-trending, skill-health, token-pick, vuln-scanner, defi-overview, token-movers, narrative-tracker, unlock-monitor, reflect, list-digest, goal-tracker, agent-buzz |
| NEW_FORK_ONLY | atlas, atlas-layers, atlas-improve, okf-export, memory-flush, vch-program, vch-plan-review, verdikta-hunter, hunter-22, picks-tracker, mine-bean, lawb-pool-monitor, github-upstream-tracker, priority-brief (14 fork-only skills vs 0 last week) |
| NEW_HEAVY_CUSTOMIZER | Svector-anu/svectors-lab, Aluma/aeon, enuno/noesis-aeon |

---

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 49 | 98% |
| Template (untouched aeon.yml) | 0 | 0% |
| Unreadable | 1 | 2% |
| **Total active** | **50** | 100% |

---

## Source status

- Trees fetched: 50 / 50
- aeon.yml readable: 49 / 50
- YAML parse failures: 0
- Rate-limited: 0
- Fork-only skills inspected: 16
- Unreadable: 1 (mirkosalvato1-ctrl/aeon — no aeon.yml found)

---

## Appendix — full divergence table

| Skill | enable_diff | schedule_overrides | model_overrides | var_overrides |
|-------|-------------|-------------------|-----------------|---------------|
| action-converter | 40 | 0 | 0 | 0 |
| search-skill | 38 | 0 | 0 | 0 |
| self-improve | 36 | 0 | 0 | 0 |
| autoresearch | 36 | 0 | 0 | 0 |
| github-trending | 34 | 0 | 0 | 0 |
| skill-health | 33 | 0 | 0 | 0 |
| security-digest | 32 | 0 | 0 | 0 |
| token-pick | 32 | 0 | 0 | 0 |
| vuln-scanner | 31 | 0 | 0 | 0 |
| defi-overview | 31 | 0 | 0 | 0 |
| token-movers | 31 | 0 | 0 | 0 |
| narrative-tracker | 30 | 1 | 1 | 1 |
| unlock-monitor | 30 | 0 | 1 | 0 |
| reflect | 28 | 0 | 0 | 0 |
| deal-flow | 28 | 0 | 0 | 0 |
| list-digest | 27 | 0 | 0 | 0 |
| goal-tracker | 27 | 0 | 0 | 0 |
| agent-buzz | 26 | 0 | 0 | 0 |
| heartbeat | 0 | 14 | 1 | 0 |
| skill-analytics | 25 | 0 | 0 | 0 |
| cost-report | 24 | 1 | 1 | 0 |
| fork-cohort | 24 | 0 | 0 | 0 |
| reg-monitor | 24 | 0 | 0 | 0 |
| skill-evals | 24 | 0 | 0 | 0 |
| skill-graph | 23 | 0 | 0 | 0 |
| on-chain-monitor | 2 | 1 | 1 | 1 |
| morning-brief | 3 | 0 | 1 | 1 |
| pr-review | 2 | 1 | 1 | 0 |
| pr-triage | 1 | 0 | 1 | 1 |
| defi-overview (schedule) | — | 1 | 0 | 0 |

+ 6 more skills with low-signal divergence (≤1 fork, single dimension)

---

*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work). Note: enable_diff counts for disable-downward signals are estimates based on explicit `enabled: false` entries sampled across the 49 configured forks; two template families each list different subsets of skills, so per-skill counts reflect the union of explicit disables observed.*
