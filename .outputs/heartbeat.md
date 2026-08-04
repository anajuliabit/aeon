## Summary

Ran heartbeat 14:45 UTC (14:00Z slot +45min dispatch-lag). Fleet has recovered from ISS-029 (usepod.ai 402 outage) — 20-of-20 dispatches post-20:14Z succeeded through 8-04 12:19Z token-alert. Verdict: 🔴 DEGRADED, notification skipped (all 6 findings dedup'd vs 8-03 20:15Z heartbeat + 8-04 07:24Z morning-brief).

**Files modified:**
- `docs/status.md` — 43-skill table wholesale rewrite (post-recovery, cost-report ❌ top of failed sort, all other 8-03+ rows ✅), 14 open issues (includes ISS-029), Overall 🔴 DEGRADED, next-run btc-levels 16:15 UTC
- `memory/logs/2026-08-04.md` — heartbeat entry with dedup rationale and fresh-signal capture

**Follow-up captured (for 18:00Z reflect):**
- ISS-029 effectively resolved via post-20:14Z recovery batch
- cost-report distinct-signature persists at consec=15 / sr=10% (up from 12/11% morning), ISS-030 candidate distinct from ISS-025 sandbox-truncation shape
- 16-consec heartbeat verdict-string durability rail CLOSES at ~124h span (memory-window record), post-recovery composition-shift begins new "chronic-cohort-alone-degraded" regime

**Output:** `HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md · NOTIFY=SKIPPED (all 6 findings dedup'd 48h)`
