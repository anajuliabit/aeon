`HEARTBEAT_OK · STATUS_PAGE=DEGRADED`

- 14:00Z tick fired ~17min late (recurring cron catch-up variance).
- P0 chronic 18-skill sr<0.5 tail unchanged (ISS-019/020/021/025 day-17). No failed rows, no >45min-stuck dispatches, all cf=0. Self-check ok (5h13min).
- P1 empty (`gh pr list` `[]`, zero urgent issues).
- P2 SLX day-15 catastrophic; daily-routine 09:05Z trending endpoint printed SLX $0.174 (-63% vs entry $0.4753 — extends -46% from last CG print). Recut still overdue T-4 to weekly-review 7-13. ISS-025 capture-step PR day-17 unshipped.
- P3 12:00Z batch dark day-12 (8 skills 11d stale). **Fresh:** 12:00Z tick 7-09 hasn't dispatched token-alert or btc-levels 12:15Z as of 14:17Z — 2h past slot, prior 3 days caught up 53min–1h late. Not flagging yet; 20:00Z hb is the checkpoint.
- Status page regenerated — skill-freshness 09:07 UTC tops, 43 enabled skills, 11 open ISS-xxx, verdict DEGRADED, next-run btc-levels @ 16:15 UTC.
- Notification skipped per 48h dedup (byte-identical classification to 7-09 09:02Z + 7-08 15:19/09:04Z + 7-07 20:29Z).
