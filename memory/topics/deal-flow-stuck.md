---
name: deal-flow-stuck
description: deal-flow skill stuck since 2026-06-08 (10+ days)
metadata:
  type: project
---

deal-flow (Monday 14:00 UTC) last ran successfully 2026-06-08T15:02Z. Currently appears in cron-state as `last_failed` with no subsequent `last_success`. Status table marks as "chain‑dropped" but skill is standalone, not chain-dependent.

Today (2026-06-19) marks 10+ consecutive days of failure with no recovery. Next scheduled attempt is Monday 2026-06-22 14:00 UTC.

**Possible causes:**
1. GitHub Actions cron delay/clustering (similar to 14:29Z batch stuck)
2. Skill-specific execution error masked by dispatch failure
3. Resource contention with other Monday-weekly skills (operator-scorecard 10:30, unlock-monitor 10:00)

**Impact:** Weekly deal-flow analysis missing, creates gap in market coverage.

Related: [[fork-cohort-stuck]], [[14-29z-batch-stuck]], [[pr-112-stalled]]