# Long-term Memory
*Last consolidated: 2026-05-25*

## About This Repo
Aeon — autonomous agent running on GitHub Actions via Claude Code. ~21 skills
enabled on cron; inbound messaging via Telegram (live). Fleet exited bootstrap
2026-05-21.

## Current Goals
- Assign agents to the 14 unassigned reppo datanets (surfaced every run, untouched
  all week).

## Completed Goals
- Unblock reppo-swarm on-chain output — completed 2026-05-26. 1st mint
  (tx 0x77f1386fb6fe3209bbf1a380b2be64f1f1c2c557416c9c7c0d31486a7e48a61f) + 1st
  vote (tx 0x937d9f3cc006e805bd2ace1b110e71e29fa659052c12b88a8ce3079c5136a455)
  both landed on-chain today; ISS-004 / ISS-006 / ISS-008 all resolved by
  PRs #10 / #23 / #21. Originally tracked three operator/config actions:
  ISS-004 (subnet grant — PR #10 merged 2026-05-25 adds auto-grant helper, awaits
  on-chain verification), ISS-005 (per-pod epoch validity in prefetch + agent
  filter — agent-side workaround already live), ISS-006 (lock REPPO for voting
  power — PR #11 merged 2026-05-25 adds lock helper, awaits on-chain verification).
- Populate `soul/` so content skills stop running in neutral voice — completed
  2026-05-25 (PR #12 populated `soul/SOUL.md` 74L + `soul/STYLE.md` 96L from
  `~/code/social`).
- Unblock reppo-swarm on-chain output. Operator actions still outstanding:
  ISS-004 (subnet grant) and ISS-006 (lock REPPO for voting power). ISS-005
  agent-side workaround live; ISS-007 (RPC retry) has PR #13 in flight.
- Assign agents to the 14 unassigned reppo datanets (surfaced every run, untouched
  all week).
- Populate `soul/` so content skills (write-tweet, article, digest, etc.) stop
  running in neutral voice — PR #12 in flight.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, recurring blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, token signals.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — last30 baseline.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail.

## Open Issues
- ISS-004 (high, config) — reppo mint dry-run reverts PUBLISHER_LACKS_SUBNET_ACCESS;
  needs operator `reppo grant-access --subnet <id>` for datanet 9's subnet.
- ISS-005 (high, prompt-bug) — vote pods fail POD_NOT_VALID_FOR_EPOCH; agent-side
  workaround live (skip pods at validityEpoch ≤ current-1); durable prefetch +
  agent-prompt fix still pending.
- ISS-006 (high, config) — vote dry-runs revert INSUFFICIENT_VOTING_POWER;
  publisher has 0 locked REPPO. Needs operator `reppo lock <amount> --duration <secs>`.
- ISS-007 (medium, timeout) — vote dry-runs intermittently hit mainnet.base.org
  RPC `INTERNAL_ERROR`. 4 occurrences in 3 runs (rate climbing). PR #13 adds
  retry-with-backoff; severity will need a bump once ISS-006 clears and real
  writes can land.

## Open PRs
- PR #12 — populate soul/SOUL.md + STYLE.md from ~/code/social. Opened 2026-05-25 14:40.
- PR #13 — postprocess-reppo.sh retry-with-backoff on transient Base RPC failures
  (closes ISS-007). Opened 2026-05-25 14:49.

## Lessons Learned
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use the prefetch pattern.
- Always save files AND commit before logging.
- Reppo ledger rows are for on-chain-confirmed actions only — a queued intent is not a mint.
- Soul files empty → all content skills use neutral voice (known gap; tracked
  in PR #12, not a per-run bug).
- "code: UNKNOWN" was a wrapping bug in postprocess-reppo.sh (PR #8) — once the raw
  CLI error surfaces, the actual blockers are usually config or prompt issues.
- Reppo on-chain blockers cascade: ISS-002 → ISS-003 → ISS-004/005 → ISS-006 → ISS-007.
  Each fix reveals the next one. Assume more remain even after these close.
- skill-evals's evals.json carries wrong `output_pattern` entries for skills that
  write to `memory/logs/` (token-alert, skill-health) or have no skills/ directory
  (hn-digest, polymarket) — action queue from 2026-05-24 bootstrap.
- Cost profile is cache-dominated (73% of spend is cache read+write). The
  standard "model-downgrade" filter (output/input ratio) misses Sonnet-rotation
  savings for high-cache skills (defi-overview, heartbeat, reppo-digest combined
  = 38% of weekly spend on Opus). Operator-call territory, not auto-fix.
- Base public mainnet.base.org RPC flakes — Reppo CLI dry-runs need
  retry-with-backoff (PR #13) or an RPC override to a private endpoint.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-25 | cost-report (week 1) | meta / fleet health |
| 2026-05-25 | security-scan bootstrap | meta / fleet health |
| 2026-05-25 | skill-freshness audit | meta / fleet health |
| 2026-05-24 | skill-evals bootstrap baseline | meta / fleet health |
| 2026-05-24 | skill-freshness audit | meta / fleet health |
| 2026-05-23 | skill-freshness audit | meta / fleet health |
| 2026-05-21 | The 100x Fix: Neuro-Symbolic AI & the AI Energy Crisis | AI / energy efficiency |
| 2026-05-21 | competitor-launch-radar | competitive intel |
| 2026-05-21 | last30 — bitcoin (30d) | crypto |
