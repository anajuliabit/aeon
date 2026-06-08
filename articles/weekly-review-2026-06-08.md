# Weekly Review — 2026-06-08

## TL;DR

claude weekly rate limit hit 2026-06-06 12:37Z and the fleet has been failing on a 429 ever since — 140 failures clustered 6-06/6-07/6-08, 0 mints on the last 2 days, 0 log entries written on 6-07 or 6-08. virtuals fallback shipped this week (PRs #77/#78/#79) covers 5 coingecko price-digest skills only — `FALLBACK_CG_SKILLS=" defi-overview token-movers token-pick token-alert market-context-refresh "` at `aeon.yml:441`. reppo-trading-agent / reppo-digest / reppo-voter / reppo-orchestrator all fall through to `exit 1`. top action next week — extend the fallback list to the reppo chain by 2026-06-11 so the next weekly limit doesn't take 48h+ of mints with it.

## Last week's actions — closed loop

From `articles/weekly-review-2026-06-01.md` "Next week — actions":

- **Action 1 — write `configs/datanets/RUBRIC.md` + ≥3 datanet configs by 2026-06-05: SLIPPED (3rd consecutive week).** `ls configs/datanets/` returns only `tradinggymai.md`. 2026-06-06 reppo-orchestrator log L4-7: "15 new datanets surfaced (1, 2, 4–8, 10, 11, 13–18)". Carries — but now structural, not a one-week miss.
- **Action 2 — patch `.github/workflows/chain-runner.yml` lines 41 + 416 to env-indirect `inputs.chain` and close ISS-017 by 2026-06-03: SHIPPED.** PR #64 merged 2026-06-03 14:10Z; `memory/issues/INDEX.md:27` shows ISS-017 under Resolved with link `focus/iss-017-chain-runner-env`.
- **Action 3 — ship ISS-009 follow-ups (a) emit-in-assistant-text contract + (b) chain-runner fail-fast `continue` → `break` by 2026-06-05: SHIPPED.** PR #69 merged 2026-06-03 23:00Z (codifies emit-in-assistant-text in `skills/reppo-orchestrator/SKILL.md`); `.github/workflows/chain-runner.yml:360` reads `[ "$ON_ERROR" = "fail-fast" ] && break`. ISS-009 row at `INDEX.md:9` still says Open — bookkeeping flip slipped, code shipped.
- **Action 4 — flip ISS-007 + ISS-010 + ISS-016 to Resolved in `memory/issues/INDEX.md` by 2026-06-03: SLIPPED on the named items.** All three still under Open. ISS-013 + ISS-014 + ISS-017 got flipped instead — bookkeeping happened, but on the wrong queue.

Result: 2 shipped / 2 slipped / 0 abandoned. The two slipped items both carry forward — datanet rubric for the 3rd time, ISS bookkeeping for the 2nd.

## Metrics

| Metric | This week (2026-06-02 → 2026-06-08) | Prior week | Δ |
|---|---|---|---|
| Skill runs (workflows) | 369 | 270 | +99 |
| Successes / failures / cancelled | 230 / 136 / 2 | 267 / 3 / 0 | −37 / +133 / +2 |
| Articles written | 5 | 16 | −11 |
| Days with a log entry written | 5 (6-02 → 6-06) | 7 | −2 |
| New issues opened | 0 | 10 | −10 |
| Issues resolved (INDEX flips) | 3 (ISS-013, ISS-014, ISS-017) | 6 | −3 |
| PRs merged | 17 (#62, #63, #64, #65, #66, #67, #69, #70, #71, #73, #74, #75, #76, #77, #78, #79, #80) | 47 | −30 |
| Reppo mints on-chain | 5 (15th–19th) | 14 | −9 |
| Reppo votes on-chain | 7 | 26 | −19 |

Sources: `gh api repos/anajuliabit/aeon/actions/runs?created=>2026-06-01T19:00:00Z` paginated, filtered to `name startswith("skill:") or startswith("chain:")` (369 with 230/136/2/1-null conclusions); failure dates `1 on 6-01 / 37 on 6-06 / 56 on 6-07 / 46 on 6-08` — 6-02 through 6-05 produced zero failures, then the cliff. `ls articles/` filtered to 2026-06-02..06-08 (5 — all `skill-freshness-*` + 1 `skill-analytics-2026-06-03.md`, none on 6-06/6-07/6-08). `gh pr list --state merged --search "merged:>=2026-06-01T19:00:00Z"` (17 — PR #68 + PR #72 were closed without merge, PR #81 was closed, PR #82 is open). `memory/issues/INDEX.md` diff vs prior review (3 flips, 0 new). `memory/topics/reppo.md` mints/votes tables (5 mint rows + 7 vote rows confirmed tx). `memory/logs/` (5 dated files 6-02 → 6-06, none on 6-07/6-08).

Sample failure (gh run view 27158884840, reppo-digest at 2026-06-08 18:36:31Z): `{"is_error":true,"api_error_status":429,"result":"You've hit your weekly limit · resets 7pm (UTC)","stop_reason":"stop_sequence"}` → `exit 1`. This is the same shape across every 6-06/6-07/6-08 failure I sampled.

## Findings (KALM, prioritized)

### Keep

- **Reppo phase 2 (Pinata pin + platform POST) clean across all 5 mints this week** (priority 20 — F5×I4÷E1). Mints 15–19 all carry "Phase 2 metadata POST returned HTTP 200" / "ipfs://Qm…" in their ledger row. Phase 2 has now run clean for **9 consecutive mints** since the 11th-mint 06e7715d breakthrough 2026-05-30. Evidence: `memory/topics/reppo.md` rows for 4a9a582a / 16671d6f / e2e925b2 / 60907e54 / cfd710ae.
- **ISS-017 + ISS-009 follow-ups shipped within deadline** (priority 15 — F3×I5÷E1). Both top-3 next-week actions from the prior review landed by 2026-06-03 23:00Z, two days early on action 3. PR #64 (env: `CHAIN` indirection at `chain-runner.yml:41/:416`) + PR #69 (emit-in-assistant-text contract in `skills/reppo-orchestrator/SKILL.md`) + `chain-runner.yml:360 break`. No incident-class recurrence of ISS-009 in the 6-02 → 6-06 window (0 chain-runner output-overwrite events logged).
- **6-05 record-setting day held the velocity before the cliff** (priority 8 — F2×I4÷E1). 4 mints in one UTC day (15th 4a9a582a / 16th 16671d6f / 17th e2e925b2 / 18th 60907e54), surpasses prior 3-mint days. Worth keeping the Step-4.2 same-wallet regression check + perp-only filter — both fired correctly across the cluster (16671d6f tiebreak, e2e925b2 Sharpe-vs-pnl pick, 4a9a582a 11.55% spot admit). Evidence: `memory/topics/reppo.md` rows 15–18 + `memory/logs/2026-06-06.md:35-46`.

### Add

- **Virtuals fallback coverage for the reppo chain — the rate-limit hole** (priority 25 — F5×I5÷E1). `aeon.yml:441` defines `FALLBACK_CG_SKILLS=" defi-overview token-movers token-pick token-alert market-context-refresh "`. Every skill outside that list — reppo-orchestrator / reppo-trading-agent / reppo-voter / reppo-digest / morning-brief / daily-routine / heartbeat / goal-tracker / skill-health / reflect / action-converter — falls straight through to `exit 1` on a 429. Result: 140 failures clustered on 6-06/6-07/6-08, 0 mints last 2 days, 0 log entries last 2 days. The fix mechanism already exists (PRs #77/#78/#79 wired Virtuals + deepseek-v4-flash); it just needs the per-skill list extended or a category split (CG-price vs reppo-chain).
- **Datanet rubric, structurally** (priority 10 — F5×I5÷E2.5). 3rd consecutive weekly review slipping the same action. `configs/datanets/` still only has `tradinggymai.md` and the orchestrator surfaces "15 unassigned" every run (2026-06-06 1st + re-run both logged). The work hasn't fit between the higher-priority reppo blockers shipping — now those have shipped, so the rubric needs a different framing: either operator pick + rubric written together, or rubric + 1 datanet (lower bar than ≥3) to unstick.
- **ISS-018 for the weekly-limit incident** (priority 8 — F3×I4÷E1.5). 140 failures in 3 days with no issue file. The pattern is recurring (Claude weekly limit will trip again next cycle), the detection is clean (`api_error_status:429` + `"weekly limit"` in `result`), and the fix locus is `aeon.yml:441`. Filing makes the issue routable to health/repair skills and lets the next health sweep see prior context.

### Less

- **Investment-advisor swarm shipped same day as the rate-limit incident** (priority 6 — F2×I3÷E1). PR #80 merged 2026-06-08 16:00Z (8 advisor skills + chain wiring), `chain:investment-advisor` first run failed 17:04Z (same 429 root cause), PR #82 opened 18:13Z to supersede with a standalone Virtuals workflow. Net: an afternoon of new-skill plumbing during an active fleet outage, followed by an immediate "supersedes #80" pivot. Two paths to keep this lower next time: (a) gate new-chain merges on a fleet-health probe, (b) flag rate-limit days as "no new skills" days. Evidence: gh PR #80 (merged), PR #81 (closed), PR #82 (open), gh run view of `chain:investment-advisor` 2026-06-08T17:04:46Z failure.
- **No daily logs written on 6-07 or 6-08** (priority 9 — F4×I3÷E1.5). `ls memory/logs/` stops at `2026-06-06.md`; 6-06 itself is only 235 lines / 9 skill entries vs the 350-700 / 30-40 entries on 6-02 → 6-05. The proximate cause is the rate limit (Claude can't run, can't append), but the loss is real — 2 days of receipts gone. Either (a) fallback skills append a stub log line, or (b) a separate cron writes "no skills ran today, here's the failure count" to plug the gap.

### More

- **Per-skill Virtuals fallback as a first-class pattern** (priority 12 — F4×I4÷E1.5). PRs #77/#78/#79 prove the mechanism works for CG-price digests. The same shape extended to reppo skills would have absorbed 6-07 and 6-08 (worst case: degraded-fidelity mints instead of zero mints). This is the highest-leverage place to invest next week — every weekly-limit cycle without it costs ~48h of mint velocity.

### Dropped from priority threshold

- INDEX bookkeeping flips for ISS-007 / ISS-010 / ISS-009 / ISS-016 (priority 5 — mechanical, fits inside next-week Action 4).
- "Cleanup chain-runner scratch" — still in MEMORY.md L46-47 but no movement and the actual files are `.candidates.json` + a few `.tmp-*` (low-impact).
- ISS-005 carries (1 trip on 2026-06-06 morning, structural — only 1 non-own/non-voted/non-HL-perp pod at epoch 102 produced the all-DISLIKE flag). Watching, not actionable.

## Next week — actions

- [ ] Extend Virtuals fallback to the reppo chain — add `reppo-orchestrator reppo-trading-agent reppo-voter reppo-digest` to a new `FALLBACK_REPPO_SKILLS` list (or a per-skill switch) in `.github/workflows/aeon.yml` around line 441, mirroring the PR #79 `deepseek-v4-flash` pattern, by 2026-06-11
  - Why: 140 failures on 6-06/6-07/6-08 + 0 mints last 2 days, all on `api_error_status:429 "weekly limit"` falling through `exit 1`
  - Done when: a new `FALLBACK_REPPO_SKILLS` constant (or equivalent) is at `aeon.yml:441` with the 4 reppo skill names; a run with `CLAUDE_OUTPUT.is_error=true && api_error_status=429` on any reppo skill emits `::warning::Claude limited — ${SKILL_NAME} via Virtuals fresh-fetch fallback` instead of `::error::Claude CLI failed`; PR merged
- [ ] File ISS-018 in `memory/issues/` for the weekly-limit incident with the 140-failure window + `aeon.yml:441` fix locus + recurrence pattern (Claude weekly cycle), and add the row to `memory/issues/INDEX.md` Open by 2026-06-09
  - Why: 3-day cluster with no issue file means skill-health can't see prior context next cycle
  - Done when: `memory/issues/ISS-018.md` exists with frontmatter (severity: high, category: rate-limit, detected_by: weekly-review, detected_at: 2026-06-08), and `grep "ISS-018" memory/issues/INDEX.md` returns 1 Open row
- [ ] Write `configs/datanets/RUBRIC.md` + add 1 new datanet config (lowered from ≥3) to break the 3-week slip pattern, by 2026-06-12
  - Why: 3rd consecutive review slipping; "15 unassigned" surfacing every orchestrator run; lowering the bar to ≥1 to actually move
  - Done when: `configs/datanets/RUBRIC.md` exists with ≥3 named criteria; `ls configs/datanets/` shows ≥2 files (existing tradinggymai.md + 1 new); next reppo-orchestrator run logs ≤14 unassigned
- [ ] Flip ISS-007 + ISS-010 + ISS-009 + ISS-016 to Resolved in `memory/issues/INDEX.md` — all four have code shipped or workarounds proven durable (ISS-009 PR #69, ISS-010 PR #32, ISS-016 ledger workaround 18+ consecutive runs) — by 2026-06-10
  - Why: bookkeeping carries from 2 consecutive weekly reviews; INDEX.md Open count overstates real open count
  - Done when: `grep -c "ISS-007\|ISS-009\|ISS-010\|ISS-016" memory/issues/INDEX.md` shows all 4 rows under Resolved

## Goals progress

From `memory/MEMORY.md` Current Goals (last consolidated 2026-06-05):

- **ISS-009 sub-task (b) — chain-runner `continue` → `break` flip.** **Shipped this week.** `.github/workflows/chain-runner.yml:360` reads `[ "$ON_ERROR" = "fail-fast" ] && break`. ISS-009 row still Open in INDEX (bookkeeping flip pending — covered by next-week Action 4). Retire after the INDEX flip.
- **Trading-agent: codify spot_pct threshold + Sharpe-vs-pnl tiebreak.** **No progress this week.** 6-06 reppo-trading-agent log proves both rules still firing as operator-defaults (11.55% spot admit + Sharpe tiebreak across mints 17/18), but `skills/reppo-trading-agent/SKILL.md` Step 4 / Step 4.2 still doesn't carry the explicit text. Operator decision required — Aeon can't codify a knob the operator hasn't picked. Cite: MEMORY.md L17-26.
- **ISS-016 own_pod_ids prefetch repair.** Workaround durability extended this week — 6-06 morning voter filtered pod 642 (18th-mint own), 6-06 evening voter filtered 642 + 644 (18th + 19th own) — **18+ consecutive voter runs at prefetch count=0**, ledger workaround absorbing every own-pod. Priority remains low; covered by next-week Action 4 (flip Resolved).
- **15 unassigned reppo datanets.** **Stalled, no progress this week.** Covered by next-week Action 3 (now ≥1 not ≥3 to unstick). Cite: 2026-06-06 reppo-orchestrator logs.
- **INDEX bookkeeping flips queued.** Partial. 3 flips happened (ISS-013 / ISS-014 / ISS-017), 4 carries (ISS-007 / ISS-009 / ISS-010 / ISS-016) — covered by next-week Action 4.
- **on-chain-monitor / defi-monitor `watches.yml`.** Still NO_CONFIG. 4+ consecutive days. Operator-gated. Propose retire-from-goals or mark explicitly as operator-action.
- **Cleanup chain-runner scratch.** No movement. Propose retire — low signal vs the rest of the queue.
- **Chain-state-flip anomaly carry.** **Recurred.** `chore(chain): reppo-swarm failed` commits on 6-06 12:37 + 6-06 18:09 + 6-07 00:09 + 6-07 06:51 + 6-07 12:27 + 6-07 18:31 + 6-08 00:13 + 6-08 07:14 + 6-08 12:21 + 6-08 18:37 — 10 consecutive cycle failures all rooted in the weekly-limit 429 (different cause than the 6-02 12:23Z step-level writer flag). Once the fallback Action 1 lands, expect this to clear.

## Notes

- The weekly limit message says "resets 7pm (UTC)" but the failures span 54h+ across multiple day-boundaries — so the reset is not happening at the natural 7pm UTC day mark. Could be a fixed weekly anchor (e.g. Monday 7pm UTC). Worth a focused observation next reset window.
- Investment-advisor architecture pivot in flight: PR #80 (aeon skills) → PR #81 (chain hotfix, closed) → PR #82 (open: standalone Virtuals workflow). PR #82 explicitly supersedes #80. Worth one more loop of operator review before counting any of it as shipped.
- Notification: this run will not send. `./notify` is unavailable in the sandbox during this review (no `.pending-notify/` queue currently, no outbound channel reachable from here) — the post-run delivery step picks up anything staged, but with the weekly limit also blocking the heartbeat skills, the channel is going to be quiet by default until the fallback lands. Notification gated on next-week Action 1 success at the earliest.
- skill-runs counted via direct `gh api` filter — `./scripts/skill-runs` again declined approval in the sandbox, same degraded-source pattern as the prior 2 reviews. `memory/cron-state.json` corroborates the success counts but does not capture the 6-06/6-07/6-08 failure spike (cron-state writers ran during dispatched, not after fail) — confirms why fleet health didn't auto-flag.
- soul/SOUL.md + STYLE.md applied — lowercase, named numbers (140 failures, 5 mints, 17 PRs, PR #s, ISS-#s, file:line), em-dash one per section, parallel-closer in TL;DR ("140 failures clustered… 0 mints on the last 2 days, 0 log entries written on 6-07 or 6-08").
