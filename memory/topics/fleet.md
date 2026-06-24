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
| #51 | 2026-05-30 | backfill 4 pre-PR-50 pod URLs — merged 2026-05-31 ~13Z |
| #54 | 2026-05-31 | enable Tier 1 crypto-builder skills — open 13:32Z |
| #55 | 2026-05-31 | canonical Tracked Tokens watchlist (WELL/MAMO/REPPO/GITLAWB) — open 15:01Z |
| #56 | 2026-05-31 | route vibecoding Reddit through oauth.reddit.com (ISS-015 fix) — open 15:09Z |
| #57 | 2026-05-31 | refactor reppo Phase 2 onto @reppo/cli≥0.6.0 native — open 15:39Z |
| #58 | 2026-05-31 | skill-graph weekly digest (NEW_ENABLED 8 · NEW_DEPS 33 · REMOVED_DEPS 10) — merged 2026-06-01 13:17Z |
| #54 | 2026-05-31 | enable Tier 1 crypto-builder skills (5 new: deal-flow Mon / reg-monitor Wed / security-digest daily / unlock-monitor Mon / vuln-scanner Sat) — merged 2026-06-01 13:12Z |
| #55 | 2026-05-31 | canonical Tracked Tokens watchlist (WELL/MAMO/REPPO/GITLAWB) — merged 2026-06-01 13:12Z |
| #56 | 2026-05-31 | route vibecoding Reddit through oauth.reddit.com (ISS-015 fix) — merged 2026-06-01 13:12Z |
| #57 | 2026-05-31 | refactor reppo Phase 2 onto @reppo/cli≥0.6.0 native — merged 2026-06-01 13:12Z |
| #59 | 2026-06-01 | dashboard Reppo swarm demo at /swarm — merged 13:13Z |
| #60 | 2026-06-01 | bump HL_TOP_N 5→12 to clear mint-ledger saturation — merged 13:50Z |
| #61 | 2026-06-01 | decouple voting from minting via new reppo-voter skill — merged 15:20Z |
| #62 | 2026-06-02 | self-improve: narrow bare `mamo` → `$MAMO` cashtag in fetch-tweets var — merged ~07:30Z |
| #64 | 2026-06-03 | chain-runner.yml `${{ inputs.chain }}` → `env:` indirection at lines 41 + 416 (closed ISS-017) — merged as commit 2a9ce1c |
| #65 | 2026-06-03 | disable vibecoding-digest + reddit-digest (closed ISS-015 wontfix) — merged |
| #67 | 2026-06-03 | enable token-movers + on-chain-monitor + defi-monitor + fork-cohort/digest/gap + operator-scorecard (34→41 enabled standalone) — merged 15:59Z |
| #69 | 2026-06-03 | reppo-orchestrator: codify emit-fenced-block-in-assistant-text contract (ISS-009 sub-task a) — merged 23:00:48Z; #68 closed 1s later as duplicate |
| #70 + chain-runner.yml:360 | 2026-06-03 | chain-runner `continue` → `break` flip (ISS-009 sub-task b shipped) — INDEX flip pending |
| #71 | 2026-06-04 | aeon personal-stack PR (priorities anchor + thought-review skill + telegram voice path) — merged this week |
| #73-#76 | 2026-06-04..05 | reppo+content-skill maintenance batch (per weekly-review 17-PR list) |
| #77/#78/#79 | 2026-06-05..07 | virtuals + deepseek-v4-flash fallback for 5 CG-price skills (`FALLBACK_CG_SKILLS` at **`.github/workflows/aeon.yml:498`** — defi-overview / token-movers / token-pick / token-alert / market-context-refresh) — reppo chain NOT covered, but reppo is off-CI post-Docker (2026-06-10) so FALLBACK_REPPO_SKILLS is moot |
| #80 | 2026-06-08 | investment-advisor swarm (8 advisor skills + chain wiring) — chain failed on same-day 429; PR #82 supersedes with standalone Virtuals workflow (open) |

## Recurring blockers
- **15 unassigned reppo datanets.** Orchestrator surfaces them every run (ids
  1, 2, 4, 5, 6, 7, 8, 10, 11, 13, 14, 15, 16, 17, 18 — id 18 ArAIstotle
  surfacing 5 consecutive days through 2026-06-05). 16+ days untouched.
  PR #30/#34/#37 unblock pod sourcing on datanet 9; still need an assignment
  rubric or operator pick for the other 15.
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
- **Trading-agent dry streak ENDED 2026-06-05** after 11 consecutive dry
  runs through 6-04 4th-run. Three mints landed same day — new single-day
  record. 15th-mint **4a9a582a** (0xecb63caa 821 HFT closes 14.69 min,
  70 markets, perp-only filter retained 1768/1999 = 11.55% spot excluded,
  +$7,500 Sharpe 1351 tx 0xdb5b7bbc), 16th-mint **16671d6f** (0x944b5f7d
  29 SOL+BTC closes in 9.548s cluster, +$8,410 **Sharpe 48,523** = 2nd
  highest in ledger ever tx 0xef7ce963), 17th-mint **e2e925b2** (0x781e95fd
  201 LINK Close-Short over 2.88h, +$9,605 Sharpe 3782 tx 0xa86b8dca).
  Two operator follow-ups emerged from the unlock: (a) formalize spot_pct
  threshold in Step 4.2 alongside NEG/regression guards (15th-mint admitted
  at 11.55% vs 10th-mint precedent rejected 0xecb63caa at ~20%); (b)
  formalize Sharpe-vs-pnl selection criterion in Step 4 (17th-mint
  Sharpe-tiebreak picked LINK 3782 over runner-up AAVE 3421 +$14,615 — an
  alternate "max absolute pnl" rule would have selected AAVE). Margin-top-12
  cohort had rotated wholly by 6-05 vs 6-04's saturated structure — likely
  HL_WINDOW=week refresh rolled out the spot HFT cluster, not an in-skill
  knob. Operator config asks (perp-only prefetch / HL_MIN_VLM_USD bump /
  HL_WINDOW switch) NO LONGER on critical path.
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
- **ISS-013 (Pinata IPFS pin HTTP 403) and ISS-014 (platform metadata
  POST HTTP 500) durably resolved 2026-05-30 → 2026-06-01.** 7 consecutive
  pin successes + 4 consecutive HTTP 200 POSTs through today's 14th-mint
  cc41abf6 / tx 0xcbe53613. INDEX bookkeeping flip queued.
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
- **Latest classification (2026-06-12 18:09Z): 41 healthy, 0 critical/
  degraded/flapping/warning, 2 no_data** (operator-scorecard +
  fork-skill-gap awaiting first weekly tick). Cleaner than the
  2026-06-10 baseline (7 no_data → 2) as autoresearch, fork-cohort,
  fork-skill-digest, unlock-monitor and vuln-scanner all acquired
  first-run data over the week. `article` still carries sr=0.5 in
  cron-state (2 runs only, under chronic threshold — known noise).
  Through 6-13, heartbeat reports 0 skills at consecutive_failures≥2
  and the only dispatched-stuck rows are 3 daily carryovers from the
  6-12 weekly-limit wave + 11 weekly carryovers draining on Sun/Mon/Sat ticks.
- Earlier classification (2026-05-31 18:21Z): 27 healthy, 0 critical/degraded/
  flapping/warning, 1 no_data (operator-scorecard — Mon 10:30 weekly slot
  remains never-run; today's 10:30 slot also passed without state entry).
- **Fleet expanded 29 → 34 enabled skills 2026-06-01 13:12Z** via PR #54:
  deal-flow (Mon), reg-monitor (Wed), security-digest (daily), unlock-monitor
  (Mon), vuln-scanner (Sat). All 5 are tier-1 crypto-builder skills. First
  runs today: deal-flow (DEAL_FLOW_OK, $65B Anthropic round headline),
  security-digest (SECURITY_DIGEST_OK, 3 PATCH TODAY + 5 PATCH THIS WEEK,
  flagged concurrent npm KEV adds: Nx Console + TanStack).
- **reppo-voter introduced 2026-06-01 15:20Z (PR #61).** Voting decoupled
  from minting — first voter run reported gate=RUN, current_epoch=100,
  56 out-of-epoch + 17 already-voted + 1 own-pod (pod 492 = 14th-mint
  cc41abf6 source wallet), eligible=0. own_pod_ids prefetch returned
  count=0 (5th consecutive run gap), voter self-recognized via ledger
  wallet shortcode cross-ref.
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
- **ISS-015 RESOLVED 2026-06-03** — wontfix: vibecoding-digest +
  reddit-digest disabled. PR #56 oauth.reddit.com route merged
  2026-06-01 but Reddit API access ungettable for this operator;
  operator chose to disable rather than wait. Frees 1 cron slot,
  removes 6+ days of daily noise.
- **ISS-016 open (medium, prompt-bug, NEW 2026-05-31)** — vote LIKE on
  agent's own pod reverts CANNOT_VOTE_FOR_OWN_POD. Fix: gate
  trading-agent vote_filter on publisher==agent (drop regardless of
  direction). own_pod_ids prefetch returning count=0 since filed
  (**15 consecutive voter runs** through 2026-06-05 3rd-run); voter
  self-recognizes via ledger cross-ref — durable workaround. 2026-06-05
  re-run was 1st time the ledger workaround actually FIRED on the active
  epoch (pod 583 = today's 15th-mint 4a9a582a self-filtered); 3rd-run
  filtered BOTH own-mints on the active epoch (pod 583 + pod 585 = today's
  15th + 16th mints in the same defensive pass). Workaround now demonstrated
  durable under load, not just theoretical — prefetch repair priority drops.
- **ISS-017 RESOLVED 2026-06-03** — chain-runner.yml `${{ inputs.chain }}`
  shell interpolation at lines 41 + 416 fixed via env: indirection
  (PR #64, commit 2a9ce1c). Day-3 carry → ship-in-morning ship cadence.
  Anti-pattern of record now closed for the chain-runner family.

## Lessons Learned
- Reppo on-chain cascade ISS-002 → ISS-003 → ISS-004/005 → ISS-006 →
  ISS-007 → ISS-008 → ISS-009 → ISS-011/012/013/014 → ISS-016. Each fix
  exposed the next layer. Phase 2 fully cleared 2026-05-30.
- Workflow-level guards only work if they abort the chain — bash `continue`
  in chain-runner's fail-fast branch silently skips to next iter. Use
  `break` or `exit`.
- Chain-runner capture step (`aeon.yml:479-493`) silently overwrites
  Write-tool output with CLI's final assistant `.result`. Fenced blocks
  must be emitted in assistant text, not via Write. Codified in
  skills/reppo-orchestrator/SKILL.md via PR #69 2026-06-03.
- HL `userFills` 2000-row cap is on the *response*, not the *query window* —
  wallet selection by margin (pnl/vlm) clears the floor.
- Sandbox blocks `./notify "$(cat ...)"` arg-passing — stage to
  `.pending-notify/` and let post-run step deliver. Dominant pattern
  across ~15 content skills.
- Sandbox blocks Reddit (datacenter IP) and X.AI authed curl — use
  prefetch. Reddit oauth route (PR #56) added but ungettable secrets
  forced ISS-015 wontfix 2026-06-03 (vibecoding + reddit disabled).
- Cost profile is cache-dominated (73% of spend). defi-overview, heartbeat,
  reppo-digest = 38% of weekly Opus spend.
- Reppo platform enforces publisher-cannot-vote-on-own-pod. Empirical
  answer to "LIKE own mints?": NO, contract-level revert (ISS-016).
- Drift-skip precedent: if `(wallet, last_t, n_close)` triple matches a
  prior mint, skip even when content hash differs — re-mint = duplicate
  dataset spam. Drift-skip spirit also applies on regressed quality (same
  wallet + same first_t + degraded sharpe/pnl) even when triple differs
  strictly. In-skill Step 4.2 quality guard now codifies the
  regression-aware variant; validated 2026-06-04 2nd-run on 0x9a1500b4.
- Workflow-injection anti-pattern needs `env:` indirection (canonical
  shape is messages.yml:586-591; chain-runner.yml closed via PR #64
  2026-06-03).
- Fetching X tweet content from sandbox: x.com direct WebFetch → HTTP 402,
  nitter.net → empty body, **api.fxtwitter.com/{handle}/status/{id}** is
  the working unauthed fallback (returns JSON with text + quoted-tweet body).
- Memory consolidation: topic-file detail, MEMORY.md is the index.

## PR sweep (2026-06-01 → 2026-06-03)
- 2026-06-01 13:12-15:20Z: 8 PRs merged in a single window. #54 enabled 5
  new tier-1 skills. #55 canonical token watchlist. #56 oauth.reddit.com
  route (later moot — ISS-015 wontfix). #57 reppo-cli≥0.6.0 native Phase
  2 path. #58 skill-graph weekly digest. #59 dashboard /swarm demo. #60
  HL_TOP_N 5→12 (unblocked the fresh wallet that landed the 14th mint).
  #61 split reppo-voter out of trading-agent.
- 2026-06-01 14:40Z 14th mint (wallet 0x9a1500b4, 74 Close-Long perp,
  hash cc41abf6, tx 0xcbe53613) — same source wallet as 13th-mint
  dce17be3 but fresh `(wallet, last_t, n_close)` triple proves
  drift-skip dedup admits genuine new activity. Thin/marginal: Sharpe
  0.84, MDD 91% vs 13th-mint's 9.98 / 171%. Wallet flipped NEG-PnL
  the next day and has stayed there — quality-guard motivator.
- 2026-06-02 ~07:30Z: PR #62 merged (self-improve: `mamo` → `$MAMO`
  cashtag in fetch-tweets var).
- 2026-06-02 1st chain run (07:00) added 2 DISLIKE votes on epoch-100
  HotBot v4 pods 498/499 — first reppo-voter-owned on-chain votes
  post-PR #61 chain split. Ledger 14 mints / 29 votes.
- 2026-06-03: PR #64 (chain-runner env: indirection) merged as commit
  2a9ce1c — closes ISS-017 (Day 3 carry → ship). ISS-015 resolved
  wontfix same day (vibecoding-digest + reddit-digest disabled).
  Open PR count back to 0. 4 high-sev opens → 3 (ISS-005, 009, 015 →
  005, 009 carry; 017 closed).

## 2026-06-06 → 2026-06-09 — rate-limit cluster + recovery
- **2026-06-06 06utc 19th mint cfd710ae** — 0xbc433ba7 52 HYPE/CBRS/QNT/
  SPCX/SNDK closes 5.37d +$25,453 Sharpe 97 tx 0xd9fb03bd. Same wallet was
  18th-mint Sharpe-tiebreak dropped runner-up 2026-06-05 4th-run — surfaces
  clean today after 0x0514f2f3 regressed under Step-4.2 (1st time Step-4.2
  regression check fired on 1-day-old prior mint: +$14,615 → +$5,856).
  Validates Sharpe tiebreak doesn't lose real signal (runner-up-becomes-
  winner-next-day).
- **2026-06-06 12:37Z Claude weekly rate-limit hit.** 140 failures clustered
  6-06/6-07/6-08; `api_error_status:429 "weekly limit"` → `exit 1`.
  18+ skills stuck in `last_status=dispatched`. 0 mints + 0 log entries
  written 6-07 + 6-08 (logs for 6-07 missing entirely; 6-08 only contains
  weekly-review + heartbeat + evening-recap + aixbt-pulse). 8+d
  reppo-swarm clean streak broken 6-08T18:37Z. Virtuals fallback covers
  5 CG-price skills only (`FALLBACK_CG_SKILLS` at
  `.github/workflows/aeon.yml:498`); reppo chain fell through at the time.
  → "extend FALLBACK to reppo" action SUPERSEDED 2026-06-10 by the Docker
  migration: reppo skills are now `enabled: false` in aeon.yml and run
  self-hosted, so CI weekly limits can't touch them. Residual gap is only
  non-reppo CI skills outside FALLBACK_CG_SKILLS (still `exit 1` on limit).
- **2026-06-08 weekly-review filed** — 369 workflow runs (230/136/2/1-null),
  17 PRs merged, 5 mints (15th-19th), 7 votes. ISS-009 + ISS-017 follow-ups
  SHIPPED; INDEX flips slipped (named items still Open). 3rd consecutive
  slip on datanet rubric. Filed article weekly-review-2026-06-08.md.
  4 next-week actions: FALLBACK_REPPO_SKILLS (by 6-11 — **VOIDED 6-10 by
  Docker migration, reppo off-CI**), ISS-018 file (by 6-09, still overdue),
  RUBRIC+1-datanet (by 6-12), 4-issue INDEX flip (by 6-10, still overdue).
- **2026-06-08 18:13Z PR #80 investment-advisor merged** then immediately
  failed on the same 429. PR #82 opened 18:13Z to supersede with
  standalone Virtuals workflow; PR #81 closed. `chain:investment-advisor`
  in cron-state with `last_failed=2026-06-08T17:04:46Z, no last_success`
  field — chain not in current `aeon.yml` per heartbeat 6-09; dropped
  from status table.
- **2026-06-09 06utc 20th mint 420334cb** — 0x06cecfba 250 AAVE Close-Short
  52.1min +$85,196 Sharpe 8458.93 MDD 0% win 100%. 2nd-highest pnl in ledger
  ever. Ends 2-day mintless streak. Multiple replays of same canonical
  (3rd-run 4th-run both correctly DEDUP'd; 4th-run also surfaced superset
  AAVE+BTC late-window dataset Sharpe 763.91 vs prior 8458.93 = materially
  regressed per Step-4.2 ≥0.5 rule despite sum_pnl improving to +$279k —
  rule held).
- **ISS-016 ledger workaround held under load 22+ consecutive runs.**
  6-09 voter caught pod 841 (today's 20th-mint) via wallet-shortcode +
  pods 764/824/825/828/832 (pre-ledger own pods) via 1st-run digest
  cross-ref. 4th-run regressed (5 own-pod reverts replayed 1st-run
  pattern — cross-ref not durable across runs, only prefetch repair
  fixes). Severity promoted medium → high after 6-09 1st-run digest
  >50% revert rate.

## Recent anomalies (through 2026-06-05)
- **2026-06-05 trading-agent triple-mint** — 11-run dry streak ended;
  3 mints landed same day (15th 4a9a582a HFT 821 closes, 16th 16671d6f
  Sharpe 48,523 SOL+BTC 9.548s cluster, 17th e2e925b2 LINK 201 single-mkt).
  New single-day record (surpasses 3-mint days 5-29 + 5-30). Two new
  operator follow-ups emerged: spot_pct threshold in Step 4.2 and
  Sharpe-vs-pnl tiebreak in Step 4. See Recurring blockers for detail.
- **ISS-016 ledger workaround fired live 2026-06-05** for the first time
  on the active epoch — re-run filtered pod 583 (own 15th-mint); 3rd-run
  filtered pods 583 + 585 (own 15th + 16th mints) in the same pass.
  15 consecutive voter runs at prefetch count=0 — workaround durable.
- **Watchlist twin trip 2026-06-04** — REPPO −17.93% + GITLAWB −26.25%
  both crossed 24h thresholds (first trips since canonical watchlist
  landed PR #55). 2026-06-05 cooldown: REPPO −6.75%, GITLAWB −0.25%;
  GITLAWB 3-day cumulative still −34% off 6-01 baseline. MAMO accelerating
  d/d 3 consecutive days (-6.11/-7.16/-9.60% 6-03→6-05) toward 15% rail.
- **narrative-tracker 2026-06-05 transitions** (Day 2 after re-baseline):
  3 NEW (capital rotation crypto→AI equities, ETH leadership crisis,
  proof-of-energy meta), 2 PROMOTED (BTC cycle-break Rising→Peak, RWA
  Rising→Peak), 3 DEMOTED (Hyperliquid Peak→Fading per HYPE −8.65%,
  privacy coins Rising→Fading per ZEC −43.66%, institutional BTC Peak→
  softening), 2 DEAD (LAB Fading→DEAD, altseason rotation Rising→DEAD).
  6-04 contrarian-FADE on BTC cycle-break was wrong; consensus bear played
  out. Reflexivity flagged 3 (Hyperliquid unlock, ZEC AI-assisted exploit,
  capital rotation self-fulfilling).
- **chain:reppo-swarm state-flip**: 2026-06-02 12:23Z `cron-state.json`
  flipped `last_status=failed` while `gh run view` confirmed workflow
  exit `conclusion=success`. ~5s gap between in-chain state-writer and
  final workflow exit; cleared on 18:12Z chain cycle. **7 successful chain
  cycles since** (6-03 × 3, 6-04 × 2, 6-05 × 2). Investigating under
  ISS-010 scope. Not a real chain failure but flips `docs/status.md`
  momentarily to DEGRADED on the literal rule.
- **on-chain-monitor + defi-monitor 2nd-consecutive NO_CONFIG 2026-06-05**
  (1st was 6-04 first-fire). Both gated behind `memory/on-chain-watches.yml`
  which is absent; skills exit cleanly without notification. Operator-populate
  required before either produces signal.
- **vibecoding-digest cron-state mismatch**: skill emits
  VIBECODING_DIGEST_ERROR notification but workflow exits 0, so
  cron-state records `last_status=success`. Workflow-exit-vs-skill-
  outcome mismatch. Now moot — skill disabled with ISS-015 resolution.

## reply-maker ad-hoc (new pattern)
- 2026-06-02 mid-day: operator forwarded an X URL via Telegram
  (RG @rgvrmdya QT'd @reppo's Orquestra launch and dedicated it to
  @anajuliabit). reply-maker drafted 2 reply options in ana voice,
  staged to `.pending-notify/reply-drafts-rgvrmdya.md`. Tweet content
  sourced via api.fxtwitter.com/{handle}/status/{id} after x.com
  direct WebFetch returned HTTP 402 and nitter.net returned empty —
  fxtwitter is the working sandbox-friendly fallback for X content.

## Project Lens & content skills
- **project-lens first article published 2026-06-01** (`sherwood.sh`
  operator-supplied lens). Industry-comparison angle vs Aeon's cron-as-
  optimistic-governance shape; angle history file seeded.
- 8 consecutive search-skill NO_GAP exits through 2026-06-01 — fleet
  gap-free on external-skill axis.

## 2026-06-12 → 2026-06-13 — 4th weekly-limit wave + ISS-018 collision
- **2026-06-12 weekly-limit wave (4th occurrence of the ISS-018 pattern).**
  ~12 daily skills hung 07:05–14:57Z with `last_status=dispatched`
  (morning-brief / daily-routine / thought-review / skill-freshness /
  github-trending / aixbt-pulse / on-chain-monitor / defi-monitor /
  narrative-tracker / security-digest / search-skill + the 08:00 + 14:00
  heartbeats themselves). **Diagnostic split confirmed**: the 5
  `FALLBACK_CG_SKILLS` (defi-overview / token-movers / token-pick /
  token-alert / market-context-refresh at
  `.github/workflows/aeon.yml:498`) SUCCEEDED via the Virtuals fresh-fetch
  fallback; every non-fallback skill dispatched in the same window HUNG.
  Confirms cause = claude weekly limit (not external API). Evening cluster
  16:00–18:16Z self-recovered. Pattern is now provably weekly-cyclical.
  Residual gap remains undocumented: non-reppo CI dailies outside
  `FALLBACK_CG_SKILLS` still `exit 1` on weekly limit.
- **2026-06-13 carryover cascade.** 10 daily-slot carryovers from the 6-12
  wave were still stuck at 08:04Z heartbeat (today's 07:00 + 08:00 slots
  guarded on stuck-state, did NOT re-dispatch). By 14:38Z, ~92% of daily
  fleet drained — 12:00 UTC cluster fully recovered (on-chain-monitor,
  btc-levels, token-alert, token-pick, defi-overview, token-movers,
  defi-monitor, market-context-refresh, narrative-tracker all ran SUCCESS).
  Residual: 3 dailies still stuck (search-skill / security-digest 6-12T14:57Z,
  self-improve 6-11T18:51Z); 11 weekly carryovers pending next tick.
- **ISS-018 number collision (NOT the weekly-limit issue).** vuln-scanner
  ran 17:00Z and filed `ISS-018` for `scripts/prefetch-vuln-scanner.sh`
  missing (sandbox blocks semgrep/trufflehog/osv-scanner installs/runs on
  every invocation). The intended "weekly-limit incident" issue —
  overdue from 2026-06-09 across 4 occurrences (6-06/07/08 + 6-12 wave) —
  remains UNFILED and should be `ISS-019` if filed. MEMORY.md goal
  renamed to reflect.
- **vuln-scanner 6-13 17:00Z**: target superloglabs/superlog (806★ TS
  Apache-2.0). 12 packages with recent high/critical advisories triaged;
  0 confirmed. esbuild Deno-only path, react-router Declarative Mode,
  next 15.5.15 demo-only `apps/sample/` → dropped per `demo/` triage
  rule. Channels: 0 PVR, 0 public PR. Dedup window armed through
  2026-07-13. Report at `articles/vuln-scan-2026-06-13.md`.
- **Skill-health 2026-06-12 18:09Z snapshot.** 41 healthy, 0
  critical/degraded/flapping/warning, 2 no_data (operator-scorecard +
  fork-skill-gap — await first weekly tick). Clean. Previous 6-10
  snapshot had 7 no_data; the 5-skill drop reflects autoresearch +
  fork-cohort + fork-skill-digest + unlock-monitor + vuln-scanner all
  acquiring first-run data during the week (vuln-scanner's today, others
  on their tick). `article` carries sr=0.5 (2 runs, under chronic
  threshold).
- **28-narrative tracker 6-13.** 5 NEW (#1 decentralized AI bid standalone
  on Anthropic Fable-5 + Mythos-5 US-gov export-control directive — TAO
  +17.4% TRENDING+UP+BREAKOUT + VVV +16.2% + MOR bid; #24 Polymarket US
  $969M CFTC-approved debut; #25 Curve gauge weight rotation on
  cvxCRV +13pts / sdcrv +3.5pts twin signal; #26 CFTC onshore BTC perp
  futures; #28 AI engineering layoffs as macro-tech context). 1 PROMOTED
  (#2 AI×crypto agent custody stack structural hardening — Coinbase
  agent accounts 6-12 = 5th big-co primitive in 4 months). 3 DEMOTED
  (#3 HL perp DEX Fading deepens, #6 stablecoin rails Peak softening,
  #8 capital rotation Bear-for-crypto → Mixed after anthropic
  export-control splits the call). 2 DEAD (#13 XMR/ZEC privacy-coin
  rotation one-session kill — 4th consecutive failed privacy-coin call,
  pattern stop holds; #15 VELVET parabolic terminal capitulation,
  6-11 FADE validated).
- **Token-alert 6-13 09:30Z.** REPPO +14.39% 24h / +22.05% 2d on baseline
  vol (0.94× rolling mean) — 61bp under the 15% rail. Closest non-trip
  on the up-side since canonical watchlist landed. No alerts fired
  (thin participation). Prior up-trip was GITLAWB +18.74% on 6-09.
- **No new mints 6-11/6-12/6-13.** Chain is `enabled: false` per Docker
  migration; ledger only advances off-CI. Still 25 mints + 45 votes
  through 2026-06-10.

## 2026-06-15 → 2026-06-16 — PR #108 durable + Hormuz risk-on + XAI quota wall
- **PR #108 file-flag notify path CONFIRMED durable.** All standalone
  skill notifications across 6-15 + 6-16 (morning-brief, daily-routine,
  weekly-shiplog, github-trending, aixbt-pulse, narrative-tracker,
  market-context-refresh, defi-overview, token-pick, token-movers,
  token-alert, list-digest, agent-buzz) delivered direct via
  `./notify -f .pending-notify/{skill}-msg.md` or `./notify` literal
  arg — no post-run `.pending-notify/` carryover fallback observed.
  6-14 caveat ("standalone runs still staging") fully cleared. PR
  retired the dominant sandbox fallback pattern noted across 6 days
  of standalone runs (6-09 → 6-14). Some `.pending-notify/` rm
  attempts still blocked by sandbox gate, but dedup catches and
  delivery still succeeds — operationally clean.
- **Weekly-shiplog 2026-06-15: SHIPLOG_OK.** 113 commits / 109 PRs
  merged / 2 issues closed in 7d window (2026-06-08→2026-06-15).
  Themes: multi-provider LLM gateway with automatic failover, soul
  & strategy builders lower the on-ramp, skills can call MCP servers
  mid-run. +11,602 / -4,784 lines across ~300 files. Article at
  `articles/weekly-shiplog-2026-06-15.md`.
- **BTC reclaim65900 FIRED 2026-06-15 14:00Z** ($66,427 spot vs
  $65,713.62 prior close). reclaim65900Alerted false→true. Both
  armed reclaim levels now SET (reclaim63500 6-11, reclaim65900
  6-15). Driver: Hormuz peace deal LANDED — Polymarket "US × Iran
  peace deal by June 15?" YES 11%→93% (+82pp) as deadline arrived;
  oil premium drained into risk. 6-16 consolidating $66k-$67k
  pre-BOJ-Tuesday (binary catalyst per morning-brief focus).
- **btc-levels recovered same-day 6-15** — failed 05:42Z (first
  failure since skill landed, empty-usage `total_cost_usd:0 /
  output_tokens:0` error, same signature as bb3ab24 chore commit)
  → RECOVERED 07:38Z. sr 0.97, cf 0.
- **Narrative tracker consolidated 34→27 on 6-15.** 1 NEW (#27
  risk-on regime flip on Hormuz landing), 1 RESURRECTED (#13 XMR/ZEC
  privacy on ZEC +24.5% squeeze + Garrett Jin $21M HL long + clean
  audit), 2 PROMOTED (#26 BOJ-tuesday Emerging→Rising, #1 decAI
  thesis-hardening), 1 DEMOTED (#22 COAI faded), 2 DEAD (#7 BTC
  capitulation contradicted, #15 VELVET parabola resolved).
- **XAI quota exhausted 6-16 (NEW MEMORY.md goal).** Team 3a8b4c1e
  monthly credit limit hit — 3 skills today: token-pick 12:42Z
  (X leg absent), list-digest 17:56Z (LIST_DIGEST_EMPTY), agent-buzz
  17:56Z (AGENT_BUZZ_ERROR). Tweet-roundup AM (07:18Z) worked because
  WebSearch returned summary-grade news (not tweets) and spec accepts
  that; agent-buzz requires engagement metadata and cannot. **Residual
  gap from ISS-019 scope extends here:** when XAI quota dies,
  x_search-dependent skills have no fallback chain that resolves to
  a deliverable curation. XAI-dependent skills (agent-buzz / token-pick /
  refresh-x / remix-tweets / tweet-roundup / narrative-tracker /
  reply-maker / list-digest / article / fetch-tweets) NOT covered by
  `FALLBACK_CG_SKILLS`. Operator action: top up XAI credits or wait
  for monthly reset.
- **Monday-weekly tick 6-15 fully cleared previous-week carryovers.**
  cost-report 07:45Z, weekly-shiplog ran ok, unlock-monitor 10:00Z
  UNLOCK_MONITOR_OK (CONX 2,886× daily-vol leverage, SPK fade-pump,
  H biggest $ at $109.8M absorbed), deal-flow Monday 14:00 tick
  FAILED to clear it (stuck since 6-08 15:02Z, ~8d). fork-cohort
  2nd consecutive Sunday weekly fail (stuck 6-14 19:09Z).
- **PR #112 stalled** (skill-graph docs auto-gen, opened 6-14
  17:41Z) — past 24h stalled threshold across 6-15 → 6-16. Action-
  converter loop "merge #112" per 6-15 19:23Z + heartbeat 20:27Z
  flag.
- **PR #122 fix(docs) opened 6-15 19:13Z** in response to all-skill
  WebSearch 400 environmental failure earlier in the day. Under 24h
  threshold at 6-16 morning-brief read.
- **skill-evals 6-14: SKILL_EVALS_RECOVERED + COVERAGE CLIFF.**
  0 new fail / 1 fixed / 1 still failing / 12 stable. Coverage
  14/57 (24%) — 24pp drop from 48%. Action queued: patch
  `evals.json:monitor-polymarket` (POLYMARKET pattern too broad
  → tighten to `### monitor-polymarket`).
- **ISS-018 number collision noted on 6-13.** vuln-scanner filed
  ISS-018 (sandbox-limitation: scripts/prefetch-vuln-scanner.sh
  missing). The "weekly-limit incident" issue overdue from 2026-06-09
  remains UNFILED and should be **ISS-019** if filed. MEMORY.md
  goal renamed.
- **Skill health stable through 6-15 19:13Z snapshot: 41 healthy /
  0 flagged / 2 no_data** (operator-scorecard + fork-skill-gap
  await first weekly tick). Same classification through entire week
  6-12 → 6-15.
- **Status page docs/status.md** regenerated each heartbeat —
  consistently Overall=🔴 DEGRADED on stuck rows (deal-flow 8d,
  fork-cohort 38h). 43-44 enabled rows sorted last-run desc.
- **search-skill 7th consecutive NO_GAP** (6-09 → 6-16). Fleet
  capability gap-free; all "missing" signals are internal shims
  (ISS-018) or operator-blocked (watches.yml).
- **Thought-review 12 consecutive zero-capture days** through
  6-16. Operator inbox cold since personal-stack PR (~12d).
  `vault/inbox/` empty (.gitkeep only).
- **on-chain-monitor / defi-monitor 12 consecutive NO_CONFIG days**
  through 6-16. Operator-gated on `memory/on-chain-watches.yml`
  seed.

## Recent Issues & Patterns (through 2026-06-21)
- **Sandbox-truncation systemic** (6-19 → 6-21): ISS-019/020/021 (defi-overview, token-pick, search-skill) extended by ISS-022/023/024 (monitor-polymarket, token-alert, skill-health) — 8 skills critical / 19 degraded share `output_tokens=0` signature. Cluster timestamps 2026-06-21 12:14-14:17Z.
- **Skill-health classification flipped 6-21**: From "41 healthy / 0 degraded" stable baseline (6-12 → 6-19) to **9 critical / 19 degraded / 3 warning / 2 no-data / 9 healthy**. systemic flag set. Caused by accumulating cron-state denominators while successes lag.
- **Heartbeat chronic tail expanded 6-21**: 24 skills with success_rate < 0.5 (vs 11 on 6-19 baseline). Worst: reg-monitor 7%, vuln-scanner 7%, skill-analytics 9%, security-digest 16%, list-digest 22%.
- **Token-alert NEW stuck mode (6-21 13:45Z)**: First time the skill hung mid-dispatch (`last_status=dispatched`, 96 min elapsed). Different failure mode from cron-tick miss.
- **on-chain-monitor seeded but degraded** (6-21): Operator populated `memory/on-chain-watches.yml` with 5 Base wallets. Etherscan v2 keyless API blocks Base chain on free tier — `ON_CHAIN_DEGRADED` until `ALCHEMY_API_KEY` / `ETHERSCAN_API_KEY` set. CoinGecko ETH/USDC prices OK.
- **defi-monitor still NO_CONFIG**: Watches file has only wallet entries. defi-monitor consumes `type: pool` / `type: position`. Needs pool/position contract addresses + ABIs seeded.
- **PR backlog cleared**: 0 open PRs as of 6-21 15:22Z heartbeat. #112 + #122 + #127 all merged or closed since 6-19.
- **Weekly-limit wave 2026-06-12**: 4th occurrence of the ISS-018 pattern. Diagnostic split confirmed: 5 `FALLBACK_CG_SKILLS` succeeded via Virtuals fresh-fetch fallback; non-fallback skills HUNG. Pattern is weekly-cyclical.
- **XAI quota exhausted since 6-16**: Team 3a8b4c1e monthly credit limit. 10+ XAI-dependent skills blocked. As of 6-21 daily-routine: `tweet-roundup` working off WebSearch fallback successfully (no 400). `agent-buzz` 6-21 ran off XAI cache (`.xai-cache/agent-buzz.json`, fresh 14:37Z) — cache still warm despite quota.
- **deal-flow stuck since 6-08** (13 days). **fork-cohort** stuck 7 days (2nd consecutive Sunday weekly fail).
- **chain:investment-advisor** failed 6-08, off status table (dropped from `aeon.yml chains:`).
- **PR #108 file-flag notify path** continues working durably across all standalone skills (no `.pending-notify/` carry-over).
- **BTC levels**: Both reclaim 63,500 (6-11) and 65,900 (6-15) triggered. 6-21 spot range $63,986–$64,080, close $64,240. No alerts fired this week. Daily close < $60,500 still arms downtrend continuation alert.
- **Token alert canonical watchlist**: REPPO ±15% trips (6-14 +18.93%, 6-16 -15.78%) → 6-19 consolidation -8.52% (no follow-through). GITLAWB downtrend through 6-19 ($0.00006304). WELL/MAMO stable.
- **Recent token picks**: EIGEN (6-22 ~13:00Z) $0.305 HIGH 9/10 EigenCloud rebrand + Darkbloom Public Alpha; AERO (6-21 13:15Z) $0.5406 +10.19% HIGH 7/10 Base DEX play; SOL (6-21 13:50Z re-fire) $73.47 +8.46% 7d HIGH 7/10; HYPE (6-20) $71.06; JTO (6-16) $0.87 — all market legs skipped on Polymarket sports-heavy / dedup gates.
- **Narrative tracker 6-22**: 15 actionable post-dedup. Transitions: 5 NEW + 1 PROMOTED (stablecoins velocity → ↑↑) + 2 DEMOTED + 4 DEAD (sovereign AI chains, privacy tech, AI agent accountability, altseason rotation) + 4 CONSOLIDATED. 4 reflexivity flags inc. **1 inverse-reflexivity** (stablecoins/x402 real infra, fundamentals catching story). **Structural shift flagged: Kaito killed Yapper 2026-01-15 → Studio + Attention Markets (Polymarket joint)** — mindshare measurement layer shifting from points-driven to prediction-market-driven. 2 FRONT-RUN (P2P security mesh, ownership tokens), 8 RIDE, 3 WATCH, 1 FADE, 1 IGNORE.
- **AIXBT Pulse 6-22 10:00Z**: 7 NEW (Toss Bank Korea Solana PoC, SOL tokenized stock vol, security cluster Taiko/Aztec/Altura, BTC ETF $6.35B quantified, China +1T yuan, Treasuries 4.48% retreating, TradFi regime flip hawkish→easing). Clusters 36 tracked (down from 46 on 6-21).
- **market-context-refresh 6-22 16:00Z**: regime chop (low conviction). BTC $64,938 +1.52%, ETH $1,755 +1.92%. F&G 20 (↓3 to Extreme Fear). Breadth 13/20 green 24h · 6/20 7d (weekly downtrend dominant). Top narrative EigenCloud/AI-infra restaking.
- **defi-overview 6-22**: Mixed — TVL $73.6B (chain delta API regression day 5). DEX vol $4.2B (-10.8% 1d, -9.1% 7d). Top mover up Dolomite +14% (7d +56% lending inflows). 3 real-yield pools recovered (WSOL-USDC 32.4%, WETH-USDT 25.1%, UNI-WETH 17.3%) vs 6-21's 0. Stables $313.9B (+0.05%).
- **token-movers 6-22 12:37Z**: 77/100 green, median +0.87% — risk-on breadth but bounce-back leaderboard. Winners UB (+21.5% [FADE] 7d -3.8%), DEXE +18.7%, EIGEN +12.2% (7d +42.8% Darkbloom pivot). Losers H -22.5% (7d -73% continued capitulation), RE -17.6% [CAPITULATION] vol $159.8M on $125M mcap. SYN [PUMP-RISK] +91.6% trending.
- **unlock-monitor 6-22 10:38Z**: 3 tiered events (2 CRISIS, 0 STRAIN, 1 DIGESTIBLE). Top leverage **NEWT at 1.36× 24h-vol-proxy** — cliff $7.14M, 139.58M tokens = **64.9% of circulating supply** on $11M mcap, supply ~doubles 6-24. H investor STRAIN→CRISIS bump (post-$36M-exploit).
- **weekly-shiplog 6-22**: 58 commits / 58 PRs (vs 113/109 6-15) / +3,300 -3,920 first net-negative-lines week (20-skill prune #473 = -3,765). Themes: flat-skill-list to packs, one-click community pack install (5 packs), dependency hygiene wired.
- **security-digest 6-22 14:42Z**: 3 today / 0 this-week / 0 monitor. New KEV adds: CVE-2026-20262 Cisco SD-WAN + CVE-2026-54420 LiteSpeed cPanel. 2 npm `type=malware` adds (node-path-utils, mddriver — both 6-22T06:30Z). SECURITY_DIGEST_OK.
- **skill-security-scan 6-22**: SECURITY_SCAN_NOCHANGE. 4 HIGH / 15 MEDIUM / 4 LOW · 0 new · 0 resolved since 6-15. All 4 HIGH persistent in aeon.yml (L86/L94/L96/L812 — workflow_dispatch / workflow_call gated, low real risk).
- **search-skill 6-22**: Queried "vulnerability scanner" (vuln-scanner sr=0.07/29 runs, ISS-018 open). Found `davila7/claude-code-templates:vulnerability-scanner` (sum=19 UNTRUSTED, manual install only) — pure-python OWASP checklist sidesteps missing semgrep/trufflehog/osv-scanner binaries. Complementary to current vuln-scanner (OWASP audit vs responsible-disclosure pipeline).
- **on-chain-monitor 6-22 12:47Z**: ON_CHAIN_OK 5/5 watches, 0 surviving events. Blockscout keyless path used (Etherscan v2 free-tier blocks Base; ALCHEMY_API_KEY/COINGECKO_API_KEY workflow refs are length=0 — secrets injected as empty). 2400-block window too narrow for slow Safe multisigs — needs operator to widen default or supply Alchemy key.
- **deal-flow recovered 6-22 ~14:30Z**: clean run after 14d stuck since 6-08. ~32 candidates → 8 kept. Top: Baseten $1.5B Series E @ $13B post (2.6× val in 5 months). Themes: capital clustered on inference/compute (Baseten + Hydra Host $100M Series A w/ Nvidia + Founders Fund); cross-camp validation (Morpho $175M w/ Ribbit + Paradigm + a16z; Ripple → Flutterwave $3.2B strategic equity for RLUSD on African corridors).
- **token-alert recovered 6-22 ~13:00Z**: TOKEN_ALERT_OK. First clean run since 6-19. REPPO +5.49% / GITLAWB +9.66% / watchlist median +1.83% (first green-median since 6-14). REPPO 3d arc $0.01716998 → $0.02505217 = +45.91% reversal of 6-16 -15.78% trip. Volume-spike leg skipped (n=2, need 5 — 6-20/6-21 missing due to stuck-dispatch gap). Closes ISS-023.
- **cost-report 6-22 NEW FAILURE**: Mon weekly tick dispatched 12:36:29Z, failed 13:05:55Z. cf=3 (crossed API-degradation threshold), sr=0.50 (3/6). output_tokens=0 signature → extends ISS-019/020/021/024 sandbox-truncation cluster.
- **skill-freshness 6-22**: FRESHNESS_WARN — operator-scorecard depends on stale articles/skill-analytics-*.md (288h/12d, weekly 192h threshold). FRESHNESS_NO_CHANGE — fingerprint d522755e unchanged since 6-21; re-emits 6-28 if still unresolved.

## Soul-builder + MemoClaw strip (2026-06-22)
- **Soul-builder run** (morning 6-22) — subject @anajuliabit. Sources: anajuliabit.eth.limo + github.com/anajuliabit + DEV.to articles + X paywalled (direct tweet fetch 402, fell back to websearch). Files written: soul/SOUL.md, soul/STYLE.md, soul/examples/good-outputs.md. Added MemoClaw, ZHC worldview, DEV.to writing samples, The Range section, Vocabulary section.
- **Operator removed MemoClaw 6-22** — declared dead project via Telegram. Stripped from soul/SOUL.md: projects bullet, current-focus paragraph, tensions bullet, "AI agents have a memory problem" worldview, "Your agent's memory should work like yours" + namespace-leak opinions, "Uses AI tooling…fix amnesia" build-philosophy line, interests list pruned (`semantic memory for agents · x402 payments` removed), pet peeve on MEMORY.md, "memory architecture" → "vault architecture" in The Range. Stripped from good-outputs.md: 7 MemoClaw shorts/mediums/long-forms (sample count 16 → 10). Sherwood/Reppo/Mamo/Moonwell kept intact. PR drafting per CLAUDE.md "never push directly to main".

## Infrastructure updates (since 6-17)
- **PR #108 file-flag notify path** confirmed durable (6-15→6-16). Retires dominant sandbox fallback pattern (`./notify "$(cat ...)"`) across standalone skills.
- **Decentralised-AI bid validated.** 6-13 narrative-tracker #1 FRONT-RUN
  call (TAO HIGH 10/10 token-pick $248.76) paying +23.5% in 24h.
  Day-2 catalyst: WSJ/TechCrunch identify Andy Jassy as the trigger
  for US-gov Anthropic Fable-5/Mythos-5 access suspension (AWS
  researchers used Fable 5 to jailbreak a software-vuln-ID
  safeguard; AWS itself lost access to its own portfolio company's
  models). Rotation INSIDE DeAI: meme-side (TRUMP/EDGE/GWEI/VVV) all
  flipped TRENDING+DOWN intraday — money rotating into
  decentralised-compute primitives (TAO/AKT/FET) over AI-token wrappers.
- **defi-overview 6-14 Mixed verdict.** TVL recovery decelerated
  sharply (+0.41% snap c1d vs 6-13's +1.47% — a third of yesterday's
  pace). DEX vol -22.2% raw / **-38% clean ex-Polymarket-US** (PM US
  $1.70b print day 2, still inside the 7-day US-launch artifact
  window — distortion intensifies vs 6-13's $969m debut). 0 chain
  movers cleared 5% snap floor. 2 protocol UP (Figure Markets RWA
  +27%, Fluid Lite +11%) both no-obvious-catalyst. 0 protocol DOWN —
  Dolomite full direction-reversal ↔ (+10.88% → -9.24%, 19.96-pt
  swing) misses the strict gate. **Steakhouse Financial rolled OFF
  fees-beating-TVL** (was 6-13's biggest-ever entry on this list at
  $2.06b; fees c7d collapsed +41.48% → +15.65% under the 20% gate;
  TVL caught up). cvxCRV gauge surge cooling (-4.14pts to 27.35,
  first cool-off in 2 days). Yesterday's hot real-yield pool
  WETH-USDT (uniswap-v3) collapsed 40.63 → 11.36 apyBase + conf
  fell 2→1 — full hot pool rollover confirmed. 3 NEW real-yield
  pools displaced (REUSDE/MSUSD/ONYC — first re-protocol entry,
  first mainstreet entry, **first Solana real-yield entry** since
  yield-list adoption). /v2/chains c1d/c7d null **DAY 16** of API
  regression.
- **token-movers 12:30Z refresh — alt-bid cooling intraday.** Breadth
  halved since 07:12Z daily-routine (59 → 40/100 green); BTC $64,449,
  ETH $1,673, SOL $68.05. DeAI basket cooled hard intraday (TAO +23.5%
  → +7.5%, AKT +21.5% → +13.7%, JASMY +16.7% → +10.2%, VELVET +20.8%
  → +10.4%). H +135.7% biggest single-session reversal of the week
  (was +75.1% AM) but 1h -7.6% suggests top cooling — earned FADE tag.
  BTW BREAKOUT accelerated (+15.8% → +23.0% intraday). BEAT -34.2%
  (deepened from -20.1% AM — parabolic giveback of 6-13 narrative-
  tracker #21 BEAT-breakout call confirmed Bear).
- **github-trending 6-14: NVIDIA/SkillSpector top pick** (Python,
  4742★ total / 804 today / 55.8 stars/d ACCELERATING) — first-party
  security scanner for the agent-skills marketplace primitive
  (addresses supply-chain risk of arbitrary skills loaded into coding
  agents). Plus LMCache v0.4.7 (CUDA 13 nightly, KV cache for vLLM),
  agentsview (Go, "100× faster ccusage replacement" claim),
  music-assistant/server (2.9.0 stable). Short trending-feed day
  (14 returned, confirmed via second WebFetch — not fetch failure).
  Same skill-marketplace meta noise pattern dropped 3× today (vs 5×
  6-13).
- **heartbeat 6-14 08:33Z: zero stuck daily-slot skills, wave fully
  drained.** Previous days' daily carryovers all recovered overnight
  (evening-recap 6-13 21:16Z, aixbt-pulse 21:17Z, btc-levels 05:31Z,
  skill-evals 07:18Z = first non-stuck Sunday weekly tick post-carryover,
  thought-review 07:09Z, morning-brief 07:11Z, daily-routine 07:15Z).
  9 weekly carryovers still stuck (all >5d old, await next weekly
  tick: 4 Sunday-scheduled clear today 17–19Z, 5 Monday-scheduled
  clear 6-15). docs/status.md still DEGRADED on the stuck rows.
  HEARTBEAT_OK · STATUS_PAGE=DEGRADED — no notify (dedup, all in last
  48h logs).
- **Skill-health latest snapshot (2026-06-13 18:18Z): 41 healthy / 0
  flagged / 2 no_data** (operator-scorecard + fork-skill-gap — await
  first weekly tick). Clean. No drift from 6-12 snapshot.
- **thought-review 8 consecutive zero-capture days** through 6-14
  morning. Operator inbox cold since the personal-stack PR landed
  (6-04 PR #71). `vault/inbox/` empty (.gitkeep only).
- **on-chain-monitor / defi-monitor 9 consecutive NO_CONFIG days**
  through 6-14. `memory/on-chain-watches.yml` still absent —
  operator-gated.

## 2026-06-23 fleet deltas

- **Regime flip chop → risk-off (high conviction).** market-context-refresh
  13:24Z: BTC $62,055 -4.66% 24h, breadth collapsed 13/20 → 3/20 green in
  one session. Triggers: Korea Kospi -10% circuit breakers, $500M crypto
  liquidations, Warsh hawkish Fed repricing, JPMorgan $165B Q2-end
  rebalancing. F&G 23 still lags (doesn't yet capture today's action).
- **ISS-025 cost-report widening.** cf escalated 6 → 7 (6-22 evening)
  → 18 (6-23 morning batch) → 23 (6-23 13:10Z batch wave), sr=0.12 (3/26).
  Same `outputTokens=12` sandbox-truncation variant of ISS-019/020/021/024
  family. Dedup-blocked across morning-brief 07:07Z + heartbeat 08:24Z +
  14:05Z — no spam-notify on same-day escalation.
- **Positive 13:10Z batch wave.** 8 skills green: defi-overview /
  token-pick / token-alert / token-movers / btc-levels / defi-monitor /
  market-context-refresh / on-chain-monitor. cost-report sole failure
  in batch. on-chain-monitor surfaced W3 cyrillic `ÚSDС` mirror attack
  (1480 fake-units, fires 3 min after legit $1480 USDC W3→W1 transfer;
  byte-swap clone of W1 address). Operator notified + explainer sent via
  Telegram.
- **token-alert 6-23 13:12Z fired GITLAWB -15.63% rail break** — first
  downside trip since REPPO -15.78% on 6-16. Watchlist median 24h
  **-11.34%** — first sub-(-10%) median print since canonical watchlist
  landed. WELL/MAMO/REPPO/GITLAWB all red, consistent with broader
  risk-off (BTC -4.66%). vol on GITLAWB at 1.26× (real bid on dump,
  well under 3× capitulation rail).
- **EIGEN 6-22 HIGH 9/10 pick at invalidation.** -15.3% morning →
  -17.0% afternoon TRENDING+DOWN. Estimated ~$0.258 vs $0.26 invalidation.
  One-day reversal of restaking → AI-infra narrative pivot. SSV Network
  TVL -38.95% 7d confirms restaking sector derisked.
- **Token pick 6-23 DEXE HIGH 7/10 $22.98** (+28.2% 24h / +23.4% 7d).
  Only large-cap green on sea-of-red day. DAO-governance rotation —
  KCEX listing + "Dexelization" framing + $1.7B platform TVL. Score
  7/10: 24h+1, 7d+1, both>5%+2, RS vs BTC/ETH+2, DEX+1. Risk: 51.5%
  supply locked Q4 unlock cliff; intraday $17.62/$24.12 range mirrors
  June 3 $24.49 wick reversal. Exit target $28 / inv $19 / 14d.
  Market: Israel × Hezbollah peace deal by July 31 — YES 16.5¢, fair
  ~6%, edge 10.5pp (sell YES / buy NO at 83.5¢).
- **Narrative-tracker 6-23 14:09Z:** 12 actionable (vs 6-22's 15).
  5 NEW + 1 PROMOTED (DePIN/GPU compute Rising→Peak w/ IO/TAO/AKT
  slate) + 2 DEMOTED + 2 DEAD + 3 CONSOLIDATED. 3 reflexivity flags +
  1 carry-over (Kaito Yapper EOL). **INVERSE flag — AI capex rationing**
  (Tencent + Uber real fundamentals catching the AI-infra story,
  contrarian-bear). Key today: 9 of 12 threads AI-side, rotation
  signal hardening.
- **AIXBT Pulse 6-23 09:00Z:** 6 NEW (Warsh hawkish repricing, BTC
  crash <$62K + $500M liqs, Solana $40 bear call + KOL skepticism,
  institutional receipts Cboe/Ripple/UBS/Allfunds, protocol unwind
  Synthetix/ENS/Sonic, SpaceX-led tech selloff). Bridge call:
  Warsh + DXY executing into BTC order book — $500M liq = macro
  reading into on-chain leverage.
- **defi-overview 6-23:** Mixed — DEX vol $6.02B +45% 1d on sell-off
  volume spike. Top mover up Mellow Core +34% / Polygon Bridge +25%.
  Top mover down SSV -37% ($4.7B drop, likely re-measurement). Real-yield
  count **301 cleared** (vs 6-22's 3, 6-21's 0 — yields data quality
  fully recovered). Aave V3 fees +31% / TVL -4% 7d (real lending demand).
  Stables $313.8B; DAI +8.5% on $4.85B = ~$380M new mint.
- **security-digest 6-23 14:12Z:** 2 today / 5 this-week / 2 monitor.
  free-claude + free-anthropic-claude = Anthropic-SDK typosquats —
  direct supply-chain shot at ecosystem operator builds against. Plus
  26 npm malware drops in single 6h window. Budibase + Gogs coordinated
  patch batches collapsed onto one line each. KEV net-new = 0 this week
  (Splunk + Joomla already in prior digests).
- **search-skill 6-23** queried "llm cost" (cost-report cf=23). 5 hits
  all failed hard gates (PostHog-coupled, playbook-not-cron, board-locked).
  Note: cost-report failure is ISS-025 sandbox-truncation, not capability
  gap. Right fix path is root-cause, not external swap. SEARCH_SKILL_EMPTY.
- **list-digest 6-23 17:10Z** + **agent-buzz 6-23 18:00Z:** both clean
  via xai-cache path. cyrilXBT anthropic 13-cert drop top tweet
  (♥266/↻62/score 19.1). agent-buzz: MCP landscape mapped + tooling
  stack fills in + production multi-agent governance.
- **skill-freshness 6-23 08:24Z:** FRESHNESS_NO_CHANGE — operator-scorecard
  still depends on stale articles/skill-analytics-*.md (312h/13d, weekly
  192h threshold). Fingerprint unchanged from 6-22; re-emits 6-28 if
  still unresolved.

## 2026-06-24 fleet deltas

- **Regime flip risk-off → chop.** market-context-refresh: BTC bounced
  $62,055 → $62,442 (+0.62%), breadth 3/20 → 10/20 green. F&G 23 → 17
  is the index catching up to 6-23 crash, not fresh deterioration.
  Both readings Extreme Fear; directional signal noise. ETF outflows
  $1.67B weekly / $4.21B 3 weeks = institutional derisking anchor.
- **cost-report ISS-025 cf=30 → 0 overnight 03:48Z.** Weekly tick on
  `claude-sonnet-4-6` succeeded after 8 days. Sr still 10%, ISS-025
  cluster structurally persists across the 22-skill chronic tail.
  6-24 cost-report normal run also clean ($237.60 / 67 runs, −55.2%
  WoW — reppo cluster absent this week).
- **reg-monitor end-to-end clean at 14:55Z.** First success with all
  4 primary sources delivering (sr was 7%). Top item: CFTC v. Kentucky
  (9th state lawsuit over prediction-market preemption, 14.25% KY
  excise tax on event-contract notional is the live test). Worth
  watching across next 2-3 runs for sustained recovery.
- **BTC sub-$60,500 16:38Z.** Spot dipped to $60,319, both reclaim
  flags re-armed. If today's UTC close < $60,500, breakdown alert
  fires next run. Spot range 6-24 $60,319 → $62,903 (intraday).
- **Operator query 17:00Z — Morpho Alpha USDC Delta V2.** Vault
  collapsed 2026-06-20 (curator AlphaPing, ~30% concentrated in
  single msY/USDC market, msY crashed 70–85%, market at 100% util →
  withdrawals frozen, ~$18M trapped). Verdict to operator: DO NOT
  DEPOSIT. Documented as general Morpho curator-risk pattern in
  [[crypto]] for surface on future Morpho queries.
- **security-digest 6-24 15:05Z:** Ubiquiti CVE-2026-34910 EPSS
  0.818 / p96 — first EPSS≥0.5 PATCH TODAY trigger of 2026. UniFi
  KEV trio (34908/909/910) + Lantronix EDS5000 KEV. 40 net-new npm
  malware drops in 48h sustained ~20-22/day.
- **Token pick 6-24 AAVE HIGH 8/10 $76.09** — DeFi blue-chip relief,
  trending #1 CG, only large-cap DeFi green 7d vs BTC -3.0%.
  Grayscale $175 FV target + V4 Tokenization Spoke audit.
- **Narrative-tracker 6-24:** first major BEAR-BTC thesis (Hedgeye
  quad4) + first btc-maxi internal contrarian (Saylor critique).
  FRONT-RUN bucket emptied first time in 4 days. RESURFACED bucket
  appears (hyperliquid + BTC dominance returning from DEAD).
- **PR #138 (goal-tracker header drift fix)** open ~24h, under
  24h stall threshold per heartbeat. No urgent issues.
