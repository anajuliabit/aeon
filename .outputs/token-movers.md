Scratch files (`movers_process.py`, `.cg-*.json`) left in working dir — sandbox blocks `rm`, postprocess cleanup unchanged. All output / notification / log artifacts are in place.

## Summary

Ran the **token-movers** skill standalone for 2026-06-11 (12:12 UTC, 12-utc cluster).

**Sources:** CoinGecko `/coins/markets?per_page=250` HTTP 200 (242KB) + `/search/trending` HTTP 200 (56KB). Filter dropped stables + wrapped + sub-$1M vol; 79 of top-100 cleared.

**Pulse:** sharp relief rally — 57/79 filtered top-100 green, median top-50 +2.0%, top-20 +2.7%. Regime flip from 6-10's 22/100 / median −3.4% tape. BTC reclaims $63k (+3.0%).

**Top signals (after dedup vs 6-10 + this morning's 07:25Z daily-routine):**
- **VELVET** TRENDING+UP+BREAKOUT — +126% / 7d +618%, mcap $328M. 3rd direction flip in 3 days (6-09 +24.5% → 6-10 −17.7% → today +126%). Whiplash, not trend.
- **BEAT** TRENDING+UP+BREAKOUT — top-50 mcap (#38), +61% / 7d +532% on $239M vol. Cleanest sustained signal.
- **SKYAI** BREAKOUT+PUMP-RISK — #159, +40% after 2-day −44% cumulative bleed. Low-cap reversal, vmc 0.23.
- **H/Humanity** TRENDING+DOWN — −6.7% / 7d −72%, bleed pace continues to decelerate but still on trending.
- Regime context: 22/100 green → 57/79 green in 24h, BTC $61k → $63k is the proximate cause.

**Files:**
- `.outputs/token-movers.md` — full report (2887 chars).
- `.pending-notify/token-movers-2026-06-11.md` — queued for postprocess delivery (direct `./notify` blocked by sandbox shell-substitution guard, same workaround as 6-10).
- `memory/logs/2026-06-11.md` — appended `### token-movers (12:12 UTC)` entry per skill step 8.

**Follow-up:** None. Postprocess will deliver the queued notification on the next workflow step.
