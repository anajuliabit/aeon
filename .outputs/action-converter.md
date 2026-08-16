*5 Actions — 2026-08-16*
Shape: close iss-032 rule-gap, batch-merge sunday queue, ship usepod detector, refresh vault priorities, activate defi-monitor

1. write memory/issues/ISS-032.md — fork-cohort stuck-dispatched classification gap (skill-health step 2 missing `status='dispatched' AND days_since_last_dispatch>=3` branch)
why: 14th+ owed cycle today, memory-window unprecedented depth; unblocks self-improve rule-gap authoring; operator-only path per exit-gate
done: memory/issues/ISS-032.md exists with full frontmatter, INDEX.md open-count 15→16
loop: iss-032-manual-file

2. batch-merge 3+ of PRs #174 · #177 · #176 · #179 · #180 in today's sunday weekly-batch window
why: only weekly merge window; #174 3rd day past 7d stall band; any 3 merges disengage self-improve exit-gate (n=3→sub-3) and unblock fork-cohort rule-gap + detect-usepod-402 + chain-drift baked-fix candidates
done: gh pr list --state open shows ≤3 of the 5 stalled PRs remaining
loop: sunday-weekly-batch

3. author scripts/detect-usepod-402.sh — usepod-402 payment-required detector per ISS-031 gate, +3d overdue
why: usepod-402 dispatcher path fired 8-10 hitting 4 skills, still no automated detection; script gates alternative-dispatcher fallback wire, was queue-blocked all week
done: scripts/detect-usepod-402.sh executable, exits 1 on synthetic {"error":"Payment required"} payload, self-test in scripts/tests/
loop: iss-031-usepod-detector

4. reset vault/priorities.md to today's current mandate — 73d-stale, refresh-ask d6 unactioned, thought-review 10-consec zero-capture streak crossed today
why: single point of coherence for weekly-review + thought-review + inbox; refresh-ask d6 (weekly-review 8-10 + thought-review 8-11/12/13/14×2/15×2/16 all surfaced); sunday is the natural weekly cadence
done: vault/priorities.md mtime = 2026-08-16 with ≤5 fresh sherwood/reppo/aeon items
loop: priorities-73d-stale

5. populate memory/on-chain-watches.yml with sherwood + moonwell + mamo positions, set ALCHEMY_API_KEY + ETHERSCAN_API_KEY in GH secrets
why: defi-monitor day-70 NO_CONFIG; sherwood + mamo agent-on-moonwell thesis wants on-chain observability the fleet can consume; single YAML + 2 secrets unblock a dormant skill
done: memory/on-chain-watches.yml with ≥3 addresses, both keys set, next defi-monitor fire produces non-NO_CONFIG output
loop: on-chain-config-day-70

sources: memory=84 logs=7 topics=11 prs=6 cron_failing=5 mode=OK
