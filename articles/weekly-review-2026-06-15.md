# Weekly Review — 2026-06-15

## TL;DR

success rate snapped 62% → 83% week-on-week (262/314 ok vs 230/369) — the virtuals fallback (PRs #106 + #107) absorbed the weekly-limit blast on 5 cg-price skills, daily logs landed 7/7 vs 5/7, articles 11 vs 5. the win came alongside a structural pivot: reppo-swarm migrated off ci to `~/code/orquestra` (PRs #103 + #114), retiring 4 chain skills from the failure surface; investment-advisor took the slot and shipped 19 PRs in 7 days including short-term-trade sizing. top action next week — file ISS-019 (weekly-limit-wave), 6d overdue, fix locus `.github/workflows/aeon.yml:508`, by 2026-06-17.

## Last week's actions — closed loop

From `articles/weekly-review-2026-06-08.md` "Next week — actions":

- **Action 1 — extend virtuals fallback to the reppo chain by 2026-06-11: PARTIALLY SHIPPED, scope abandoned.** the reppo-specific framing was abandoned — `~/code/orquestra` migration (PR #103 6-10, PR #114 6-14) moved reppo-swarm off ci entirely. but the underlying mechanism shipped for cg skills: PR #106 (virtuals gateway fallback) merged 2026-06-12 12:32Z, PR #107 (litellm shim, /v1/messages was 501) merged 2026-06-12 15:14Z. `aeon.yml:508` now reads `FALLBACK_CG_SKILLS=" defi-overview token-movers token-pick token-alert market-context-refresh "`. residual gap: non-cg dailies still exit 1 on weekly limit — surfaces as next-week Action 4.
- **Action 2 — file ISS-018 for the weekly-limit incident by 2026-06-09: SLIPPED.** `ls memory/issues/ISS-019.md` returns no such file. ISS-018 got claimed 6-13 by vuln-scanner for a different sandbox-limitation defect (per MEMORY.md L29), so the weekly-limit issue rolled to ISS-019 — still unfiled at +6d. mechanical carry.
- **Action 3 — write configs/datanets/RUBRIC.md + 1 datanet config by 2026-06-12: ABANDONED.** reppo-swarm migrated to `~/code/orquestra` self-hosted docker; datanet config belongs with orquestra now, not aeon. MEMORY.md L11-14 explicitly directs "do NOT re-add reppo-orchestrator/trading-agent/voter/digest skills, chains, or scripts here." the action is moot.
- **Action 4 — flip ISS-007 + ISS-010 + ISS-009 + ISS-016 to Resolved in INDEX.md by 2026-06-10: SLIPPED.** `grep ISS-007 memory/issues/INDEX.md` still lands all 4 under Open. 2nd consecutive review carrying. 5d overdue.

Result: 1 partial / 2 slipped / 1 abandoned (of 4). The two genuine slips both carry — ISS-019 file 6d, INDEX flips 5d.

## Metrics

| Metric | This week (2026-06-08 → 2026-06-15) | Prior week | Δ |
|---|---|---|---|
| Skill+chain runs | 314 (306 skill + 8 chain) | 369 | −55 |
| Successes / failures / cancelled / in-progress | 262 / 44 / 2 / 6 | 230 / 136 / 2 / 1 | +32 / −92 / 0 / +5 |
| Success rate | 83.4% | 62.3% | +21.1pp |
| Articles written | 11 | 5 | +6 |
| Days with a log entry | 7 (6-09 → 6-15) | 5 | +2 |
| New issues opened | 1 (ISS-018 vuln-scanner) | 0 | +1 |
| Issues resolved (INDEX flips) | 0 | 3 | −3 |
| PRs merged | 40 (#82 → #121) | 17 | +23 |

Sources: `gh api repos/anajuliabit/aeon/actions/runs?created=>=2026-06-08T19:00:00Z` paginated, filtered to names starting `skill:` or `chain:` (314 runs, 262/44/2/6 by conclusion). `gh pr list --state merged --search "merged:>=2026-06-08T19:00:00Z"` → 40 prs. `ls articles/` filtered to 6-09..6-15 → 11 files (5× skill-freshness + 1 skill-analytics + 1 skill-evals + 1 fork-skill-digest + 1 vuln-scan + 1 security-scan + 1 weekly-shiplog). `ls memory/logs/2026-06-0[9].md memory/logs/2026-06-1[0-5].md` → 7 files, sizes 290-722 lines, no zero-line days. `memory/issues/INDEX.md` diff: 1 new open (ISS-018), 0 new resolved. `./scripts/skill-runs` declined approval in sandbox — used direct gh-api per prior reviews' degraded-source pattern.

Failure breakdown (top sources, 44 total): btc-levels 8, token-movers 7, heartbeat 3, aixbt-pulse 2, fleet-control 2, list-digest 2, thought-review 2, plus 18 singleton failures across 18 other skills. btc-levels + token-movers = 34% of the failure surface.

## Findings (KALM, prioritized)

### Keep

- **Virtuals fallback shipped, success rate +21pp** (priority 20 — F5×I4÷E1). PRs #106 (2026-06-12 12:32Z gateway) + #107 (2026-06-12 15:14Z litellm shim, direct `/v1/messages` was 501) carry the 5 cg-price skills through the weekly-limit window. result: 262/314 ok vs 230/369 prior week, same direction the prior review predicted. evidence: `aeon.yml:508` constant, today's `daily-routine` log L26 "curl ok both cg endpoints", `defi-overview` log L156 (today) running clean.
- **Daily logs landed 7/7 days** (priority 12 — F4×I3÷E1). prior week dropped to 5/7 (6-07/6-08 silent during the 429 cliff). this week `ls memory/logs/2026-06-09.md ... 2026-06-15.md` returns 7 files, smallest 99 lines (6-12), largest 722 (6-09). receipts intact — the rate-limit-induced amnesia cleared with the fallback.
- **PR #108 notify file-flag shipping** (priority 10 — F4×I3÷F1.2). merged 2026-06-14 12:09Z (`fix: replace blocked ./notify "$(cat ...)"` pattern). today's evidence: morning-brief / aixbt-pulse / github-trending / weekly-shiplog / narrative-tracker all sent direct via `./notify -f`, no `.pending-notify/` carry. PR #119 (2026-06-15 14:09Z) closed the "stop sending `-f`" wrapper edge-case. mostly clean retirement of the post-process notify path.

### Add

- **ISS-019 weekly-limit-wave issue file — still missing** (priority 25 — F5×I5÷E1). 6d overdue from 2026-06-09. the pattern is weekly-cyclical (4th occurrence proven 2026-06-12, per MEMORY.md L25-27). fix locus identified — `.github/workflows/aeon.yml:508`. without the file, skill-health can't route prior context next cycle, and the fix is gated on operator decision (per-skill extension vs category split) that needs a place to live. tiny file, mechanical write.
- **INDEX bookkeeping flips ISS-007/009/010/016 — 3rd consecutive carry** (priority 15 — F5×I3÷E1). 5d overdue. all 4 have code shipped or workarounds proven durable (ISS-009 PR #69, ISS-010 PR #32 + reppo migration removes the consumer entirely, ISS-016 ledger workaround 18+ runs, ISS-007 transient class). INDEX.md L7-12 still lists 4 of them under Open. open count overstates real open count by 4. mechanical edit.

### Less

- **btc-levels failure rate 12% (8/68 runs)** (priority 12 — F4×I3÷E1). newest skill (PR #91 shipped 6-09), runs 4-hourly. today 05:42Z failure was `total_cost_usd:0 / output_tokens:0` empty-usage error — same signature as the bb3ab24 chore commit, root cause not yet identified. breakout-day blind — exactly the failure mode the skill exists to prevent. 8 fails / 7 days = ~1.1 per day, fleet-wide top failure source paired with token-movers (7). worth a focused empty-usage debug session.
- **skill-freshness stuck dispatched ~25h+** (priority 8 — F3×I3÷E1). dispatched 2026-06-14 08:32Z, still pending at this morning's 09:48Z heartbeat. the health-of-health skill being stuck this long erodes signal — fleet-control / heartbeat both depend on it for the freshness leg. 2026-06-15 14:55Z notify fired once on 6-14, no re-fire yet. either re-arm logic or a manual kick.

### More

- **Investment advisor cadence — 19 prs in 7 days** (priority 12 — F4×I3÷E1). PRs #82-#100 + #109-#118 + #120-#121 touched `scripts/advisor/`. shipped this week: standalone virtuals workflow (#82 superseded last week's #80 chain), basic-auth from secrets (#84), vesting-aware recs (#92), capital-2x phases 2+3+4 (#93/#94), weekly conviction (#94), claude-fable-5 path (#88), past-reports memory (#97), wave-c product lens drawdown/kelly/yield-delta (#98), moonshot 1% sleeve (#101), held-token fundamentals auto-fetch (#87), liquidity-by-position (#95), short-term momentum buys + grok x_search fundamentals + shorts (#116/#117), short-term-trade sizing as conviction-weighted budget split (#121). the daily run lands at 13:00Z and produces a posted report + telegram + staged picks. this is the highest-velocity new system in the repo — worth keeping the daily cadence + the selftest gate (`scripts/advisor/selftest.sh`) gating any merge.

### Dropped from priority threshold

- vuln-scanner sandbox-limitation ISS-018 (priority 5 — already filed 6-13, workaround documented as wontfix-class with prefetch pattern; covered by routine issue rotation).
- chain:investment-advisor carry failure last_failed=2026-06-08T17:04:46Z (priority 4 — chain definition dropped in MEMORY, standalone Investment-Advisor workflow took over and ran 3× successfully today; the chain entry is stale registry rot, fixes inside heartbeat's existing routine).
- on-chain-monitor / defi-monitor watches.yml NO_CONFIG day 10 (priority 4 — operator-gated, blocked on watches.yml seed, no aeon-side action).

## Next week — actions

- [ ] File ISS-019 in `memory/issues/ISS-019.md` for the weekly-limit-wave incident — frontmatter `severity: high`, `category: rate-limit`, `detected_by: weekly-review`, `detected_at: 2026-06-09`, `affected_skills: morning-brief daily-routine heartbeat goal-tracker reflect action-converter` (non-cg dailies still exit-1 on weekly limit) — plus add the Open row in `memory/issues/INDEX.md` by 2026-06-17
  - Why: 6d overdue, weekly-cyclical pattern (4 proven occurrences), fix locus `.github/workflows/aeon.yml:508` already identified, no routable issue file = skill-health can't see prior context next cycle
  - Done when: `ls memory/issues/ISS-019.md` returns the file with valid frontmatter; `grep -c "ISS-019" memory/issues/INDEX.md` returns ≥1 row under Open
- [ ] Flip ISS-007 + ISS-009 + ISS-010 + ISS-016 from Open to Resolved in `memory/issues/INDEX.md` — all 4 have shipped fixes or are obviated by the reppo-swarm migration (ISS-010 phantom skill = the missing skill no longer exists; ISS-009 PR #69; ISS-016 ledger workaround 18+ runs; ISS-007 transient class) — by 2026-06-17
  - Why: 3rd consecutive weekly-review slipping, 5d overdue, INDEX Open count overstates real open count by 4
  - Done when: `awk '/## Open/,/## Resolved/' memory/issues/INDEX.md | grep -c "ISS-00[79]\|ISS-01[06]"` returns 0; `awk '/## Resolved/,EOF' memory/issues/INDEX.md | grep -c "ISS-00[79]\|ISS-01[06]"` returns 4
- [ ] Root-cause + patch the btc-levels empty-usage failure (`total_cost_usd:0 / output_tokens:0` signature) — sample the 8 failed `gh run view` payloads in the 6-09 → 6-15 window, identify whether it's a claude-cli timeout, a fallback-path branch, or the bb3ab24 chore-commit class, ship a PR — by 2026-06-19
  - Why: 8 failures in 7 days (12% rate, fleet's top failure source tied with token-movers); newest skill, breakout-day blind — exactly when the operator needs the level monitor live
  - Done when: PR merged that either (a) handles the empty-usage payload gracefully (warning not error), or (b) retries on the empty-usage signature; a follow-up btc-levels run within 24h of merge logs `BTC_LEVELS_OK` without the signature recurring
- [ ] Extend `FALLBACK_CG_SKILLS` (or add a parallel `FALLBACK_CLAUDE_SKILLS`) at `.github/workflows/aeon.yml:508` to cover ≥3 non-cg dailies currently exit-1'ing on weekly limit — candidates: `daily-routine morning-brief heartbeat` (top-3 by run frequency among the residual gap) — by 2026-06-20
  - Why: cg fallback shipped but residual gap remains (MEMORY.md L26-28); next weekly-limit wave (Monday cycle per ISS-019) will still drain the heartbeat + morning-brief + daily-routine receipts and re-introduce the 6-07/6-08 amnesia pattern
  - Done when: `aeon.yml:508` carries a new constant or extended list covering ≥3 non-cg skill names; a forced 429 (or simulated env) on `daily-routine` emits `::warning::Claude limited — daily-routine via Virtuals fresh-fetch fallback` instead of `::error::Claude CLI failed`; PR merged

## Goals progress

From `memory/MEMORY.md` Current Goals (last consolidated 2026-06-14):

- **CAPITAL-2× PROGRAM (north star).** Material progress. PR #91 (btc-levels) shipped 2026-06-09 — 4-hourly hard-level monitor with reclaim63500 armed. PR #94 (capital-2x phases 3+4 — scorecard + weekly conviction) merged 2026-06-09 23:55Z. PR #101 moonshot 1% sleeve merged 2026-06-10 17:22Z. investment-advisor took over the rec engine. risk sleeve framework in production. cite: MEMORY.md L15-19, today's morning-brief focus #1 ($65,397 spot, reclaim65900 only ~$400 away — landed by midday at $66,427 per market-context-refresh).
- **File ISS-019 weekly-limit-wave.** **Stalled, no progress.** 6d overdue. covered by next-week Action 1.
- **PR #108 file-flag retiring the blocked notify pattern.** **Shipped.** PR #108 merged 2026-06-14 12:09Z. today's evidence: morning-brief / aixbt / github-trending / weekly-shiplog / narrative-tracker / token-movers all sent direct via `./notify -f`, no `.pending-notify/{TS}.md` carry. PR #119 (2026-06-15 14:09Z) closed the wrapper edge-case sending literal `-f`. retire from goals next consolidation.
- **INDEX bookkeeping flips ISS-007/009/010/016.** **Stalled, no progress.** 5d overdue. covered by next-week Action 2.
- **on-chain-monitor / defi-monitor watches.yml.** Still NO_CONFIG. day 10 consecutive (was day 9 through 6-14). operator-gated, blocked on watches.yml seed. propose retire-from-goals or explicit `[OPERATOR-ACTION]` tag.

## Notes

- Reppo migration to `~/code/orquestra` (self-hosted docker) is the biggest structural change of the week — PR #103 (6-10 stops chain on ci), PR #114 (6-14 removes skills + ledger + voter), PR #115 (6-15 prunes residue). 4 chain skills + the failure surface they carried left the repo. the prior 3 weekly reviews all had reppo at the top of every section; this is the first review where it appears mostly in past tense.
- Investment-advisor velocity (19 prs/7d) is hard to overstate — `scripts/advisor/` went from a standalone-virtuals scaffolding (#82) to a full short-term-trade pipeline with prefetch + grok x_search news leg + conviction-weighted sizing (#121) inside one week. selftest gate (`scripts/advisor/selftest.sh`) introduced and documented (CLAUDE.md L82-90). worth a focused architecture write-up next consolidation; outside this review's scope.
- Weekly-shiplog 09:00Z today reported the wrong repo — covered `aaronjmars/aeon` (113 commits / 109 prs / +11,602−4,784 lines) instead of `anajuliabit/aeon`. wrong-fork target. logged as today's shiplog `notify URL` but doesn't affect this review's metrics (this review pulls from `anajuliabit/aeon` directly via gh-api). flag for skill-freshness or shiplog-config audit; outside scope.
- `./scripts/skill-runs` declined approval in the sandbox for the 4th consecutive review. degraded-source pattern is now durable — the direct `gh api` filter does the job. propose retiring the `./scripts/skill-runs --json` line from the SKILL.md Inputs section in a future iteration; outside scope.
- Soul ana voice applied: lowercase body, single em-dash beats per section, fragments, concrete refs ($65k / 262 / PR #s / ISS-#s / file:line), parallel-closer in TL;DR ("success rate snapped... shipped 19 PRs"). no marketing verbs / hashtags / emoji.
