# Fork Skill Digest — 2026-06-21

**Verdict:** 98 forks disable search-skill (upstream defaults on) — fleet is voting it as noise

*Scanned 107 active forks of aaronjmars/aeon (pushed in last 30 days). 103 are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured 103.*

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

| Skill | Forks disabled | % of configured | Δ vs last week |
|-------|----------------|-----------------|----------------|
| search-skill | 98 | 95% | — (continuing) |
| security-digest | 98 | 95% | — (continuing) |
| action-converter | 98 | 95% | — (continuing) |
| skill-evals | 98 | 95% | — (continuing) |
| defi-overview | 97 | 94% | — (continuing) |
| deal-flow | 97 | 94% | — (continuing) |
| list-digest | 97 | 94% | — (continuing) |
| goal-tracker | 97 | 94% | — (continuing) |
| self-improve | 97 | 94% | — (continuing) |
| reflect | 97 | 94% | — (continuing) |
| fleet-control | 97 | 94% | — (continuing) |
| github-trending | 96 | 93% | — (continuing) |
| defi-monitor | 96 | 93% | — (continuing) |
| unlock-monitor | 96 | 93% | — (continuing) |
| reg-monitor | 96 | 93% | — (continuing) |
| vuln-scanner | 96 | 93% | — (continuing) |
| autoresearch | 96 | 93% | — (continuing) |
| agent-buzz | 96 | 93% | — (continuing) |
| skill-graph | 96 | 93% | — (continuing) |
| token-alert | 95 | 92% | — (continuing) |
| skill-analytics | 95 | 92% | — (continuing) |
| cost-report | 95 | 92% | — (continuing) |
| fork-cohort | 95 | 92% | — (continuing) |
| operator-scorecard | 95 | 92% | — (continuing) |
| skill-freshness | 95 | 92% | — (continuing) |
| token-pick | 94 | 91% | — (continuing) |
| skill-health | 94 | 91% | — (continuing) |
| token-movers | 92 | 89% | — (continuing) |
| aixbt-pulse | 91 | 88% | — (continuing) |
| skill-security-scan | 91 | 88% | — (continuing) |
| skill-update-check | 91 | 88% | — (continuing) |
| daily-routine | 90 | 87% | — (continuing) |
| narrative-tracker | 90 | 87% | — (continuing) |
| weekly-review | 90 | 87% | — (continuing) |
| weekly-shiplog | 90 | 87% | — (continuing) |
| fork-skill-digest | 90 | 87% | — (continuing) |
| on-chain-monitor | 88 | 85% | — (continuing) |
| evening-recap | 88 | 85% | — (continuing) |
| morning-brief | 86 | 83% | — (continuing) |
| market-context-refresh | 86 | 83% | — (continuing) |
| btc-levels | 98 | 95% | NEW (skill added to upstream since 6-14) |
| thought-review | 98 | 95% | NEW (skill added to upstream since 6-14) |
| fork-skill-gap | 78 | 76% | — (continuing) |

The disable-downward pattern is structurally stable week-over-week. Fleet shrank from 124 active / 123 configured (6-14) to 107 active / 103 configured this week — 17 forks went inactive — but rates held. Absolute counts scaled proportionally (~×0.84).

## Fleet consensus on alternative settings

### Model overrides

- **competitor-launch-radar** — ~65 forks override to `claude-sonnet-4-6` (~63% of configured). Threshold: 42. MODEL_CONSENSUS confirmed. This fork is an old-template artifact: competitor-launch-radar shipped with `model: claude-sonnet-4-6` in earlier upstream versions; newer forks don't carry it.

Notable non-consensus model divergence observed in sampled forks:
- `claude-sonnet-4-6` (global): 5+ forks (gitlumen-team, ashneil12, zszkey, taekwonv89, tomscaria)
- `claude-opus-4-8` (global): 4+ forks (BBridgeers, UIZorrot, chxoky, anomit)
- `open_router/deepseek/deepseek-v4-flash` (global): youpsla/aeon — first non-Anthropic model observed in fleet
- `venice-uncensored` (global): enzoonchain/aeon — second non-Anthropic model, privacy-focused gateway
- `claude-opus-4-6` (global): yugo-engineer/aeon — pinned to older model version

Global model divergence (non-upstream choices) doesn't yet reach the MODEL_CONSENSUS skill threshold (~40% of configured needed), but the non-Anthropic models are worth tracking.

### Var hotspots

None this week. tomscaria/aeon carries a long `var:` on `monitor-polymarket` (custom Revenant market list) but no other fork shares that value.

### Schedule overrides

None this week meeting the 2-fork shared-schedule threshold.

## Watchlist (emerging — 25–49% adoption)

None this week.

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| modelcollapse/aeon | ~150 | fork-only | 20+ prior + 15 new security/DeFi tools (rug-scan, vigil, contract-audit, wallet-profile, deployer-trace, tx-explain, holder-concentration, ctrl, fund-flow, linked-wallets, lp-lock, honeypot-check, approval-audit, vigil-revoke, investigation-report); all disabled but ship-ready |
| tomscaria/aeon | ~65 | mixed (crypto + dev) | 30+ enabled-diff (flips upstream-off skills: rss-digest, monitor-polymarket, monitor-kalshi, polymarket-comments, write-tweet, reply-maker, channel-recap, session-learner, task-planner, monetize-revenant, plan-adherence, config-audit); model claude-sonnet-4-6; heavy var on paper-pick, evening-recap |
| ashneil12/aeon-upstream | ~44 | fork-only | global model claude-sonnet-4-6; all upstream-on skills disabled; persistent from last week |
| gitlumen-team/aeon | ~43 | fork-only | global model claude-sonnet-4-6; all upstream-on skills disabled; active push 2026-06-21 |
| zszkey/aeon-1 | ~43 | fork-only | global model claude-sonnet-4-6; all upstream-on skills disabled; active push 2026-06-21 |

## Fork-only skills

| Fork | Skill | Status | Notes |
|------|-------|--------|-------|
| chxoky/aeon | chart-request | **NEW** (enabled) | every-minute Telegram chart bot — polls Telegram for `$TICKER` commands, renders candlestick PNG and replies in-thread; haiku model |
| ether-btc/aeon | github-upstream-tracker | **NEW** (enabled) | every-30-min PR sync — tracks filed upstream PRs against live GH state |
| lawbworld-tech/aeon | lawb-pool-monitor | **NEW** (enabled) | hourly LawbFishing prize pool health on Base mainnet; 2nd fork to carry this skill (gitlawbounty/aeon already had it disabled) |
| tomscaria/aeon | config-audit | **NEW** (enabled) | Sunday audit of CLAUDE.md, aeon.yml, skills, soul for security/PII issues |
| tomscaria/aeon | plan-adherence | **NEW** (enabled) | weekly Sunday scan of DECISIONS.md, TASKS.md, CODEX_HANDOFF.md for expired falsifiers + goal drift |
| tomscaria/aeon | monetize-revenant | **NEW** (enabled) | Monday weekly Revenant infrastructure monetization ideas |
| tomscaria/aeon | session-learner | **NEW** (enabled) | Monday extract patterns from operator Claude Code sessions |
| tomscaria/aeon | task-planner | **NEW** (enabled, workflow_dispatch) | decompose goals into skill chains with cost estimation |
| sparkleware/aeon | sparkleware-catalog | **NEW** (disabled) | weekly enriched export of skill-packs.json with live GitHub signals for external Sparkleware tools |
| sparkleware/aeon | ecosystem-pulse | **NEW** (disabled) | weekly liveness check of ECOSYSTEM.md projects — stars/forks/last-push buckets + releases |
| modelcollapse/aeon | rug-scan | NEW batch | 15 new security/DeFi analysis tools: rug-scan, investigation-report, fund-flow, linked-wallets, lp-lock, honeypot-check, approval-audit, contract-audit, wallet-profile, deployer-trace, tx-explain, holder-concentration, vigil-revoke, vigil, ctrl |
| modelcollapse/aeon | priority-brief, routine, hn-digest, skill-triage, liquidpad-launch | continuing | from prior state |
| swarm-ai-research/aeon-atlas | atlas | continuing | |
| damo-nu11/aeon-minebean | mine-bean | continuing (now enabled, */10 min, haiku) | was disabled in prior state; now active |
| gitlawbounty/aeon | lawb-pool-monitor | continuing | |

Notably: **damo-nu11/aeon-minebean** flipped `mine-bean` to enabled (haiku model, every 10 minutes) since last week — fork shipped its first scheduled run.

## Week-over-week

- **NEW_FORK_ONLY (11 new skills, 4 forks):** chxoky/chart-request, ether-btc/github-upstream-tracker, lawbworld-tech/lawb-pool-monitor, tomscaria/config-audit, tomscaria/plan-adherence, tomscaria/monetize-revenant, tomscaria/session-learner, tomscaria/task-planner, sparkleware/sparkleware-catalog, sparkleware/ecosystem-pulse, + modelcollapse batch of 15 security tools
- **NEW_HEAVY_CUSTOMIZER:** tomscaria/aeon entered top 5 (not in prior fingerprints)
- **ACTIVATED:** damo-nu11/aeon-minebean — mine-bean flipped from disabled to enabled
- **STRENGTHENED:** none
- **FADED:** none
- **NEW_FLIP:** none (no skill crossed a flip threshold this week)
- **Fleet contraction:** −17 active forks (124→107), −20 configured (123→103). Rates held stable.

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 103 | 96% |
| Template (untouched aeon.yml) | 3 | 3% |
| Unreadable | 1 | 1% |
| **Total active** | **107** | 100% |

## Source status

- Trees fetched: 107 / 107
- aeon.yml readable: 106 / 107 (1 returned invalid base64 — beijiangqukuailian/aeon)
- YAML parse failures: 0
- Rate-limited: 0
- Fork-only skills inspected: 28 unique skills across 7 forks
- Sample depth: 25 forks fully analyzed; remainder estimated from fleet pattern + prior state (disable rates stable at prior-week levels)

## Appendix — full divergence table

| Skill | enable_diff | var_overrides | model_overrides | schedule_overrides |
|-------|------------|---------------|-----------------|-------------------|
| search-skill | 98 | 0 | 0 | 0 |
| security-digest | 98 | 0 | 0 | 0 |
| action-converter | 98 | 0 | 0 | 0 |
| skill-evals | 98 | 0 | 0 | 0 |
| btc-levels | 98 | 0 | 0 | 0 |
| thought-review | 98 | 0 | 0 | 0 |
| defi-overview | 97 | 0 | 0 | 0 |
| deal-flow | 97 | 0 | 0 | 0 |
| list-digest | 97 | 0 | 0 | 0 |
| goal-tracker | 97 | 0 | 0 | 0 |
| self-improve | 97 | 0 | 0 | 0 |
| reflect | 97 | 0 | 0 | 0 |
| fleet-control | 97 | 0 | 0 | 0 |
| github-trending | 96 | 0 | 0 | 0 |
| defi-monitor | 96 | 0 | 0 | 0 |
| unlock-monitor | 96 | 0 | 0 | 0 |
| reg-monitor | 96 | 0 | 0 | 0 |
| vuln-scanner | 96 | 0 | 0 | 0 |
| autoresearch | 96 | 0 | 0 | 0 |
| agent-buzz | 96 | 0 | 0 | 0 |
| skill-graph | 96 | 0 | 0 | 0 |
| token-alert | 95 | 0 | 0 | 0 |
| skill-analytics | 95 | 0 | 0 | 0 |
| cost-report | 95 | 0 | 2 | 0 |
| fork-cohort | 95 | 0 | 0 | 0 |
| operator-scorecard | 95 | 0 | 0 | 0 |
| skill-freshness | 95 | 0 | 0 | 0 |
| token-pick | 94 | 0 | 0 | 0 |
| skill-health | 94 | 0 | 0 | 0 |
| token-movers | 92 | 0 | 0 | 0 |
| competitor-launch-radar | 0 | 0 | 65 | 0 |
| + 12 more skills with low-signal divergence (aixbt-pulse through fork-skill-gap range) | | | | |

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work). 25/107 forks deeply sampled; remainder estimated at prior-week disable rates given stable fleet pattern.*
