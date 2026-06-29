## Summary

Ran the weekly-review skill end-to-end against the 2026-06-22 → 2026-06-29 window.

**Headline:** success rate snapped back **22% → 88%** (265/301 ok vs 178/807) and dispatch volume collapsed **874 → 302** — without the structural `aeon.yml` capture-step PR shipping. Recovery is organic: PR #128 (usepod gateway, prior week) propagated + scheduler back-off + thinner cron slate.

**Closed loop on prior actions:** 1 shipped (deal-flow unstuck), 1 obviated (scheduler-audit doc — recovery healed itself), 1 partial (ISS-025 named, not fixed), 2 slipped (INDEX hygiene 5th consecutive carry, PR #133 harvest).

**Next week — 4 SMART actions:** (1) merge the action-converter-flagged ISS-025 PR (4.6/5, day 6 unshipped) by 2026-07-04; (2) flip ISS-007/009/010/016 to Resolved by 2026-07-02 (5th carry); (3) enable `config-validator` + `batch-health` + `api-health` from PR #133 by 2026-07-05; (4) gate `STATUS_PAGE=DEGRADED` on cf≥3 not chronic sr by 2026-07-06.

**Files:**
- `articles/weekly-review-2026-06-29.md` — full review
- `.pending-notify/weekly-review-2026-06-29.md` — notification queued (direct `./notify` exec blocked in sandbox per skill spec)
- `memory/logs/2026-06-29.md` — `### weekly-review` log entry appended

**Follow-up:** notification will deliver via the postprocess step when this run finishes.
