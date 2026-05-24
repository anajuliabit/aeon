# Agent Fleet — Status & Infrastructure

The fleet exited bootstrap on 2026-05-21. ~21 skills are now enabled and running on
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
| #9 | 2026-05-23 | self-improve: tighten token-alert step 2 (volume-spike sample-size, threshold-cross config). **Open** as of 2026-05-24. |

## Recurring blockers
- **Soul files empty.** `soul/` files are still unpopulated templates. Every content
  skill (write-tweet, article, digest, etc.) runs in neutral voice. Flagged by
  morning-brief and multiple write-tweet runs. Persistent — needs operator content.
- **Sandbox network limits.** Two confirmed classes:
  - Reddit blocks the GitHub Actions datacenter IP — curl returns "Blocked" HTML and
    WebFetch rejects both old/www.reddit.com. last30 runs degrade without Reddit.
  - X.AI authed curl is blocked (env-var expansion / approval gate). Fix is the
    per-skill prefetch pattern in `scripts/prefetch-xai.sh` (one `case` per skill).
- **Reppo on-chain writes (cascading blockers).** With the `UNKNOWN` wrapper removed
  (PR #8), three concrete blockers surfaced in sequence:
  - ISS-004 (config) — mint dry-run reverts PUBLISHER_LACKS_SUBNET_ACCESS; the
    publisher account behind `REPPO_PRIVATE_KEY` has no access to datanet 9's subnet.
    Needs operator `reppo grant-access --subnet <id>`.
  - ISS-005 (prompt-bug) — vote dry-runs revert POD_NOT_VALID_FOR_EPOCH; the trading
    agent picks pods from cache without checking epoch validity. Fix is two-part:
    record per-pod epoch validity in prefetch, then filter in the agent prompt.
    **Agent-side workaround live** as of 2026-05-24 (filter pods at validityEpoch
    ≤ current-1); durable prefetch fix still pending.
  - ISS-006 (config, filed 2026-05-24) — vote dry-runs revert
    INSUFFICIENT_VOTING_POWER; publisher has 0 locked REPPO. Needs operator
    `reppo lock <amount> --duration <secs>`.
  - Pattern: each fix reveals the next blocker. Assume more remain even after these
    three close.
- **14 unassigned reppo datanets.** Orchestrator surfaces them every run; none
  have ever been picked up. No agent skill covers them.
- **skill-evals spec drift.** evals.json carries wrong `output_pattern` for
  token-alert / skill-health (both write to `memory/logs/` not `articles/`) and
  two orphaned entries (hn-digest, polymarket — no skills/ directory). Action
  queue from 2026-05-24 skill-evals run captures the patches.

## Skill health
- skill-health last classification (2026-05-23): 12 healthy, 0
  critical/degraded/flapping/warning, 9 no_data (skill-security-scan, autoresearch,
  skill-analytics, self-improve, cost-report, skill-evals, skill-update-check,
  operator-scorecard, weekly-review — all weekly/biweekly slots not yet hit, not
  scheduler gaps).
- 2 per-skill quality records on disk: `search-skill` (4/5) and `reppo-digest`
  (4/5). No flags. Too thin for trend analysis.
- `article` carries sr=0.5 in cron-state, but with only 2 runs — below the
  chronic-failure threshold (≥5). morning-brief, heartbeat, and skill-health all
  flag-and-skip it.
- skill-evals bootstrap baseline (2026-05-24): 12/29 coverage, 1 PASS, 1 STALE
  (expected — disabled `changelog`), 12 NO_OUTPUT (mix of disabled, weekly-not-yet-due,
  and the spec-drift entries above).

## Issues
- ISS-001 resolved (PR #3). ISS-002 resolved (PR #4). ISS-003 resolved (PR #8, merged 2026-05-23).
- ISS-004 open (high, config) — reppo mint dry-run PUBLISHER_LACKS_SUBNET_ACCESS.
- ISS-005 open (high, prompt-bug) — reppo vote dry-runs POD_NOT_VALID_FOR_EPOCH.
- ISS-006 open (high, config) — reppo vote dry-runs INSUFFICIENT_VOTING_POWER.
