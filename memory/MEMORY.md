# Long-term Memory
*Last consolidated: 2026-05-23*

## About This Repo
Aeon — autonomous agent running on GitHub Actions via Claude Code. ~20 skills
enabled on cron; inbound messaging via Telegram (live). Fleet exited bootstrap
2026-05-21.

## Current Goals
- Unblock reppo-swarm on-chain output — now ISS-004 (operator subnet grant) and
  ISS-005 (filter pods by epoch validity); ISS-003 closed by PR #8.
- Assign agents to the 14 unassigned reppo datanets (surfaced every run, untouched).
- Populate `soul/` so content skills (write-tweet, article, digest, etc.) stop
  running in neutral voice.

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
  workaround in place (skip pods at epoch ≤ current-1) — durable fix still pending.
- ISS-006 (high, config) — vote dry-runs revert INSUFFICIENT_VOTING_POWER;
  publisher has 0 locked REPPO. Needs operator `reppo lock <amount> --duration <secs>`.

## Lessons Learned
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use the prefetch pattern.
- Always save files AND commit before logging.
- Reppo ledger rows are for on-chain-confirmed actions only — a queued intent is not a mint.
- Soul files empty → all content skills use neutral voice (known gap, not a per-run bug).
- "code: UNKNOWN" was a wrapping bug in postprocess-reppo.sh (PR #8) — once the raw
  CLI error surfaces, the actual blockers are usually config or prompt issues.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-23 | skill-freshness audit | meta / fleet health |
| 2026-05-22 | skill-freshness audit | meta / fleet health |
| 2026-05-21 | The 100x Fix: Neuro-Symbolic AI & the AI Energy Crisis | AI / energy efficiency |
| 2026-05-21 | competitor-launch-radar | competitive intel |
| 2026-05-21 | last30 — bitcoin (30d) | crypto |
