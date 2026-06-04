## Summary

**Skill executed**: `skills/token-movers/SKILL.md` — produced the daily movers/losers/trending report with signal enrichment.

**Data fetched** (live curl, no key needed): CoinGecko `/coins/markets` (250 coins, 245kB) + `/search/trending` (15 coins). No WebFetch fallback triggered.

**Market pulse**: deep risk-off — 15/100 top-100 mcap green, median 24h −4.8% (vs −0.75% yesterday). BTC −4.8% / 7d −13%, HYPE finally cracks at −7.8% after holding green-only-major status yesterday.

**Key signals tagged**:
- **REVERSALS dominate**: yesterday's winners PIEVERSE, NEAR, VVV, LIT all flipped to today's losers; SKYAI flipped from −48% loser to +19% winner (dead-cat relief).
- **NEAR**: TRENDING+DOWN + CAPITULATION (−18.3% on vol/mcap 0.46) — aligns with this morning's aixbt-pulse Hayes-dump callout.
- **LAB**: day-6 vertical still holds (7d +303%), only green name trending — ZachXBT insider-supply flag carried.
- **HOME**: 6-02 token-pick at $0.0475 entry now $0.0369 — lost the 24h entry-window cushion 6 days before june-10 unlock.

**Files created/modified**:
- `.pending-notify/1780577611-token-movers.md` (3,122 chars, under 4000 cap) — post-run delivery step will fan out to Telegram/Discord/Slack
- `memory/logs/2026-06-04.md` — appended `### token-movers` entry per skill step 8
- `.tmp-cg-markets.json`, `.tmp-cg-trending.json` — scratch (sandbox blocks `rm` mid-run; tracked under MEMORY.md cleanup goal)

**Follow-up**: none specific to this skill. Watchlist tokens didn't screen top-20 either side; token-alert covers those directly.
