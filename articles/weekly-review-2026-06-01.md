# Weekly Review — 2026-06-01

## TL;DR

reppo went from 0 mints + 0 votes day-4 last week to 14 mints + 26 votes on-chain this week. five of the open blockers (ISS-004 / ISS-006 / ISS-008 / ISS-012 / ISS-013 / ISS-014) cleared in code; phase 2 (pin + platform POST) ran clean 3 runs in a row. the one thing the loop has not produced: forward motion on the 14 unassigned datanets, surfaced every reppo-orchestrator run for 12 consecutive days. top action next week — write `configs/datanets/RUBRIC.md` and map ≥3 of those 14 datanets to a concrete agent by 2026-06-05.

## Last week's actions — closed loop

From `articles/weekly-review-2026-05-25.md` "Next week — actions":

- **Action 1 — on-chain verification + close ISS-004 + ISS-006 by 2026-05-28: SHIPPED.** ISS-004 closed by PR #10 (auto-grant subnet), ISS-006 closed by PR #23 (auto-lock veREPPO), both flipped Resolved 2026-05-26 in `memory/issues/INDEX.md`. Evidence: first mint tx `0x77f1386f…` 2026-05-26 + first vote tx `0x937d9f3c…` 2026-05-26 (memory/topics/reppo.md L11, L29). 14 mints + 26 votes on-chain through 2026-06-01 — the receipt the action demanded.
- **Action 2 — write `configs/datanets/RUBRIC.md` + map ≥3 of 14 datanets by 2026-05-30: SLIPPED.** `configs/datanets/` still contains only `tradinggymai.md`; no RUBRIC.md exists. Today's reppo-orchestrator (2nd run) log: "14 unassigned datanets surfaced (1, 2, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17 — same set as 1st run, **12th consecutive day**)". Carries.
- **Action 3 — patch `skills/skill-evals/evals.json` `output_pattern` for token-alert / skill-health / hn-digest / polymarket by 2026-05-31: SHIPPED.** PR #31 "fix(skill-evals): align output_pattern with actual skill output locations" merged 2026-05-28T12:05Z (3 days early).

Result: 2 shipped / 1 slipped / 0 abandoned / 0 blocked. Slipped item is the highest-ROI one and carries into next week.

## Metrics

| Metric | This week | Prior week | Δ |
|---|---|---|---|
| Skill runs | 270 | 111 | +159 |
| Successes / failures | 267 / 3 | 108 / 3 | +159 / 0 |
| Articles written | 16 | 10 | +6 |
| Notifications staged/sent | ~90 | 36 | +54 |
| New issues opened | 10 | 7 | +3 |
| Issues resolved | 6 | 3 | +3 |
| PRs merged | 47 | 8 | +39 |
| Reppo mints on-chain | 14 | 0 | +14 |
| Reppo votes on-chain | 26 | 0 | +26 |

Sources: `gh api repos/{owner}/{repo}/actions/runs` filtered to `created_at >= 2026-05-25T19:00:00Z` and `name startswith "skill:"` (270 with conclusion: 267 success / 1 failure / 2 cancelled); `gh pr list --state merged --search "merged:>=2026-05-25T19:00:00Z"` (47); `ls articles/` filtered to 2026-05-26..06-01 (16); `memory/issues/INDEX.md` open vs resolved tables (10 new — ISS-008..017 — and 6 resolved — ISS-004/006/008/012/013/014); `memory/topics/reppo.md` Minted-strategies + Votes-cast tables (14 mint rows + 26 vote rows, all tx-confirmed). The 3 non-success runs: 1 `defi-overview` failure 2026-05-26 12:39Z, 1 `reppo-trading-agent` cancelled 2026-05-28 13:15Z, 1 `skill-leaderboard` cancelled 2026-06-01 17:01Z.

## Findings (KALM, prioritized)

### Keep

- **reppo on-chain loop is producing receipts at scale** (priority 25 — F5×I5÷E1). 14 mints + 26 votes on-chain in 7 days from 0/0 the prior week. Five blockers cleared in code (ISS-004 PR #10, ISS-006 PR #23, ISS-008 PR #21, ISS-012 PR #44, ISS-013 operator JWT rotation, ISS-014 platform self-healed). Phase 2 (pin + platform POST) clean 3 consecutive runs (2026-05-30 → 2026-05-31 morning per MEMORY.md L9-10). Evidence: memory/topics/reppo.md L11-24 (14 success tx rows) + L29-50+ (26 vote success tx rows).
- **PR throughput** (priority 20 — F5×I4÷E1). 47 PRs merged 2026-05-25T19:00Z → 2026-06-01 — 5.9× prior week's 8. Issue → PR → close cycle ran on ISS-008/009/010/012/013/014/015/016 within the same day for most. Evidence: `gh pr list --state merged --search "merged:>=2026-05-25T19:00:00Z"` returns 47; PR #21 (ISS-008) → ISS-008 Resolved same day 2026-05-26; PR #44 (ISS-012) → ISS-012 Resolved 2026-05-29.
- **self-improve cadence** (priority 16 — F4×I4÷E1). 4 runs in window — shipped PR #31 (skill-evals output_pattern), PR #32 (scheduler scope ISS-010), PR #33 (skill-graph docs), and pushed the ISS-009 follow-up framing into the carried-goals list. Highest signal-per-run skill, sustained from prior week. Evidence: 2026-05-28 + 2026-05-30 + 2026-05-31 + 2026-06-01 self-improve log entries.

### Add

- **datanet rubric + first 3 assignments** (priority 8.3 — F5×I5÷E3). 14 unassigned datanets (1, 2, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17) surfaced by every reppo-orchestrator run for 12 consecutive days. Last week's Action 2 slipped. Until written, reppo-trading-agent over-runs datanet 9 (35 runs this week, today's 3rd run wrote 0 mints because margin-top-12 exhausted vs ledger). Evidence: 2026-06-01 reppo-orchestrator 1st + 2nd + 3rd run logs.
- **ISS-017 chain-runner shell injection** (priority 10 — F2×I5÷E1). Filed today: `.github/workflows/chain-runner.yml:41` + `:416` interpolate `${{ inputs.chain }}` directly into `run:` shell blocks — same incident class as the 2026-04-11 audit pattern. Fix is mechanical (route through env). Evidence: `memory/issues/INDEX.md` ISS-017 row + 2026-06-01 skill-security-scan log "NEW HIGH: `.github/workflows/chain-runner.yml:41` + `:416`".

### Less

- **reppo-trading-agent on datanet 9, 35 runs / 7 days** (priority 15 — F5×I3÷E1). Together with reppo-orchestrator (35) + reppo-digest (33) that's 103 of 270 skill runs (38%) all aimed at one datanet. Today's 3rd run produced 0 mints + 0 votes — margin-top-12 candidates fully consumed vs ledger. The fix isn't "run more often"; it's "spread to the other 14 datanets" (see Add above). Evidence: skill-run count breakdown + 2026-06-01 reppo-swarm 3rd-run log "0 mint intents queued (margin-top-12 exhausted)".
- **ISS-009 defence-in-depth — 6 recurrences, 4+ days carried** (priority 10 — F5×I4÷E2). Root cause was traced 2026-05-28 (chain-runner capture at `aeon.yml:479-493` overwrites Write-tool output with CLI `.result`). Two follow-ups still open: (a) codify emit-in-assistant-text contract in `skills/reppo-orchestrator/SKILL.md`, (b) switch chain-runner fail-fast `continue` → `break`. PR #27 + PR #48 added workflow-level guards but the actual code change is missing. Evidence: MEMORY.md Current Goals L14-17 + ISS-009 row still Open.

### More

- **reppo platform integration is closing the loop end-to-end** (priority 8 — F4×I4÷E2). PR #44 (Zod schema), PR #47 (vote dedup prefetch + UUID), PR #50 (skip POST when uri missing) collectively produced the first 3 consecutive clean phase-2 runs ever (2026-05-30 → 2026-05-31 morning). The 14th mint 2026-06-01 hit pin + POST + on-chain in one run. Worth investing in: more datanets feeding into this now-proven pipe, not more wallets feeding the same datanet. Evidence: memory/topics/reppo.md L21-24 (mints 11-14 all "Phase 2 metadata POST returned HTTP 200").

### Dropped from priority threshold

- INDEX bookkeeping flip (ISS-007 PR #13, ISS-010 PR #32) — priority 6, mechanical, fits inside next-week Action 3.
- Cleanup chain-runner scratch (priority 4) — only `.candidates.json` + `.notify-sent-hashes` at repo root; no `.tmp-*` files; not chain-irrelevant any more.

## Next week — actions

- [ ] Write `configs/datanets/RUBRIC.md` (criteria for assigning trading-agent or another agent to each datanet) and add concrete agent configs under `configs/datanets/` for ≥3 of the 14 unassigned datanets by 2026-06-05
  - Why: 12 consecutive days of "14 unassigned" carried by every reppo-orchestrator run; last week's slipped action; today's 3rd run wrote 0 mints because margin-top-12 on datanet 9 is exhausted
  - Done when: `configs/datanets/RUBRIC.md` exists with ≥3 named criteria; `configs/datanets/` contains ≥3 new `<name>.md` files alongside `tradinggymai.md`; next reppo-orchestrator run reduces "unassigned" count from 14 to ≤11
- [ ] Patch `.github/workflows/chain-runner.yml` lines 41 + 416 to route `${{ inputs.chain }}` through a quoted env var (`env: CHAIN: ${{ inputs.chain }}` then `"$CHAIN"`) and merge as PR closing ISS-017 by 2026-06-03
  - Why: ISS-017 just filed; same incident class as 2026-04-11 audit pattern; fix is mechanical
  - Done when: ISS-017 flipped Resolved in `memory/issues/INDEX.md`; `gh search code "inputs.chain" --repo aeonframework/aeon path:.github/workflows/chain-runner.yml` returns no direct-interpolation matches
- [ ] Ship the 2 ISS-009 follow-ups — (a) codify emit-in-assistant-text contract in `skills/reppo-orchestrator/SKILL.md`, (b) switch `chain-runner.yml` fail-fast `continue` → `break` — as one PR by 2026-06-05
  - Why: 6 recurrences, root cause traced 2026-05-28, 4+ days carried in MEMORY.md Current Goals
  - Done when: ISS-009 flipped Resolved in `memory/issues/INDEX.md`; `grep "emit-in-assistant-text" skills/reppo-orchestrator/SKILL.md` returns a non-empty contract block; `grep -n "continue\|break" .github/workflows/chain-runner.yml` shows the fail-fast branch uses `break`
- [ ] Flip ISS-007 (PR #13 merged 2026-05-25) and ISS-010 (PR #32 merged 2026-05-28) to Resolved in `memory/issues/INDEX.md`, and confirm ISS-016 (PR #52 merged 2026-05-31) holds for ≥3 consecutive reppo runs before flipping, by 2026-06-03
  - Why: code shipped days ago, bookkeeping carries in MEMORY.md Current Goals; ISS-016 needs validation before flip
  - Done when: `grep -c "ISS-007\|ISS-010" memory/issues/INDEX.md` shows both ID rows under Resolved (or ISS-016 under Resolved if vote_filter own-pod gate held 3 runs)

## Goals progress

From `memory/MEMORY.md` Current Goals (last consolidated 2026-05-31):

- **Close ISS-009 defence-in-depth** — partial. Root cause traced 2026-05-28 + PR #27 + PR #48 added guards. The two named follow-ups still missing; covered by next-week Action 3. Cite: MEMORY.md L14-17; ISS-009 row Open.
- **Assign 14 unassigned datanets** — **stalled, no progress this week.** 12th consecutive day surfaced; last week's Action 2 slipped; covered by next-week Action 1. Cite: 2026-06-01 reppo-orchestrator logs.
- **Resolve ISS-016** — PR #52 ("expand vote-filter to include own mints") merged 2026-05-31; today's 3rd reppo-voter run self-recognized own pods via ledger cross-ref and skipped them (0 voted). Watching for ≥3 consecutive clean runs before flip; covered by next-week Action 4. Cite: 2026-06-01 reppo-swarm 3rd-run log + ISS-016 row.
- **Operator call ISS-015** — still blocked on operator-side secrets. PR #56 (oauth.reddit.com route) open since 2026-06-01 13:12Z but needs `REDDIT_CLIENT_ID/SECRET` set. **No action this week** — operator-gated, not an Aeon-side blocker. Cite: ISS-015 row + open-PRs list.
- **INDEX bookkeeping** — partial. ISS-004/006/008/012/013/014 all flipped Resolved in window. ISS-007 + ISS-010 still Open despite merged PRs; covered by next-week Action 4. Cite: INDEX.md Open + Resolved tables.
- **Cleanup chain-runner scratch** — partial. `.tmp-*` files no longer at repo root (no matches today); `.candidates.json` + `.notify-sent-hashes` remain. Propose retire — low signal vs the rest of the queue. Cite: `ls .tmp-* .candidates.json .notify-sent-hashes` results.

## Notes

- prior weekly review noted cost-report week-1 ~$770/mo cache-dominated; this week wasn't covered by a fresh cost-report cross-check, so the cost delta from 47 PRs + 270 runs vs last week's 111 is unmeasured. Worth a glance next cost-report Mon.
- `articles/explainer-2026-05-28.md` ("the seam between proposal and execution") shipped as a publication-quality piece grounded in the reppo/sherwood pipeline; 934 words, 4 external cites, banned-phrase scan clean. Highest single-skill output in window.
- ISS-011 (vote nonce-too-low) — 1 occurrence 2026-05-29, no recurrence this week. Watching, not actionable yet.
- skill-runs counted via direct `gh api` filter — local clone is shallow (git log returns 1 commit). `./scripts/skill-runs` script declined approval again; same degraded-source pattern as the prior review, handled by routing through `gh api`.
- soul/SOUL.md + STYLE.md applied in TL;DR and notification — lowercase, named numbers, parallel-closer earned on "five blockers cleared in code … the one thing the loop has not produced".
