# Fork Skill Digest — 2026-06-14

**Verdict:** 117 forks disable search-skill (upstream defaults on) — fleet is voting it as noise

*Scanned 124 active forks of aaronjmars/aeon (pushed in last 30 days). 123 are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured 123.*

*Context: this instance's aeon.yml is the comparison baseline. aaronjmars/aeon has evolved since this instance forked from it — ~102 of the "fork-only" skills per fork are aaronjmars/aeon upstream additions not yet in this instance.*

---

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

41 skills. The fleet is running aaronjmars/aeon's conservative defaults, which have rolled back many skills this instance still enables. Signal is genuine: if 87–95% of active operators leave a skill off, the "enabled: true" default is working against them.

| Skill | Forks disabled | % of configured | Δ vs last week |
|-------|----------------|-----------------|----------------|
| search-skill | 117 | 95% | First snapshot |
| security-digest | 117 | 95% | First snapshot |
| action-converter | 117 | 95% | First snapshot |
| skill-evals | 117 | 95% | First snapshot |
| defi-overview | 116 | 94% | First snapshot |
| deal-flow | 116 | 94% | First snapshot |
| list-digest | 116 | 94% | First snapshot |
| goal-tracker | 116 | 94% | First snapshot |
| self-improve | 116 | 94% | First snapshot |
| reflect | 116 | 94% | First snapshot |
| fleet-control | 116 | 94% | First snapshot |
| github-trending | 115 | 93% | First snapshot |
| defi-monitor | 115 | 93% | First snapshot |
| unlock-monitor | 115 | 93% | First snapshot |
| reg-monitor | 115 | 93% | First snapshot |
| vuln-scanner | 115 | 93% | First snapshot |
| autoresearch | 115 | 93% | First snapshot |
| agent-buzz | 115 | 93% | First snapshot |
| skill-graph | 115 | 93% | First snapshot |
| token-alert | 113 | 92% | First snapshot |
| skill-analytics | 113 | 92% | First snapshot |
| cost-report | 113 | 92% | First snapshot |
| fork-cohort | 113 | 92% | First snapshot |
| operator-scorecard | 113 | 92% | First snapshot |
| skill-freshness | 113 | 92% | First snapshot |
| token-pick | 112 | 91% | First snapshot |
| skill-health | 112 | 91% | First snapshot |
| token-movers | 110 | 89% | First snapshot |
| aixbt-pulse | 108 | 88% | First snapshot |
| skill-security-scan | 108 | 88% | First snapshot |
| skill-update-check | 108 | 88% | First snapshot |
| daily-routine | 107 | 87% | First snapshot |
| narrative-tracker | 107 | 87% | First snapshot |
| weekly-review | 107 | 87% | First snapshot |
| weekly-shiplog | 107 | 87% | First snapshot |
| fork-skill-digest | 107 | 87% | First snapshot |
| on-chain-monitor | 105 | 85% | First snapshot |
| evening-recap | 105 | 85% | First snapshot |
| morning-brief | 102 | 83% | First snapshot |
| market-context-refresh | 102 | 83% | First snapshot |
| fork-skill-gap | 93 | 76% | First snapshot |

---

## Fleet consensus on alternative settings

### Model overrides

- **competitor-launch-radar** — 78 forks → `claude-sonnet-4-6` (63% of configured). Upstream has no model override (inherits default). Fleet consensus: add `model: "claude-sonnet-4-6"` to this skill.

### Var hotspots

None this week.

### Schedule overrides

| Skill | Forks | Common schedule | Note |
|-------|-------|-----------------|------|
| token-movers | 119 | `0 12 * * *` | Upstream: `10 12 * * *` (staggered) |
| defi-monitor | 119 | `0 12 * * *` | Upstream: `40 12 * * *` (staggered) |
| on-chain-monitor | 111 | `0 12 * * *` | Upstream: `20 12 * * *` (staggered) |

119/123 configured forks removed the stagger offsets and collapsed all three crypto monitoring skills to `0 12 * * *`. The stagger exists to avoid cluster congestion — but 97% of the fleet ignores it. Worth revisiting whether the stagger is load-bearing or just noise.

---

## Watchlist (emerging — 25–49% adoption)

None this week.

---

## Heaviest customizers (top 5)

*Note: all top customizers show totalOverrides=134, dominated by 102 fork-only skills from aaronjmars/aeon's newer upstream config. The fingerprints reflect aaronjmars/aeon template adoption, not unique operator choices.*

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| modelcollapse/aeon | 134 | fork-only | 102 aaronjmars/aeon upstream skills + 30 enable-diff + custom: liquidpad-launch, rug-scan, investigation-report |
| ghostx-dev/aeon | 134 | fork-only | Same cluster as modelcollapse — identical override profile |
| sinfronterasai/aeon | 134 | fork-only | Same cluster — sinfronteras = "without borders" crypto focus |
| gitlumen-team/aeon | 134 | fork-only | Same cluster |
| ashneil12/aeon-upstream | 134 | fork-only | Same cluster |

---

## Fork-only skills

**157 unique skill names** across 3,494 (fork, skill) pairs. Heavy concentration: ~34 forks each carry aaronjmars/aeon's 102 newer skills not yet in this instance.

Notable genuinely custom skill clusters found across specific forks:

**Security / DeFi analysis**
- `rug-scan`, `contract-audit`, `wallet-risk`, `wallet-risk-audit`, `wallet-risk-weekly`
- `holder-concentration`, `approval-audit`, `lp-lock`, `lp-lock-check`, `honeypot-check`
- `fund-flow`, `linked-wallets`, `deployer-trace`, `tx-explain`

**Prediction market tooling**
- `polymarket-thesis`, `polymarket-edge`, `polymarket-contrarian`, `polymarket-alpha-comments`, `pm-pulse`, `pm-intel`, `pm-manipulation`
- `prediction-journal`, `narrative-vs-markets`, `polymarket`

**Content / social automation**
- `article-queue`, `content-performance`, `thread-writer`, `soul-builder`
- `tweet-digest`, `mention-radar`

**Fleet / system ops**
- `fork-health`, `fork-health-score`, `skill-gap`, `skill-adoption`, `fleet-skill-adoption`
- `batch-health`, `frequency-guard`, `config-validator`, `janitor`, `memory-flush`, `memory-dedupe`
- `self-review`, `signal-verdict`, `skill-enabler`, `api-health-probe`

**Research / intelligence**
- `narrative-convergence`, `topic-momentum`, `fear-divergence-scout`
- `builder-map`, `launch-radar`, `ecosystem-entrants`, `ecosystem-pulse`

**Instance-specific**
- `atlas`, `atlas-layers`, `atlas-improve` (swarm-ai-research/aeon-atlas)
- `mine-bean`, `powerloom-bds` (damo-nu11/aeon-minebean)
- `liquidpad-launch` (liquidpadbot cluster)
- `lawb-pool-monitor` (gitlawbounty/aeon)

---

## Week-over-week

First divergence snapshot — no comparison available.

---

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 123 | 99% |
| Template (untouched aeon.yml) | 0 | 0% |
| Unreadable | 1 | 1% |
| **Total active** | 124 | 100% |

---

## Source status

- Trees fetched: 124 / 124
- aeon.yml readable: 123 / 124
- YAML parse failures: 0
- Rate-limited: 0
- Fork-only skills inspected: 157 unique skill names across 3,494 (fork, skill) pairs

---

## Appendix — full divergence table

Skills with at least one non-zero divergence signal, sorted by total override count desc. Columns: enable_diff (negative = forks disable it; positive = forks enable it), var_overrides, model_overrides, schedule_overrides.

| Skill | enable_diff | var_overrides | model_overrides | schedule_overrides | total |
|-------|-------------|---------------|-----------------|-------------------|-------|
| defi-monitor | -115 | 1 | 0 | 119 | 235 |
| token-movers | -110 | 2 | 1 | 119 | 232 |
| on-chain-monitor | -105 | 2 | 1 | 111 | 219 |
| defi-overview | -116 | 1 | 0 | 1 | 118 |
| list-digest | -116 | 1 | 0 | 1 | 118 |
| agent-buzz | -115 | 1 | 0 | 2 | 118 |
| self-improve | -116 | 0 | 0 | 2 | 118 |
| reflect | -116 | 0 | 0 | 2 | 118 |
| search-skill | -117 | 0 | 0 | 0 | 117 |
| security-digest | -117 | 0 | 0 | 0 | 117 |
| action-converter | -117 | 0 | 0 | 0 | 117 |
| skill-evals | -117 | 0 | 0 | 0 | 117 |
| goal-tracker | -116 | 0 | 0 | 1 | 117 |
| deal-flow | -116 | 0 | 0 | 0 | 116 |
| fleet-control | -116 | 0 | 0 | 0 | 116 |
| github-trending | -115 | 0 | 0 | 0 | 115 |
| unlock-monitor | -115 | 0 | 0 | 0 | 115 |
| reg-monitor | -115 | 0 | 0 | 0 | 115 |
| vuln-scanner | -115 | 0 | 0 | 0 | 115 |
| autoresearch | -115 | 0 | 0 | 0 | 115 |
| skill-graph | -115 | 0 | 0 | 0 | 115 |
| token-alert | -113 | 0 | 0 | 0 | 113 |
| skill-analytics | -113 | 0 | 0 | 0 | 113 |
| cost-report | -113 | 0 | 0 | 0 | 113 |
| fork-cohort | -113 | 0 | 0 | 0 | 113 |
| operator-scorecard | -113 | 0 | 0 | 0 | 113 |
| skill-freshness | -113 | 0 | 0 | 0 | 113 |
| token-pick | -112 | 0 | 0 | 0 | 112 |
| skill-health | -112 | 0 | 0 | 0 | 112 |
| competitor-launch-radar | 0 | 0 | 78 | 0 | 78 |

+ 11 more skills with low-signal divergence (token-movers model, on-chain-monitor model, heartbeat schedule, skill-health schedule, etc.)

---

*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from this instance's defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. First run — no prior snapshot for week-over-week comparison. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
