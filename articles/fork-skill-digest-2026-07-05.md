# Fork Skill Digest — 2026-07-05

**Verdict:** 77 forks disable action-converter (upstream defaults on) — fleet is voting it as noise

*Scanned 79 active forks of aaronjmars/aeon (pushed in last 30 days). 78 are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured 78.*

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

| Skill | Forks disabled | % of configured | Δ vs last week |
|-------|----------------|-----------------|----------------|
| action-converter | 77 | 99% | — |
| search-skill | 77 | 99% | — |
| security-digest | 77 | 99% | — |
| deal-flow | 76 | 97% | — |
| defi-overview | 76 | 97% | — |
| goal-tracker | 76 | 97% | — |
| reflect | 76 | 97% | — |
| unlock-monitor | 76 | 97% | — |
| autoresearch | 75 | 96% | — |
| github-trending | 75 | 96% | — |
| reg-monitor | 75 | 96% | — |
| self-improve | 75 | 96% | — |
| skill-evals | 75 | 96% | — |
| vuln-scanner | 75 | 96% | — |
| list-digest | 74 | 95% | — |
| agent-buzz | 73 | 94% | — |
| cost-report | 73 | 94% | — |
| skill-graph | 73 | 94% | — |
| token-pick | 73 | 94% | — |
| skill-health | 72 | 92% | — |
| token-movers | 72 | 92% | — |
| fork-cohort | 71 | 91% | — |
| skill-analytics | 71 | 91% | — |
| narrative-tracker | 69 | 88% | — |
| aixbt-pulse | 68 | 87% | — |
| defi-monitor | 48 | 62% | — |
| token-alert | 44 | 56% | — |

The disable signal is overwhelming and consistent: 25 of 27 skills sit at 87–99%, meaning the fleet is near-unanimous in keeping these skills off. The two lowest (defi-monitor at 62%, token-alert at 56%) are still clear majorities. The pattern suggests these skills were enabled upstream as aspirational defaults that operators don't activate until they've completed their own configuration; for many this never happens.

## Fleet consensus on alternative settings

### Model overrides

- **smithery-manifest** — 34 forks (44% of configured) override to `claude-sonnet-4-6` (upstream default: none set). Recommend matching fleet model in upstream.

### Var hotspots

None this week.

### Schedule overrides

No schedule value shared by ≥2 configured forks for any upstream skill crossed the threshold this week.

*Note: Many top-fingerprint forks carry 100+ schedule_overrides, reflecting an older snapshot of aeon.yml with different schedule strings. These are stale-sync artifacts rather than deliberate customizations.*

## Watchlist (emerging — 25–49% adoption)

None this week. No upstream-disabled skill sits between 25–49% enable adoption.

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| SahilParikh03/aeon | 176 | meta | 35 enabled_diff · 24 model_overrides · 117 schedule_overrides — high schedule delta indicates older aeon.yml snapshot not yet synced |
| mnemedb/aeon | 174 | meta | 40 enabled_diff · 23 model_overrides · 111 schedule_overrides — same stale-sync signature |
| NASTYZUNI/aeon | 174 | meta | 40 enabled_diff · 23 model_overrides · 111 schedule_overrides |
| dannysrod/aeon | 174 | meta | 40 enabled_diff · 23 model_overrides · 111 schedule_overrides |
| daxaur/aeon | 174 | meta | 40 enabled_diff · 23 model_overrides · 111 schedule_overrides |

*All five lead forks show the same schedule-override signature (111–117 overrides each), pointing to a shared upstream snapshot from an earlier version of aeon.yml. The "meta" dominant category reflects these forks having the meta-skill cluster enabled (skill-health, goal-tracker, reflect, etc.) where most other forks have them disabled.*

## Fork-only skills

Tree calls were not executed this run due to API budget constraints. Fork-only skill detection is not available for this run. See prior snapshot (2026-06-21) for the last known fork-only skill list (33 skills across 8 forks: modelcollapse, tomscaria, ashneil12, gitlumen-team, zszkey, swarm-ai-research, damo-nu11, sparkleware, gitlawbounty, lawbworld-tech, chxoky, ether-btc, tomscaria).

## Week-over-week

*Prior snapshot: 2026-06-21 (14 days ago — at boundary of comparison window).*

**No new DEFAULT_FLIP signals** — all 27 disable-downward skills were present in the prior run.

**FADED from DEFAULT_FLIP_DISABLE** (16 skills dropped below 50% threshold in this active-fork window):
btc-levels · thought-review · fleet-control · skill-security-scan · skill-update-check · daily-routine · weekly-review · weekly-shiplog · fork-skill-digest · on-chain-monitor · evening-recap · morning-brief · market-context-refresh · fork-skill-gap · operator-scorecard · skill-freshness

These faded because the current 30-day window (79 forks) is a different cohort than June's 107-fork window — newer/recently-synced forks that haven't yet customized these skills contribute lower explicit-disable rates. The underlying signal (fleet disagrees with these defaults) likely persists in the broader fork population.

**MODEL_CONSENSUS shift:**
- NEW: `smithery-manifest → claude-sonnet-4-6` (34 forks, 44%)
- FADED: `competitor-launch-radar` dropped below MODEL_CONSENSUS threshold in this window

**NEW_HEAVY_CUSTOMIZER:** All five top fingerprint forks are new to the top-5 list (SahilParikh03, mnemedb, NASTYZUNI, dannysrod, daxaur). Prior top-5 (modelcollapse, tomscaria, ashneil12, gitlumen-team, zszkey) are not in the current 30-day active window.

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 78 | 99% |
| Template (untouched aeon.yml) | 0 | 0% |
| Unreadable | 1 | 1% |
| **Total active** | 79 | 100% |

The 0% template rate is notable — virtually every active fork has diverged from upstream defaults on at least one dimension. This is consistent with last run (3 templates of 107).

## Source status

- Trees fetched: 0 / 79 (not executed — aeon.yml fetched directly via contents API)
- aeon.yml readable: 78 / 79
- YAML parse failures: 0
- Rate-limited: 0
- Fork-only skills inspected: 0 (tree calls skipped)

## Appendix — full divergence table

*(Skills with at least one non-zero divergence signal, sorted by total override count desc. Top 30 shown; many rows are schedule-dominated.)*

| Skill | Direction | Enable diff | Var overrides | Model overrides | Schedule overrides |
|-------|-----------|-------------|---------------|-----------------|--------------------|
| deep-research | ENABLE_UPWARD | 4 | 1 | 1 | 77 |
| paper-pick | ENABLE_UPWARD | 1 | 1 | 1 | 77 |
| token-movers | DISABLE_DOWNWARD | 72 | 0 | 0 | 78 |
| changelog | ENABLE_UPWARD | 0 | 0 | 0 | 77 |
| code-health | ENABLE_UPWARD | 0 | 0 | 0 | 77 |
| digest | ENABLE_UPWARD | 0 | 0 | 0 | 77 |
| fetch-tweets | ENABLE_UPWARD | 1 | 0 | 0 | 77 |
| reply-maker | ENABLE_UPWARD | 1 | 0 | 0 | 77 |
| skill-repair | ENABLE_UPWARD | 1 | 0 | 0 | 77 |
| farcaster-digest | ENABLE_UPWARD | 0 | 1 | 0 | 76 |
| auto-workflow | ENABLE_UPWARD | 1 | 0 | 0 | 76 |
| create-skill | ENABLE_UPWARD | 1 | 0 | 0 | 76 |
| deploy-prototype | ENABLE_UPWARD | 1 | 0 | 0 | 76 |
| distribute-tokens | ENABLE_UPWARD | 2 | 0 | 0 | 76 |
| fleet-control | ENABLE_UPWARD | 0 | 0 | 0 | 76 |
| fork-fleet | ENABLE_UPWARD | 0 | 0 | 0 | 76 |
| last30 | ENABLE_UPWARD | 1 | 0 | 0 | 76 |
| refresh-x | ENABLE_UPWARD | 2 | 1 | 1 | 75 |
| skill-evals | DISABLE_DOWNWARD | 75 | 0 | 0 | 76 |
| spawn-instance | ENABLE_UPWARD | 1 | 0 | 0 | 76 |
| tool-builder | ENABLE_UPWARD | 1 | 0 | 0 | 76 |
| treasury-info | ENABLE_UPWARD | 1 | 0 | 0 | 76 |
| idea-capture | ENABLE_UPWARD | 0 | 0 | 0 | 75 |
| onboard | ENABLE_UPWARD | 1 | 0 | 0 | 75 |
| research-brief | ENABLE_UPWARD | 2 | 0 | 0 | 75 |
| star-milestone | ENABLE_UPWARD | 0 | 0 | 0 | 75 |
| channel-recap | ENABLE_UPWARD | 1 | 0 | 0 | 74 |
| external-feature | ENABLE_UPWARD | 1 | 0 | 0 | 74 |
| project-lens | ENABLE_UPWARD | 0 | 0 | 0 | 74 |
| push-recap | ENABLE_UPWARD | 0 | 0 | 0 | 74 |

*+ many more skills with schedule-override-only divergence (artifacts of stale fork snapshots).*

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
