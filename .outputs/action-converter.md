*5 Actions — 2026-08-03*
Shape: file usepod P0, graft regen-step, rebase PR#165, raise ISS-025 d20, advance ISS-028 d5

1. file `memory/issues/ISS-030.md` for fleet-wide usepod.ai HTTP-402 outage — 11+ skills consec_failures≥3 at 18:27Z burst (thought-review=9, skill-freshness/cost-report/unlock-monitor/btc-levels/daily-routine=6, security-digest=5, search-skill=4, deal-flow/self-improve/heartbeat=3), signature `Payment required. Retry with X-PAYMENT or PAYMENT-SIGNATURE header`
why: fresh dominant P0 today, no ISS-file exists, operator-gated billing/proxy path unclear until surfaced
done: `memory/issues/ISS-030.md` written with YAML frontmatter (severity=critical, category=missing-secret), `INDEX.md` open-table advances 13 → 14
loop: file-iss-030-usepod-402-outage

2. graft `./generate-skills-json` regen step into `skills/self-improve/SKILL.md` commit process — closes ci-skills-json 3-consec-day formal-pattern on PR #171 + #172
why: root cause `skills.json stale` identified 8-02 via `gh run view 30713133283 --log-failed`; systemic fix unblocks Sunday-batch merge window opening today
done: `skills/self-improve/SKILL.md` diff committed to a fix branch, PR opened against main, `gh pr checks` on #171/#172 rerun once merged
loop: fix-ci-skills-json-shared-root-cause

3. rebase PR #165 `docs(skill-graph): shared_state 21→27` against main to resolve `docs/skill-graph.md` merge conflict
why: d15 CONFLICTING sole survivor past-gate cohort, CLAUDE.md ~7d-past-touch escalation window open, Sunday-batch weekly-review 8-03 sole shot before d16 rolls
done: `gh pr view 165` shows MERGEABLE and green on required checks
loop: rebase-pr-165-conflict-d15

4. raise ISS-025 T+5 day-20 addendum block in `memory/issues/ISS-025.md` — cost-report weakest chronic-failure sr=11% (7/64) durable, 20d slip past 7-30 deadline
why: hand-off milestone rolls today Sunday-batch, weekly-review 8-03 action #1, operator-author still needed against `.github/workflows/aeon.yml:479-495`
done: `memory/issues/ISS-025.md` appended with `## T+5 d20 update — 2026-08-03` block naming sr regression + weekly-batch escalation
loop: raise-iss-025-t-plus-5-d20

5. advance ISS-028 kill-test d5 block in `memory/issues/ISS-028.md` — 8-02 kill-test d3+d4 NEGATIVE at 3 sub-agent + call-site probes, workaround-chain n=18+ durable 12-UTC-day span 7-22 → 8-02, 4-consec-day formal-pattern
why: reflect 8-03 (Sunday-batch) reopens root-cause investigation into PR #167 fix-scope narrowness; pre-populated evidence block feeds that
done: `memory/issues/ISS-028.md` appended with `## Kill-test d5 — 2026-08-03` block naming today's blocked call-sites (skill-graph 5-blocked-form fingerprint recompute / list-digest `>>` append / daily-routine hn-digest sub-agent)
loop: advance-iss-028-kill-test-d5

sources: memory=75L logs=8d topics=~20 prs=3 cron_failing=11+consec-3 mode=OK
