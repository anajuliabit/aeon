# Weekly Review — 2026-08-17

## TL;DR

zero operator PR merges in 7d = memory-window-deepest single-window stall. queue grew 3 → 6 (+#179 +#180 +#181), #174 Brier-weight now 9d 19h = deepest single-PR stall in memory. offsetting it: **memory-window-first full-cohort natural recovery** — mon-batch 4/4 stuck skills (unlock-monitor 10:37Z + search-skill 14Z + deal-flow 14:07Z + skill-security-scan 16Z) all cleared 8-17 via direct-exec bypass on the 8-10 usepod-402 cohort, and fork-cohort self-healed sunday 8-16 19:30Z after 6d 2h stuck. of last week's 3 SMART actions: 1 shipped (weekly-shiplog self-healed 8-17 09:06Z), 2 slipped (scripts/detect-usepod-402.sh +4d overdue, memory/topics/scheduler-primitives.md 2nd-consec-week slip). top action next week is **ship scripts/detect-usepod-402.sh + wire into heartbeat** — the manual-detection loop has now cost aeon a 2nd 7d cycle to a re-shipping action.

## Last week's actions — closed loop

From `articles/weekly-review-2026-08-10.md` "Next week — actions":

- **Action 1 — File ISS-031.md + ship `scripts/detect-usepod-402.sh` operator-page gate by 2026-08-13: PARTIAL / +4d overdue.** `memory/issues/ISS-031.md` exists (filed 8-10 19:14Z by skill-health, not weekly-review; INDEX.md open-table row present; two update sections 8-11 + 8-13). Cross-links to ISS-029 + ISS-030 present. **But `scripts/detect-usepod-402.sh` DOES NOT EXIST** — `ls scripts/detect-usepod-402.sh` = no such file, `git log --all --oneline` empty for the path. Heartbeat prefetch step un-wired. No fix PR. Overdue by 4 UTC-days at write-time. The gate that would have shortened the manual-detection loop on any 3rd recurrence still isn't in place. See Action 1 next week — re-authored, deadline tightened.
- **Action 2 — Diagnose weekly-shiplog dark d20 root cause + open fix PR OR file ISS-032 by 2026-08-14: SHIPPED via 3rd-tier acceptable (self-heal).** No fix PR opened. No `ISS-032.md` filed (memory/issues/ ls empty of ISS-032). But `weekly-shiplog` `last_success 2026-08-17T09:06:38Z` per cron-state — skill fired clean 8-17 morning, `articles/weekly-shiplog-2026-08-17.md` exists (7-commit / 7-PR post-surge tail digest). Self-heal-without-diagnosis path (which SKILL step 6 explicitly marked "3rd-tier acceptable, proves self-heal") landed 3d late but landed. No root cause identified — if it goes dark again the diagnosis debt returns.
- **Action 3 — Retire aixbt-pulse d43 → move to `memory/topics/scheduler-primitives.md` as wontfix-until-scheduler-rebuild by 2026-08-13: SLIPPED (2-consec-week same-action shape).** `ls memory/topics/scheduler-primitives.md` = no such file. `memory/MEMORY.md` Current Goals section (line 5-11) doesn't carry aixbt-pulse as a line at all now — but the retirement pathway prescribed (topic file + cross-link) never got written. Third-week authoring risk: if the same SMART action re-appears in Next-week 2026-08-17 → 2026-08-24, the retirement itself becomes the churn the retirement was supposed to prevent. Drop the action shape entirely this cycle.

Result: **1 shipped (via self-heal) / 2 slipped of 3.** Worse than prior week's 3/1 of 4. Both slips are Aeon-authored actions that need Aeon-shipped code — not operator-gated. The manual-detection gate slip is the load-bearing one: same-signature usepod events (ISS-029 + ISS-031) recurred once already, and the automation gap Aeon promised to close remains open through a 2nd 7d cycle.

## Metrics

Window: 2026-08-10T19:30:00Z → 2026-08-17T19:30:00Z. Prior week: 2026-08-03T19:30:00Z → 2026-08-10T19:30:00Z.

| Metric | This week | Prior week | Δ |
|---|---|---|---|
| Skills with ≥1 success in window (of 60 tracked) | 31 | 30 | +1 |
| Skills consec≥3 at write-time (CRITICAL cohort) | 1 (cost-report c=14 sr=0.07) | 14 mid-cascade | −13 |
| Skills with last_failed in window | 2 (cost-report, fork-skill-digest) | ~20 (ISS-031 wave) | −18 |
| Articles written (non-freshness) | 12 | 10 | +2 |
| Skill-freshness daily articles | 6 (8-11 → 8-17) | 6 | 0 |
| Notifications sent (grep SENT in logs) | 198 | 90 | +108 (2.2×) |
| New issues opened | 0 | 1 (ISS-031, filed 8-10 19:14Z technically prior-window) | −1 |
| Issues resolved | 0 | 0 | 0 |
| **PRs merged in window** | **0** | 6 (#165, #171, #172, #173, #175, #178) | **−6** |
| PRs opened in window + still open | 3 (#179 8-11, #180 8-13, #181 8-16) | 3 (#174 8-08, #176 8-09, #177 8-09) | 0 |
| Total open PR queue at write-time | 6 (#174 / #176 / #177 / #179 / #180 / #181) | 3 | +3 |
| Oldest open PR at write-time | #174 9d 19h (memory-window-deepest single-PR stall) | #174 2d 19h | +7d |
| Commits in window (all) | 593 | ~830 | −237 |
| Non-chore / non-auto-commit code commits | 0 | 5 | −5 |

Sources: `jq` on `memory/cron-state.json` for skill success/failure counts + consec + sr (fidelity preserved; `./scripts/skill-runs` needs approval in sandbox, `_degraded source_` per SKILL fallback). `gh api repos/anajuliabit/aeon/commits --paginate --since 2026-08-10T19:00:00Z` for commit count (593). `gh pr list --state merged --search "merged:>=2026-08-10"` = empty. `gh pr list --state all --search "created:>=2026-08-10"` for 3 opened PRs. `gh pr list --state open` for full queue (6). `grep -c "SENT" memory/logs/2026-08-1{1..7}.md` for notification count. `ls articles/` filtered `2026-08-1[0-7]` for article count.

**Fleet health snapshot at write-time (8-17T19:30Z):**
- CRITICAL (consec ≥3): 1 skill (cost-report c=14, chronic ISS-030 signature `sdk_opt_in_required` per skill-health)
- WARNING (consec 1-2): 0 skills
- ISS-031 stuck-cohort at write-time: 0 (all 4 mon-batch cleared 8-17 via direct-exec bypass)
- Fork-cohort at write-time: OK (last_success 8-16 19:30Z organic recovery, 8/8 sr=1.00)
- Aeon-fleet clean d18 (0/45 fresh malware match tracked deps, 18-consec-day span)
- Heartbeat 7-consec-clean since 8-15 crash
- CG clean-day d56

**cost-report Mon 07Z chronic re-fire held**: consec=1 → 14 today via 8+ retry-failures 08:00Z → 18:30Z, sr=8% → 7%. Same ISS-030 signature (`sdk_opt_in_required`), not usepod-402. Chronic pattern on scheduler retry loop — the workflow's own retry policy is doubling the notify-cost of the failure.

**Articles this week (12 non-freshness):** cost-report 8-11, fork-cohort 8-16, fork-skill-digest 8-16, security-scan 8-17, skill-analytics 8-12, skill-evals 8-16, vuln-scan 8-15, weekly-shiplog 8-17, plus this weekly-review + prior weekly-review 8-10 fetched into window + 6 skill-freshness dailies.

## Findings (KALM, prioritized)

Scoring: **Frequency × Impact ÷ Effort** (1-5 each). Top 5 kept.

### Keep

- **Direct-exec bypass path clears mon-batch 4/4 same day** (priority 15 — F5×I3÷E1). Memory-window-first full-cohort natural clear of an ISS-031-stuck cohort. Evidence: `unlock-monitor last_success 2026-08-17T10:37:26Z` (168h+ stuck since 8-10 15:10Z) + `search-skill 14:10Z` + `deal-flow 14:12Z` + `skill-security-scan 17:07Z` — all cron-state confirmed. Chain-runner + direct-exec-through-Claude-Code path holds under load, does NOT route through usepod dispatcher. Codify: this is the mitigation-path the ISS-031 postmortem was missing. Do not touch.

- **Sunday-cadence self-heal absorbed the weekly-shiplog dark d20 slip** (priority 8 — F4×I2÷E1). `weekly-shiplog last_success 2026-08-17T09:06:38Z` per cron-state → `articles/weekly-shiplog-2026-08-17.md` exists (7-commit post-surge tail digest). The 3rd-tier "self-heal wins" fallback in prior week's Action 2 landed 3d after deadline but landed. Fork-cohort natural recovery 8-16 19:30Z (same shape — 6d 2h stuck-state → clean natural fire, `[[fork-cohort]] sr=1.00 total_runs=8`) confirms the pattern isn't luck. The sunday tick is doing the healing work when Aeon's ships can't.

### Add

- **Ship `scripts/detect-usepod-402.sh` + wire into heartbeat prefetch** (priority 15 — F5×I5÷E3). Auto-detect gate has now missed one full 7d cycle post-authorship. ISS-031 mitigation path (direct-exec bypass) proven this week, but detection latency remains "operator reads next digest hours later" — the exact loop the gate was supposed to shorten. If ISS-029 → ISS-031 recurrence cadence holds (~7d), the 3rd event is due 2026-08-17 or later, and the gate would already have been earning its keep. Highest-priority action, re-authored below.

- **Rebase or close PR #174 (Brier-weight Advisor)** (priority 10 — F4×I3÷E1.5). Opened 2026-08-08T00:31:19Z, 9d 19h at write-time = **memory-window-deepest single-PR stall** and 2nd consecutive weekly-review it appears in the queue. `mergeable=UNKNOWN`, statusCheckRollup empty, likely pre-squash-history rebase needed (same recipe used 8-09 batch). Advisor pipeline itself was retired 8-09 via #175 + #178, so #174's underlying purpose (Brier-weight the analyst vote) may already be moot — decide-then-act, don't roll a 3rd weekly-review with it in inventory.

### Less

- **cost-report scheduler retry-loop noise** (priority 8 — F5×I2÷E1). 8+ retry-failures between 08:00Z and 18:30Z today alone, consec=1 → 14 over 24h. Every failed retry emits a `chore(cron): cost-report failed` commit into main + fires notify-noise on the CRITICAL rail. ISS-030 already known chronic sr=7%. The retry policy is doubling the load without doubling the diagnostic surface — one clean fail per scheduled tick would surface the same signal at 8× less commit-log churn.

- **Self-improve PR authoring while queue-full exit-gate ENGAGED n=3** (priority 6 — F4×I2÷E1.5). Queue grew 3 → 6 this week via #179 + #180 + #181 authored under exit-gate condition (per MEMORY.md line 6 + `skills/self-improve/SKILL.md` step 1). Each new fix-PR is well-scoped individually but the compound effect is: operator's sunday-batch surface area doubled from 3 → 6 PRs to triage without a single merge in-window. Authoring capacity should route to bug-list / test-shim shape (that doesn't add to review load) until queue drains below n=3.

### More

- Not action-shaped this week — the top-3 priority slots are already filled by Add + Keep actions above. Structural observation for next reflect scope: the direct-exec bypass pattern (Keep #1) should be documented as a reusable primitive in `memory/topics/fleet.md` so the same recovery is one-command instead of skill-by-skill next time a cohort gets stuck.

### Dropped from priority threshold

- **ISS-030 cost-report chronic** — no new signal; 4th deciding-test-window rolled forward under 402 noise. Aeon-side observation-only, operator-gated to add SDK-opt-in header. No action.
- **Operator on-chain config day-72** — operator-owned, no automation path.
- **priorities.md 74d stale + 11-consec zero-capture-day** — operator-owned; thought-review 07:31Z refresh-ask d7 unactioned; no automated nudge per spec.
- **ISS-028 workaround-chain n=49+ 26-UTC-day span** — durable + tracked; PR #177 (open) is the doc-gap fix, no fresh call-site work to author while #177 pends.
- **12:00 UTC batch DARK d51** — same-class as retired aixbt-pulse d43; ISS-027 tracked, no fresh signal, no operator-side action requested.
- **Aixbt-pulse d51 dead-slot** — retirement action itself now 2-consec-week slipped; dropping the action from action-cycle per Action 3 note (removed, not re-authored).

## Next week — actions

3 actions clear priority threshold. Action 1 is a re-ship of last week's Action 1 with tighter deadline + explicit non-op-gated ownership.

- [ ] **Ship `scripts/detect-usepod-402.sh` + wire into heartbeat prefetch (or every-15min cron)** by **2026-08-20** (72h from now).
  - Why: same authored action slipped last week +4d overdue. Detection loop is still manual = operator reads digest N hours after the 3rd consec-failed skill hits. Direct-exec bypass (Keep #1) proves the mitigation exists; the gate is what routes operator to invoke it fast. Aeon-side code, not operator-gated.
  - Done when: `scripts/detect-usepod-402.sh` exists + is executable + runs against `memory/cron-state.json` + exits 0 quiet / ≥1 with `./notify` fired on 3+ skills consec≥3 sharing the 402 signature; the script is invoked from heartbeat's prefetch step OR from a new every-15min cron entry in `.github/workflows/aeon.yml`; a fix PR merges before deadline.

- [ ] **Rebase or close PR #174 (Brier-weight Advisor)** by **2026-08-20** (72h from now).
  - Why: #174 at 9d 19h = deepest single-PR stall in memory-window, 2nd weekly-review appearance. Advisor pipeline retired via #175 + #178 8-09, so #174 may be moot — decide + act rather than let the review carry it a 3rd cycle. Pre-squash-history rebase recipe (per `[[pre-squash-history-rebuild-recipe]]`) is the working path if the change is still relevant.
  - Done when: EITHER `gh pr view 174 --json state` returns `MERGED`, OR `gh pr view 174 --json state` returns `CLOSED` with a comment linking #175/#178 as the retirement PRs that supersede it. A 3rd cycle carrying #174 with no action = do-nothing failure mode.

- [ ] **Document direct-exec bypass path as reusable recovery primitive in `memory/topics/fleet.md`** by **2026-08-21** (96h from now).
  - Why: Keep-finding #1 = memory-window-first full-cohort recovery via bypass, 4 skills cleared same day. The mechanism (direct Claude Code invocation, skipping usepod dispatcher) is not yet named or documented anywhere reusable — next stuck-cohort event, next-Aeon-in-context has to re-discover it. One-command primitive with copy-pasteable invocation would collapse the recovery from N skill-by-skill decisions to a routine.
  - Done when: `memory/topics/fleet.md` has a section titled `## Recovery primitives / direct-exec bypass` with (a) the invocation shape, (b) when it applies (usepod-402 or similar dispatcher stall), (c) the 4-skill mon-batch 8-17 as the reference case, (d) links from `memory/issues/ISS-031.md` back into that section, (e) MEMORY.md `[[recovery-bypass-direct-exec]]` link added.

(Action-4 candidate — "cost-report retry-loop dampener: one-fail-per-tick instead of 8+" — priority 8 raw; deferred to next-week note. Change is a workflow tweak but the surface belongs in ISS-030 close-out, not weekly-review.)

## Goals progress

From `memory/MEMORY.md` `## Current Goals` (last consolidated 2026-08-17):

- **ISS-031 detect-usepod-402 gate +4d overdue** — SLIPPED (see Action 1 close-loop). Re-authored with tighter deadline. Bypass mitigation exists (Keep #1) — this closes the detection latency gap alongside it.
- **Self-improve PR queue exit-gate ENGAGED n=3** — HELD + WORSENED. Queue grew 3 → 6 in-window (#179 + #180 + #181 authored). Exit-gate contract per `skills/self-improve/SKILL.md` step 1 says "pauses new authoring until operator clears queue" — 0 operator merges in window = pause was earned but not observed. Under Less-finding #2, structural.
- **PR queue at 5 on 8-15 / 6 on 8-17** — GREW. Composition: #174 (9d 19h) / #176 (8d) / #177 (8d) / #179 (5d) / #180 (3d) / #181 (~1d). Three PRs (#174, #176, #177) now cross CLAUDE.md's 7d weekly-review stall band. #174 is memory-window-deepest single-PR stall. Actions 2 addresses #174 directly.
- **chronic-cohort-alone-degraded regime ~264h+ span** — STABLE. 13-skill composition-locked; unlock-monitor moved OUT of stuck-cohort but stays IN chronic-cohort at sr=41%. No action-shaped surface this week; reflect + heartbeat track.
- **12:00 UTC batch DARK d51** — STABLE. Same-class as retired aixbt-pulse. `[[12Z-slot-dark-immunity-per-skill]]` 10-consec BROKE via token-alert 12:11Z GITLAWB fire. No action.
- **Operator on-chain config day-72** — STABLE. Operator-gated, no automation path.
- **priorities.md 74d stale + vault inbox 56d cold + 11-consec zero-capture-day** — WORSENED (record extends 10 → 11 days). Operator-owned, no automated nudge available per thought-review spec. Refresh-ask 8-10 T-0 now d7 unactioned.

New goal implicit from this week: **direct-exec bypass = recovery primitive**. Codify + link (Action 3). Next weekly-review 8-24 audits whether the primitive gets referenced by a stuck-cohort recovery in-window.

## Notes

- **Biggest signal of the week is the 0-merge stall**, not a single fleet-wide event. Prior week had 6-merge sunday batch; this week has 0 merges + 3 new opens = net queue +3. This is exactly the state CLAUDE.md line 191 exit-gate primitive was designed for, and per MEMORY.md it did engage — the observation is that authoring didn't pause.
- **Mon-batch full-cohort recovery via direct-exec bypass is the offsetting positive** — 4 stuck skills that had cost the fleet ~168h of downtime cleared in a single UTC-day. Memory-window-first for a stuck-cohort natural clear.
- **weekly-shiplog self-healed via natural sunday-morning fire** — Action 2's 3rd-tier acceptable clause caught the outcome; without that clause the metric would read as slip. Codify: SMART actions with a "self-heal-counts" tier are worth writing when the failure mode has a plausible auto-recovery path.
- **aixbt-pulse action retired via drop, not via topic-file** — 3-consec-week slip on retirement itself would have been ironic; dropping it entirely respects the "if can't make it SMART, drop the finding" constraint. MEMORY.md Current Goals already carries no aixbt-pulse line, which was the practical outcome the retirement action was supposed to produce.
- **cost-report retry-loop churn = 8+ chore(cron) commits per day** — worth an ISS-030 follow-up but not weekly-review action-shaped; it's a workflow policy tweak, one-line change, belongs in the ISS thread.
- **PR #167 bash-redirect fix continues holding on merged surfaces** — ISS-028 workaround-chain n=49+ 26-UTC-day span. PR #177 open, documents doc-gap on sub-agent + append surfaces. No fresh work this cycle.
- **Voice ana applied** — lowercase body, single em-dash per section where it earns a beat, terse verdict lines (`PARTIAL / +4d overdue`, `SHIPPED via 3rd-tier acceptable`, `SLIPPED (2-consec-week same-action shape)`), concrete refs (PR#s, timestamps to the second where cron-state supplies them, `consec=N sr=X.XX`, T±N relative dates), no marketing verbs / hashtags / emoji, no "in summary" / "tldr:" recap ending.
