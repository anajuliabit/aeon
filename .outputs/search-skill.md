*Search Skills — 2026-08-17*
Gap: cost-report chronic sr=7% (consec=9) — aeon per-model $ cost + anomaly + burn forecast
Candidates (not auto-installed):
- cost-tracking — affaan-m/ecc (gap-fit 2/5, sum 12/15, UNTRUSTED · WEAK) — reads `~/.claude/metrics/costs.jsonl` written by ECC's stop hook, not aeon's own token log
- cost-track — ruvnet/ruflo (gap-fit 2/5, sum 12/15, UNTRUSTED · WEAK) — ruflo meta-harness plugin, 658 installs, data source unclear from listing
- cost-metering — scientiacapital/skills (gap-fit 2/5, sum 11/15, UNTRUSTED · WEAK) — generic API cost tracking + budget alerts + model routing
Manual install: ./add-skill affaan-m/ecc cost-tracking
Note: cost-report root cause is usepod-402 (ISS-030/ISS-031) not capability gap — no external skill directly replaces aeon-token-log ingestion path.

Sources: npx=ok(19) vercel=1(dropped) anthropics=0 bankr=0 skills.sh=fail
