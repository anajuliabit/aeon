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
| #8 | 2026-05-22 | (OPEN) surface real dry-run/write error in postprocess Execution Results — addresses ISS-003 |

## Recurring blockers
- **Soul files empty.** `soul/` files are still unpopulated templates. Every content
  skill (write-tweet, article, digest, etc.) runs in neutral voice. Flagged by
  morning-brief and multiple write-tweet runs. Persistent — needs operator content.
- **Sandbox network limits.** Two confirmed classes:
  - Reddit blocks the GitHub Actions datacenter IP — curl returns "Blocked" HTML and
    WebFetch rejects both old/www.reddit.com. last30 runs degrade without Reddit.
  - X.AI authed curl is blocked (env-var expansion / approval gate). Fix is the
    per-skill prefetch pattern in `scripts/prefetch-xai.sh` (one `case` per skill).
- **Reppo on-chain writes.** Chain is active (datanet 9, TradingGym AI) and mints/votes
  are queued correctly, but postprocess dry-runs fail with `code: UNKNOWN` — see ISS-003.

## Skill health
- Only `search-skill` has a skill-health record so far (score 4/5, 1 run, no flags).
- Not enough history for trend analysis. Re-assess once 3+ skills have multiple records.

## Issues
- ISS-001 resolved (PR #3). ISS-002 resolved (PR #4, chain verified running 2026-05-22).
- ISS-003 open — reppo postprocess dry-run `code: UNKNOWN`; PR #8 open to address it.
