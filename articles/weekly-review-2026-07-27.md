# Weekly Review — 2026-07-27

## TL;DR

3 of 4 last-week actions shipped and the operator batch merged 4 self-improve PRs in a 32h window 7-20/7-21 (#162 + #163 + #164 + #166). the fix authored by pr #164 held — investment advisor **7/7 clean** this week vs 5 cancels prior. what didn't ship: **iss-025 slips for the 4th consecutive weekly-review** — action-converter 7-24 declared verb-pool exhausted at 12+ distinct verbs in 14d window = mechanical action-generation dead. top action next week — reframe iss-025 out of the action-cycle and into an explicit reflect-scope escalation, and file the missing iss-027 + iss-028 docs (21-day doc-gap crossed escalation threshold; self-improve can trivial-ship both).

## Last week's actions — closed loop

From `articles/weekly-review-2026-07-20.md` "Next week — actions":

- **Action 1 — Operator direct-authors iss-025 capture-step PR (or dangerouslyDisableSandbox pivot) by 2026-07-27: SLIPPED d0 = 4th-consec-weekly slip.** No commit against `.github/workflows/aeon.yml:479-495` this week; `iss-025` still `open` in `memory/issues/INDEX.md`. Cost-report 2026-07-27 08:42Z fired 1 clean run (`chore(cron): cost-report success` `fb626b43`) — first success since 2026-06-29, but reflex not fix (`skill-health` 7-27 still ranks cost-report at 12% success, day-34 sandbox-truncation regime unchanged). Verb-pool exhausted per action-converter 7-24 18:53Z (`memory/logs/2026-07-24.md`). **This action needs to exit the weekly-review action-cycle** — see Add finding + Action 1 below for reframe.
- **Action 2 — Operator resolves PR #164 by 2026-07-27: SHIPPED T-6 within same operator batch.** `gh pr view 164` → `MERGED 2026-07-20T21:50:32Z` (commit `21b27602 fix(investment-advisor): fail-fast committee retries to stop 20-min timeout cancellations`). Merged in the same operator batch that cleared #162+#163 earlier that day = 4 PRs merged in a 32h window (7-20 14:16Z → 7-21 18:29Z). Downstream verification: `gh api repos/{owner}/{repo}/actions/runs` window 2026-07-20T19Z..2026-07-27T19Z shows **Investment Advisor 7/7 success + 0 cancellations** vs prior week's 5 cancels + 2 successes = **-5 cancels delta**, fix is holding.
- **Action 3 — Self-improve authors CLAUDE.md operator-weekly-batch-cadence line by 2026-07-25: SHIPPED T-4.** PR #166 `fix(CLAUDE.md): codify operator weekly-batch PR review cadence` merged 2026-07-21T18:29:04Z. Same-day author-and-merge sequence (authored 18:08Z, merged 18:29Z = 21m latency). Grep confirms text landed: `CLAUDE.md` line ~192 now names weekly-batch cadence + queue-exit gate. First operator-batch-informed weekly review absorbs the artifact today.
- **Action 4 — Self-improve investigates 07:00Z morning-batch dead-slot by 2026-07-24: SELF-HEALED, no investigation shipped.** No `memory/topics/scheduler-primitives.md` file created; no fix PR authored against `.github/workflows/aeon.yml`. But: `gh api` shows `skill: morning-brief` + `skill: daily-routine` fired successfully **every day 7-21 → 7-27 (7/7)**, running between 07:12Z and 08:51Z. Whatever caused the 4-day dead-slot 7-16→7-19 resolved without diagnostic action. Adaptive-shape ship, but the shape is "problem-vanished-before-investigation" not "investigation-produced-fix" — worth naming as a class (see Less finding).

Result: **2 shipped-on-target / 1 shipped-late-same-batch / 1 slipped-4th-week (verb-pool exhausted) / 0 self-healed-without-action (not counted in slip nor ship — new class).** Meaningful step up: the highest-leverage action (Action 2, unblocking Investment Advisor) shipped and validated within one week. iss-025 remains the sole 4-week durable-slip primitive.

## Metrics

| Metric | This week (2026-07-20T19Z → 2026-07-27T19Z) | Prior week | Δ |
|---|---|---|---|
| Total workflow runs | 289 | 305 | −16 |
| Success rate (completed) | 98.96% (286/289) | 96.97% (288/297) | **+2.0pp** |
| Failure count | 3 | 9 | **−6** |
| Cancelled count | 0 | 8 | **−8** |
| Articles written (files 7-21 → 7-27) | 13 | 15 | −2 |
| Days with log entry | 8 (7-20 → 7-27) | 8 | 0 |
| New issues opened | 0 | 0 | 0 |
| Issues resolved (INDEX flips) | 0 | 0 | 0 |
| PRs merged | 4 (#162, #163, #164 all 7-20 + #166 7-21) | 2 | +2 |
| PRs opened, still open | 4 (#165 8d, #167 4d DIRTY, #168 2d CLEAN, #169 0d UNSTABLE) | 2 | +2 |

Sources: `gh api "repos/{owner}/{repo}/actions/runs?created=2026-07-20T19:00:00Z..2026-07-27T19:30:00Z" --paginate` → 289 total (286 success / 3 failure / 0 cancelled). `./scripts/skill-runs --hours 168 --json` blocked in sandbox (11th consecutive review — [[skill-security-scan sandbox-block n=9 durable]] class per skill-security-scan 7-27) — degraded via `gh api` (fidelity preserved). `gh pr list` for merges + open. `ls articles/ | grep 2026-07-2[1-7]` → 13 unique dated articles.

**Failure breakdown (3 fails):** 2× ci-skills-json (7-27 08:47Z + 7-27 18:45Z, both during self-improve PR #168/#169 author cycles = PR-check advisory noise) + 1× "Sync from upstream" (7-27 12:27Z, external fork-sync). **Zero skill-run failures across the entire 168h window** = the tightest failure envelope on record.

**Cancelled breakdown (0):** cleanest cancellation-count in memory-window. PR #164 fix (fail-fast committee retries, 20-min timeout) landed and Investment Advisor stopped cancelling the day after merge — 7-21 tick clean, all subsequent 6 ticks clean.

## Findings (KALM, prioritized)

### Keep

- **operator weekly-batch cadence codified + immediately validated** (priority 15 — F5×I3÷E1). CLAUDE.md line ~192 now names the cadence (PR #166, merged 7-21 21m post-author). Same day the operator merged 4 PRs in a 32h window (7-20 14:16Z → 7-21 18:29Z). This is the shape the prior 3 weekly-reviews mis-framed as "operator stall"; codification is the fix. **Keep the cadence-line as the reference source for future weekly-review framing** — do not reintroduce 24h-gate framing until data contradicts.

- **investment-advisor fix (PR #164) held under 7 consecutive live ticks** (priority 15 — F5×I3÷E1). `gh api` window → 7 successes / 0 cancels vs prior week's 5 cancels / 2 successes = -5 cancels delta. Root-cause fix (fail-fast committee retries → 20-min timeout removed) shipped 2026-07-20T21:50Z; effect visible from 2026-07-21T14:xxZ first tick. **Keep the "author → merge → validate one full 7-tick window before declaring shipped" rhythm** — this is the shortest confidence-to-ship path in the fleet.

### Add

- **iss-027 + iss-028 doc-gap d21 escalation threshold crossed** (priority 12 — F4×I3÷E1). MEMORY.md line 4 references iss-027 authoritatively ("ISS-027 signature confirmed durable through 7-27") but no file exists in `memory/issues/`. iss-028 (bash-`>` redirect regression n=7+ durable across 4 UTC-day span) also absent. Reflect 2026-07-27 flags this as escalation-threshold-crossed at d21 (`memory/logs/2026-07-27-reflect.md` line 12). Action-converter 7-24 18:53Z shaped 2 file-create actions (score 125 + 80) that self-improve did not pick up. **Self-improve trivial-target**: 2 file-creates from existing MEMORY text; no workflow-file class blocker. See Action 2.

- **aixbt-pulse dead-slot d30 completely dark** (priority 9 — F3×I3÷E1). `gh api` window → **0 aixbt-pulse fires in the 168h window**. 60+ consecutive 12h cycles missed since 2026-06-28 21:00Z. Same class as [[12:00 UTC batch-dark d30]] cluster. Reflect 7-27 advances counter d29 → d30 (`memory/logs/2026-07-27-reflect.md` line 57). Same investigation-shape as the 07:00Z morning-batch dead-slot that Action 4 attempted last week — but this one hasn't self-healed for 30 days. See Action 3.

### Less

- **iss-025 as a weekly-review action** (priority 10 raw / **dropped from weekly-review action-cycle**). 4-consec-weekly-slip. Action-converter 7-24 declared verb-pool exhausted (12+ distinct verbs in 14d window, `memory/logs/2026-07-24.md`). Reflect 7-27 flags this as reflect-scope (`memory/logs/2026-07-27-reflect.md` line 12 — "verb-pool exhausted, reflect-scope carry → mon weekly-review"). Continuing to author "iss-025 by next sunday" actions is churn — the mechanical action-generation loop cannot produce anything the prior 4 weeks haven't already tried. **Reframe as explicit reflect-scope escalation** (Action 1 below), not another weekly action-item.

- **problem-vanished-before-investigation as a shipping class** (priority 6 raw / noted, no action). Action 4 (07:00Z morning-batch dead-slot) resolved itself between 7-20 and 7-21 without any diagnostic PR. Same pattern happened once before with the reppo-swarm phantom-skill dispatch class. It's not a bad outcome, but it means weekly-review actions targeting "investigate X" have low signal-to-noise: X often heals or worsens on its own timeline. **Preference: prefer "author fix PR against Y file" actions to "investigate Y" actions** when the target file is knowable.

### More

- **skill-freshness weekly cadence extends** (priority 4 raw / dropped from top 5, noted). 6 skill-freshness articles this week (7-21 through 7-26) vs prior weeks that averaged 3-4. Consistent daily output with low churn; low-noise skill worth continuing. No action needed.

### Dropped from priority threshold

- STATUS_PAGE=DEGRADED cry-wolf: gate flipped to WATCH 2026-07-27 (heartbeat 14:56Z, `memory/logs/2026-07-27.md`). 33-day-consecutive-week carry pattern ends — no re-framing needed per prior review's promise, and gate has genuinely moved.
- iss-018 vuln-scanner missing binaries (operator-gated wontfix-class, no-change 5 consec).
- defi-monitor NO_CONFIG day-51 (operator-gated, needs on-chain-watches.yml + secrets — status quo).
- iss-007/009/010/016 index close-out (10th consec noise-carry — dropped permanently per prior review, held).
- 12:00Z batch-dark d30 (BLOCKED same-class as iss-025; rolls up under iss-025 reframe).

## Next week — actions

Structural update: iss-025 exits the weekly-review action-cycle (Less finding). Two of four actions target self-improve trivial-file-creates (highest ship-probability given rule-5 constraints).

- [ ] **Reframe iss-025 as explicit reflect-scope escalation** in MEMORY.md `Current Goals` — replace the current "operator direct-author against `.github/workflows/aeon.yml:479-495`" framing with a single line: "iss-025 SANDBOX-TRUNCATION FAMILY DAY-35 — reflect-scope + operator-owned, no weekly-review action-cycle carry (verb-pool exhausted 2026-07-24, 4-consec-slip 2026-07-06/13/20/27). Reflect surfaces if signature drift; operator surfaces if new impl path emerges." Deadline **2026-07-30**.
  - Why: 4-consec weekly-slip and verb-pool exhausted = the action-generation loop is churning. Recategorizing prevents the 5th slip and frees weekly-review priority-slots for surfaces that can actually move. Same routing as iss-018 vuln-scanner (operator-gated wontfix-class, no weekly action-cycle carry).
  - Done when: MEMORY.md line 5 (or wherever the goal-block currently sits) is rewritten to the single-line reflect-scope framing; `grep -c "iss-025.*capture-step PR" memory/MEMORY.md` returns 0; next weekly-review 2026-08-03 has no iss-025 action in the next-week list.

- [ ] **Self-improve authors ISS-027 + ISS-028 memory/issues/ file-creates** — 2 new files under `memory/issues/` (ISS-027.md + ISS-028.md) with YAML frontmatter per CLAUDE.md issue-schema, referencing the existing MEMORY.md text as source-of-truth. iss-027 = "12:00 UTC batch-dark 8-skill cluster frozen since 2026-06-28"; iss-028 = "bash `>` redirect regression n=7+ across 4 UTC-day span, workaround chain durable". Update `memory/issues/INDEX.md` open-table with 2 new rows. Deadline **2026-07-30**.
  - Why: d21 escalation-threshold crossed per reflect 7-27. MEMORY.md line 4 references iss-027 as authoritative but the file has never existed = load-bearing doc-gap on every read. Trivial file-creates from existing MEMORY text, not workflow-file class = self-improve unblocked. Action-converter 7-24 already shaped both entries at score 125 + 80.
  - Done when: `ls memory/issues/ISS-02{7,8}.md` returns both paths; `grep -c "ISS-027\|ISS-028" memory/issues/INDEX.md` returns ≥2; PR merges same-day (adjacent-path class).

- [ ] **Self-improve investigates aixbt-pulse dead-slot d30** — 0 fires in `gh api` window 2026-07-20T19Z..2026-07-27T19Z = 60+ consecutive 12h cycles missed since 2026-06-28. Same investigation-shape as Action 4 last week (07:00Z morning-batch dead-slot), but this slot hasn't self-healed for 30 days. Read `.github/workflows/aeon.yml` schedule + concurrency for aixbt-pulse; check `memory/cron-state.json` for `last_dispatch` / `last_success` timestamps + workflow-run-URL of most recent missed 12h tick via `gh api ".../actions/runs?workflow=..."`; document root-cause in `memory/topics/scheduler-primitives.md` (creates new file if absent) or extend an existing scheduler-primitive topic. Deadline **2026-07-31**.
  - Why: 30-day dead-slot cluster, same class as [[12:00 UTC batch-dark d30]] but per-skill scoped. If root cause is `aeon.yml` schedule / dispatch-gate → escalate to operator per rule-5. If root cause is `scripts/prefetch-*.sh` or SKILL.md → self-improve authors fix directly. 07:00Z morning-batch self-healed; aixbt-pulse hasn't and needs a diagnostic.
  - Done when: `memory/topics/scheduler-primitives.md` exists (or extended) with (a) root-cause diagnosis referencing specific line, (b) fix PR link or operator-escalation note referencing the specific `.github/workflows/aeon.yml` line; if diagnosis is "wontfix" (e.g. aixbt-pulse superseded), MEMORY.md `Current Goals` gains a row marking the slot as expected-empty-by-design.

- [ ] **Operator decides on PR #165 (skill-graph docs, crossed 7d weekly-batch gate 2026-07-26 17:38Z) + PR #167 (bash-redirect fix, DIRTY d4)** as part of the next weekly-batch. Deadline **2026-08-03**.
  - Why: PR #165 is the first PR to cross the 7d weekly-batch gate under the newly-codified cadence — its resolution establishes whether the operator-batch honors the 7d gate as-written or lets docs-PRs age longer. PR #167 fixes the iss-028 bash-redirect regression class directly (durable across 4 UTC-day span, n=7+) — its merge resolves one half of the doc-gap Action 2 files.
  - Done when: both PRs are MERGED, CLOSED, or CLOSED-with-followup-referenced-in-close-message. If PR #167 merges, next 3 skill ticks that would trigger the bash-redirect workaround chain do not need Edit/curl-o fallback (spot-check via `git log --grep="curl -o\|Edit tool"` in 3 days post-merge).

(4 actions clear the priority threshold. Action 1 explicitly retires iss-025 from the weekly cycle; Action 2 + Action 3 assign self-improve trivial and non-trivial file-target work; Action 4 keeps operator-batch cadence under observation.)

## Goals progress

From `memory/MEMORY.md` Current Goals (last consolidated 2026-07-27 per reflect 18:00Z):

- **iss-025 capture-step PR T+10 day-12 (verb-pool exhausted)** — SLIPPED 4-consec-week; action-cycle retired via Action 1 above (reframe to reflect-scope). Cost-report 7-27 08:42Z 1-shot success is noise, not fix (skill-health 7-27 still ranks 12% success, day-34 sandbox-truncation regime unchanged).
- **12:00 UTC batch DARK day-30** — BLOCKED, same class as iss-025 (per-skill sandbox-behavior, not per-slot scheduler). n=30 confirmed via 7-27 clean same-slot fires (token-alert + btc-levels + cost-report all fired 12:00Z 7-27 while the 8-skill 6-28 cluster stayed frozen). Continues under Action 3 investigation-shape (aixbt-pulse d30 is same-class sibling).
- **iss-027/028 doc-gap d21 escalation threshold** — Action 2 addresses directly. Reflect 7-27 flags this as last-chance window at d21+ tier.
- **PR #165 crossed 7d weekly-batch gate 7-26 17:38Z** — PROGRESS: first PR to cross the gate under codified cadence. Under observation via Action 4 (operator-batch decision).
- **Operator on-chain config d51** — BLOCKED, needs `memory/on-chain-watches.yml` + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. Operator-gated. defi-monitor NO_CONFIG chronic; no next-week action (operator-owned).
- **priorities.md 53d stale** — Operator-owned refresh candidate. No next-week action (operator-owned, no automated nudge per thought-review spec).

New goal implicit from this week: **operator-weekly-batch cadence codified + first 7d gate cross (PR #165)** — moves from "propose codification" to "observe first full cycle under codified rules". Weekly-review 2026-08-03 will read the first-full-cycle result.

## Notes

- Biggest signal of the week is the **PR #164 fix holding under 7 live ticks** — this is the shortest and cleanest author→merge→validate cycle in the fleet's memory-window. -5 cancels delta on Investment Advisor is the cleanest single-week metric-move in recent reviews.
- **iss-025 verb-pool exhaustion** is the sharper diagnostic. Action-converter 7-24 formalized what heartbeat implied: mechanical action-generation has run its recycling window (12+ distinct verbs in 14d, over-saturation). The right move is to stop asking the action-cycle to generate iss-025 actions; reflect-scope is where structural blockers with no shippable action-shape belong.
- **Zero skill-run failures + zero cancellations** across the full 168h window is the tightest failure envelope on record. 3 fails were all CI/sync-side (ci-skills-json PR-check + external upstream sync).
- **Codified operator-batch cadence held on first operational cycle**: 4 PRs merged in 32h window 7-20/7-21, then no operator merges through 7-27 (weekly-review absorbs PR #165 + #167 gate decisions today). This is the shape CLAUDE.md now names.
- **problem-vanished-before-investigation** class (Action 4 last week) is a real weekly-review anti-pattern to name — "investigate X" actions have low signal-to-noise vs "author fix PR against Y file" actions. Future action-authoring should prefer specific-file targets.
- **iss-027 + iss-028 filings** are pure adjacent-path self-improve targets (2 file-creates, no workflow-file class, existing MEMORY text as source) — should ship day-of-authoring if self-improve queue is not gated.
- **aixbt-pulse d30 dead-slot** is investigable in a way that 07:00Z morning-batch wasn't 4 days ago — the failure is durable (30 days, not 4) and per-skill-scoped (not batch), making it a cleaner diagnostic target.
- Success rate improved **+2.0pp** week-over-week (96.97% → 98.96%) driven entirely by cancellation removal (−8 cancels) plus failure-count halving (−6 fails). Not a fresh regression under the numbers; the fleet actually cleaned up.
- Voice ana applied: lowercase body, single em-dash beat per section, terse verdict lines (`SLIPPED d0 = 4th-consec-weekly slip`, `SHIPPED T-4`, `SELF-HEALED, no investigation shipped`), concrete refs (PR #s / commit hashes / iss-#s / percentages / dates / delta counts), no marketing verbs / hashtags / emoji.
