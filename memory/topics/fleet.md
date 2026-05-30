# Agent Fleet — Status & Infrastructure

The fleet exited bootstrap on 2026-05-21. ~21 enabled skills on cron (plus
chains and operator-invokable extras). soul/ populated 2026-05-25. Reppo-swarm
chain first on-chain output landed 2026-05-26. This file tracks fleet-wide
state: what was built, recurring blockers, and health.

## Infrastructure built (PRs)
| PR | Date | What |
|----|------|------|
| #1 | 2026-05-21 | Telegram webhook worker for instant inbound messaging |
| #2 | 2026-05-21 | Reppo agent swarm — orchestrator + trading agent vertical slice |
| #3 | 2026-05-21 | agent-buzz X.AI prefetch case + cache fallback (closed ISS-001) |
| #4 | 2026-05-21 | reppo-swarm activation — TradingGymAI datanet_id + integer-id support (closed ISS-002) |
| #5 | 2026-05-22 | chain-runner no longer aborts on a var-less first step |
| #6 | 2026-05-22 | reppo ledger reflects on-chain reality, not queued intent |
| #7 | 2026-05-22 | REPPO_PRIVATE_KEY wired into the post-process workflow step |
| #8 | 2026-05-23 | postprocess-reppo.sh surfaces raw CLI error (closed ISS-003) |
| #9 | 2026-05-25 | self-improve: tighten token-alert step 2 (volume-spike, threshold-cross config) |
| #10 | 2026-05-25 | auto-grant datanet access on PUBLISHER_LACKS_SUBNET_ACCESS (initial ISS-004 helper) |
| #11 | 2026-05-25 | reppo-lock setup helper (REPPO → veREPPO for voting power, initial ISS-006 helper) |
| #12 | 2026-05-25 | populate soul/SOUL.md + soul/STYLE.md from ~/code/social |
| #13 | 2026-05-25 | postprocess-reppo.sh retry-with-backoff on Base RPC failures (ISS-007) |
| #14 | 2026-05-25 | self-improve: tighten scan.sh backtick-with-$ HIGH pattern (97.5% noise cut) |
| #15 | 2026-05-25 | auto-approve REPPO spend on INSUFFICIENT_ALLOWANCE (initial ISS-008 helper) |
| #16 | 2026-05-25 | messages workflow apostrophe escape fix |
| #17 | 2026-05-25 | structured/scannable reppo-digest format |
| #18 | 2026-05-25 | install foundry via workflow action (auto-approve blocker) |
| #19 | 2026-05-26 | reppo approve (v0.5) — drop cast/foundry/REPPO_TOKEN_ADDRESS dep |
| #20 | 2026-05-26 | retry grant-access with backoff after auto-approve (post-confirmation stale-read fix) |
| #21 | 2026-05-26 | auto-recover pod-manager allowance on mint InsufficientAllowance (closed ISS-008) |
| #23 | 2026-05-26 | auto-lock 500 REPPO into veREPPO on INSUFFICIENT_VOTING_POWER (closed ISS-006) |
| #24 | 2026-05-26 | reppo-orchestrator: make fenced reppo-plan block non-negotiable (ISS-009 v1, prompt-side; insufficient) |
| #25 | 2026-05-26 | INDEX bookkeeping — close ISS-009, fix ISS-006 fix_pr link |
| #26 | 2026-05-26 | widen vote dry-run retry budget after auto_recover_lock to 5/10/15s |
| #27 | 2026-05-26 | chain-runner workflow-level grep guard for fenced reppo-plan (ISS-009 v2; insufficient — `continue` not `break`) |
| #28 | 2026-05-26 | align tradinggymai rubric with operator-shared contributor spec |
| #29 | 2026-05-26 | register pod metadata to platform DB for UI visibility |
| #30 | 2026-05-28 | rewrite reppo-trading-agent: construct pods from HL public data |
| #31 | 2026-05-28 | skill-evals — align output_pattern with actual skill output locations |
| #32 | 2026-05-28 | scheduler: scope skill parser to skills: block (closed ISS-010) |
| #33 | 2026-05-28 | skill-graph SKILL_GRAPH_NEW — 124 skills, 21 enabled |
| #34 | 2026-05-28 | HL prefetch: use `userFillsByTime` (window matches rubric 7-day floor) |
| #35 | 2026-05-28 | Telegram poller: fall back to `.message.caption` |
| #36 | 2026-05-28 | enable daily content + meta skills |
| #37 | 2026-05-28 | reppo: rank HL wallets by margin (pnl/vlm), drop 7d span floor, add anti-regurgitation contract — unlocked 4th mint ever |
| #38 | 2026-05-28 | replicate: pin pending-JSON contract + surface API errors |
| #39 | 2026-05-28 | HL_TOP_N default 10 → 3 to fit Aeon's 30-min timeout |
| #41 | 2026-05-29 | replicate-oneoff workflow (workflow_dispatch image gen) — merged |
| #42 | 2026-05-29 | capture HTTP status + response body on Pinata pin / platform POST failures (root-caused ISS-012 + ISS-013) — merged |
| #43 | 2026-05-29 | vibecoding-digest same-day dup-notify suppression — merged |
| #44 | 2026-05-29 | platform metadata Zod schema fix (subnetId string, podName ≤50, podDescription ≤200, extract_detail ≤600) — closed ISS-012 — merged |
| #47 | 2026-05-30 | move ISS-005 epoch filter into prefetch + cast subnetId UUID (durable ISS-005 + ISS-014 fixes) — merged 2026-05-30 ~08-14 UTC |

## Recurring blockers
- **14 unassigned reppo datanets.** Orchestrator surfaces them every run (ids
  1, 2, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17). 8 days untouched. PR #30/#34/#37
  unblock pod sourcing on datanet 9; still need an assignment rubric or operator
  pick for the other 14.
- **ISS-005 durable fix still pending.** Agent-side filter (validityEpoch ≤
  current-1) is in place since 2026-05-24; durable prefetch fix still pending.
  Compounding side-effect: pods 372/373 were DISLIKE'd 7× each on-chain
  2026-05-28 alone (1 per chain run, no CLI idempotency check). Today's runs
  (2026-05-29) **deliberately steered off 372/373** to break the compounding
  pattern — DISLIKE'd 332/390/391 instead, 1st vote on each. Organic
  mitigation works but isn't durable.
- **ISS-011 nonce-too-low REVERT.** Vote-391 1st run REVERTed (CLI provided
  nonce below current chain nonce after sibling votes landed same batch).
  2nd-run retry landed clean. Single occurrence so far; watch for recurrence.
- **ISS-015 Reddit blocked.** vibecoding-digest hits PREFETCH_FAILED on
  runner IP (Reddit 403 on datacenter ASN) AND WebFetch refuses
  `*.reddit.com` at the Claude Code tool layer. 3rd consecutive day
  2026-05-28/29/30. No in-skill workaround — needs authed Reddit API
  (`oauth.reddit.com` + `REDDIT_CLIENT_ID`/`REDDIT_CLIENT_SECRET`) or
  alternate source (pushshift, HN /r/programming mirror). Operator call.
- **Sandbox `./notify "$(cat ...)"` arg-passing.** Now the dominant pattern —
  most content skills stage to `.pending-notify/` and let the post-run delivery
  step pick it up (today: morning-brief, github-trending, defi-overview,
  agent-buzz ×2, daily-routine, token-pick, reppo-digest ×1, thread-formatter,
  technical-explainer ×5, market-context-refresh, vibecoding-digest, weekly-shiplog).
  `./notify` direct exec still works for some (token-alert, defi-overview when
  args are short).
- **Sandbox: Reddit endpoints.** Datacenter IP block on `curl`; WebFetch tool
  refuses both `old.reddit.com` and `www.reddit.com`. vibecoding-digest emits
  PREFETCH_FAILED markers even from the runner host (2nd ERROR run today) —
  worth auditing `scripts/prefetch-vibecoding.sh` (likely Reddit-side rate
  limit / UA rejection on runner IP too).
- **Sandbox: X.AI authed curl.** Fixed via `scripts/prefetch-xai.sh`; expand
  with one `case` per skill that needs `XAI_API_KEY`.
- **HL `userFills` 2000-row cap.** PR #30/#34 widened the prefetch *query*
  window to 7d, but cap is on the *response* — surfaced after 4 mintless runs.
  PR #37 fixed by switching wallet selection to rank-by-margin (pnl/vlm) and
  dropping the (non-existent) 7d span floor; 4th mint ever landed on 6th run.
- **operator-scorecard never run.** Mon 10:30 weekly slot — no cron-state entry
  since fleet bootstrap. Under 2x interval threshold so heartbeat doesn't flag.

## Resolved blockers
- **Phase 2 platform/IPFS cleared 2026-05-30.** ISS-013 (Pinata HTTP 403
  NO_SCOPES_FOUND → operator rotated PINATA_JWT with `pinFileToIPFS` scope;
  5 consecutive pin successes 2026-05-29 4th-run through 2026-05-30 5th-run).
  ISS-012 (platform metadata POST HTTP 400 — payload Zod bug → PR #44 merged
  2026-05-29T19:21Z). ISS-014 (post-PR-#44 HTTP 500 server-side fault →
  self-healed; 1st HTTP 200 on 2026-05-30 4th-run, 2nd consecutive on
  5th-run). First end-to-end clean mints in chain history.
- **Reppo on-chain blocker cascade (CLEARED 2026-05-26).** Full sequence took
  6 days: ISS-002 (PR #4) → ISS-003 (PR #8) → ISS-004 (PR #10/#19/#20) →
  ISS-006 (PR #11/#23) → ISS-007 (PR #13/#26) → ISS-008 (PR #21) → ISS-009
  (PR #24, recurred → PR #27, recurred).
- **ISS-009 root cause traced 2026-05-28.** 4 recurrences across 05-26/05-27/
  05-28 morning. Chain-runner's "Capture skill output" step (`aeon.yml:479-493`)
  `cp`s the Claude CLI's `.result` (final assistant text) over
  `.outputs/${SKILL}.md`, silently overwriting any Write-tool output. PR #24
  (prompt-tightening) and PR #27 (workflow grep guard) both targeted the
  wrong layer. Fix path: orchestrator emits fenced block in final assistant
  *text*, not via Write tool. Validated across runs 2/3/4 on 2026-05-28 —
  gate cleared every time. Still want `continue` → `break` in chain-runner's
  fail-fast branch as a defence-in-depth. ISS-009 INDEX status still "open"
  pending the workflow fix.
- **ISS-010 dispatch phantom (CLEARED 2026-05-28).** `aeon.yml` parser scoped
  to skills: block via PR #32. INDEX still shows open — bookkeeping queued.
- **Soul files empty.** PR #12 populated 2026-05-25. Content skills now ship
  ana voice.
- **scan.sh backtick-with-$ noise.** PR #14 — 97.5% false-positive cut.
- **HL wallet selection mintless ceiling.** PR #34 (`userFillsByTime`) +
  PR #37 (rank by margin, drop span floor) — 6th chain run on 2026-05-28
  landed 4th mint ever (hash 397ee2e8e5e7e593, wallet 0x2b3349ff…33f7,
  110 closed trades, sharpe 110, win 0.76). 2026-05-29 added the 5th
  (LIT 9794ed80, wallet 0x8def9f50, sharpe 19515) and 6th (xyz:BRENTOIL
  7029a48d, wallet 0xebe126ad, sharpe 295k — **first commodity-perp mint**).

## Skill health
- Last classification (2026-05-28, 18:44Z): 27 healthy, 0 critical/degraded/
  flapping/warning, 1 no_data (operator-scorecard — never run since enabled,
  scheduled Mon 10:30). Fleet expanded 21→29 enabled consumers; the prior
  NO DATA list narrowed [autoresearch, skill-analytics, operator-scorecard]
  → [operator-scorecard].
- Data-quality gap: vibecoding-digest cron-state shows last_status=success
  but log entries record VIBECODING_DIGEST_ERROR (Reddit endpoints blocked,
  prefetch host failing too). Workflow exits 0 with a notification-only
  error — classifier follows cron-state, so the skill is HEALTHY by the
  rules. Surfaced to self-improve as a workflow-exit-vs-skill-outcome mismatch.
- Per-skill quality records on disk: `reppo-digest` 4/5 (3 runs: 05-23, 05-26,
  05-28); `search-skill` 4/5 (1 run, 05-22). No flags.
- `article` carries sr=0.5 in cron-state (2 runs only — under chronic-failure
  threshold).
- `github-trending` sr=0.88 (7/8) — above 0.5 threshold.
- `chain:reppo-swarm` last_status=failed 2026-05-28T13:53Z — trading-agent-step
  NOT executed in 5th chain run (orchestrator + digest only ran). Watching
  for recurrence; not yet a filed defect. Single occurrence.
- skill-evals 2026-05-24 baseline: 12/29 coverage, 1 PASS, 1 STALE, 12 NO_OUTPUT.
  PR #31 (merged 05-28) repointed token-alert + skill-health to memory/logs/
  and renamed hn-digest → hacker-news-digest, polymarket → monitor-polymarket.
  Expected next eval: 2 FIXED + 2 still NO_OUTPUT (disabled targets).
- security-scan 2026-05-25 bootstrap: 5 workflow-injection anti-pattern sites
  (messages.yml:578, aeon.yml:86/94/96/718). All auth-gated, exposure low.
  Follow-up PR still pending.
- search-skill: 7th consecutive NO_GAP exit (2026-05-22 → 05-28). Fleet
  gap-free on external-skill axis.

## Cost profile (week 1, bootstrap-inflated)
- Total: $179.73 across 61 runs, 4 days of actual data.
- 30-day projection: ~$770 raw; ~$1,290 trimmed (~$43/day post-bootstrap).
- Cache read + write = 73% of spend.
- defi-overview + heartbeat + reppo-digest = 38% of weekly Opus spend.
  Sonnet rotation could cut ~$55–65/wk; standard model-downgrade filter
  doesn't flag them because cache_read dominates direct input tokens.
- Week 2 baseline due at next cost-report (full Monday→Sunday).

## Issues
- ISS-001/002/003/004/006/008/012/013/014 resolved.
- ISS-005 open (high, prompt-bug) — agent-side workaround live; PR #47
  (durable prefetch fix + CLI vote-dedup) merged 2026-05-30 morning. Watch
  next runs for compounding-pattern break.
- ISS-007 open in INDEX (medium, timeout) — PR #13 retry + PR #26 widened
  budget; INDEX close queued (5+ days).
- ISS-009 open (high, prompt-bug) — root cause traced + fix path validated
  2026-05-28; 5th recurrence 2026-05-30 2nd-run after 6 consecutive runs held.
  Two follow-ups: (a) codify orchestrator emit-in-assistant-text in skill
  prompt, (b) chain-runner `continue` → `break` in fail-fast branch.
- ISS-010 open in INDEX (medium, config) — fix shipped in PR #32; close queued.
- ISS-011 open (medium, unknown) — vote nonce-too-low REVERT after sibling
  votes land same batch. 1 occurrence; retry landed; not recurring.
- **ISS-015 open (high, sandbox-limitation, NEW 2026-05-30)** —
  vibecoding-digest can't reach Reddit; prefetch (runner IP) + WebFetch
  (tool layer) both dead, 3 consecutive days. No in-skill workaround —
  needs authed Reddit API or alternate source.
