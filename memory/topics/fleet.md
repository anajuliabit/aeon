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
| #77/#78/#79 | 2026-06-05..07 | virtuals + deepseek-v4-flash fallback for 5 CG-price skills (`FALLBACK_CG_SKILLS` at `aeon.yml:441`) — reppo chain NOT covered, gap surfaced by 6-06 weekly-limit cluster |
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
- Last classification (2026-05-31 18:21Z): 27 healthy, 0 critical/degraded/
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
  5 CG-price skills only (`FALLBACK_CG_SKILLS`); reppo chain falls through.
  → top priority next week (extend FALLBACK list).
- **2026-06-08 weekly-review filed** — 369 workflow runs (230/136/2/1-null),
  17 PRs merged, 5 mints (15th-19th), 7 votes. ISS-009 + ISS-017 follow-ups
  SHIPPED; INDEX flips slipped (named items still Open). 3rd consecutive
  slip on datanet rubric. Filed article weekly-review-2026-06-08.md.
  4 next-week actions: FALLBACK_REPPO_SKILLS (by 6-11), ISS-018 file (by
  6-09), RUBRIC+1-datanet (by 6-12), 4-issue INDEX flip (by 6-10).
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
