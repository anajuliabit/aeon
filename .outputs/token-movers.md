The wrapper file is harmless (uncommitted). Skill is complete.

## Summary

Executed `skills/token-movers/SKILL.md` for 2026-06-09.

**Data sources:** CoinGecko `/coins/markets?per_page=250` (HTTP 200, 244KB) and `/search/trending` (HTTP 200, 55KB). Filter dropped 63 → 187 ranked coins (stables, wrapped, sub-$1M vol).

**Pulse:** Mixed-flat tape — 42/100 top-100 green, median top-50 −0.06%, median top-100 −0.31%. Materially less risk-off than 6-06's 25/100 green.

**Top calls:**
- KTA +32.9% (#244, $6.5M vol) — TRENDING+UP + **PUMP-RISK** (rank>150, +30%, low liquidity, also on trending list)
- VELVET +24.5% / 7d +327% — **BREAKOUT**
- GWEI/ETHGas +16.3% / 7d +73% — **BREAKOUT**
- H/Humanity **−70.9% / 7d −72%** — TRENDING+DOWN + **CAPITULATION** ($453M vol, vol/mcap 1.26x)
- LAB day-3 unwind continues (−19.4%, was −38.9% on 6-06)
- ZEC relief bounce extends off 6-06 capitulation; now on trending list

**Dedup vs 6-08 / 6-06:** WLD kept (7.9% → 13.9%, 7d flipped positive — material), ZEC kept (now trending), LAB kept (day-3). BEAT/DEXE/HASH/NEAR/INJ from 6-08 winners all rotated off — not reinstated.

**Files:**
- `/home/runner/work/aeon/aeon/.outputs/token-movers.md` — fresh report (overwrote 6-08 carryover)
- `/home/runner/work/aeon/aeon/.pending-notify/1781008454.md` — notification dropped to notify's sandbox-fallback path (postprocess will deliver)
- `/home/runner/work/aeon/aeon/memory/logs/2026-06-09.md` — token-movers log entry appended

**Notify path:** `./notify "$(cat ...)"` was blocked by sandbox shell-substitution guard, so I wrote the message directly to `.pending-notify/{ts}.md` (the exact path `notify` line 30 uses for post-run delivery in sandboxed runs). No data loss — the postprocess delivery step will ship it.

**Follow-up:** None required. Tracked tokens (WELL/MAMO/REPPO/GITLAWB) did not surface in the top-250 with sufficient volume — they go through `token-alert` separately.
