## Summary

Self-improve targeted vibecoding-digest's duplicate-error-notification noise — the recurring same-day pain I could fix inside the skill-files-only scope.

**Target:** `skills/vibecoding-digest/SKILL.md` Step 2 fallback path
**Problem:** When Reddit prefetch fails (host-side, not just sandbox), both daily slots ship identical `VIBECODING_DIGEST_ERROR` notifications. 2 dup pings/day on 2026-05-28 and the same pattern flagged in 2026-05-29 morning-brief + skill-health + action-converter.
**Fix:** Grep today's log for prior `VIBECODING_DIGEST_ERROR`; if found, suppress the notification and log "2nd same-day error, suppressed". First failure still pages.
**PR:** https://github.com/anajuliabit/aeon/pull/43 (+4 / -1, skill file only)

**Files modified:**
- `skills/vibecoding-digest/SKILL.md` (on PR #43 branch)
- `memory/logs/2026-05-29.md` (Self Improve entry appended on main, uncommitted)
- `.pending-notify/1780064000-self-improve.md` (notification staged for post-run delivery)

**Out of scope (deferred):** root-cause prefetch fix lives in `scripts/prefetch-vibecoding.sh`, which self-improve isn't permitted to touch — that's a separate PR. ISS-005 dedup, HL wallet-rank fix, and `HL_OHLCV_COINS` widening are similarly script-side.

**Pre-run gate:** 2 open improvement PRs (#41, #42), under the 3+ ceiling.
