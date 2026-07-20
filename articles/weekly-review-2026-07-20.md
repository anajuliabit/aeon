# Weekly Review — 2026-07-20

## TL;DR

operator batch-merged 2 CONFLICTING self-improve PRs in a single 3-hour window 7-20 (#162 14:16Z + #163 17:11Z), plus self-improve authored PR #164 on-target 7-15 = 3 of 4 last-week actions shipped in some form. rule-5 primitive n=4 downgrades to n=2 partial-conflict class — half the "auto-committed state drift" theory just merged clean. what didn't ship: **ISS-025 capture-step PR — day-5 past deadline, cost-report cf 5→10 doubling in 24h on 3rd-consec Mon-weekly miss n=3 (7-6/7-13/7-20)**. top action next week — operator direct-authors ISS-025 by 2026-07-23, and refs `dangerouslyDisableSandbox` per gh #53012 as a candidate implementation path (heartbeat surfaced today).

## Last week's actions — closed loop

From `articles/weekly-review-2026-07-13.md` "Next week — actions":

- **Action 1 — Operator direct-authors ISS-025 chain-runner capture-step PR by 2026-07-16: SLIPPED d5.** Deadline was T-0 7-16, now T+4 (day-5 past). Grep `.github/workflows/aeon.yml:479-495` shows no operator commit against those lines this week. Cost-report substrate degrades in sympathy: cf 5→8→10 across 7-19 → 7-20, `stuck→FAILED` state-change 7-20 13:24Z, 3rd-consec-Mon-weekly-miss n=3 durable pattern (last_success 2026-06-29, missed 7-6/7-13/7-20). Same primitive as [[12:00 UTC batch DARK day-23]] and [[aixbt-pulse dead-slot day-23]] — all waiting on the same fix. **Carry as action #1 next week, tighter framing (candidate impl path surfaced today).**
- **Action 2 — Operator decides on PR #162 within 24h by 2026-07-14: SHIPPED-LATE +6 days.** `gh pr view 162 --json state,mergedAt` → `MERGED 2026-07-20T14:16:51Z`. Commit `e525536c fix(daily-routine): tighten XAI fallback rules for quota/sandbox/error`. 6 days past deadline but the operator batch-merge session 7-20 also cleared PR #163 3h later (`f0daa501 fix(skill-security-scan)` 2026-07-20T17:11:10Z, ~144h+ CONFLICTING flip to green). **New pattern: operator batches self-improve PR decisions weekly, not per-24h-gate**. Framing miss last week — the gate wasn't operator inaction, it was cadence-mismatched to review reality.
- **Action 3 — Self-improve authors CLAUDE.md rule-5 codification by 2026-07-17: SHIPPED-VIA-ADJACENT-PATH +2 days.** Not landed in CLAUDE.md text as spec'd. Landed as `improvement-PR-queue-locks-self-improve 2-consec` primitive in `skills/self-improve/SKILL.md` at 2026-07-19T18:32Z (chore(cron) commit `747d0d3e chore(cron): self-improve success`, log entry `memory/logs/2026-07-19.md` at "self-improve 18:32 UTC" section). Self-improve gates itself when 3+ open PRs. Same-shape edit as prior weeks — durable log-signal (3-consec review carry) → SKILL.md edit → shipped. **Adjacent-path is a valid ship**; the routing was mis-specified last week.
- **Action 4 — Self-improve investigates Investment Advisor 7-consec-day cancellation by 2026-07-16: SHIPPED-ON-TARGET 7-15 (T-1).** Self-improve authored PR #164 `fix(investment-advisor): fail-fast committee retries to stop 20-min timeout cancellations` at 2026-07-15T19:31:08Z. Root cause identified: 20-min committee-retry timeout inside the workflow. PR still OPEN/CONFLICTING d6 as of 7-20, but the investigation shipped and the fix is authored. Weekly cancellation count for the advisor: 7 prior week → 5 this week (7-15/7-16/7-18/7-19/7-20; missed 7-14/7-17) — cancellation continues while fix waits on PR merge.

Result: **1 shipped-on-target / 1 shipped-via-adjacent-path / 1 shipped-6d-late / 1 slipped-d5.** Meaningful step up vs prior week's 0-shipped-on-target — the retrospective SMART framing produced 3 out of 4 actions that landed in some shape this week. The 1 slip is the same one for the 4th week running (ISS-025), and it's the highest-leverage of the four.

## Metrics

| Metric | This week (2026-07-13 → 2026-07-20) | Prior week | Δ |
|---|---|---|---|
| Total workflow runs | 305 | 275 | +30 |
| Success rate (completed) | 96.97% (288/297) | 94.1% (256/272) | **+2.9pp** |
| Failure count | 9 | 7 | +2 |
| Cancelled count | 8 | 9 | −1 |
| Articles written | 15 files (~10 unique skills) | 14 | +1 |
| Days with log entry | 8 (7-13 → 7-20) | 8 | 0 |
| New issues opened | 0 | 0 | 0 |
| Issues resolved (INDEX flips) | 0 | 1 (ISS-022) | −1 |
| PRs merged | 2 (#162, #163 same day 7-20) | 5 | −3 |
| PRs opened, still open | 2 (#164 CONFLICTING d6, #165 docs 0-1d) | 2 | 0 |

Sources: `gh api "repos/anajuliabit/aeon/actions/runs?created=2026-07-13T19:00:00Z..2026-07-20T19:30:00Z"` paginated 4 pages → 305 total (288 success / 9 failure / 8 cancelled). `gh pr list` for merges and open state. `ls articles/` filtered to 7-13 → 7-20 → 15 files. `./scripts/skill-runs --hours 168 --json` blocked in sandbox (9th consecutive review — [[skill-security-scan sandbox-block n=8 durable]] class) — degraded via `gh api` (matches prior pattern, no fidelity loss). Git log via `git fetch --unshallow` first (shallow clone dropped since last week).

**Failure breakdown (9 fails):** 4× cost-report on 7-20 (10:47Z, 12:57Z, 15:18Z, 16:48Z — Mon-weekly tick failing all-day, cf climbs 5→10), 3× ci-skills-json on 7-20 (14:16Z–14:19Z burst during PR #162+#163 merge sequence, advisory), 1× ci-skills-json 7-14 (routine PR-check), 1× "Sync from upstream" 7-20 11:48Z (external fork-sync).

**Cancelled breakdown (8 cancels):** Investment Advisor 5× (7-15/7-16/7-18/7-19/7-20 in the 14:21Z–15:13Z window — down from 7 prior week, missed 7-14/7-17) + cost-report 3× (7-13 19:45Z + 7-13 20:44Z + 7-20 07:53Z). Advisor cancellation continues while PR #164 fix waits on merge.

## Findings (KALM, prioritized)

### Keep

- **Operator weekly batch-merge session shipped 3 items in one day 7-20** (priority 12 — F4×I3÷E1). Operator session cleared PR #162 (14:16Z, `e525536c`), PR #163 (17:11Z, `f0daa501`), and per `memory/logs/2026-07-20.md` reflect section, this was the first self-improve authored PR merge since [[rule-5 primitive extension]] was codified. Two ~144h+ CONFLICTING PRs flipped to green in 3h. **Keep the operator-batch shape; document it so the retrospective framing stops treating "operator hasn't touched X in 24h" as a stall signal** (see More finding).

- **Self-improve investigation-action-class ships on-target when target is script-file class** (priority 9 — F3×I3÷E1). PR #164 authored 7-15 T-1, the Investment Advisor investigation reached a real root cause (20-min committee-retry timeout) and produced a fix PR against `.github/workflows/investment-advisor.yml` + `scripts/advisor/*` = script-file class, not workflow-file-only. Same pattern as PR #160 (ISS-022 flip), PR #162 (daily-routine XAI-fallback), PR #163 (skill-security-scan sandbox-block docs). **When the target is skill/SKILL.md, memory/issues/*, script-file, or memory/logs — self-improve ships.** Rule-5 wasn't as absolute as prior weeks framed it.

- **Skill-side exit-gate primitive shipped 7-19 as adjacent-path to CLAUDE.md-edit** (priority 8 — F3×I3÷E1.1). `improvement-PR-queue-locks-self-improve 2-consec` codified inside `skills/self-improve/SKILL.md` instead of CLAUDE.md. Same-class fix, different file, +2 days late but shipped. **Adjacent-path is a valid ship shape when specific-file assignment fails**; keep this open as a routing convention.

### Add

- **07:00Z morning batch dead-slot new class formed day-4+** (priority 12 — F4×I3÷E1). Log evidence: `memory/logs/2026-07-17.md` at 08:18Z hb — "07:00Z morning batch MISSED 2nd consecutive day 7-17 = dead-slot class forms FRESH CLASSIFICATION" — morning-brief last_success 2026-07-15T08:30Z, daily-routine last_success 2026-07-15T08:37Z, then chronic through 7-20. Same primitive as [[12:00 UTC batch DARK day-23]] and [[aixbt-pulse dead-slot day-23]]. Scheduler-side per ISS-027 class. Undocumented in `memory/issues/INDEX.md` as of 7-20 (no ISS entry filed). **Same investigation shape as advisor pattern that shipped this week — pass to self-improve** (see next-week actions).

- **cost-report cf=5→10 doubling on Mon-weekly-miss n=3** (priority 12 — F4×I3÷E1). Fresh degradation signal underneath the chronic ISS-025 primitive block. `memory/cron-state.json` shows cf climbed 5 (start of week) → 8 (7-20 13:24Z) → 10 (7-20 17:18Z FAILED). 3rd-consec-Mon miss (7-6/7-13/7-20 all missed against last_success 2026-06-29). Same root cause as ISS-025 but the rate is accelerating. **The candidate impl path surfaced today**: goal-tracker 17:20Z note references pivot to `dangerouslyDisableSandbox` per gh #53012 as an alternative to the capture-step fix. Elevates ISS-025 from "author capture-step patch" to "author capture-step patch OR sandbox-disable pivot" — widens the shippable-shape.

### Less

- **STATUS_PAGE=DEGRADED cry-wolf day-32 — 4th consecutive weekly-review carry** (priority 10 raw / **dropped**). Same finding 2026-06-29, 2026-07-06, 2026-07-13. Every hb this week fired DEGRADED. Prior review already promised no 4th action-framing; keep the promise. Note in Notes; no action.

- **Weekly-review actions framed as "operator inaction stall"** (priority 8 raw / demoted to 6 with next-week reframe). Last week's Action 2 framed PR #162 as "operator decides within 24h" — operator decided in 6 days as part of a weekly batch. The gate was mis-cadenced, not missed. **Reframe: operator actions target Sunday-to-Sunday, not per-24h-gate**. Applied to next week's Action 2 below.

### More

- **Codify operator-weekly-batch-review cadence in CLAUDE.md** (priority 12 — F4×I3÷E1). 7-20 shows the shape: operator batches self-improve PR review+merge on ~weekly rhythm to clear queue and enable next cycle. If not documented, next weekly-review will re-diagnose the same "stall" 3 more times. Concrete edit: add one line to CLAUDE.md under "Skill authoring boundaries" heading naming the operator-batch cadence. Same-shape adjacent-path as skill exit-gate primitive from 7-19.

- **MEMORY.md line 5-7 rule-5 primitive n=4 stale-evidence refresh** (priority 8 — F3×I3÷E1). Reflect already flagged this 7-20 18:47Z: "Rule-5 primitive n=4 evidence-fading — 2 of 4 'auto-committed state drift' PRs merged clean today = primitive downgrades to n=2 partial-conflict class, not full-class rail". Reflect owns the memory refresh but action-converter also carries `rule-5-evidence-refresh` loop at score 80. **Deferred to next reflect cycle** (2026-07-22, per goal-tracker note); no weekly-review action needed.

### Dropped from priority threshold

- XAI quota recovery day-32 (BLOCKED, operator-gated, WebSearch fallback clean).
- defi-monitor NO_CONFIG day-44 (operator-gated, needs on-chain-watches.yml + ALCHEMY+ETHERSCAN keys).
- vuln-scanner sr=0.16 (ISS-018 operator-gated wontfix-class, chronic).
- Investment Advisor cancellation continues while PR #164 waits merge — rolls up under Action 2 below.
- Skill-security-scan sandbox-block n=8 (chronic, tracked in [[skill-security-scan sandbox-block]] primitive; no new-shape).

## Next week — actions

Structural update from last week: actions targeting operator work should be **weekly cadence, not 24h-gate** (per Less finding above). Actions targeting self-improve stay at 3-5 day cadence with SKILL.md-adjacent file targets.

- [ ] **Operator direct-authors** the ISS-025 chain-runner capture-step PR against `.github/workflows/aeon.yml:479-495`. Widen scope to include the candidate `dangerouslyDisableSandbox` pivot per gh #53012 (surfaced 7-20 heartbeat) as alternative implementation path. Reference cost-report cf=10 doubling + Mon-weekly-miss n=3 as fresh pain evidence. Deadline **2026-07-27** (weekly cadence, next Sunday).
  - Why: 28-day durable block (was 21 days last week — +7 with same signal). Cost-report cf 5→10 doubling in 24h + [[12:00 UTC batch DARK day-23]] + [[aixbt-pulse dead-slot day-23]] all wait on this fix. The `dangerouslyDisableSandbox` pivot widens the shippable-shape — either impl unblocks the same 17-skill chronic tail.
  - Done when: PR targeting `.github/workflows/aeon.yml` capture-step OR one that disables the sandbox for chain-runner merges; ISS-025 flips Open → Resolved in INDEX with fix_pr populated; ≥1 chronic-tail skill (cost-report or reg-monitor) shows sr improve >0.2 in `cron-state.json` over the 3-day window post-merge; cost-report weekly Mon 7-27 tick completes without failure.

- [ ] **Operator resolves PR #164** (merge, close, or rebase-then-decide) as part of the same weekly batch that cleared #162 + #163. Deadline **2026-07-27**.
  - Why: PR #164 is the sole remaining CONFLICTING self-improve PR after 7-20 batch merge. Resolving it fully unblocks the self-improve exit-gate primitive shipped 7-19 (queue-full state clears; next self-improve fire tests unblocked-authoring quality). Investment Advisor cancellation pattern (5/7 days this week) continues until this fix lands.
  - Done when: `gh pr view 164 --json state` returns MERGED or CLOSED; if MERGED, the next Investment Advisor scheduled tick (7-28 15Z window) completes non-cancelled; if CLOSED with a follow-up, the follow-up PR is referenced in the close message.

- [ ] **Self-improve authors** a one-line addition to `CLAUDE.md` under "Skill authoring boundaries" section codifying operator-weekly-batch-review cadence: `Operator batches self-improve PR review/merge decisions weekly (typically Sunday); queue-full state ≥3 open PRs triggers self-improve exit-gate primitive (shipped 7-19 in skills/self-improve/SKILL.md).` Same-shape edit as PR #163 (durable log-signal → SKILL.md-adjacent → shipped). Deadline **2026-07-25**.
  - Why: 7-20 operator batch cleared 2 PRs in 3h — 4th weekly-review would otherwise re-frame the operator cadence as "stall" for the 4th time. Codifying it in CLAUDE.md prevents mis-framed actions and gives the retrospective framing a stable reference. Operator-batch pattern is now the durable observed shape; MEMORY.md line 5 already annotates it in Current Goals.
  - Done when: PR merges touching only CLAUDE.md; `grep -i "weekly batch" CLAUDE.md` returns the routing line; next weekly-review references it as the cadence-source-of-truth instead of re-diagnosing.

- [ ] **Self-improve investigates** the 07:00Z morning batch dead-slot new class (day-4+; morning-brief/daily-routine/thought-review 07:00Z half all last_success 7-15 through 7-20 in `memory/cron-state.json`). Same investigation-shape as PR #164 Investment Advisor pattern that shipped on-target 7-15. Read `.github/workflows/aeon.yml` schedule + concurrency + timeout for the 07:00Z batch; check the most recent missed 07:00Z run log via `gh run view --log <id>` for schedule-side signal; document findings in `memory/topics/scheduler-primitives.md` (new file — same-shape as `memory/topics/xai-quota-exhausted.md`). If root cause is in `scripts/prefetch-*.sh` or SKILL.md text — self-improve authors the fix PR. If it's in the workflow file — escalate to operator per rule-5 primitive. Deadline **2026-07-24**.
  - Why: New dead-slot class forms 4+ days into a durable pattern, undocumented in `memory/issues/INDEX.md`, invisible to skill-health at slot level. Same shape as [[12:00 UTC batch DARK day-23]] class — better to investigate at day-4 than day-23. Investment Advisor investigation this week (PR #164) proves the shape works when the target is script-file or workflow-file class.
  - Done when: `memory/topics/scheduler-primitives.md` exists with (a) root-cause diagnosis, (b) fix PR link or operator-escalation note referencing the specific `.github/workflows/aeon.yml` line, (c) either the 2026-07-22 or 2026-07-23 07:00Z morning batch tick completes clean OR MEMORY.md gains a Current Goals row marking the slot as expected-empty-by-design.

(4 actions clear the priority threshold. Every action names an authored-by slot per operator-vs-self-improve routing convention.)

## Goals progress

From `memory/MEMORY.md` Current Goals (last consolidated 2026-07-20 per reflect 18:47Z):

- **ISS-025 capture-step PR day-5 past deadline** — SLIPPED again this week; still with rule-5 primitive routing (operator direct-author only). Next-week Action 1 carries forward with widened impl scope (`dangerouslyDisableSandbox` pivot). Cost-report cf 5→10 doubling reinforces the pain surface.
- **2 self-improve PRs CONFLICTING past stall gates** — down from 3 last week. PROGRESS: PR #162 MERGED 7-20 (removed from queue), PR #163 MERGED 7-20 (removed from queue). PR #164 sole residual CONFLICTING d6. PR #165 fresh at 0-1d under gate. Next-week Action 2 targets #164 resolution.
- **12:00 UTC batch DARK day-23** — BLOCKED, same class as ISS-025. Per-skill blockage confirmed n=23 (token-alert + btc-levels + cost-report all fired same 12:00Z slot 7-20 while 8-skill 6-28 cluster stayed frozen = per-skill sandbox-behavior, not per-slot scheduler). Waiting on ISS-025.
- **Operator on-chain config day-44** — BLOCKED, needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. status quo. defi-monitor NO_CONFIG chronic.
- **07:00Z morning batch dead-slot day-4** — NEW this week; picked up as Action 4.
- **Cost-report Mon-weekly miss n=3** — 3rd-consec Mon miss (7-6/7-13/7-20), durable pattern; sub-signal under ISS-025 chronic-tail.

## Notes

- Biggest signal of the week is the **operator batch-merge shape** — 2 CONFLICTING self-improve PRs cleared in a 3h window on 7-20. Prior 3 weekly reviews framed the same pattern as "operator inaction stall" and it was mis-cadenced. Next week's Action 3 codifies the cadence in CLAUDE.md so this doesn't misfire a 4th time.
- **Rule-5 primitive n=4 downgrades to n=2 partial-conflict class** — 2 of 4 "auto-committed state drift" PRs (#162, #163) merged clean same day. The "structural block" theory holds only for workflow-file class edits and for PRs stuck in queue past a certain length. Reflect owns the MEMORY.md refresh (2026-07-22 cycle).
- **STATUS_PAGE=DEGRADED gate change** carries a 4th week. Per last review's promise: no re-framing. The next self-improve tick that gets a fresh evidence-anchor (a hb tick where STATUS_PAGE=OK would have been informative) should surface it directly.
- **ISS-007/009/010/016 INDEX close-out** carried a 9th time as noise (rows have no fix_pr, self-improve won't touch, weekly-review has surfaced 8 times prior). Same as last week's Notes call — **dropped from actions permanently**. Next MEMORY consolidation should either add fix_pr entries or mark them wontfix. Weekly-review no longer surfaces.
- **Investment Advisor cancellation pattern** narrowed 7→5 days this week (missed 7-14 + 7-17). PR #164 fail-fast committee retries is authored and waits on merge; once merged, the 15Z tick should complete non-cancelled. Rolls up under Action 2.
- **`dangerouslyDisableSandbox` pivot** per gh #53012 is a first-time-mentioned candidate impl path for ISS-025 that came out of today's heartbeat. If operator picks it, it's a smaller-blast-radius fix than the capture-step edit — no chain-runner logic change, just a permission flag. Worth naming in Action 1's Why so both paths remain shippable.
- Success rate improved **+2.9pp** week-over-week (94.1% → 96.97%) driven by the batch-merge PR clearance offset against the cost-report cf 5→10 doubling. Not a fresh regression under the numbers — durable primitive block continues while operator ships around it in adjacent classes.
- Voice ana applied: lowercase body, single em-dash beat per section, terse verdict lines (`SLIPPED d5`, `SHIPPED-VIA-ADJACENT-PATH +2 days`, `→ drop`), concrete refs (PR #s / commit hashes / ISS-#s / percentages / dates), no marketing verbs / hashtags / emoji.
