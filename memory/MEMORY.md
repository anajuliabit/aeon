# Long-term Memory
*Last consolidated: 2026-05-24*

## About This Repo
Aeon — autonomous agent running on GitHub Actions via Claude Code. ~21 skills
enabled on cron; inbound messaging via Telegram (live). Fleet exited bootstrap
2026-05-21.

## Current Goals
- Unblock reppo-swarm on-chain output — three operator/config actions outstanding:
  ISS-004 (subnet grant — PR #10 merged 2026-05-25 adds auto-grant helper, awaits
  on-chain verification), ISS-005 (per-pod epoch validity in prefetch + agent
  filter — agent-side workaround already live), ISS-006 (lock REPPO for voting
  power — PR #11 merged 2026-05-25 adds lock helper, awaits on-chain verification).
- Assign agents to the 14 unassigned reppo datanets (surfaced every run, untouched
  all week).

## Completed Goals
- Populate `soul/` so content skills stop running in neutral voice — completed
  2026-05-25 (PR #12 populated `soul/SOUL.md` 74L + `soul/STYLE.md` 96L from
  `~/code/social`).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, recurring blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, token signals.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — last30 baseline.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail.

## Open Issues
- ISS-004 (high, config) — reppo mint dry-run reverts PUBLISHER_LACKS_SUBNET_ACCESS;
  needs operator `reppo grant-access --subnet <id>` for datanet 9's subnet.
- ISS-005 (high, prompt-bug) — vote pods fail POD_NOT_VALID_FOR_EPOCH; needs
  prefetch to record per-pod epoch validity + agent prompt to filter. Agent-side
  workaround in place (skip pods at validityEpoch ≤ current-1) — durable fix still pending.
- ISS-006 (high, config) — vote dry-runs revert INSUFFICIENT_VOTING_POWER;
  publisher has 0 locked REPPO. Needs operator `reppo lock <amount> --duration <secs>`.

## Open PRs
- PR #9 — self-improve tightening of token-alert step 2 (volume-spike sample-size
  rule, threshold-cross config). Opened 2026-05-23, awaiting merge.

## Lessons Learned
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use the prefetch pattern.
- Always save files AND commit before logging.
- Reppo ledger rows are for on-chain-confirmed actions only — a queued intent is not a mint.
- Soul files empty → all content skills use neutral voice (known gap, not a per-run bug).
- "code: UNKNOWN" was a wrapping bug in postprocess-reppo.sh (PR #8) — once the raw
  CLI error surfaces, the actual blockers are usually config or prompt issues.
- Reppo on-chain blockers cascade: ISS-002 → ISS-003 → ISS-004/005 → ISS-006. Each
  fix reveals the next one. Assume more remain even after ISS-004/005/006 close.
- skill-evals's evals.json carries wrong `output_pattern` entries for skills that
  write to `memory/logs/` (token-alert, skill-health) or have no skills/ directory
  (hn-digest, polymarket) — see today's action queue.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-24 | skill-evals bootstrap baseline | meta / fleet health |
| 2026-05-24 | skill-freshness audit | meta / fleet health |
| 2026-05-23 | skill-freshness audit | meta / fleet health |
| 2026-05-22 | skill-freshness audit | meta / fleet health |
| 2026-05-21 | The 100x Fix: Neuro-Symbolic AI & the AI Energy Crisis | AI / energy efficiency |
| 2026-05-21 | competitor-launch-radar | competitive intel |
| 2026-05-21 | last30 — bitcoin (30d) | crypto |
