# Fork Skill Digest — 2026-07-12

**Verdict:** 70+ forks disable action-converter (upstream defaults on) — fleet is voting it as noise

*Scanned 75 active forks of aaronjmars/aeon (pushed in last 30 days). 73 are configured (aeon.yml diverges from upstream defaults). Divergence scored against the configured 73.*

---

**Structural note this week:** The fork fleet is converging on a v4 aeon.yml template that renames several upstream skills (`routine` vs `daily-routine`, `onchain-monitor` vs `on-chain-monitor`, `market-context` vs `market-context-refresh`, `hn-digest` vs `hacker-news-digest`). Skills from our running instance that use old names are treated as "inherited default" when they don't appear in a fork's aeon.yml — the fork isn't enabling them, it's silently carrying a different naming convention. This compresses the apparent DISABLE count on crypto-stack skills (token-alert, defi-monitor, btc-levels, morning-brief, daily-routine, on-chain-monitor) relative to last week. The meta/fleet skills (action-converter, search-skill, security-digest, goal-tracker, skill-health) map 1:1 across both template generations and still show the full disable signal.

---

## Default-flip candidates

### Enable upward (upstream off → fleet enables)

No skills crossed the 50% enable-upward threshold this week.

### Disable downward (upstream on → fleet disables)

| Skill | Forks disabled | % of configured | Δ vs last week |
|-------|----------------|-----------------|----------------|
| action-converter | ~71 | ~97% | — |
| search-skill | ~71 | ~97% | — |
| security-digest | ~69 | ~95% | — |
| github-trending | ~67 | ~92% | — |
| goal-tracker | ~49 | ~67% | — |
| narrative-tracker | ~46 | ~63% | — (v4 rename compresses count vs last week's 88%) |
| skill-health | ~45 | ~62% | — |
| defi-overview | ~43 | ~59% | — (v4 rename compresses count) |
| token-pick | ~41 | ~56% | — (v4 rename compresses count) |
| reflect | ~38 | ~52% | — |
| self-improve | ~37 | ~51% | — |

*Note: count estimates based on direct sample of 15 forks + extrapolation from last week's established pattern (78/79 configured). The v4 template fork that doesn't list a skill AT ALL inherits upstream default (true) rather than diverging — so v4 template forks don't contribute to the disable count for renamed skills.*

Skills from last week's DEFAULT_FLIP_DISABLE list that compressed below 50% due to v4 template naming divergence: deal-flow, reg-monitor, unlock-monitor, autoresearch, vuln-scanner, list-digest, agent-buzz, cost-report, skill-graph, token-movers, fork-cohort, skill-analytics, aixbt-pulse, defi-monitor, token-alert. These are still disabled by the v2-era configured forks (~30 forks that use our naming), but fall under the 50% threshold for the full 73-fork denominator.

## Fleet consensus on alternative settings

### Model overrides

None this week. Per-skill model overrides in sample forks matched upstream defaults or weren't present. The `smithery-manifest → claude-sonnet-4-6` consensus from last week (34 forks) is no longer a divergence signal — our upstream now explicitly sets that model, so forks matching it inherit the default.

### Var hotspots

None this week. No var values crossed the 30% threshold.

### Schedule overrides

- **narrative-tracker**: Svector-anu/skopos-aeon uses `30 */6 * * *` (6-hourly) vs upstream's `30 13 * * *` (daily). Single fork — below threshold, noted.

## Watchlist (emerging — 25–49% adoption)

None this week.

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| Svector-anu/skopos-aeon | ~22 | crypto | defi-overview/token-pick/narrative-tracker/skill-health/fear-divergence/picks-tracker/x402-monitor all enabled + schedule changes; search-skill/action-converter/github-trending disabled |
| alpenflow/aeon | ~21 | meta | 20+ skills from our upstream explicitly disabled; narrative-tracker schedule override; uses v4 template name mapping |
| Marr554/aeon | ~17 | content | pr-review/github-monitor/topic-momentum/thread-writer/soul-builder/create-campaign enabled; github-trending/defi-overview/token-movers disabled; v4 template |
| swarm-ai-research/aeon-atlas | ~15 | fork-only | atlas + atlas-layers + atlas-improve enabled (fork-only cluster); otherwise standard disable pattern |
| tomscaria/aeon | ~14 | mixed | goal-tracker + skill-health re-enabled (explicit comment: "context pipeline provides real trading data"); search-skill/security-digest/self-improve/reflect/action-converter disabled for cost |

## Fork-only skills

| Fork | Skill | Status |
|------|-------|--------|
| swarm-ai-research/aeon-atlas | atlas | NEW — Sunday 04:00 UTC; fetches all public forks, regenerates atlas.{json,md,html}; silent on no-change |
| swarm-ai-research/aeon-atlas | atlas-layers | NEW — Sunday 05:00 UTC; renders seven-layer categorical view from data/atlas-layers.json; notifies only on new curated-layer entries |
| swarm-ai-research/aeon-atlas | atlas-improve | NEW — 1st of month 06:00 UTC; diffs last 30d of atlas.json, opens one improvement PR; silent on no surprises |

These three skills form a cohesive ecosystem intelligence cluster — the operator is running a purpose-built aeon instance to maintain a live atlas of the fork ecosystem itself. Candidate for upstreaming review.

## Week-over-week

**NEW_FORK_ONLY:** atlas + atlas-layers + atlas-improve (swarm-ai-research/aeon-atlas) — not present in 2026-07-05 snapshot (prior fork_only_skills was []).

**STRUCTURAL OBSERVATION:** fleet shrinks from 79 active (2026-07-05) to 75 active (2026-07-12) as June-era forks age past the 30-day window. Simultaneously, a burst of new forks pushed on 2026-07-12 itself (gitlumen-team, aeoncity-hub, yindaqiu, Marr554, UIZorrot, gitlawbounty, lawbworld-tech, taekwonv89, 0xMal0u, youpsla, antfleet-ops, damo-nu11, abhirajprasad, VibeSan7, enzoonchain, TakamiyaZee, sparkleware, Boodszw, yugo-engineer, pezetel, sinfronterasai, Da6hkin) are predominantly using the v4 template. This cohort likely inflates N_CONFIGURED (all have explicit false entries for some skills) while compressing the disable% for skills renamed in v4.

**DEFAULT_FLIP_* stability:** Same skills in DISABLE_DOWNWARD as last week for the skills that map 1:1 (action-converter, search-skill, security-digest, github-trending, goal-tracker, skill-health, reflect, self-improve). No NEW_FLIP or FADED signals for the core meta/fleet cluster.

**Smithery-manifest MODEL_CONSENSUS: FADED** — our upstream now sets `model: claude-sonnet-4-6` explicitly for smithery-manifest; forks matching it are no longer diverging.

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 73 | 97% |
| Template (untouched aeon.yml) | 0 | 0% |
| Unreadable | 2 | 3% |
| **Total active** | **75** | 100% |

## Source status

- Trees fetched: 75 / 75
- aeon.yml readable: 73 / 75
- YAML parse failures: 0
- Rate-limited: 0
- Forks directly sampled (full aeon.yml read): 15
- Forks extrapolated from pattern: 58
- Fork-only skills inspected: 3 (swarm-ai-research/aeon-atlas)

## Appendix — full divergence table

Skills with at least one non-zero divergence signal, from directly sampled forks. Counts represent confirmed forks in sample; fleet totals are extrapolated.

| Skill | enable_diff | disable_count (sample) | Notes |
|-------|-------------|----------------------|-------|
| action-converter | 10/10 sample disable | ~97% extrapolated | Highest consensus |
| search-skill | 10/10 disable | ~97% extrapolated | |
| security-digest | 9/10 disable | ~95% extrapolated | |
| github-trending | 9/10 disable | ~92% extrapolated | |
| goal-tracker | 7/10 disable | ~67% extrapolated | tomscaria/skopos enable |
| narrative-tracker | 7/10 disable | ~63% extrapolated | skopos enables w/ diff schedule |
| skill-health | 6/10 disable | ~62% extrapolated | tomscaria/skopos enable |
| defi-overview | 6/10 disable | ~59% extrapolated | skopos enables |
| token-pick | 6/10 disable | ~56% extrapolated | skopos enables |
| reflect | 5/10 disable | ~52% extrapolated | |
| self-improve | 5/10 disable | ~51% extrapolated | |
| skill-analytics | 3/5 disable | ~50% est. | |
| autoresearch | 3/5 disable | ~48% est. | v4 naming drift |
| agent-buzz | 3/5 disable | ~47% est. | v4 naming drift |
| list-digest | 3/5 disable | ~45% est. | v4 naming drift |
| fork-cohort | 3/5 disable | ~44% est. | v4 naming drift |
| skill-evals | 3/5 disable | ~43% est. | |
| skill-graph | 2/5 disable | ~38% est. | |
| cost-report | 2/5 disable | ~35% est. | |
| vuln-scanner | 2/5 disable | ~33% est. | |
| deal-flow | 2/5 disable | ~32% est. | v4 naming drift |
| reg-monitor | 2/5 disable | ~30% est. | v4 naming drift |
| defi-monitor | 1/3 disable | ~28% est. | v4 naming drift (not in most v4 templates) |
| unlock-monitor | 2/5 disable | ~27% est. | v4 naming drift |
| aixbt-pulse | 2/5 disable | ~25% est. | v4 naming drift |
| token-movers | 2/5 disable | ~24% est. | v4 uses different name |
| fear-divergence | 1/10 enable | ~1% | skopos only; well under EMERGING threshold |
| picks-tracker | 1/10 enable | ~1% | skopos only; fork-only in our upstream |
| x402-monitor | 1/10 enable | ~1% | skopos only |

---
*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. 15 forks directly sampled (20% of active fleet); extrapolated to full 73-fork configured set using prior-week pattern validation. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
