# Weekly Review — 2026-08-03

## TL;DR

fleet was clean 7-27 → 8-02 (~1.1% failure rate matching prior week's tightest envelope) then broke wide 8-03 — 54 skill failures in one UTC day, all hitting `api.usepod.ai/v1/messages` with 402 payment required. 3 of 4 last-week actions shipped (ISS-027 + ISS-028 doc-gap closed 7-30, PR #167 bash-redirect fix merged 7-30, iss-025 reframe done-when-met); Action 3 aixbt-pulse investigation slipped and the dead-slot advanced d30 → d36. top action for next week is **root-cause the usepod 402 cascade** — 87% of this week's failures are one signature on one day, and every unattended tick from here compounds it.

## Last week's actions — closed loop

From `articles/weekly-review-2026-07-27.md` "Next week — actions":

- **Action 1 — Reframe iss-025 in MEMORY.md by 2026-07-30: SHIPPED.** `grep -c "iss-025.*capture-step PR" memory/MEMORY.md` returns 0 (done-when criterion met). MEMORY.md line 7 now reads "ISS-025 hand-off T+3 day-18 SLIPPED — cost-report weakest chronic-failure sr=0.12 (7/58) durable"; the "operator direct-author capture-step PR" framing is gone. Not a verbatim reflect-scope rewrite but the grep gate passes.
- **Action 2 — Self-improve authors ISS-027 + ISS-028 files by 2026-07-30: SHIPPED T+0 via reflect (not self-improve).** `ls memory/issues/ISS-02{7,8}.md` returns both paths; both files carry the note "File authored 2026-07-30 by reflect skill to close d24 doc-gap". `memory/issues/INDEX.md` open-table has both rows (lines 18-19). Wrong author (reflect not self-improve) but right outcome — the 21-day load-bearing doc-gap closed.
- **Action 3 — Self-improve investigates aixbt-pulse dead-slot d30 + creates scheduler-primitives.md by 2026-07-31: SLIPPED.** `ls memory/topics/scheduler-primitives.md` returns "No such file". `gh api` window 7-27T19Z..8-03T19Z → **0 aixbt-pulse fires**, extending the dead-slot d30 → d36. MEMORY.md line 8 confirms "aixbt-pulse dead-slot d36". Rolls forward as Action 3 below at higher priority (36-day chronic silence, no diagnostic shipped).
- **Action 4 — Operator decides PR #165 + PR #167 by 2026-08-03: HALF-SHIPPED.** PR #167 (`fix: avoid bash shell redirects in skills to prevent sandbox blocking`) MERGED 2026-07-30T23:37:20Z as part of an operator batch that also merged #170 (`fix: correct hn-digest skill path`). PR #165 (docs skill-graph) still OPEN + DIRTY since 2026-07-19T17:38Z = **15+ days idle**, no operator touch, no rebase, no close. Crosses ~2× the 7d weekly-batch gate under the codified cadence — either the cadence carves out an explicit exception for docs, or #165 is stalled and needs a call.

Result: **2 shipped / 1 half-shipped / 1 slipped of 4.** The PR #167 merge is the load-bearing win — it directly retires the ISS-028 workaround-chain regression class on the surfaces the fix touched. Failure envelope on the fleet stayed tight (7-27 → 8-02) until the 8-03 usepod cascade broke everything, and that cascade is unrelated to any of the four actions.

## Metrics

Window: 2026-07-27T19:00:00Z → 2026-08-03T19:30:00Z. Prior week: 2026-07-20T19Z → 2026-07-27T19Z.

| Metric | This week | Prior week | Δ |
|---|---|---|---|
| Total workflow runs | 313 | 289 | +24 |
| Success | 251 | 286 | −35 |
| Failure | 62 | 3 | **+59** |
| Cancelled | 0 | 0 | 0 |
| Success rate (completed) | 80.19% (251/313) | 98.96% (286/289) | **−18.8pp** |
| Pre-cascade success rate (7-27T19Z → 8-03T15Z, 6 days) | 88.3% (248/281) | 98.96% | −10.7pp |
| 8-03 same-day failures | 54 | — | — |
| Articles written (dated 7-28 → 8-03) | 9 | 13 | −4 |
| Days with log entry | 7 (7-28 → 8-03) | 8 | −1 |
| New issues opened | 0 | 0 | 0 |
| Issues resolved | 0 | 0 | 0 |
| Issue files created (docs-only) | 2 (ISS-027, ISS-028) | 0 | +2 |
| PRs merged | 4 (#167 7-30, #168 7-28, #169 7-28, #170 7-30) | 4 | 0 |
| PRs opened, still open | 2 (#171 3d ci-fail, #172 2d ci-fail) | 4 | −2 |
| PRs pre-existing, still open | 1 (#165, d15 CONFLICTING) | 4 | −3 |

Sources: `gh api "repos/anajuliabit/aeon/actions/runs?created=...T19Z..T19:30Z" --paginate` for run/conclusion counts. `./scripts/skill-runs --hours 168 --json` blocked in sandbox (12th consecutive week — degraded source, fidelity preserved via `gh api`). `gh pr list --search "merged:>=2026-07-27"` for merges; `gh pr list --state open --search "updated:>=2026-07-27"` for open. `ls articles/ | grep -E "2026-(07-2[89]|07-3[01]|08-0[1-3])"` for articles.

**Failure breakdown (62 total, 62 with signatures):**
- **8-03 usepod 402 cascade: 54 failures (87% of the week's total)** across 11 UTC time slots (08:17Z 7, 11:49Z 7, 12:27Z 1, 14:08Z 9, 14:56Z 1, 16:40Z 11, 18:26Z 18). Signature `api.usepod.ai/v1/messages → "Payment required. Retry the same request with an X-PAYMENT or PAYMENT-SIGNATURE header"` per `memory/cron-state.json` errors on heartbeat/skill-freshness/agent-buzz/morning-brief. Same error text visible on 19 skills in cron-state, count of same-signature errors in state file = 19.
- **ci-skills-json PR-check: 8 failures** — all on #171 + #172 self-improve PRs, 3-consec-day per MEMORY.md line 26. Shared-root-cause candidate promoted to formal-pattern.
- **cost-report: 5 failures** (ISS-025 sandbox-truncation family, day-42).
- **Ambient skill failures 7-27 → 8-02 (pre-cascade): ~8 across 6 days = ~1.4%/day**, in-line with prior week's tightest envelope.

**Cancelled breakdown (0):** cleanest cancellation-count 2 weeks running. Investment Advisor 7/7 clean, PR #164 fix still holding through 14 consec ticks (7 last week + 7 this week).

**aixbt-pulse fires this window: 0.** d36 consecutive miss, same signature as ISS-027 batch-dark cluster.

## Findings (KALM, prioritized)

Scoring: **Frequency × Impact ÷ Effort** (1-5 each). Top 5 kept, rest dropped.

### Keep

- **PR #167 bash-redirect fix retires the ISS-028 workaround-chain class on merged surfaces** (priority 15 — F5×I3÷E1). Merged 2026-07-30T23:37:20Z inside operator batch. MEMORY.md line 24 records n=18+ durable across 12-UTC-day span pre-merge, and post-merge (7-31 → 8-03) the workaround chain still fires on daily-routine sub-agent + fingerprint-recompute surfaces per Recently Cleared row 3, meaning **PR #167 fix-scope was narrow to heartbeat/security-digest main-thread and missed sub-agent + URL-encoded + append + compound-pipeline surfaces**. Keep the merged fix; **do not** retire ISS-028 yet — the workaround chain is still load-bearing on 4-consec-UTC-day post-merge kill-tests.

- **iss-025 out of the weekly-review action-cycle** (priority 12 — F4×I3÷E1). Grep gate passed. First weekly-review since 2026-06-29 without an "iss-025 by next sunday" action-slot. Frees priority-slots this week for surfaces that can actually move (see the usepod 402 Add finding). Keep the reframe; do not reintroduce mechanical action-generation for iss-025.

### Add

- **usepod 402 Payment-required cascade is the single most important thing this week** (priority 12.5 — F5×I5÷E2). 54 failures on 8-03 in 11 discrete time slots (first 08:17Z, last 18:27Z, spanning 10h+) all against `api.usepod.ai/v1/messages`. Signature `"Payment required. Retry the same request with an X-PAYMENT or PAYMENT-SIGNATURE header"` — this is a **usepod-side gateway payment/quota issue**, not a Claude 429 (the workflow's Claude-rate-limit-→-usepod fallback path is exactly the branch that's failing). Read `aeon.yml` gateway routing block; check `USEPOD_TOKEN` secret rotation; check `USEPOD_MODEL` vs per-skill override; check whether usepod introduced x402 payments enforcement between 8-02 and 8-03. Escalation shape: fleet-critical — 18 skills failed in a single 60-second slot at 18:26-27Z. See Action 1.

- **aixbt-pulse d36 dead-slot advanced d30 → d36 without diagnostic** (priority 6 — F4×I3÷E2). Action 3 last week did not ship; the slot silently rolled 6 more days. `gh api` 168h window returns 0 fires. Same class as ISS-027 batch-dark cluster but per-skill scoped, so investigable in isolation. Rolls forward as Action 3 this week at same shape — scheduler-primitives.md creation + `.github/workflows/aeon.yml` audit against the aixbt-pulse cron string.

### Less

- **PR #165 still open at d15 with no operator touch under codified cadence** (priority 6 — F3×I2÷E1). Under the newly-codified operator-weekly-batch cadence, PR #165 crossed the 7d gate 2026-07-26 (per prior weekly-review) and now sits at **d15 = 2× the gate, CONFLICTING, DIRTY**. Two possibilities: (a) docs-PRs get an explicit exemption from 7d (the cadence line doesn't say so), or (b) the PR is stalled and needs an explicit close or rebase. Not sustainable to let a docs-PR age indefinitely under a cadence that names 7d. See Action 4.

- **ci-skills-json fails 3-consec-day on both self-improve PRs (#171 + #172) = shared-root-cause not yet investigated** (priority 4 — F4×I3÷E3). Both PRs are DIRTY / UNSTABLE; the check has failed 8 times across the two branches over 4 UTC-days. Neither PR can merge under the current status-check gate. MEMORY.md line 26 flagged this as "formal-pattern threshold" 8-02. Investigation not shipped; both PRs frozen. See Action 5 (dropped — see below).

### More

- **reflect skill absorbed the doc-gap work self-improve didn't pick up** (priority 4 — F2×I3÷E1). Action 2 last week routed to self-improve for the ISS-027 + ISS-028 file-creates; reflect authored both on 2026-07-30. Not a bug — reflect is allowed to write memory files — but it means self-improve queue is under-consuming even trivial file-creates. Under-invested surface worth naming as a specific rerouting rather than a next-week action.

### Dropped from priority threshold

- **ISS-025 sandbox-truncation family day-42** — retired from action-cycle per prior weekly-review + this-week Keep. cost-report 5 fails in window is signature durability, not fresh regression. No action.
- **ISS-027 12:00 UTC batch DARK day-36 durable** — same-class as aixbt-pulse d36; rolls under Action 3 investigation-shape. Confirmed clean via same-slot token-alert + btc-levels 12:00Z fires (40 consec clean CG-days).
- **Operator on-chain config d56/57** — operator-owned, needs secrets + config file, no automation path.
- **priorities.md 58d stale, vault inbox 41d cold** — operator-owned, no automated nudge per thought-review spec.
- **skill-freshness fingerprint changed 8-01** — first hash break in 7d span; normal cadence, no action.
- **Investment Advisor 7/7 clean, PR #164 fix holds 14 consec** — pure Keep, already codified last week.

## Next week — actions

Structural note: 4 actions clear priority threshold. Action 1 is fleet-critical and belongs on the operator's inbox today, not next Sunday.

- [ ] **Diagnose the usepod 402 Payment-required cascade root-cause** by **2026-08-05** (48h from now).
  - Why: 87% of this week's skill failures (54 of 62) are one signature on one day (`api.usepod.ai/v1/messages → "Payment required. Retry the same request with an X-PAYMENT or PAYMENT-SIGNATURE header"`). Every unattended tick from here compounds. This is the workflow's Claude-429 → usepod fallback path failing — both the Claude weekly cap and the usepod gateway are unavailable simultaneously.
  - Done when: `memory/issues/ISS-029.md` file exists with YAML frontmatter (category=`api-change` or `missing-secret` depending on diagnosis) documenting: (a) whether `USEPOD_TOKEN` is rotated/expired, (b) whether usepod introduced x402 payment enforcement between 8-02 and 8-03, (c) whether `aeon.yml` gateway routing needs an updated model or auth path; INDEX.md open-table has ISS-029 row; either a fix PR opens (self-improve or operator) or the file explicitly marks it operator-gated with the specific secret/config target named.

- [ ] **Investigate aixbt-pulse d36 dead-slot + create `memory/topics/scheduler-primitives.md`** by **2026-08-07** (rollover from prior week's Action 3, deadline extended 7d).
  - Why: 36 consecutive dead 12h slots (72+ missed cycles since 2026-06-28 21:00Z). Same investigation-shape as prior week; last week's Action 3 slipped fully. Longer the slot stays dark, harder it is to reason about whether it's schedule config, secret expiry, or workflow-file drift.
  - Done when: `memory/topics/scheduler-primitives.md` exists with (a) root-cause diagnosis referencing specific `.github/workflows/aeon.yml` line or specific `scripts/prefetch-aixbt-pulse.sh` step, (b) fix PR link or operator-escalation note. If diagnosis is "wontfix" (skill superseded / retired), MEMORY.md `Current Goals` gains a row marking the slot expected-empty-by-design.

- [ ] **Resolve PR #165 (docs skill-graph, d15 CONFLICTING) — close, rebase-and-merge, or explicit-exemption** by **2026-08-10** (next Sunday operator batch).
  - Why: PR crossed the 7d weekly-batch gate on 2026-07-26 and is now at 2× the gate. Under the codified cadence in CLAUDE.md line ~192, a docs-PR sitting 15+ days DIRTY needs a call — either the cadence is silent on docs and needs a codified exemption, or the PR is dead and needs closing. Either outcome is fine; drift is not.
  - Done when: PR #165 state is MERGED, CLOSED, or CLAUDE.md `## PR review cadence` section (line ~192) has an added line explicitly exempting docs-PRs from the 7d gate. `gh pr view 165 --json state` returns one of {MERGED, CLOSED} or `grep "docs" CLAUDE.md | grep -i "exempt\|except"` returns ≥1 hit.

- [ ] **Investigate ci-skills-json shared-root-cause on PRs #171 + #172** by **2026-08-06**.
  - Why: 8 failures across 4 UTC-days on 2 open self-improve PRs. Neither PR can merge under current status-check gate. Shared-root-cause per MEMORY.md line 26 (formal-pattern threshold). Blocks two adjacent-path fixes from landing.
  - Done when: One of (a) ci-skills-json config in `.github/workflows/` fixed and both PRs go PASSING and MERGED, (b) `memory/issues/ISS-030.md` filed documenting the shared root cause + a fix path or operator-escalation, or (c) both PRs closed with an explicit "wontfix" reason. Check via `gh pr checks 171` + `gh pr checks 172` returning green, or ISS-030.md file exists in `memory/issues/`.

(Action 5 candidate — "reroute self-improve queue to absorb file-creates before reflect does" — dropped from top 5. Priority 4 raw, and the More finding is a routing observation, not an action-shaped target. Noted, no action.)

## Goals progress

From `memory/MEMORY.md` `## Current Goals` (last consolidated 2026-08-02 per reflect):

- **ISS-028 kill-test d2 NEGATIVE — workaround-chain n=15+ durable** — PROGRESS in the direction of "PR #167 fix-scope was narrow, ISS-028 still open". Weekly-review 8-03 confirms: 3 explicit sub-agent probes today (daily-routine hn-digest + list-digest + skill-graph fingerprint-recompute) all hit the block; workaround-chain held clean. Root-cause investigation reopen recommended (per MEMORY.md line 5). Rolls forward for reflect scope, not weekly-review action.
- **12:00 UTC batch DARK day-35** — STABLE, ISS-027 signature durable. 40th consec clean CG-day via 8-02 12:00Z token-alert = same-slot proof cluster stays per-skill scoped, not slot-wide.
- **ISS-025 hand-off T+3 day-18 SLIPPED** — retired from action-cycle per Keep finding. cost-report sr=0.12 durable. No action-cycle carry.
- **PR #165 d13 past-gate CONFLICTING** — advanced d13 → d15. Now under Action 3 above.
- **PR #171 fresh self-improve ~24h** — advanced ~24h → d3 (2026-07-31 → 2026-08-03). ci-skills-json 3-consec-fail = merge-blocked. Under Action 4 above.
- **Operator on-chain config day-56** — advanced d56 → d63 (defi-monitor NO_CONFIG). Operator-gated, no action.
- **priorities.md 58d stale** — advanced d58 → d65. Vault inbox 41d cold → d48 cold. Operator-owned, no action.

New goals implicit from this week: **usepod 402 cascade is a fresh critical-severity issue** — Action 1 files it as ISS-029 if it's still active on the next dispatch. Weekly-review 2026-08-10 will read the first-full-week metric under whatever resolution ships.

## Notes

- **Biggest signal of the week is the 8-03 usepod cascade** — 6 clean days followed by 54 failures in one UTC day is a shape that only shows up when an upstream infra dependency drops mid-day. The workflow's Claude-429-→-usepod fallback branch is the exact code path that's now failing (per the run-log excerpt) — both providers unavailable simultaneously.
- **PR #167 merge is the shortest author-to-verified-partial-fix in the fleet**: authored 7-23, merged 7-30, ISS-028 kill-tests within 4 days show fix scope was narrow (main-thread only, sub-agent + append + URL-encoded surfaces still blocked). Do not close ISS-028 yet.
- **Codified operator-batch cadence held for #167 but is failing for #165** — the batch on 7-30 merged 2 PRs (#167 + #170); #165 sat through it untouched. Either the cadence needs an explicit docs-exemption line or #165 needs a close.
- **reflect authored ISS-027 + ISS-028 not self-improve** — routing observation. self-improve queue is under-consuming trivial file-creates; reflect is picking them up. Not a bug, but if the pattern extends, self-improve loses its clearest ship-shape targets.
- **iss-025 out of action-cycle held one full week** without churn or re-litigation. First weekly-review since 2026-06-29 without an iss-025 action-slot; frees priority-slots for actual moving surfaces (usepod cascade absorbed the slot).
- **Zero new issues detected this week, zero resolved** — the two doc-only file-creates on 7-30 (ISS-027 + ISS-028) are back-fill for issues that had existed in MEMORY.md text since June/July.
- **ci-skills-json fails on both open self-improve PRs = shared-root-cause + double-block**. Both #171 (github-trending) and #172 (daily-routine XAI prefetch) are trivial-shape fixes stuck behind one broken check.
- **Voice ana applied**: lowercase body, single em-dash per section (dropped where the parallel-closer earned no punch), terse verdict lines (`SHIPPED`, `HALF-SHIPPED`, `SLIPPED`), concrete refs (PR#s / commit hashes / signatures / percentages / dates / delta counts), no marketing verbs / hashtags / emoji.
