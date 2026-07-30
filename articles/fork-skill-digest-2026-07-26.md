# Fork Skill Digest — 2026-07-26

**Verdict:** 77 forks disable action-converter, search-skill, security-digest (upstream defaults on) — fleet voting as noise. 27 skills show 50%+ disable-downward alignment, indicating upstream is enabling too much.

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

**Key insight:** The massive fleet-wide disable-downward signal (27 skills at 50%+) suggests upstream defaults have drifted toward enabling skills that the configured fleet actively turns off. This is the inverse of typical adoption patterns — fleet consensus is to reduce noise, not add capability. Consider auditing upstream `enabled: true` defaults; the fleet has already voted these skills as noise.

## Fleet consensus on alternative settings

### Model overrides

- **smithery-manifest** — 34 forks prefer `claude-sonnet-4-6` (44% of configured)

### Var hotspots

None this week.

### Schedule overrides

Observed in 76+ forks across multiple skills, but no single alternative schedule achieved consensus (>40% adoption).

## Watchlist (emerging — 25–49% adoption)

None this week.

## Heaviest customizers (top 5)

| Fork | Total overrides | Dominant category | Notes |
|------|-----------------|-------------------|-------|
| SahilParikh03/aeon | 176 | meta | schedule-heavy customizer (117 schedule overrides) |
| mnemedb/aeon | 174 | meta | meta-heavy, 40 enabled/disabled changes |
| NASTYZUNI/aeon | 174 | meta | mirrors mnemedb pattern |
| dannysrod/aeon | 174 | meta | meta-heavy, 40 enabled/disabled changes |
| daxaur/aeon | 174 | meta | meta-heavy, 40 enabled/disabled changes |

**Dominant pattern:** Top customizers are all meta-category focused, with heavy schedule overrides (>110 each) and minimal enabled divergence (~40). Suggests they're tuning skill cadence/timing, not capability selection.

## Fork-only skills

None this week — no forks are shipping custom skills outside upstream.

## Week-over-week

**Comparison to 2026-07-19:** 
- Active forks: 79 (was 61, +18 new pushes within 30-day window)
- Configured: 78 (was 58, +20 upgraded from template/unreadable status)
- DEFAULT_FLIP_DISABLE count unchanged — same 27 skills at 50%+ disable-downward
- Heaviest customizers unchanged — same top 5 forks dominating the override counts

**Status:** Fleet behavior durable week-over-week; no new flip signals, no emerging patterns breaking 25% adoption threshold.

## Fleet composition

| Tier | Count | % |
|------|-------|---|
| Configured | 78 | 99% |
| Template (untouched aeon.yml) | 0 | 0% |
| Unreadable | 1 | 1% |
| **Total active** | 79 | 100% |

## Source status

- Trees fetched: 79 / 79
- aeon.yml readable: 78 / 79
- YAML parse failures: 0
- Rate-limited: 0
- Fork-only skills inspected: 0

## Appendix — full divergence table (top 30 by signal magnitude)

| Skill | Direction | Enabled diff | Var overrides | Model overrides | Schedule overrides | Total |
|-------|-----------|--------------|----------------|-----------------|-------------------|-------|
| token-movers | DISABLE_DOWNWARD | 72 | 0 | 0 | 78 | 156 |
| changelog | ENABLE_UPWARD | 0 | 0 | 0 | 77 | 154 |
| code-health | ENABLE_UPWARD | 0 | 0 | 0 | 77 | 154 |
| digest | ENABLE_UPWARD | 0 | 0 | 0 | 77 | 154 |
| refresh-x | ENABLE_UPWARD | 2 | 1 | 1 | 75 | 152 |
| fleet-control | ENABLE_UPWARD | 0 | 0 | 0 | 76 | 152 |
| fork-fleet | ENABLE_UPWARD | 0 | 0 | 0 | 76 | 152 |
| skill-evals | DISABLE_DOWNWARD | 75 | 0 | 0 | 76 | 152 |
| idea-capture | ENABLE_UPWARD | 0 | 0 | 0 | 75 | 150 |
| research-brief | ENABLE_UPWARD | 2 | 0 | 0 | 75 | 150 |
| external-feature | ENABLE_UPWARD | 1 | 0 | 0 | 74 | 148 |
| project-lens | ENABLE_UPWARD | 0 | 0 | 0 | 74 | 148 |
| push-recap | ENABLE_UPWARD | 1 | 0 | 0 | 73 | 146 |
| repo-actions | ENABLE_UPWARD | 0 | 0 | 0 | 72 | 144 |
| repo-article | ENABLE_UPWARD | 0 | 0 | 0 | 72 | 144 |
| repo-pulse | ENABLE_UPWARD | 0 | 0 | 0 | 72 | 144 |
| article | ENABLE_UPWARD | 0 | 0 | 0 | 70 | 140 |
| github-monitor | ENABLE_UPWARD | 0 | 0 | 0 | 70 | 140 |
| github-issues | ENABLE_UPWARD | 0 | 0 | 0 | 70 | 140 |
| issue-triage | ENABLE_UPWARD | 0 | 0 | 0 | 70 | 140 |

(27 skills total with 50%+ disable-downward alignment; schedule overrides dominate the tail, indicating fleet-wide tuning of skill cadence rather than capability disagreement.)

---

*Source: GitHub API — forks of aaronjmars/aeon. Methodology: a fork is "configured" if its aeon.yml diverges from upstream defaults on enabled, model, var, or schedule for any skill. Untouched templates are excluded from divergence math. Companion to skill-leaderboard (popularity) and fork-fleet (per-fork work).*
