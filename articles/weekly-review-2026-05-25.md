# Weekly Review — 2026-05-25

## TL;DR

baseline week. fleet bootstrapped 2026-05-21, ran 111 skill runs across 29 skills with 3 failures and 7 issues filed → 3 resolved. the loop that worked: issue → PR → next issue. the loop that didn't: 4 straight days of reppo intents minted and reverted in dry-run. top action next week: actually verify on-chain after today's PR #10 + #11 merges — without that, every other receipt is fiction.

## Last week's actions — closed loop

_No prior review to audit — this is the baseline._

## Metrics

| Metric | This week | Prior week (if known) | Δ |
|---|---|---|---|
| Skill runs | 111 | — | — |
| Successes / failures | 108 / 3 | — | — |
| Articles written | 10 | — | — |
| Notifications sent | 36 | — | — |
| New issues opened | 7 | — | — |
| Issues resolved | 3 | — | — |
| Commits / PRs merged | 8+ PRs (#3, #4, #8, #9, #10, #11, #12, #14 known merged) | — | — |

_Source: `memory/cron-state.json` (skill-runs script declined approval in sandbox — degraded source per SKILL.md fallback) + grep of `memory/logs/2026-05-2*.md` for notification count + `ls articles/` for article count + `memory/issues/INDEX.md` for issues + log mentions for PR merges (shallow CI clone, git log shows only the most recent commit)._

## Findings (KALM, prioritized)

### Keep

- **The issue → PR loop is the spine of this fleet** (priority 25 — F5×I5÷E1). 7 issues filed this week, 3 already resolved by code (PR #3 closed ISS-001 2026-05-21; PR #4 closed ISS-002 2026-05-22; PR #8 closed ISS-003 2026-05-23). PRs #9 (token-alert step-2), #10 (auto-grant helper), #11 (lock helper), #12 (soul/ populated), #14 (scan.sh pattern fix) all merged 2026-05-23 → 05-25. Evidence: `memory/issues/INDEX.md` Resolved table; logs 2026-05-25 action-converter, self-improve, reflect.
- **Daily memory consolidation via reflect** (priority 16 — F4×I4÷E1). 4 consecutive runs (2026-05-22 → 05-25), each one refreshing MEMORY.md + topics/fleet.md + topics/crypto.md, reconciling INDEX.md, and surfacing recurring patterns. MEMORY.md "Last consolidated" stamp moved daily; today's reflect captured PR #10/#11/#12/#13 within 9 minutes of merge. Evidence: 2026-05-25 reflect log; MEMORY.md L2 `*Last consolidated: 2026-05-25*`.
- **Heartbeat dedup prevented notification storm** (priority 15 — F5×I3÷E1). ISS-004 + ISS-005 + ISS-006 carried across 4 days of heartbeats (08:00, 14:00, 20:00 slots) — every single one "deduped, no notification". Operator inbox stayed clean while 0/0 on-chain ran day after day. Evidence: every heartbeat block in logs 2026-05-23 → 05-25.

### Add

- **An actual on-chain verification step after merging the unblock PRs** (priority 12.5 — F5×I5÷E2). PR #10 (auto-grant subnet) + PR #11 (lock REPPO) merged today 2026-05-25 but ISS-004 + ISS-006 stayed Open in INDEX.md pending a real on-chain run. Day 4 of 0 mints / 0 votes confirmed. Evidence: 2026-05-25 goal-tracker log "BLOCKED: ... 0 on-chain day 4"; INDEX.md still lists ISS-004 + ISS-006 as Open.
- **A rubric for assigning agents to the 14 unassigned datanets** (priority 6.7 — F5×I4÷E3). Surfaced by every single reppo-orchestrator run for 5 days running (2026-05-21 → 05-25), untouched. action-converter has carried "unassigned-datanets" as a loop 3 days in a row with "no concrete first step — needs a rubric or operator pick" (2026-05-25 action-converter log). Evidence: 2026-05-25 reflect log pattern (3): "14 unassigned datanets surfaced every reppo-orchestrator run for 5 days running, untouched".

### Less

- **Re-running reppo-trading-agent on datanet 9 three times a day while 14 datanets sit idle**. 2026-05-22 alone had 3 separate orchestrator runs all queuing datanet 9 (mint-only de-dup is by content hash, so the trading agent kept writing new intents). All 4 dry-runs still revert per the open blockers. Evidence: 2026-05-22 reppo-orchestrator log: 3 distinct "Plan: 1 agent RUN ... datanet 9" entries. Carries 4 days of running into a known revert.
- **Writing mint + vote intents that we know will revert in dry-run**. ~4 mint intents + ~12 vote intents queued across 4 days, every one reverted: ISS-004 (subnet), ISS-006 (voting power), ISS-007 (transient RPC). Productive-looking output, zero on-chain effect. Evidence: 2026-05-22/23/24/25 reppo-digest logs all end with "0 mints / 0 votes on-chain".

### More

- **self-improve cadence**. 2 runs this week (every-other-day per cron), each one shipped a focused, high-leverage PR: PR #9 tightened token-alert step-2 rules (closed a silent-skip bug), PR #14 cut scan.sh false-positive rate ~97.5% (769 → 19 matches). Highest signal-per-run of any skill. Evidence: 2026-05-23 self-improve log → PR #9; 2026-05-25 self-improve log → PR #14.

### Dropped from priority threshold

- evals.json `output_pattern` drift for token-alert / skill-health / hn-digest / polymarket (priority 1.5 — F1×I3÷E2). Captured in 2026-05-24 skill-evals action queue but skill-evals only fires Sundays — low frequency, easy to fix next cycle.
- competitor-launch-radar staleness (priority 2). Single run 2026-05-21; cadence may be intentional.

## Next week — actions

- [ ] Run `gh workflow run chain-runner.yml -f chain=reppo-swarm`, confirm reppo-digest reports ≥1 mint **and** ≥1 vote on-chain, and move ISS-004 + ISS-006 to `memory/issues/INDEX.md` Resolved by 2026-05-28
  - Why: PR #10 (auto-grant) + PR #11 (lock REPPO) merged 2026-05-25 but on-chain output still 0/0 day 4 — every receipt downstream of these PRs is fiction until verified
  - Done when: `memory/topics/reppo.md` Minted-strategies + Votes tables each grow by ≥1 row tagged on-chain-confirmed (real tx hash), and INDEX.md Resolved table contains ISS-004 + ISS-006 with the verification commit SHA
- [ ] Write `configs/datanets/RUBRIC.md` (criteria for assigning trading-agent or another agent to each datanet) and map ≥3 of the 14 unassigned datanets to a concrete agent by 2026-05-30
  - Why: 5 days of reppo-orchestrator runs surfaced "14 unassigned datanets" with zero forward motion; loop has been carried by action-converter 3 days in a row with no first step
  - Done when: `configs/datanets/RUBRIC.md` exists with ≥3 named criteria; ≥3 of the 14 datanets have agent configs added under `configs/datanets/`; next reppo-orchestrator run reduces "unassigned" count to ≤11
- [ ] Patch `skills/skill-evals/evals.json` `output_pattern` rows for token-alert, skill-health, hn-digest, polymarket by 2026-05-31 (next Sunday's skill-evals fires)
  - Why: 2026-05-24 skill-evals bootstrap surfaced spec drift; current paths point at `articles/*` for skills that write to `memory/logs/` or have no skills/ dir — 4 skills silently mis-evaluated
  - Done when: `skills/skill-evals/evals.json` has corrected `output_pattern` for all 4 named skills; next Sunday's skill-evals run shows ≥4 newly evaluated skills in its coverage diff

## Goals progress

From `memory/MEMORY.md` Current Goals:

- **Unblock reppo-swarm on-chain output** — partial progress, structurally blocked. PR #10 (auto-grant helper) + PR #11 (lock helper) merged 2026-05-25 (today); ISS-005 agent-side workaround live since 2026-05-24 (validityEpoch filter in trading agent). But ISS-004 + ISS-006 stay Open pending on-chain verification (next-week action 1). ISS-007 (transient Base RPC) tracked in flight (PR #13). Cite: 2026-05-25 reflect + goal-tracker logs.
- **Assign agents to the 14 unassigned reppo datanets** — **stalled, no progress this week**. Carried by action-converter 3 days running, surfaced by every orchestrator run 2026-05-21 → 05-25. Needs the rubric (next-week action 2) before forward motion is possible. Cite: 2026-05-25 action-converter "Loops carried over: unassigned-datanets-14 (5d untouched, no concrete first step)".

Note: MEMORY.md "Completed Goals" section retains the soul/ populate goal completed today (PR #12). No goals to retire — both remain real.

## Notes

- Article skill `success_rate=0.5` (1/2) carried all week but stayed below every surface threshold (≥5 runs needed). Not a finding — too thin to act on.
- github-trending `success_rate=0.8` (4/5) — one failure on 2026-05-25 09:47Z (log fragment in cron-state suggests a notify-output truncation, not a content failure). Watch but not actionable yet.
- Cost-report week-1 bootstrap projects ~$770/mo (cache-dominated, 73% spend). Bootstrap day inflates the number; another week of data needed for a real baseline.
- The shallow CI clone means `git log --since="7 days ago"` returns 1 commit. PR-merge count above comes from log mentions, not git history. If the operator runs this skill from a full clone, that column gets more accurate.
- Three skills filed nothing all week and have no signal: `last30`, `narrative-tracker`, `competitor-launch-radar`, `token-pick`, `fetch-tweets` (all 1 run on 2026-05-21). Weekly cadence may be intended — not flagged.
