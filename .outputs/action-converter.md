*5 Actions — 2026-08-08*
Shape: rebase #173, triage #174, audit ci-skills-json, add LIT, refresh market-context

1. rebase pr #173 fix/self-improve-2026-08-03 onto origin/main and force-push (`gh pr checkout 173 && git rebase origin/main && git push --force-with-lease origin fix/self-improve-2026-08-03`)
why: ci cold ~112h since 8-03 20:19z push; yesterday's close-reopen didn't fire; commit-hash change is stronger trigger; T-1 to 8-09 sunday-batch, one lift unblocks 3-pr chain (#171 + #172 + #173)
done: `gh pr view 173 --json statusCheckRollup` non-empty within 30 min
loop: pr-173-ci-cold

2. triage pr #174 (advisor brier-weight in pm synthesis) — read diff, verify prompt/schema changes, decide approve or request-changes
why: first advisor-workflow-authored pr in memory-window opened 00:31z overnight, queue-full 4→5 tests self-improve exit-gate, needs risk-tier + skill-scan before 8-09 batch
done: `gh pr review 174 --approve` or `--request-changes` with comment posted
loop: pr-174-advisor-triage

3. audit `.github/workflows/ci-skills-json.yml` against last failing run — `gh run list --workflow=ci-skills-json.yml --limit 5` + `gh run view <id> --log-failed` to identify root cause blocking #171 + #172
why: yesterday's follow-up gate — if pr #173 ci stays dark 24h+ (now 112h), escalate to workflow-config investigation; #171 + #172 both fail on same shared root cause, audit unblocks the chain even if the #173 rebase itself doesn't fire
done: root cause written as comment on #171 or #172 (or as new entry in memory/topics/fleet.md)
loop: ci-skills-json-shared-root-cause

4. add LIT (lighter protocol) to memory/MEMORY.md Tracked Tokens table — 5th row with 15% threshold and coingecko id
why: list-digest 8-08 flowslikeosmo surfaced on-chain-verifiable distribution thesis (robinhood chain 1.8% of lighter perps vol, $11.14M on-chain deposits post-integration, 15.5M LIT burned 6.3% supply since 6-30 buyback, 125M staked at 6% apy, no unlocks until 12-29); tracking gate opens now so token-alert can surface any threshold cross rather than reconstruct after the fact
done: `head -125 memory/MEMORY.md | grep -c LIT` returns ≥1 in the Tracked Tokens block
loop: lit-token-add

5. refresh memory/topics/market-context.md baseline snapshot dated 2026-08-08 — btc regime + tracked-token state + pr queue + fleet-health line, replacing 2026-07-16 stale header
why: 23d/552h stale, crossed 2× threshold on 8-01, has been carried in every action-converter run since 8-03 without action; downstream skills (morning-brief, reg-monitor, security-digest) all reference this file for baseline framing, stale baseline drifts framing across the fleet
done: `head -1 memory/topics/market-context.md` shows date 2026-08-08
loop: market-context-md-stale-2x

sources: memory=156L logs=10d topics=19 prs=5 cron_failing=0 mode=OK
