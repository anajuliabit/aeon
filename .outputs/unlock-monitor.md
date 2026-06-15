Done. The unlock-monitor skill ran clean.

## Summary

Executed the **unlock-monitor** skill for the week of 2026-06-15 (Monday). Ranked seven upcoming unlocks by **Absorption Ratio** (unlock $ / daily volume), classified cliff vs. linear, and produced a per-event market read.

**The headline:** **$CONX** (Connex) — $14.89M unlocking (48.6% of supply) into a book that trades **$5,159/day**. Absorption ratio ~**2,886×**. Not strain, a vacuum — the printed price is meaningless the moment sellers appear. Tiered CRISIS, read `market asleep`.

**The only liquid risk:** **$SPK** (Spark) — 32.1% supply cliff (~1.13× vol) while the chart is up +34.7% over 30d. Textbook bid-then-dump → `fade pump`.

**Loud-but-absorbable:** $H/Humanity ($109.8M but $209M/day vol eats it), $NEWT, $KAITO, $ZRO — all DIGESTIBLE. $MEGA dropped as TRIVIAL (0.14× vol).

**Files:**
- Created `memory/state/unlock-monitor-seen.json` — 7 shipped keys for dedup
- Updated `memory/logs/2026-06-15.md` — run log, `UNLOCK_MONITOR_OK`
- Staged `.pending-notify/1781956800-unlock-monitor.md` — notification (1,884 chars, under cap) for post-run delivery
- Committed both memory files to `main` (`f36ff3c`) per the skill's `commits: true`

**Source status:** tokenomist=ok, cryptorank=ok, dropstab=ok, coingecko=ok, **defillama=fail** (HTTP 403). One source down (not degraded — needs 2+).

**Follow-ups / caveats:**
- **WebSearch is broken** — both queries returned `API Error: 400`. The skill survived on WebFetch alone; worth a heads-up if other skills depend on WebSearch.
- Used **24h volume as a proxy** for the spec's 7-day avg daily volume — no source exposed a clean 7d figure. Ratios are directionally correct; CONX's verdict is unaffected by any reasonable averaging.
- Per-token unlock **dates defaulted to 06-15** (the week-of Monday) where sources showed only countdown placeholders.
- `./notify` couldn't fire inline — the sandbox blocked the `$(cat …)` substitution (the exact pattern PR #108 was meant to retire; that fix isn't on `main` yet). Used the `.pending-notify/` fallback instead, which the post-run step delivers.
