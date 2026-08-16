# Fork Skill Digest — 2026-08-16

**Verdict:** Da6hkin shipped lead-finder — not in upstream

*Scanned 71 active forks of aaronjmars/aeon (pushed in last 30 days). 18 are confirmed configured (aeon.yml diverges from upstream defaults). Divergence scored against the confirmed 18. Note: a full recursive tree scan of all 71 forks was not feasible this run; counts represent a verified lower bound from targeted sampling of the most active forks.*

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

No skills crossed the 50% disable-downward threshold.

*Observation: chxoky/aeon is the lone v1 fork running a sharply trimmed stack — 35+ upstream-enabled skills explicitly disabled, retaining only 7 crypto/trading skills and a custom trader-memory-compact. One fork doing deep pruning doesn't move the fleet needle, but the shape itself is worth watching. If 3–4 more forks converge on the same trim, that's a real signal.*

## Fleet consensus on alternative settings

### Model overrides

None this week. Da6hkin blankets ~12 skills with `claude-sonnet-4-6` (vs upstream `claude-opus-4-7`) but no other confirmed fork shares that pattern at the 40% threshold (≥8 of 18).

### Var hotspots

None this week.

### Schedule overrides

**heartbeat** — at least 5 confirmed forks (`alexverify/aeon`, `Cristian35s/aeon`, `kdegeek/aeon`, `amritmirch/aeon`, `hesreallyhim/aeon-fork`) override the upstream schedule from `0 8,14,20 * * *` (3× daily) to `0 8 * * *` (1× daily). This is a v2 community norm: once-daily heartbeat instead of three-times. Not a flip candidate (one fork running 3× vs many running 1× doesn't signal upstream is wrong — it signals the community prefers quieter ambient checks). Surface as an informational data point.

## Watchlist (emerging — 25–49% adoption)

**github-monitor** — upstream defaults `enabled: false`. Confirmed enabled in at least 4 v2-style forks (`olanotolu/aeon`, `bspacer/aeon`, `belikh/aeon`, `enuno/noesis-aeon`). With N_CONFIGURED = 18, that's 22% — just below the 25% EMERGING threshold. Last week it sat at 26.3% (5/19 configured). The apparent dip is partially a sampling artifact (12 new active forks joined the 30-day window, diluting the denominator); the absolute count may be stable or growing. Watch at next run.

**digest** — upstream defaults `enabled: false`. Enabled in `Svector-anu/svectors-lab`, `bspacer/aeon`, `olanotolu/aeon` = 3/18 = 17%. Below threshold, but a consistent cluster of heavier customizers is running it.

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| chxoky/aeon | ~36 | trading | 35 explicit upstream-enabled disables + trader-memory-compact fork-only; keeps only 7 crypto trading skills (morning-brief, token-alert, token-movers, market-context-refresh, narrative-tracker, skill-health, heartbeat). Maximum trim. |
| olanotolu/aeon | ~25 | mixed | v2 fork; 15+ skill enables with var overrides (`Concya/concya-platform`); fork-only: robinhood-mcp, glim-mcp, finance-district-mcp. Dev + trading composite. |
| bspacer/aeon | ~22 | dev | v2 fork; auto-merge, article, digest, changelog, vuln-tracker enabled; fork-only: robinhood-mcp, you-web-search, aeon-doctor, seo-audit. Heavy dev-tooling posture. |
| Da6hkin/aeon | ~17 | content/trading | 3 enable upward (paper-digest, monitor-kalshi, vibecoding-digest); model overrides on ~12 skills to claude-sonnet-4-6; fork-only: money-radar, lead-finder (new). Finance-first stack. |
| Svector-anu/svectors-lab | ~9 | fork-only | 4 enable upward (digest, auto-workflow, x402-monitor, fear-divergence); schedule overrides on defi-overview + narrative-tracker (every 6h vs 12h/13h upstream); fork-only: verdikta-hunter, hunter-22, picks-tracker. Bounty + high-freq intel posture. |

## Fork-only skills

| Fork | Skill | Status |
|------|-------|--------|
| swarm-ai-research/aeon-atlas | atlas | carry-forward |
| swarm-ai-research/aeon-atlas | atlas-layers | carry-forward |
| swarm-ai-research/aeon-atlas | atlas-improve | carry-forward |
| Svector-anu/svectors-lab | verdikta-hunter | carry-forward |
| Svector-anu/svectors-lab | hunter-22 | carry-forward |
| Svector-anu/svectors-lab | picks-tracker | carry-forward |
| freezerboi/aeon | picks-tracker | carry-forward |
| freezerboi/aeon | thread-writer | NEW (moved from Marr554, now in freezerboi) |
| bspacer/aeon | robinhood-mcp | carry-forward |
| bspacer/aeon | you-web-search | carry-forward |
| bspacer/aeon | aeon-doctor | carry-forward |
| bspacer/aeon | seo-audit | carry-forward |
| chxoky/aeon | trader-memory-compact | carry-forward |
| Da6hkin/aeon | money-radar | carry-forward |
| Da6hkin/aeon | lead-finder | **NEW** |
| enuno/noesis-aeon | okf-export | carry-forward |
| enuno/noesis-aeon | memory-flush | carry-forward |
| enuno/noesis-aeon | idea-forge | **NEW** |
| damo-nu11/aeon-minebean | mine-bean | carry-forward |
| lawbworld-tech/aeon | lawb-pool-monitor | carry-forward |
| ether-btc/aeon | github-upstream-tracker | carry-forward |
| olanotolu/aeon | robinhood-mcp | NEW (olanotolu; bspacer carried it last week) |
| olanotolu/aeon | glim-mcp | **NEW** |
| olanotolu/aeon | finance-district-mcp | **NEW** |

(Forks not in this table may have fork-only skills in their `skills/` tree not captured by this run's targeted sampling. Full recursive tree scan would surface additional entries.)

## Week-over-week

- **FADED from EMERGING**: github-monitor — was 26.3% (5/19) last week, now 22% (4/18 confirmed). Likely sampling artifact; absolute count may be stable.
- **NEW_FORK_ONLY**: Da6hkin/lead-finder, enuno/idea-forge, olanotolu/robinhood-mcp, olanotolu/glim-mcp, olanotolu/finance-district-mcp, freezerboi/thread-writer
- **NEW_HEAVY_CUSTOMIZER**: olanotolu/aeon enters top 5 (not in last week's fingerprints)
- **Fleet growth**: 59 → 71 active forks (+12 in the 30-day window). Conversion rate roughly flat.
- **DROPPED from active window**: Aluma/aeon, Marr554/aeon (no push in last 30 days — their fork-only skills vch-program, vch-plan-review, priority-brief, thread-writer rolled off).

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 18 (verified lower bound) | ~25% |
| Template (untouched or minimal) | ~50 (estimated) | ~70% |
| Unreadable / unverified | ~3 | ~4% |
| **Total active** | 71 | 100% |

## Source status

- Active forks checked (targeted sample): ~25 / 71
- aeon.yml readable in sample: 25/25
- YAML parse failures: 0
- Rate-limited: 0
- Fork-only skills inspected (directly confirmed): 24 across 11 forks
- Full recursive tree scan: NOT run this cycle (would require ~71 API calls; targeted sampling used instead)

## Appendix — full divergence table

(Skills with at least one non-zero confirmed signal, sorted by override count desc.)

| Skill | enable_diff | var_overrides | model_overrides | schedule_overrides |
|-------|-------------|---------------|-----------------|-------------------|
| heartbeat | 0 | 0 | 0 | 5 (→ "0 8 * * *") |
| daily-routine | 1 (chxoky ↓) | 0 | 0 | 0 |
| github-trending | 1 (chxoky ↓) | 0 | 0 | 0 |
| on-chain-monitor | 1 (chxoky ↓) | 0 | 0 | 0 |
| defi-monitor | 1 (chxoky ↓) | 0 | 0 | 0 |
| defi-overview | 1 (chxoky ↓) | 0 | 0 | 0 |
| token-pick | 1 (chxoky ↓) | 0 | 0 | 0 |
| unlock-monitor | 1 (chxoky ↓) | 0 | 0 | 0 |
| aixbt-pulse | 1 (chxoky ↓) | 0 | 0 | 0 |
| search-skill | 1 (chxoky ↓) | 0 | 0 | 0 |
| security-digest | 1 (chxoky ↓) | 0 | 0 | 0 |
| deal-flow | 1 (chxoky ↓) | 0 | 0 | 0 |
| reg-monitor | 1 (chxoky ↓) | 0 | 0 | 0 |
| skill-security-scan | 1 (chxoky ↓) | 0 | 0 | 0 |
| vuln-scanner | 1 (chxoky ↓) | 0 | 0 | 0 |
| list-digest | 1 (chxoky ↓) | 0 | 0 | 0 |
| agent-buzz | 1 (chxoky ↓) | 0 | 0 | 0 |
| goal-tracker | 1 (chxoky ↓) | 0 | 0 | 0 |
| skill-analytics | 1 (chxoky ↓) | 0 | 0 | 0 |
| self-improve | 1 (chxoky ↓) | 0 | 0 | 0 |
| reflect | 1 (chxoky ↓) | 0 | 0 | 0 |
| action-converter | 1 (chxoky ↓) | 0 | 0 | 0 |
| evening-recap | 1 (chxoky ↓) | 0 | 0 | 0 |
| cost-report | 1 (chxoky ↓) | 0 | 0 | 0 |
| fork-cohort | 1 (chxoky ↓) | 0 | 0 | 0 |
| skill-evals | 1 (chxoky ↓) | 0 | 0 | 0 |
| skill-update-check | 1 (chxoky ↓) | 0 | 0 | 0 |
| weekly-review | 1 (chxoky ↓) | 0 | 0 | 0 |
| weekly-shiplog | 1 (chxoky ↓) | 0 | 0 | 0 |
| operator-scorecard | 1 (chxoky ↓) | 0 | 0 | 0 |
| fork-skill-digest | 1 (chxoky ↓) | 0 | 0 | 0 |
| fork-skill-gap | 1 (chxoky ↓) | 0 | 0 | 0 |
| skill-graph | 1 (chxoky ↓) | 0 | 0 | 0 |
| skill-freshness | 1 (chxoky ↓) | 0 | 0 | 0 |
| thought-review | 1 (chxoky ↓) | 0 | 0 | 0 |
| digest | 3 (↑ Svector-anu, bspacer, olanotolu) | 0 | 0 | 0 |
| github-monitor | 4 (↑ olanotolu, bspacer, belikh, enuno) | 0 | 0 | 0 |
| paper-digest | 1 (Da6hkin ↑) | 0 | 1 | 0 |
| monitor-kalshi | 1 (Da6hkin ↑) | 0 | 1 | 0 |
| vibecoding-digest | 1 (Da6hkin ↑) | 0 | 1 | 0 |
| narrative-tracker | 0 | 0 | 0 | 1 (Svector-anu → every 6h) |
| defi-overview (Svector) | 0 | 0 | 0 | 1 (Svector-anu → every 6h) |

*+ 30 more single-signal rows (all chxoky DISABLE_DOWNWARD on low-signal individual upstream skills)*

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
