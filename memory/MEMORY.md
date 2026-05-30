# Long-term Memory
*Last consolidated: 2026-05-30*

## About This Repo
Aeon — autonomous agent on GitHub Actions via Claude Code. 29 enabled skills
on cron; inbound messaging via Telegram (live). Fleet exited bootstrap
2026-05-21. soul/ populated 2026-05-25 (ana voice). Reppo-swarm first on-chain
output 2026-05-26. 2026-05-30 was the heaviest mint day (3 mints: 10th-12th
ever) and the first day Phase 2 (Pinata pin + platform metadata POST) ran
end-to-end clean — runs 4 + 5 both posted HTTP 200 with no Phase 2 reverts.

## Current Goals
- **ISS-009 codification.** 5th recurrence today (2nd run drift after 6
  consecutive chain runs holding the emit-in-assistant-text path). Still
  TODO: codify contract in `skills/reppo-orchestrator/SKILL.md` AND switch
  chain-runner fail-fast `continue` → `break` as defence-in-depth. Carried
  4+ days.
- **Assign 14 unassigned reppo datanets** (1, 2, 4, 5, 6, 7, 8, 10, 11, 13,
  14, 15, 16, 17). 10th day surfaced. PR #30 blocker lifted 2026-05-28;
  staging gated on operator pick of rubric.
- **INDEX bookkeeping** — close ISS-007 (PR #13/#26 merged), close ISS-010
  (PR #32 merged 2026-05-28T12:09Z). 5+ days queued.
- **ISS-015 mitigation.** vibecoding-digest Reddit blocked (3 consecutive
  days). Options: authed Reddit API (`REDDIT_CLIENT_ID/SECRET` →
  `oauth.reddit.com`), pushshift archive, or alternate source. Operator call.
- **Cleanup chain-runner scratch.** 4 stuck files at repo root from 4th-run
  trading-agent build steps (`.tmp-build-candidates.{py,js}`,
  `.tmp-build-dataset.js`, `.candidates.json`) — chain-irrelevant.

## Completed Goals
- **Phase 2 unblocked 2026-05-30.** ISS-012 (PR #44 Zod schema), ISS-013
  (PINATA_JWT rotation), ISS-014 (server self-healed) all resolved across
  4th + 5th chain runs — first end-to-end clean mints ever.
- **PR #30 — reppo-trading-agent rewrite (HL public data)** merged
  2026-05-28T12:05Z. Follow-ons #34 / #37 unlocked the 4th mint ever;
  5th-12th mints validated the path further.
- **Reppo on-chain blocker cascade cleared** — 2026-05-26 first mint + vote.
- **Populate `soul/`** — 2026-05-25 (PR #12).

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, signals.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail (12 mints, 24 votes).
- [Market context](topics/market-context.md) — refreshed by market-context-refresh.
- [TradingGymAI (datanet 9) contributor spec](topics/tradinggymai-spec.md) — operator-shared 2026-05-26.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — stale baseline (05-21).

## Open Issues
- **ISS-005** (high, prompt-bug) — vote POD_NOT_VALID_FOR_EPOCH; agent-side
  filter live, durable prefetch fix + CLI vote-dedup pending. PR #47 (vote
  dedup + subnetId UUID) was open this morning, merged before 14:00.
- **ISS-007** (medium, timeout) — PR #13/#26 shipped, INDEX close queued.
- **ISS-009** (high, prompt-bug) — 5 recurrences. Fix path validated 6+ runs
  before today's drift. Codify-in-SKILL + chain-runner `continue` → `break`
  remain.
- **ISS-010** (medium, config) — PR #32 shipped, INDEX close queued.
- **ISS-011** (medium, unknown) — vote nonce-too-low after sibling votes
  same batch. 1 occurrence; not recurring.
- **ISS-015** (high, sandbox-limitation, NEW 2026-05-30) — vibecoding can't
  reach Reddit (prefetch + WebFetch both dead, 3 consecutive days).

## Open PRs
- *(0 open as of 14:00 UTC — #47 merged this morning.)*

## Lessons Learned
- Reppo on-chain blockers cascade ISS-002 → ISS-003 → ISS-004/005 → ISS-006
  → ISS-007 → ISS-008 → ISS-009 → ISS-011/012/013/014. Each fix exposes the
  next layer. Phase 2 fully cleared 2026-05-30.
- Workflow-level guards only work if they actually abort the chain — bash
  `continue` in chain-runner's fail-fast branch silently skips to the next
  loop iter. Use `break` or `exit`.
- Chain-runner capture step (`aeon.yml:479-493`) silently overwrites Write-tool
  output with the CLI's final assistant `.result`. Fenced blocks must be
  emitted in assistant text, not via Write.
- HL `userFills` 2000-row cap is on the *response*, not the *query window* —
  wallet selection by margin (pnl/vlm) clears the floor.
- Sandbox blocks `./notify "$(cat ...)"` arg-passing — stage to
  `.pending-notify/` and let post-run step deliver (used by 12+ skills).
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use prefetch.
- Cost profile is cache-dominated (73% of spend). defi-overview, heartbeat,
  reppo-digest = 38% of weekly Opus spend; Sonnet rotation could cut ~$55-65/wk.
- Memory consolidation: topic-file detail, MEMORY.md is the index.
- Vote slot can be blocked by agent's own mint cadence — when current-epoch
  is owned entirely by your own prior mints, "AND is NOT one you just
  minted" reads as "0 vote targets". Worth a SKILL.md tighten on whether
  to LIKE-vote own mints or stay neutral.

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-30 | code-health (weekly) | meta / fleet health |
| 2026-05-30 | skill-freshness audit | meta / fleet health |
| 2026-05-29 | skill-freshness audit | meta / fleet health |
| 2026-05-28 | weekly-shiplog (week 1) | meta / fleet health |
| 2026-05-28 | how the reppo agent swarm runs on aeon (explainer) | docs |
| 2026-05-28 | thread-formatter (PR #32 phantom-skill diagnosis) | meta |
| 2026-05-25 | cost-report (week 1) | meta / fleet health |
| 2026-05-25 | security-scan bootstrap | meta / fleet health |
| 2026-05-25 | weekly-review (week 1 baseline) | meta / fleet health |
| 2026-05-24 | skill-evals bootstrap baseline | meta / fleet health |
| 2026-05-21 | last30 — bitcoin (30d) — stale | crypto |
