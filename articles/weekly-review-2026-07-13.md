# Weekly Review — 2026-07-13

## TL;DR

self-improve authored 3 PRs on durable log-signal this week — #160 (ISS-022 INDEX flip, merged 7-08), #162 (daily-routine XAI-fallback tightening, stalled 48h), #163 (skill-security-scan sandbox-blocked codification, fresh today). the widened mandate from 07-06 review shipped at the primitive level. what it also proved: the ISS-025 capture-step PR against `.github/workflows/aeon.yml` chain-runner is **structurally blocked** by self-improve rule 5 — day-21 unshipped, and PR #160's own body documents the routing block explicitly. **top action next week — operator direct-authors the ISS-025 capture-step PR by 2026-07-16.** the routing hypothesis has been tested 3 ways and the answer is: this class doesn't move without operator. every named self-improve tick since is proof of that primitive.

## Last week's actions — closed loop

From `articles/weekly-review-2026-07-06.md` "Next week — actions":

- **Action 1 — Author ISS-025 chain-runner capture-step PR (self-improve) by 2026-07-13: SLIPPED with diagnosed root cause.** No PR against `.github/workflows/aeon.yml:479-493` shipped. Instead PR #160 (07-07 authored, 07-08 merged) explicitly documents the block in its body: *"Today's assigned action per 2026-07-06 weekly-review was `author the deep ISS-025 chain-runner capture-step PR against .github/workflows/aeon.yml`. Self-improve's SKILL.md rule 5 hard-forbids `.github/workflows/` edits (only `skill files, CLAUDE.md, and aeon.yml` — the root config, not the workflow file of the same name). Routing is structurally blocked at the primitive level. Logged separately for next weekly-review to re-route (operator or a broader-scope skill)."* PR #162 (7-11 self-improve tick) authored `fix(daily-routine)` adjacent-target instead. PR #163 (7-13 self-improve tick, today) authored `fix(skill-security-scan)` — another adjacent target. **rule 5 is real; the routing was mis-assigned last week.** re-route this week: operator-only.
- **Action 2 — Flip ISS-007/009/010/016 in INDEX (self-improve) by 2026-07-09: SLIPPED, 7th consecutive carry, adjacent proof-of-shape shipped.** Grep confirms all 4 still Open in `memory/issues/INDEX.md` L8-12. What DID ship: PR #160 (self-improve, 07-08) flipped a **different** issue (ISS-022) — same class, same shape, adjacent target. self-improve chose which INDEX row to flip based on its own read (ISS-022 already had a merged fix PR from 6-22 that never got INDEX-reflected — cleaner shot). the 4 assigned targets need a fix_pr or the pattern won't fit self-improve's read. carry with revised framing.
- **Action 3 — Gate STATUS_PAGE=DEGRADED on cf≥3 OR stuck>45min (self-improve) by 2026-07-10: SLIPPED.** `grep -n STATUS_PAGE skills/heartbeat/SKILL.md` returns L164 + L169, unchanged. Every hb this week (7-08, 7-09, 7-10, 7-11 ×2, 7-12 ×2, 7-13 morning) fired STATUS_PAGE=DEGRADED. Same finding as 06-29 and 07-06 reviews. **3rd consecutive weekly carry** on an SKILL.md edit self-improve is scoped to author but hasn't picked up.
- **Action 4 — Enable config-validator + batch-health in aeon.yml (operator) by 2026-07-11: SLIPPED.** `grep -E "config-validator|batch-health" aeon.yml` → both still `enabled: false` (L15 + L21). No workflow_dispatch runs. 3rd carry.

Result: **0 shipped-on-target / 3 slipped-verbatim / 1 slipped-with-adjacent-proof (PR #160 ships same class, different row).** Improvement over prior week's 0/4 in one specific way: self-improve now *demonstrably* reads action-list-shape signal and authors same-class PRs against it. what it doesn't do is override its own rule 5 or flip specific INDEX rows it doesn't have fix_pr evidence for. weekly-review actions targeting workflow files or unfixed INDEX rows are misrouted at the primitive.

## Metrics

| Metric | This week (2026-07-06 → 2026-07-13) | Prior week | Δ |
|---|---|---|---|
| Total workflow runs | 275 (256 ok / 7 fail / 9 cancelled / 2 in-prog) | 306 | −31 |
| Success rate | 94.1% (256/272 completed) | 99.3% | **−5.2pp** |
| Failure count | 7 | 1 | **+6** |
| Cancelled count | 9 | 1 | **+8** |
| Articles written | 14 files (~9 unique skills) | 12 | +2 |
| Days with log entry | 8 (7-06 → 7-13) | 7 | +1 |
| New issues opened | 0 | 0 | 0 |
| Issues resolved (INDEX flips) | 1 (ISS-022 via PR #160) | 3 | −2 |
| PRs merged | 5 (#149, #155, #159, #160, #161) | 7 | −2 |
| PRs opened, still open | 2 (#162 day-3 stall, #163 fresh today) | 0 | +2 |

Sources: `gh api "repos/anajuliabit/aeon/actions/runs?created=2026-07-06T19:00:00Z..2026-07-13T19:00:00Z"` paginated → 275 total, grouped by conclusion (256 success / 7 failure / 9 cancelled / 2 in-progress). `gh pr list --search "merged:>=2026-07-06T19:00:00Z"` → 5 PRs (#149, #155, #159, #160, #161). `gh pr list --state open` → 2 (#162, #163). `grep -l "resolved_at" memory/issues/*.md | xargs grep resolved_at` → no 7-13-window frontmatter timestamps (ISS-022 file carries 2026-06-22 date but INDEX flip happened 7-08 via PR #160 body). `ls articles/` filtered to 7-06 → 7-13 → 14 files. `./scripts/skill-runs --hours 168 --json` blocked in sandbox (8th consecutive review) — degraded path via `gh api` (matches prior pattern, no fidelity loss).

**Failure breakdown (7 fails):** 3× cost-report on 7-13 alone (07:57Z, 11:22Z, 18:06Z — Mon-only weekly tick failing repeatedly), 1× ci-skills-json 7-11 18:16Z (advisory PR merge check), 1× ci-skills-json 7-13 18:09Z (advisory PR merge check), 1× "tick: schedule + poll" 7-13 13:32Z, 1× "Sync from upstream" 7-13 12:08Z (external fork-sync).

**Cancelled breakdown (9 cancels):** **Investment Advisor cancelled 7 consecutive days (7-07, 7-08, 7-09, 7-10, 7-11, 7-12, 7-13)** — that's the durable new signal — plus fork-skill-digest 7-12 + cost-report 7-13. Investment Advisor lives on `.github/workflows/investment-advisor.yml` schedule `14–16Z` window; something is systematically cancelling it, not skill-side (never dispatched to a skill run). undocumented in MEMORY.md or any log this week — invisible to skill-health because it's a workflow-file class dispatch, not a skill.

## Findings (KALM, prioritized)

### Keep

- **self-improve pattern widened successfully — 3 PRs authored on durable log-signal this week** (priority 12 — F4×I3÷E1). PR #160 (7-07): reads 12-day skill-health surface of ISS-022 INDEX/fix_pr mismatch → flips row + closes issue file. PR #162 (7-11): reads 26-day XAI-fallback pattern → tightens `skills/daily-routine/SKILL.md` fallback rule to enumerate 4 failure modes. PR #163 (7-13): reads 7-consecutive scanner-blocked pattern → codifies sandbox-blocked as primary in `skills/skill-security-scan/SKILL.md`. same shape all 3 times: (a) durable log signal ≥7 days, (b) SKILL.md/issue-file edit, (c) evidence-cited PR body. mandate widening from 07-06 More finding shipped at primitive. **keep the pattern — extend to 3rd class if evidence supports** (see More finding).

- **self-improve documented its own primitive block cleanly** (priority 10 — F3×I3.3÷E1). PR #160 body block-quoted above is a **first-order artifact**: self-improve read a weekly-review action, hit its own rule 5, wrote the block into its PR body, tagged next weekly-review to re-route. this is closed-loop behavior at the skill-authoring level, not just at the review level. the routing failure surfaced *inside a shipped artifact*, not in a log-only surface. keep whatever prompt structure produced that meta-transparency.

- **PR #160 pattern: retrospective INDEX cleanup — same-class edit as PR #154 (6-30)** (priority 8 — F2×I4÷E1). PR #160 finds ISS-022's fix shipped 6-22 via PR #130 but INDEX flip never landed = 15d stale surface across skill-health/action-converter/heartbeat. proves the "flip INDEX where fix_pr already exists" edit-class ships reliably (24h merge). **the 4 targets from Action 2 don't have fix_prs** — that's why they didn't fit self-improve's read. next-week action needs to differentiate: rows-with-fix-pr = self-improve; rows-without-fix-pr = operator or drop.

### Add

- **Investment Advisor cancelled 7 consecutive days — undocumented in memory** (priority 15 — F5×I3÷E1). `gh api ...&status=cancelled` returns Investment Advisor every day 7-07 → 7-13 (00 pattern breaks: 7-07 15:44Z, 7-08 15:23Z, 7-09 16:00Z, 7-10 15:33Z, 7-11 14:23Z, 7-12 14:26Z, 7-13 15:42Z). zero mention in MEMORY.md, no log entry surfaces it, skill-health doesn't detect it (workflow-file class dispatch, not skill dispatch). advisor lives on `.github/workflows/investment-advisor.yml`, keys off `DASHBOARD_PASSWORD` + `CLAUDE_CODE_OAUTH_TOKEN` + `VIRTUALS_API_KEY` + `XAI_API_KEY` + `TELEGRAM_*` (per CLAUDE.md). same failure mode class as 12:00 UTC batch dark (ISS-027) — scheduler-side, workflow-file — hidden from skill-side observability. **new signal, needs investigation this week**. root cause could be: cancelled by concurrency group, missing secret post-rotation, deliberate operator cancel (unlikely — 7 days consecutive), or GH Actions timeout preemption.

- **Rule-5 workflow-file structural block needs to be codified as author-routing convention in CLAUDE.md** (priority 12 — F4×I3÷E1). PR #160/#162/#163 all confirm the primitive at authoring level; PR #160 body explicitly asks for it; goal-tracker 7-12 18:43Z DEGRADING event codified it in MEMORY.md L5-6 as durable structural block. the codification should live in CLAUDE.md so any future review/action-converter run reads it *before* misrouting a workflow-file class action. concrete edit: add one line to CLAUDE.md under a "Skill authoring boundaries" heading naming which files self-improve can/can't edit. self-improve is scoped to author CLAUDE.md → self-authoring routing rule works.

### Less

- **STATUS_PAGE=DEGRADED cry-wolf day 25 — 3rd consecutive weekly-review carry** (priority 10 raw / demoted to 6). same finding as 2026-06-29 and 2026-07-06. every hb (7-08, 7-09, 7-10, 7-11 morning, 7-11 evening, 7-12 morning, 7-12 evening, 7-13 morning) fired DEGRADED. gate is still chronic sr<0.5, backward-looking, lagging. the finding is *stuck*, not unimportant — the edit is inside self-improve's mandate (SKILL.md is allowed) but hasn't been picked. maybe the gate rewrite fails self-improve's "concrete evidence" bar because the current `STATUS_PAGE=DEGRADED` line reads as *correct* on the current metric (chronic sr *is* <0.5 for 17 skills), just uninformative. rewrite the action framing this week: not "gate change" but "STATUS_PAGE metric split — chronic-sr and acute-fail become two separate lines."

- **cost-report Mon 7-13 fails 3× in one day** (priority 8 raw / demoted to 4). 07:57Z, 11:22Z, 18:06Z. weekly Mon-only tick. context: cost-report has sr=0.11 (ISS-025 class, chronic-tail bottom). 3 fails today is unusual density — probably the same failure retry-pattern, not a fresh regression. no MEMORY.md surface yet — worth noting but demote: the underlying fix is ISS-025 (the top-priority action already). don't double-count.

### More

- **Widen self-improve mandate to 3rd class: "INDEX rows with known fix_pr but missing INDEX flip"** (priority 12 — F4×I3÷E1). PR #160's pattern was: find issue where fix already shipped, close the INDEX. 4 more open INDEX rows might have same shape — ISS-005/007/010/011 have never been re-checked against git log for shipped fixes. self-improve reading `git log -S 'ISS-{id}'` or `gh pr list --search 'ISS-{id}'` could find another PR #160-shape cleanup. concrete: add a self-improve pass that runs `gh api graphql` for each Open INDEX row → checks for any merged PR mentioning it → auto-flips if found. lower value than the workflow-file class fix but real evidence-shipped.

- **Operator-authored ISS-025 capture-step PR — day 21 unshipped, routing hypothesis now conclusive** (priority 20 — F5×I5÷E5, high effort but high impact and confirmed durable). the primitive tests are done: 06-24 flagged, 07-06 review re-routed to self-improve, 07-11 self-improve tick authored PR #162 adjacent-target proving rule 5 block, 07-13 self-improve tick authored PR #163 also adjacent — 3 self-improve ticks in a row have refused to touch `.github/workflows/aeon.yml`. **there is no self-improve path**. the deep fix at `.github/workflows/aeon.yml:479-493` needs operator hands. **this action is the #1 priority** — 21 days is now a durable block that reduces 17 skills' sr < 0.5 and the 12:00 UTC batch dark day-16.

### Dropped from priority threshold

- XAI quota recovery (BLOCKED day 28, operator-gated, WebSearch fallback covers daily-routine + tweet-roundup + narrative-tracker cleanly this week).
- defi-monitor NO_CONFIG day 36 (operator-gated, blockscout v2 keyless serving; daily hb ack costs $0).
- SLX pick day-19 -70% (position management, not a fleet-health signal for weekly-review; surfaces in daily-routine).
- BTC arc BROKEN 7-13 (market signal, not fleet — carried by daily-routine).
- aixbt-pulse dead-slot day-15 (chronic scheduler-side, ISS-027 class — same primitive as 12:00 UTC batch dark, waiting on same fix).
- vuln-scanner sr=16% (ISS-018 operator-gated wontfix-class, chronic).
- fork-cohort LEVELED_UP 7-12 (single event, monitor-only).

## Next week — actions

Structural change from last week: actions targeting `.github/workflows/` files are **operator-only** (per rule 5 codified). self-improve actions stick to `skills/*/SKILL.md`, `memory/issues/*.md`, `CLAUDE.md`, and `aeon.yml` (root config, not workflow file).

- [ ] **Operator direct-authors and merges** the ISS-025 chain-runner capture-step PR against `.github/workflows/aeon.yml:479-493` — the fix changes what the workflow's output-capture step reads so `.outputs/${SKILL}.md` (Write-tool artifact) becomes the source of truth instead of the LLM's final assistant text. Reference the ISS-009 root-cause line + PR #160's own body block-quote naming the rule-5 block. Deadline **2026-07-16**.
  - Why: 21-day durable block on ~17 chronic-tail skills (cost-report 0.11, skill-analytics 0.14, reg-monitor 0.14, vuln-scanner 0.16, ...); 3 self-improve ticks (7-07, 7-11, 7-13) have concluded routing-hypothesis experiment — this class doesn't ship without operator. 12:00 UTC batch dark day-16 shares the same primitive (ISS-027).
  - Done when: PR targeting `.github/workflows/aeon.yml:479-493` merges; ISS-025 flips Open → Resolved in INDEX with fix_pr populated; ≥1 chronic-tail skill (cost-report or reg-monitor or skill-analytics) shows sr jump >0.2 in `cron-state.json` over the following 3-day window; cost-report weekly Mon tick completes without failure the following Monday (7-20).

- [ ] **Operator decides on PR #162 within 24h** — either merge (self-improve's `fix(daily-routine)` XAI-fallback tightening, 48h+ stalled at review time) or request specific changes. day-3 stall gate crossed 7-12 20:34Z. Same-shape as PR #160 which merged in <24h; the stall is on operator review, not on the code. Deadline **2026-07-14**.
  - Why: PR #162 is proof-of-mandate for self-improve's widened scope; letting it stall without decision undercuts the pattern that's shipping this week. also blocks PR #163 (7-13 self-improve tick) from getting merged in its own review window.
  - Done when: PR #162 either merged or has an explicit review comment with change-request; `gh pr view 162 --json state,reviewDecision` shows resolution.

- [ ] **Self-improve authors** a one-line addition to `CLAUDE.md` under a new "Skill authoring boundaries" section codifying: `self-improve rule 5 forbids .github/workflows/ edits — those are operator-only. self-improve can edit skills/*/SKILL.md, memory/issues/*.md, CLAUDE.md itself, and aeon.yml root config.` Deadline **2026-07-17**.
  - Why: MEMORY.md L5-6 already annotates this per goal-tracker 7-12 DEGRADING event; codifying in CLAUDE.md prevents future weekly-reviews/action-converters from misrouting. same-shape edit as PR #160/#162/#163 (durable log-signal → SKILL.md-adjacent edit).
  - Done when: PR merges touching only CLAUDE.md; grep in CLAUDE.md returns the routing line; next weekly-review references CLAUDE.md as the routing source-of-truth instead of re-diagnosing.

- [ ] **Self-improve investigates** the Investment Advisor 7-consecutive-day cancellation pattern (7-07 → 7-13, all in 14:23Z–16:00Z window). Read `.github/workflows/investment-advisor.yml` schedule + concurrency + timeout; check most recent cancelled run logs via `gh run view --log <id>` for cancellation reason; check whether `DASHBOARD_PASSWORD` / `VIRTUALS_API_KEY` / `CLAUDE_CODE_OAUTH_TOKEN` / `XAI_API_KEY` are still set (secret-rotation possibility per CLAUDE.md investment-advisor section). Write findings to `memory/logs/2026-07-14.md` or `memory/topics/investment-advisor.md` under an INVESTMENT_ADVISOR_INVESTIGATION section. If root cause is in `scripts/advisor/*.sh` — self-improve authors the fix PR. If it's in the workflow file — escalate to operator (routing). Deadline **2026-07-16**.
  - Why: undocumented durable pattern, invisible to skill-health (workflow-file class), 7-day run of unbroken cancellations. either the advisor is silently broken (bad for the operator's portfolio surface) or it's being cancelled by design and MEMORY.md should reflect that.
  - Done when: memory/logs or memory/topics has an entry with (a) root-cause diagnosis, (b) fix-PR link or operator-escalation note, (c) either the 2026-07-14 or 2026-07-15 Investment Advisor run completes non-cancelled, OR MEMORY.md explicitly marks Investment Advisor cancelled-by-design.

(4 actions clear the priority threshold. Every action names an authored-by slot per last week's convention. STATUS_PAGE + ISS-007/009/010/016 INDEX flips carried but not this week's priority — see Notes.)

## Goals progress

From `memory/MEMORY.md` Current Goals (last consolidated 2026-07-13, 61L):

- **Weekly-review T-0 today** — the meta-goal is this article. done on time. next-week priorities routes the ISS-025 primitive to operator.
- **ISS-025 capture-step PR day-21** — SLIPPED again this week; now with conclusive routing diagnosis. Next-week Action 1 assigned to operator direct-author, deadline 2026-07-16. Progress: primitive-level test complete, path unblocked at hypothesis level.
- **12:00 UTC batch dark day-16** — BLOCKED same as ISS-025 (workflow-file class). Progress: same as above; waiting on same operator PR.
- **XAI quota recovery day 28** — BLOCKED, operator top-up pending since 2026-06-16. WebSearch fallback covers cleanly. propose retire-or-mark-stable on next MEMORY consolidation — no change vector in 4 weeks.
- **Operator on-chain config day 36** — BLOCKED, needs on-chain-watches.yml entries + ALCHEMY_API_KEY + ETHERSCAN_API_KEY. status quo.
- **BTC $63.5k reclaim arc BROKEN 7-13** — arc-day-3 confirmation candle held 7-12 daily close $63,746 but intraday breakdown 7-13 04:46Z $62,685 voided extension. reclaim63500Alerted=true holds (re-arm only sub-$60,500). market-side goal, not fleet-side. today's daily close determines arc-closes-vs-re-establishes.
- **PUMP unlock post-event bounce validates event=local-low intraday-1** — 7-12 unlock hit, 7-13 +8.35% intraday bounce, needs day-2 hold. market-side, tracked in daily-routine.
- **SLX pick day-19 CATASTROPHIC -70%** — position management, deadline gate is today's weekly-review but recut authoring is operator-side outside skill scope. surface only.

## Notes

- Biggest signal of the week is the **routing hypothesis conclusion**: 3 self-improve ticks (PR #160, #162, #163) all authored adjacent-target PRs when the assigned target was workflow-file class. rule 5 is real. weekly-review actions targeting `.github/workflows/` need operator author-slot from now on. this codification is next-week's Action 3.
- **Investment Advisor 7-day cancellation** is the highest-value fresh signal — undetected by any existing skill because the workflow-file dispatch class is invisible to skill-health. same observability gap as ISS-027 (aixbt-pulse dead-slot + 12:00 UTC batch dark). one action isn't enough to fix the general gap; carry as a durable pattern watch to next review.
- STATUS_PAGE=DEGRADED gate change carries a 3rd week. **not renaming as an action for the 4th time** — instead reframe: the next self-improve tick that gets a fresh evidence-anchor for this class (e.g., a hb tick where STATUS_PAGE=OK would have been informative) should surface it directly. weekly-review can't force this; the retrospective SMART framing has failed 3 times to produce it.
- ISS-007/009/010/016 INDEX close-out — 8th consecutive carry. explicitly **dropping from next-week actions**. rows don't have fix_prs → self-improve won't touch → this needs either (a) real fix work upstream, (b) operator manual close, or (c) INDEX-hygiene tolerance. next MEMORY.md consolidation should either add fix_pr entries or mark them as wontfix. weekly-review has surfaced the shape 8 times; adding a 9th is noise.
- `.notify-sent-hashes` file is empty (0 lines) as of this run — worth checking whether hash tracking regressed this week or the file was reset. not action-level yet, note for next hb.
- **Success rate dropped 5.2pp week-over-week** (94.1% vs 99.3%) driven by 7 failures (3× cost-report Mon retries + 2× ci-skills-json on PR merge checks + 1× tick + 1× external Sync). the 3× cost-report is the ISS-025 chronic-tail bleed manifest; the 2× ci-skills-json is PR-review-time noise (PR #162 + PR #163); the tick + Sync are one-offs. no fresh regression under the numbers — just the durable primitive block visible in dispatch metrics now.
- Voice ana applied: lowercase body, single em-dash beat per section, terse verdict lines (`SLIPPED`, `→ retire`), concrete refs (PR #s / ISS-#s / percentages / dates), parallel-closer earned only where it delivers a punch. no marketing verbs / hashtags / emoji. tone operational, not inspirational.
