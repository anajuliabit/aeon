# Fork Skill Digest — 2026-08-09

**Verdict:** bspacer shipped robinhood-mcp, aeon-doctor, seo-audit, you-web-search — not in upstream

*Scanned 59 active forks of aaronjmars/aeon (pushed in last 30 days). 19 are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured 19.*

---

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

No skills crossed the 50% disable-downward threshold.

> **Context:** both buckets are empty because the configured fleet contracted sharply — 49 → 19 configured forks (98% → 32% of active). The 18-skill disable-downward cohort from last run required 49 configured forks to sustain majority counts; with 19, no skill reaches the 9-fork threshold. This is a fleet-composition event, not a defaults reversal. See Fleet Composition below.

---

## Fleet consensus on alternative settings

### Model overrides

None this week. Aluma/aeon runs gpt-terra/luna/sol aliases at scale, but those are non-standard model IDs not shared by any other fork — not counted as fleet consensus.

### Var hotspots

None this week. No skill had ≥6 configured forks sharing the same non-empty var value.

### Schedule overrides

None this week meeting the ≥2 shared-schedule threshold.

---

## Watchlist (emerging — 25–49% adoption)

| Skill | Forks enabled | % of configured | Notes |
|-------|---------------|-----------------|-------|
| github-monitor | 5 | 26.3% | Marr554, olanotolu, Aluma, madebyshun, bspacer — repo monitor (PRs/issues/releases). Upstream: `enabled: false`. |

`github-monitor` is building adoption as forks point it at their own repos (olanotolu → Concya/concya-platform, madebyshun → madebyshun/blue-agent). Not a signal to flip the upstream default yet — it requires a `var:` target repo to be useful, so the right move is documentation, not defaulting it on.

---

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| Aluma/aeon | ~39 | dev | 16 skills enabled, 11 per-skill model overrides (gpt-luna/terra/sol), 10 var overrides. Entire stack pointed at Aluma/vybose-context-hub. skill-repair runs on gpt-sol reactively. pr-review, vuln-scanner, feature run on claude-opus-4-8. Fork-only: vch-program, vch-plan-review. |
| bspacer/aeon | ~33 | dev | 25 enable divergences. Runs robinhood-mcp (portfolio + on-demand trades via Robinhood MCP), you-web-search (You.com API), aeon-doctor (static config linter), seo-audit (daily on-page + Core Web Vitals). Custom heartbeat: `45 4 * * *` with var "Fart". create-skill var="AI"; auto-workflow var="pump.fun". |
| nigelon11/aeon | ~13 | meta | Heartbeat-only runtime but explicitly disables 13+ upstream-on skills (narrative-tracker, vuln-scanner, skill-health, self-improve, reflect, cost-report, operator-scorecard, etc.). V4-format aeon.yml, model: claude-sonnet-4-6. Migrated from 25 overrides last week to stripped-down config. |
| olanotolu/aeon | ~13 | mixed | Enables 12 skills including pr-triage+pr-review+github-monitor (all var: Concya/concya-platform), token-movers, defi-overview, investigation-report, monitor-polymarket. |
| Svector-anu/svectors-lab | ~12 | fork-only | fork-only: verdikta-hunter, hunter-22, picks-tracker. Also enables: price-alert, digest, auto-workflow, x402-monitor, fear-divergence. Two aggressive schedule overrides: defi-overview → `0 */6 * * *` (6× daily vs 1×), narrative-tracker → `30 */6 * * *`. |

---

## Fork-only skills

### New this run (not in prior snapshot)

| Fork | Skill | Notes |
|------|-------|-------|
| bspacer/aeon | robinhood-mcp | On-demand: portfolio report, orders, trade instruction via Robinhood MCP agent.robinhood.com |
| bspacer/aeon | you-web-search | High-quality web search via You.com API (YDC_API_KEY). On-demand. |
| bspacer/aeon | aeon-doctor | Weekly static config linter — unquoted schedules, dup keys, mode typos. Read-only. |
| bspacer/aeon | seo-audit | Daily on-page + technical SEO audit with Core Web Vitals (PAGESPEED_API_KEY). |
| chxoky/aeon | trader-memory-compact | Sunday 20:00 UTC — re-compact traders.md to bounded canonical format + regenerate baseline. Guards 200K-token Worker limit. |
| Da6hkin/aeon | money-radar | Twice daily 08:00 + 19:00 UTC — cross-stream synthesis of all skill outputs into ranked money-first ideas. |
| Marr554/aeon | thread-writer | On-demand — 5–10 tweet thread in operator voice from topic/URL or memory signal. |

### Carried from prior snapshot

| Fork | Skill |
|------|-------|
| swarm-ai-research/aeon-atlas | atlas, atlas-layers, atlas-improve |
| enuno/noesis-aeon | okf-export, memory-flush |
| Aluma/aeon | vch-program, vch-plan-review |
| Svector-anu/svectors-lab | verdikta-hunter, hunter-22, picks-tracker |
| freezerboi/aeon | hunter-22, picks-tracker |
| damo-nu11/aeon-minebean | mine-bean |
| lawbworld-tech/aeon | lawb-pool-monitor |
| ether-btc/aeon | github-upstream-tracker |
| Marr554/aeon | priority-brief |

---

## Week-over-week

**Fleet composition shift (critical):** configured forks collapsed 49 → 19 (98% → 32% conversion rate). This is not a defaults-reversal — the 18-skill disable-downward cohort from 2026-08-02 all FADED because the denominator (N_CONFIGURED) dropped below the floor needed for 50%+ majority.

| Change | Details |
|--------|---------|
| FADED (from DEFAULT_FLIP_DISABLE) | All 18 skills: action-converter, search-skill, self-improve, autoresearch, github-trending, skill-health, security-digest, token-pick, vuln-scanner, defi-overview, token-movers, narrative-tracker, unlock-monitor, reflect, deal-flow, list-digest, goal-tracker, agent-buzz |
| NEW_FORK_ONLY | robinhood-mcp (bspacer), you-web-search (bspacer), aeon-doctor (bspacer), seo-audit (bspacer), trader-memory-compact (chxoky), money-radar (Da6hkin), thread-writer (Marr554) |
| NEW_HEAVY_CUSTOMIZER | bspacer (new #2, wasn't in prior top 5) |
| DROPPED from fingerprint | stefrogovskyi/aeon (was #1, 30 overrides — pushed > 30 days ago, no longer active) |
| CONFIG_RESET | nigelon11/aeon (was #2, 25 overrides — now heartbeat-only, v4 format, all skills disabled) |

**Why 49 → 19 configured:** 9 net-new forks joined this week (+18% growth), but all are template-level (heartbeat only). The pre-existing configured forks either became inactive (pushed > 30 days) or reset. The conversion rate tells the real story: last week 98% of active forks diverged from defaults; this week 32%.

---

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 19 | 32% |
| Template (untouched or heartbeat-only) | 39 | 66% |
| Unreadable | 1 | 2% |
| **Total active** | **59** | **100%** |

---

## Source status

- Trees fetched: 59 / 59
- aeon.yml readable: 58 / 59 (mirkosalvato1-ctrl: 404)
- YAML parse failures: 0
- Rate-limited: 0
- Fork-only skills inspected: 7 new + 16 carried = 23 total

---

## Appendix — full divergence table

Skills with at least one non-zero signal across configured forks, sorted by total override count desc. Cap: 20 rows.

| Skill | Enable diff | Var overrides | Model overrides | Schedule overrides |
|-------|-------------|---------------|-----------------|-------------------|
| github-monitor | +5 (enabled) | 3 (olanotolu, Aluma, madebyshun with repo var) | 1 (Aluma: gpt-luna) | 0 |
| pr-review | +4 (enabled) | 2 (olanotolu, Aluma: repo var) | 2 (Aluma: gpt-luna/opus-4-8) | 0 |
| auto-merge | +3 (enabled) | 1 (Aluma: repo var) | 1 (Aluma: gpt-terra) | 0 |
| strategy-builder | +3 (enabled) | 1 (Aluma: full goal var) | 0 | 0 |
| monitor-polymarket | +3 (enabled) | 0 | 1 (Boodszw: sonnet-4-6) | 0 |
| soul-builder | +3 (enabled) | 1 (enuno: name+links) | 0 | 0 |
| deep-research | +3 (enabled) | 0 | 0 | 0 |
| narrative-tracker | -2 (disabled by nigelon11, freezerboi) | 1 (0xMal0u: custom var) | 2 (0xMal0u, Da6hkin: sonnet-4-6) | 1 (Svector-anu: */6h) |
| skill-health | -2 (disabled) / +5 (enabled by others) | 1 (Aluma: analytics:168) | 1 (Aluma: gpt-luna) | 0 |
| vuln-scanner | -2 (disabled) / +3 (enabled by others) | 2 (Aluma, Svector-anu: repo var) | 1 (Aluma: opus-4-8) | 0 |
| self-improve | -2 (disabled) / +3 (enabled by others) | 1 (Aluma: audit var) | 1 (Aluma: gpt-terra) | 0 |
| reflect | -2 (disabled) / +1 (enabled by others) | 0 | 1 (Da6hkin: sonnet-4-6) | 0 |
| pr-triage | +2 (enabled) | 2 (olanotolu, Aluma: repo var) | 1 (Aluma: gpt-luna) | 0 |
| defi-overview | 0 (mixed: some enable, same as upstream) | 0 | 1 (Da6hkin: sonnet-4-6) | 1 (Svector-anu: */6h) |
| skill-repair | +2 (enabled) | 0 | 1 (Aluma: gpt-sol) | 0 |
| unlock-monitor | -1 (disabled) | 0 | 1 (Da6hkin: sonnet-4-6) | 0 |
| operator-scorecard | -1 (disabled) | 1 (olanotolu: push var) | 0 | 0 |
| action-converter | -2 (disabled) | 0 | 0 | 0 |
| heartbeat | 0 | 1 (bspacer: "Fart") | 0 | 1 (bspacer: 45 4 * * *) |
| on-chain-monitor | 0 | 1 (0xMal0u: contract var) | 1 (0xMal0u: sonnet-4-6) | 1 (0xMal0u: */30 min) |

+ 12 more skills with low-signal divergence (single-fork model or var overrides only)

---

*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
