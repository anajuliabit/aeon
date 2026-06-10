## Summary

Ran the **token-movers** skill standalone for 2026-06-10.

**Sources:** CoinGecko `/coins/markets?per_page=250` HTTP 200 (245KB) + `/search/trending` HTTP 200 (58KB). Filter dropped 65 → 185 ranked entries.

**Pulse:** broad risk-off — 22/100 top-100 green, median top-50 −3.4%. Regime flip from 6-09's mixed-flat tape (was 42/100 green). Aligns with the aixbt-pulse bridge call (US strikes confirmed + Fable-5 reflexive fear) and BTC at $61.1k.

**Top signals (after dedup vs 6-09 + 6-08):**
- **BEAT** TRENDING+UP+BREAKOUT — top-100 mcap, +23% on +337% week, cleanest positive signal.
- **BTW** PUMP-RISK — #176, +43% on +621% week, parabolic.
- **ZEC** full reversal — yesterday's TRENDING+UP +12.6% relief flips to TRENDING+DOWN −12.7% on the same trending list. Quantum-resistance trade gets a brutal day-3.
- **VELVET** CAPITULATION — yesterday's BREAKOUT (+24.5%) unwinds to −17.7% with vmc 0.35. Confirms 6-09 token-pick rejection.
- HOME flipped: yesterday's loser at −10% to today's winner +12.5% (FADE — 7d still −20%).

**Files:**
- `.outputs/token-movers.md` — full report (2425 chars).
- `.pending-notify/token-movers-2026-06-10.md` — queued for postprocess delivery (direct `./notify` blocked by sandbox shell-substitution guard, same path as the 6-10 daily-routine log).
- `memory/logs/2026-06-10.md` — appended `### token-movers` entry per skill step 8.

**Follow-up:** None. Postprocess will deliver the queued notification on the next workflow step.
