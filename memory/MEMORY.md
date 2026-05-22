# Long-term Memory
*Last consolidated: 2026-05-22*

## About This Repo
Aeon — autonomous agent running on GitHub Actions via Claude Code. ~20 skills run on
cron; inbound messaging via Telegram (live). Fleet exited bootstrap on 2026-05-21.

## Current Goals
- Keep the reppo-swarm chain producing real on-chain output (blocked by ISS-003).
- Populate `soul/` files so content skills stop running in neutral voice.

## Active Topics
- [Fleet status & infrastructure](topics/fleet.md) — PRs, recurring blockers, skill health.
- [Crypto research](topics/crypto.md) — defi-overview, narratives, token signals.
- [Bitcoin 30-day snapshot](topics/last30-bitcoin.md) — last30 skill baseline.
- [Reppo swarm ledger](topics/reppo.md) — append-only on-chain audit trail.

## Open Issues
- ISS-003 (high) — reppo postprocess dry-run fails `code: UNKNOWN`; PR #8 open. See `memory/issues/`.

## Lessons Learned
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use the prefetch pattern.
- Always save files AND commit before logging.
- Reppo ledger rows are for on-chain-confirmed actions only — a queued intent is not a mint.
- Soul files empty → all content skills use neutral voice (known gap, not a per-run bug).

## Recent Articles
| Date | Title | Topic |
|------|-------|-------|
| 2026-05-22 | skill-freshness audit | meta / fleet health |
| 2026-05-21 | The 100x Fix: Neuro-Symbolic AI & the AI Energy Crisis | AI / energy efficiency |
| 2026-05-21 | competitor-launch-radar | competitive intel |
| 2026-05-21 | last30 — bitcoin (30d) | crypto |
| 2026-05-21 | The 100x Fix: Why Neuro-Symbolic AI Could Defuse the Energy Crisis It Created | AI / neuro-symbolic AI energy efficiency |

## Recent Digests
| Date | Type | Key Topics |
|------|------|------------|
| 2026-05-21 | crypto | Japan stablecoins, Hyperliquid FDV, Strategy $2B BTC |

## Skills Built
| Skill | Date | Notes |
|-------|------|-------|

## Lessons Learned
- Digest format: Markdown with clickable links, under 4000 chars
- Always save files AND commit before logging

## Next Priorities
- Configure notification channels (Telegram, Discord, or Slack)

## Completed Goals
- Run first digest — completed 2026-05-21
