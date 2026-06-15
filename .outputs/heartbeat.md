HEARTBEAT_OK · STATUS_PAGE=DEGRADED — wrote docs/status.md, no notify (dedup)

P0 surface (3 items, all in last-48h logs): `chain:investment-advisor` failed-carry (off-table, chain dropped from `aeon.yml`); `deal-flow` stuck since 6-08 — today's Monday 14:00 tick didn't clear it (the 09:48Z heartbeat explicitly expected it to clear); `fork-cohort` stuck ~25h (2nd consecutive Sunday weekly miss). All other Monday weeklies recovered today. Heartbeat self-check OK (~10.6h since last_success).

Status page regen: 43 enabled rows sorted last-run desc, 2 🕸 stuck (deal-flow + fork-cohort), 2 never-run at bottom (operator-scorecard + fork-skill-gap), 7 open issues, evening-recap 21:00 UTC up next. Token pulse omitted (no `articles/token-report-*.md` on disk).
