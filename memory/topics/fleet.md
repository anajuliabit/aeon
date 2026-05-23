# Agent Fleet — Status & Infrastructure

The fleet exited bootstrap on 2026-05-21. ~20 skills are now enabled and running on
cron. This file tracks fleet-wide state: what was built, recurring blockers, and health.

## Infrastructure built (PRs)
| PR | Date | What |
|----|------|------|
| #1 | 2026-05-21 | Telegram webhook worker for instant inbound messaging |
| #2 | 2026-05-21 | Reppo agent swarm — orchestrator + trading agent vertical slice |
| #3 | 2026-05-21 | agent-buzz X.AI prefetch case + cache fallback (closed ISS-001) |
| #4 | 2026-05-21 | reppo-swarm activation — TradingGymAI datanet_id + integer-id support (closed ISS-002) |
| #5 | 2026-05-22 | chain-runner no longer aborts on a var-less first step |
| #6 | 2026-05-22 | reppo ledger reflects on-chain reality, not queued intent |
| #7 | 2026-05-22 | REPPO_PRIVATE_KEY wired into the post-process workflow step |
| #8 | 2026-05-23 | postprocess-reppo.sh surfaces raw CLI error instead of collapsing to `code: UNKNOWN` (merged; closed ISS-003) |

## Recurring blockers
- **Soul files empty.** `soul/` files are still unpopulated templates. Every content
  skill (write-tweet, article, digest, etc.) runs in neutral voice. Flagged by
  morning-brief and multiple write-tweet runs. Persistent — needs operator content.
- **Sandbox network limits.** Two confirmed classes:
  - Reddit blocks the GitHub Actions datacenter IP — curl returns "Blocked" HTML and
    WebFetch rejects both old/www.reddit.com. last30 runs degrade without Reddit.
  - X.AI authed curl is blocked (env-var expansion / approval gate). Fix is the
    per-skill prefetch pattern in `scripts/prefetch-xai.sh` (one `case` per skill).
- **Reppo on-chain writes (post-PR-#8).** With the `UNKNOWN` wrapper removed, two
  underlying blockers surfaced on 2026-05-23:
  - ISS-004 (config) — mint dry-run reverts PUBLISHER_LACKS_SUBNET_ACCESS; the
    publisher account behind `REPPO_PRIVATE_KEY` has no access to datanet 9's subnet.
    Needs an operator `reppo grant-access --subnet <id>`.
  - ISS-005 (prompt-bug) — vote dry-runs revert POD_NOT_VALID_FOR_EPOCH; the trading
    agent picks pods from cache without checking epoch validity. Fix is two-part:
    record per-pod epoch validity in prefetch, then filter in the agent prompt.
- **14 unassigned reppo datanets.** Orchestrator surfaces them every run; none
  have ever been picked up. No agent skill covers them.

## Skill health
- 2 skill-health records on disk: `search-skill` (4/5, 1 run, no flags) and
  `reppo-digest` (4/5, 1 run, no flags). Most enabled skills still NO DATA.
- 0 critical / 0 degraded / 0 flapping / 0 warning in the latest classification.
- Not enough history for trend analysis yet. Re-assess once 3+ skills have ≥3 records.

## Issues
- ISS-001 resolved (PR #3). ISS-002 resolved (PR #4). ISS-003 resolved (PR #8, merged 2026-05-23).
- ISS-004 open (high, config) — reppo mint dry-run PUBLISHER_LACKS_SUBNET_ACCESS.
- ISS-005 open (high, prompt-bug) — reppo vote dry-runs POD_NOT_VALID_FOR_EPOCH.
