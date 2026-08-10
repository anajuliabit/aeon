# Weekly Review — 2026-08-10

## TL;DR

second fleet-wide usepod 402 event of the memory-window fired today 8-10 10:49Z-18:03Z+ (still active at write-time) — same signature as ISS-029 exactly 7 UTC-days ago. 14 skills stuck on `api.usepod.ai/v1/messages → Payment required`, first fail morning-brief 10:49Z, last fail 18:03Z, consec range 1-17. prior event self-healed in ~2h; this one crossing hour-7 with 0 successes today. 3 of 4 prior actions shipped (usepod diagnosis ISS-029.md → ISS-030.md filed + resolved, PR #165 merged 8-09 via pre-squash rebuild recipe, ci-skills-json shared-root cause fixed via PR #173); aixbt-pulse d43 slipped a 2nd consecutive week. top action for next week is **file ISS-031 + ship a `scripts/detect-usepod-402.sh` operator-page gate** — signature has now recurred 2× in 7d and the manual-detection loop is the load-bearing gap.

## Last week's actions — closed loop

From `articles/weekly-review-2026-08-03.md` "Next week — actions":

- **Action 1 — Diagnose usepod 402 cascade root-cause + file ISS-029.md by 2026-08-05: SHIPPED T-0.** `memory/issues/ISS-029.md` exists (frontmatter `resolved_at: 2026-08-04T18:19:52Z`, category `missing-secret`). Filed by reflect 8-03T20:14Z not weekly-review. Documented usepod self-heal ~2h window (8-03 18:27Z last-402 → 20:14Z next-batch-clean). Also opened ISS-030 same run for the cost-report `sdk_opt_in_required` follow-on. Both rows in INDEX.md open-table. **Caveat: same signature is fleet-wide again today** — see Add finding.
- **Action 2 — Investigate aixbt-pulse d36 dead-slot + create `memory/topics/scheduler-primitives.md` by 2026-08-07: SLIPPED (2-consec-week).** `ls memory/topics/scheduler-primitives.md` returns "No such file". aixbt-pulse `last_success 2026-06-28T21:21:07Z` unchanged, slot rolled d36 → **d43**. Same slip shape as prior week; action must be reframed or retired. See Action 3 below.
- **Action 3 — Resolve PR #165 (docs skill-graph, d15) by 2026-08-10: SHIPPED T-1.** `gh pr view 165 --json state` returns `MERGED` at 2026-08-09T13:00:59Z. Not via straight rebase — root cause was pre-squash-history (main squashed to single commit `e6da7438`; PR head carried 5895 commits from before the squash → `git merge-base` empty → "refusing to merge unrelated histories"). Fresh branch off main + cherry-pick load-bearing deliverables + force-push-with-lease. Recipe generalized same day to PRs #172 + #173.
- **Action 4 — Investigate ci-skills-json shared root-cause on PRs #171 + #172 by 2026-08-06: SHIPPED delayed T+3.** Root cause was: SKILL.md edits landed without regenerating `skills.json`, tripping the `ci-skills-json` staleness gate. Fix shipped via PR #173 (`fix(claude): require skills.json regen when editing SKILL.md`), merged 8-09T11:15Z (squash `f866fd37`). Adds mandatory `./generate-skills-json` step to CLAUDE.md `## Rules` section. Both blocked PRs merged same batch: #171 8-09T12:52Z, #172 8-09T11:51Z.

Result: **3 shipped / 1 slipped of 4.** Better than prior week's 2/1/1. The Sunday-batch rebuild recipe is the load-bearing win — 4 stuck PRs (#165 + #171 + #172 + #173) cleared same day via generalized cherry-pick-onto-fresh-main pattern. Slip is aixbt-pulse for the second straight week — action needs retirement, not another rewrite.

## Metrics

Window: 2026-08-03T19:30:00Z → 2026-08-10T19:30:00Z. Prior week: 2026-07-27T19Z → 2026-08-03T19:30Z.

| Metric | This week | Prior week | Δ |
|---|---|---|---|
| Skill successes 8-03 → 8-10 (per cron-state `last_success`) | 30 of 43 skills had ≥1 success | 41 of 43 | −11 |
| Skills failing at write-time (18:03Z 8-10, usepod 402) | 14 | 0 (post-cascade recovery same day) | +14 |
| Skills with 0 successes today (8-10) | 43/43 | — | — |
| Fleet clean-consec streak 8-04 21:48Z → 8-10 10:48Z | 5.5 UTC-days (crashed at morning-brief 10:49Z) | broken 8-03 by ISS-029 | — |
| Articles written 8-03 → 8-09 (excl. this week's review) | 11 | 9 | +2 |
| Notifications ./notify SENT (grep `notify -f`/`SENT` in logs) | ~204 (23+36+53+10+50+37+25) | — | — |
| New issues opened | 1 (ISS-030 8-04) | 1 (ISS-029 8-03) | 0 |
| Issues resolved | 1 (ISS-029 8-04) | 0 | +1 |
| PRs merged this week | 6 (#165, #171, #172, #173, #175, #178) | 4 | +2 |
| PRs opened this week + still open | 3 (#174 8-08, #176 8-09, #177 8-09) | 2 | +1 |
| Real-work commits (non-chore, non-scheduler) | 5 (all merged 8-09 batch) | 4 | +1 |
| Chore commits (cron + scheduler) 8-03 → 8-10 | 533 total; 107 chore(cron):failed on 8-10 alone | — | — |

Sources: `jq` on `memory/cron-state.json` for skill success/failure/consec state (fidelity preserved via structured cron-state; `./scripts/skill-runs` blocked in sandbox 13th consecutive week — `_degraded source_`). `git log --after "2026-08-03 19:00" --before "2026-08-10 19:00"` for commits + `grep -v ^chore` for real work. `gh pr list --search "updated:>=2026-08-03"` for PR states. `grep -c "SENT\|notify -f"` on `memory/logs/2026-08-0[3-9].md` for notification counts.

**Fleet-wide usepod 402 event 8-10 — active at write-time (18:03Z→):**
- **First fail:** morning-brief 2026-08-10T10:49:18Z (consec=7 at write-time)
- **Latest fail:** heartbeat 2026-08-10T18:03:45Z (consec=10)
- **14 skills stuck:** heartbeat (10), agent-buzz (2), skill-freshness (13), goal-tracker (3), skill-health (1), reflect (1), action-converter (1), cost-report (15), weekly-shiplog (12), daily-routine (14), security-digest (8), list-digest (3), thought-review (15), (btc-levels 17 same-window, +search-skill/unlock-monitor/github-trending/token-alert/deal-flow/skill-security-scan intermittent)
- **Signature:** `api.usepod.ai/v1/messages → "Payment required. Retry the same request with an X-PAYMENT or PAYMENT-SIGNATURE header"` — same string as ISS-029 8-03
- **Duration at write-time:** ~7h 15min unbroken (10:49Z → 18:04Z+). ISS-029 self-healed in ~2h; this event now 3.5× longer.
- **Successful skills today:** 0/43.

**Skills that succeeded any day in window (30):** skill-evals, evening-recap, thought-review (last 8-09 21:32Z), btc-levels, heartbeat, fork-skill-digest, skill-update-check, action-converter, skill-health, reflect, goal-tracker, self-improve, agent-buzz, skill-graph, list-digest, security-digest, token-alert, github-trending, skill-freshness, daily-routine, morning-brief, vuln-scanner, skill-analytics, reg-monitor, cost-report (8-04 21:48Z only), deal-flow, unlock-monitor, search-skill, plus btc-levels/skill-security-scan intermittent. 13 skills went the full 7d with no success (chain:investment-advisor + defi-overview / token-pick / on-chain-monitor / defi-monitor / aixbt-pulse / narrative-tracker / market-context-refresh + 5 others all last_success ≥14d ago).

**Cancellations breakdown (0 in cron-state):** Investment Advisor 7/7 clean this week (PR #164 fix holds 21 consec ticks); superseded by PRs #175 + #178 which retire the pipeline entirely (see Notes).

**aixbt-pulse fires 8-03 → 8-10: 0.** d43 dead-slot, same signature as ISS-027 batch-dark cluster. 2-consec-week slip on the same investigation action.

## Findings (KALM, prioritized)

Scoring: **Frequency × Impact ÷ Effort** (1-5 each). Top 5 kept, rest dropped.

### Keep

- **Operator Sunday-batch cadence held + amplified 8-09** (priority 15 — F5×I3÷E1). 4 PRs cleared in single afternoon: #173 11:15Z, #172 11:51Z, #175 11:42Z, #165 13:00Z, #171 12:52Z, #178 22:26Z = **6 PRs merged 8-09** (best single-day ship-throughput in memory-window). Queue collapsed 5 → 1 (only #174 Advisor Brier-weight remains open). CLAUDE.md line 191 codified cadence held under load. Do not touch — the cadence is working.

- **Pre-squash-history rebuild recipe generalizes** (priority 12 — F4×I3÷E1). Root-cause diagnosis: main squashed to single commit `e6da7438` → PR heads carrying pre-squash commits produce `git merge-base` empty → "refusing to merge unrelated histories" unresolvable by rebase. Fix: `git checkout -b tmp-rebuild-N main && git cherry-pick <load-bearing-only> && git push --force-with-lease origin <head-ref>`. Applied 3× same day (#173 11:15Z, #172 11:50Z, #165 13:09Z). NEW `[[pre-squash-history-rebuild-recipe]]` observation per MEMORY.md line 21. Do not lose the recipe — it's the only working path for any remaining pre-squash PRs.

### Add

- **Fleet-wide usepod 402 recurs 8-10 = 2nd event in 7d, same signature as ISS-029** (priority 12.5 — F5×I5÷E2). First fail 10:49Z (morning-brief consec=7), still active at 18:04Z write-time (heartbeat consec=10). 14 skills stuck on `api.usepod.ai/v1/messages → Payment required`. Duration already 3.5× ISS-029's 2h self-heal window. **The 8-03 event's diagnosis (ISS-029: usepod-side transient, operator-gated, no code fix) means Aeon has no self-repair path** — this is what recurrence looks like when the mitigation is "wait it out". Missing gate: no automated operator-page path when the signature reappears. See Action 1.

- **weekly-shiplog dark d20** (priority 6 — F4×I3÷E2). `last_success 2026-07-20T10:55:26Z`, consec=12 at 18:03Z 8-10, 7d cadence but 20 UTC-days silent = fleet governance-signal blind. Sits on the same surface as aixbt-pulse d43 (both "silent scheduled skill without diagnosis"), and just crossed 2× the cadence for the first time in the memory-window. If this drifts another week it enters the same 2-consec-slip class as aixbt-pulse. See Action 2.

### Less

- **aixbt-pulse d43 dead-slot investigation-action, 2-consec-week slip** (priority 1.5 — F3×I2÷E4). Same SMART action authored 2 weeks running; slipped both times. Operator-gated / same-class as ISS-027 8-skill batch-dark; the mechanical fix (workflow file audit + cron string check) hasn't happened either week. Continuing to author the same action-cycle line item just churns priority-slots without shipping. Retire from action-cycle; move to `memory/topics/scheduler-primitives.md` as wontfix-until-scheduler-rebuild-scoped. See Action 3.

- **chronic-cohort-alone-degraded regime observation-only cycles** (priority 2 — F3×I2÷E3). 10-skill sub-50% cohort composition-locked across 11-consec-heartbeat-tick ~119h span 8-04 → 8-09 per MEMORY.md line 6, deepest composition-identity print in memory-window. Heartbeat + skill-health surface it every tick; 0 self-improve PRs opened to address any of the 10. The observation is durable + accurate, but eats memory + heartbeat cycles without shipping a fix. Not action-shaped this week (fleet-wide 402 absorbs the priority-slot); flag for reflect scope.

### More

- **Self-improve queue picked up during 8-09 batch window** (priority 8 — F4×I3÷E2). 3 fresh PRs opened 8-09 alone (#175 11:35Z, #176 17:10Z, #177 18:18Z, #178 22:25Z merged same day) = 4-PR-in-24h burst on the batch day. Under-invested surface: authoring _into_ the batch window is when merges are most likely; the queue-full self-improve exit-gate that engaged 8-07 disengaged 8-09 at queue=1, so authoring capacity is available. Reroute self-improve to prioritize authoring on batch-day Sunday/eve-of-Sunday rather than mid-week. Not action-shaped this week (structural feedback for reflect); noted.

### Dropped from priority threshold

- **ISS-030 cost-report SDK opt-in day-6** — deciding-test 8-10 Mon 07Z FAILED but via unrelated 402 not the SDK signature (today's failures are all `Payment required`, not `sdk_opt_in_required`). Test inconclusive; issue rolls forward without new signal. No action.
- **Operator on-chain config day-64** — operator-owned, needs secrets + config file, no automation path.
- **priorities.md 66d stale, vault inbox 49d cold streak** — operator-owned, no automated nudge per thought-review spec.
- **12:00 UTC batch DARK day-43** — same-class as aixbt-pulse d43; ISS-027 tracked, no fresh signal.
- **ISS-028 workaround-chain n=36+ 18-UTC-day span** — durable, but PR #167 already retired the main-thread surfaces + PR #177 (open) documents the sub-agent + append surfaces. Not action-shaped this week.

## Next week — actions

3 actions clear priority threshold. Action 1 is fleet-critical and belongs on the operator's inbox _tonight_, not next Sunday.

- [ ] **File `memory/issues/ISS-031.md` for the 8-10 usepod 402 recurrence + ship `scripts/detect-usepod-402.sh` operator-page gate** by **2026-08-13** (72h from now).
  - Why: usepod 402 signature has now recurred 2× in 7d (8-03 + 8-10). Today's event crossed 7h at write-time = 3.5× the prior event's 2h self-heal window. ISS-029's diagnosis (operator-gated, no code fix) means Aeon has no self-repair — but Aeon _can_ shorten the manual-detection loop from "operator reads next digest / notice hours later" to "operator gets ./notify-pinged within 30min of 3rd consec-failed skill same-signature".
  - Done when: `memory/issues/ISS-031.md` exists with YAML frontmatter (`category: api-change`, cross-links to ISS-029 + ISS-030); INDEX.md open-table has ISS-031 row; `scripts/detect-usepod-402.sh` exists + runs against `memory/cron-state.json` (exit 0 = quiet, exit ≥1 = ./notify SENT with the 3+ failing skill list); the script is wired into the heartbeat prefetch step OR gated by cron every 15min; a fix PR (self-improve or direct) merges before deadline.

- [ ] **Diagnose weekly-shiplog dark d20 root cause + open a fix PR OR file ISS-032** by **2026-08-14** (96h from now).
  - Why: 7d-cadence skill 20 UTC-days silent = 2× cadence crossed for the first time in memory-window. Fleet governance-signal blind. Same silent-scheduled-skill shape as aixbt-pulse d43 (which just slipped a 2nd consecutive week). Prevent third-week slip class from forming; catch this one before the same "roll-forward + no diagnosis" trap.
  - Done when: `.github/workflows/aeon.yml` gets a diff touching weekly-shiplog's schedule/trigger and a fix PR opens, OR `memory/issues/ISS-032.md` exists with root-cause diagnosis + operator-escalation-or-fix-path, OR the skill fires clean at least 1× in the window (proving self-heal without diagnosis, which is 3rd-tier acceptable).

- [ ] **Retire aixbt-pulse d43 investigation from weekly-review action-cycle → move to `memory/topics/scheduler-primitives.md` as wontfix-until-scheduler-rebuild** by **2026-08-13** (72h from now).
  - Why: 2-consec-week slip on same SMART action shape (2026-07-27 + 2026-08-03 both authored + slipped). Operator-gated / same-class as ISS-027 batch-dark cluster d43. Keeping the same investigation-action every Sunday just eats a priority-slot; retirement into a topic file preserves the observation without action-churn.
  - Done when: `memory/topics/scheduler-primitives.md` file exists with (a) aixbt-pulse d43 + ISS-027 8-skill batch-dark cluster cross-linked, (b) explicit wontfix-until-scheduler-rebuild scope note, (c) MEMORY.md `## Current Goals` no longer carries aixbt-pulse as an action-cycle line (either removed or reframed as "operator-gated / no action / see [[scheduler-primitives]]"), (d) next 3 weekly-reviews do not authorize an aixbt-pulse investigation action.

(Action 4 candidate — "rebase + push PR #174 Brier-weight so CI fires + it enters operator batch window" — dropped from top 3. Priority 4 raw; #174 opened 8-08 = only d3 at write-time, not yet in stall territory. Note for next-week review, no action this cycle.)

## Goals progress

From `memory/MEMORY.md` `## Current Goals` (last consolidated 2026-08-09):

- **ISS-030 cost-report OPEN pending 8-10 Mon 07Z deciding-test** — deciding-test INCONCLUSIVE. Today's cost-report failure at 18:03Z is the fleet-wide 402, not the `sdk_opt_in_required` signature. `consec=15` chronic sr=9% (7/93) durable; last_success 2026-08-04T21:48Z = 5.8 UTC-days silent. Signature test rolls forward until a non-402 tick fires. No action.
- **chronic-cohort-alone-degraded 11-consec-heartbeat-tick ~119h span** — STABLE + broken by fleet-wide 402 today (all skills fail, cohort composition irrelevant while everyone is red). Regime observation resumes when fleet recovers. Under Less finding, no action.
- **ISS-028 workaround-chain n=36+ durable 18-UTC-day span** — STABLE. PR #177 (`fix(claude-md): document ISS-028 file-redirect sandbox block`, opened 8-09 18:18Z) covers the doc-gap on the sub-agent + append surfaces. Rolls forward for reflect + operator-decision on #177; no weekly-review action.
- **12:00 UTC batch DARK day-43** — STABLE. `[[12Z-slot-dark-immunity-per-skill]]` 4-consec clean token-alert print confirms per-skill scoping. Rolls under Action 3 (retirement into scheduler-primitives.md alongside aixbt-pulse d43).
- **PR queue at 1 on 8-09** — CLEARED via 8-09 Sunday batch (5 → 1); only #174 open pre-write. Grew to 3 open post-write (#174 + #176 + #177 opened 8-09). Under structural "More" observation, no action.
- **Operator on-chain config day-64 → day-65** — advanced 1d, defi-monitor NO_CONFIG. Operator-gated, no action.
- **priorities.md 66d → 67d stale + vault inbox 49d → 50d cold** — advanced 1d, operator-owned, no action.

New goals implicit from this week: **usepod 402 recurrence pattern is now a repeated-signature not one-off** — Action 1 files ISS-031 which frames the pattern (not the individual outage). Weekly-review 2026-08-17 will read whether the auto-detect gate shipped + whether a 3rd recurrence hit.

## Notes

- **The biggest signal of the week is the recurrence shape** — same signature, same blast radius (14+ skills), longer duration (>7h vs 2h), same operator-gated fix pathway. 2× in 7d = signature has crossed one-off → pattern threshold. This is the exact shape where a runbook + auto-page is worth more than another retroactive diagnosis.
- **Advisor pipeline retired 8-09** — PR #175 (`feat(advisor): stop posting picks`) merged 11:42Z + PR #178 (`chore(advisor): disable the cron schedules`) merged 22:26Z. `investiments` removed the track record so posting was pulling stale conviction. Investment Advisor 7/7 clean this week is the last data point on that pipeline before it goes quiet by design. Not a Keep or a Less — a retirement.
- **PR queue swap 8-09 = 5-out / 4-in same day** — merged #173/#172/#171/#165/#175/#178, opened #175 (merged same day)/#176/#177/#178 (merged same day). Net open after batch = #174 + #176 + #177 = 3. Under structural "More" observation: self-improve authoring capacity is highest on the eve of + during the operator batch window, and this cycle proved it.
- **Fleet clean-consec d5 held through 8-10 10:48Z, crashed 10:49Z with morning-brief 402** — 5.5 UTC-days unbroken from 8-04 21:48Z ISS-029 recovery to today's 10:49Z first-fail. Cleanest streak in memory-window bookended by two same-signature fleet events exactly 7d apart.
- **PR #167 bash-redirect fix continues holding on merged surfaces** — sub-agent + URL-encoded + append + compound-pipeline surfaces still block per ISS-028 workaround-chain n=36+ (memory-window durability 18 UTC-days 7-22 → 8-09). PR #177 documents the gap without extending the fix; extending is a future cycle.
- **cost-report ISS-030 deciding-test inconclusive** — today's 07Z cost-report tick failed with 402 not sdk_opt_in_required, so the 4-consec-week formal-pattern threshold does not advance. Rolls forward without new signal; do not close ISS-030.
- **13 skills went the full 7d with 0 successes** — chain:investment-advisor (retired by #175 + #178), defi-overview, token-pick, on-chain-monitor, defi-monitor, narrative-tracker, market-context-refresh, plus the ISS-027 batch cluster remnants. Same shape as prior week; retirement-via-topic-file is the working pattern to keep memory clean.
- **Voice ana applied**: lowercase body, single em-dash per section where it earns a beat, terse verdict lines (`SHIPPED T-0`, `SHIPPED T-1`, `SHIPPED delayed T+3`, `SLIPPED 2-consec-week`, `INCONCLUSIVE`), concrete refs (PR#s / commit hashes / signatures / consec counts / dates / delta counts / relative dates T±N), no marketing verbs / hashtags / emoji, no "in summary" / "tldr:" recap ending.
