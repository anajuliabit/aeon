`HEARTBEAT_FLAGGED · STATUS_PAGE=DEGRADED — wrote docs/status.md`

## Summary

Heartbeat ran at 15:08Z (Tue afternoon slot). P0 trigger fired: `chain:reppo-swarm` flipped `last_status` to "failed" in `cron-state.json` at 12:23:02Z, but `gh run view 26818451669` confirms `conclusion=success` at 12:23:07Z — state-file/reality desync, ~5sec window. All four component skills (orchestrator/voter/trading-agent/digest) logged success this chain; ledger unchanged at 14 mints / 29 votes. Operationally healthy, but literal P0 rule (`last_status=failed` → DEGRADED) fires the verdict.

- **Files modified:** `docs/status.md` (regenerated to 🔴 DEGRADED, 34 enabled skills tabled, 8 open issues), `memory/logs/2026-06-02.md` (heartbeat entry appended)
- **Notification staged:** `.pending-notify/1780412925-heartbeat.md` (post-run delivery)
- **Follow-up:** trace which sub-step within the 12:00 chain wrote the failed state-record after the workflow ended green — likely a postprocess/state-update step under `on_error: continue`. File under ISS-010 (chain-key bookkeeping) scope if a structural bug confirms.
