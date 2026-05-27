# Agent Fleet — Status & Infrastructure

The fleet exited bootstrap on 2026-05-21. ~21 skills are now enabled and running on
cron. soul/ populated 2026-05-25. Reppo-swarm chain first on-chain output landed
2026-05-26. This file tracks fleet-wide state: what was built, recurring blockers, and health.

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
| #24 | 2026-05-26 | reppo-orchestrator: make fenced reppo-plan block non-negotiable (closed ISS-009) |
| #25 | 2026-05-26 | INDEX bookkeeping — close ISS-009, fix ISS-006 fix_pr link |
| #26 | 2026-05-26 | widen vote dry-run retry budget after auto_recover_lock to 5/10/15s |
| #27 | 2026-05-26 | chain-runner workflow-level grep guard for fenced reppo-plan (ISS-009) |
| #28 | 2026-05-26 | align tradinggymai rubric with operator-shared contributor spec |
| #29 | 2026-05-26 | register pod metadata to platform DB for UI visibility |
| #30 | 2026-05-26 (open) | rewrite reppo-trading-agent to construct pods from HL public data |

## Recurring blockers
- **14 unassigned reppo datanets.** Orchestrator surfaces them every run; none
  have ever been picked up. No agent skill covers them. 7 days untouched —
  needs an assignment rubric or operator pick.
- **Sandbox network limits.** Two confirmed classes:
  - Reddit blocks the GitHub Actions datacenter IP — curl returns "Blocked" HTML and
    WebFetch rejects both old/www.reddit.com. last30 runs degrade without Reddit.
  - X.AI authed curl is blocked (env-var expansion / approval gate). Fix is the
    per-skill prefetch pattern in `scripts/prefetch-xai.sh` (one `case` per skill).
  - `./notify "$(cat ...)"` arg-passing also intermittently fails in sandbox —
    defi-overview stages to `.pending-notify/`, post-run step picks it up.
- **ISS-005 durable fix still pending.** Agent-side filter (validityEpoch ≤
  current-1) is in place since 2026-05-24, but prefetch + agent-prompt update
  is the proper fix. With only epoch-97 yielding 2 valid pods, vote_cap=3 is
  bottlenecked.
- **skill-evals spec drift.** evals.json carries wrong `output_pattern` for
  token-alert / skill-health (both write to `memory/logs/` not `articles/`) and
  two orphaned entries (hn-digest, polymarket — no skills/ directory). Action
  queue from 2026-05-24 captures the patches — still unworked.
- **operator-scorecard never run.** Mon 10:30 weekly slot — no cron-state entry
  since fleet bootstrap. Under 2x interval threshold so heartbeat doesn't flag,
  but worth a watch.

## Resolved blockers
- **Reppo on-chain blocker cascade (CLEARED 2026-05-26).** Full sequence took
  6 days: ISS-002 (datanet placeholder, PR #4) → ISS-003 (UNKNOWN wrapping,
  PR #8) → ISS-004 (subnet access, PR #10/#19/#20) → ISS-006 (no veREPPO,
  PR #11/#23) → ISS-007 (RPC flakes, PR #13/#26) → ISS-008 (pod-manager
  allowance, PR #21) → ISS-009 (orchestrator dropped fenced block, PR #24).
  Each fix exposed the next blocker; assume more surface as real writes scale.
  ISS-009 recurred a 3rd time 2026-05-27 — PR #27's workflow-level grep guard
  in chain-runner did NOT abort downstream dispatch (bash `continue` skips to
  next loop iteration instead of breaking the chain); reopened with `continue→break`
  escalation. ISS-009 reopened in the index.
- **Soul files empty.** PR #12 populated 2026-05-25. Content skills now ship
  ana voice (lowercase, no marketing verbs, concrete numbers).
- **scan.sh backtick-with-$ noise.** PR #14 tightened the HIGH pattern from
  `` `[^`]*\$ `` to `` `[^`]*\$\([^)]+\) ``, dropping false positives 769 → 19
  on the SKILL.md corpus (~97.5% cut).

## Skill health
- Last classification (2026-05-26, 18:27Z): 18 healthy, 0 critical/degraded/
  flapping/warning, 3 no_data (autoresearch [workflow_dispatch],
  skill-analytics [Wed-only — first Wed-fire was today 05-27],
  operator-scorecard [Mon 10:30, never run since enabled, 2nd miss 05-25
  under 2x weekly threshold]).
- Per-skill quality records on disk: `search-skill` (4/5, 1 run) and
  `reppo-digest` (4/5, 2 runs 05-23 + 05-26). No flags. Trend stable.
- `article` carries sr=0.5 in cron-state, but with only 2 runs — below the
  chronic-failure threshold (≥5). All meta-skills flag-and-skip it.
- skill-evals bootstrap baseline (2026-05-24): 12/29 coverage, 1 PASS, 1 STALE
  (expected — disabled `changelog`), 12 NO_OUTPUT (mix of disabled,
  weekly-not-yet-due, and spec-drift entries).
- security-scan bootstrap (2026-05-25): 5 workflow-injection anti-pattern sites
  flagged (messages.yml:578, aeon.yml:86/94/96/718). All auth-gated, exposure
  low. Fix shape: env-var indirection per articles/workflow-security-audit-2026-04-11.md.
  PR #14 closed the scan.sh noise; the 5 workflow sites still need a follow-up PR.
- 2026-05-26 12:39Z defi-overview FAILED on `foundry-rs/foundry-toolchain@v1`
  action download (HTTP 404, single attempt) — transient GH Actions infra
  flake, not a skill bug. Single occurrence; not pinned.
- 2026-05-27 08:23Z chain:reppo-swarm FAILED — ISS-009 3rd occurrence
  (trading-agent SKIP on missing fenced reppo-plan block).

## Cost profile (week 1, bootstrap-inflated)
- Total: $179.73 across 61 runs, 4 days of actual data (fleet bootstrapped 2026-05-21).
- 30-day projection: ~$770 raw; ~$1,290 if you trim the bootstrap day and project
  the 05-22→05-24 daily avg (~$43/day).
- Cache read + write = 73% of spend — typical for a context-heavy agent.
- 1 anomaly: reppo-digest 2026-05-24 cache_read spike to 1.51M tokens, cost $4.12
  (µ=$2.03, µ+2σ=$4.09). Single-run outlier, not classified as degraded.
- defi-overview + heartbeat + reppo-digest = 38% of weekly Opus spend. Sonnet
  rotation could cut ~$55–65/wk but the standard model-downgrade filter doesn't
  flag them because cache_read dominates direct input tokens. Operator-call.
- Week 2 baseline should be richer (full Monday→Sunday) — re-evaluate at next cost-report.

## Issues
- ISS-001 resolved (PR #3). ISS-002 resolved (PR #4). ISS-003 resolved (PR #8).
- ISS-004 resolved 2026-05-26 (PR #10/#19/#20 — auto-approve + auto-grant with retry).
- ISS-005 open (high, prompt-bug) — agent-side workaround live; durable prefetch
  fix pending.
- ISS-006 resolved 2026-05-26 (PR #11/#23 — auto-lock 500 REPPO into veREPPO).
- ISS-007 open in INDEX (medium, timeout) — PR #13 retry shipped, PR #26 widened
  budget; action-converter has the close queued.
- ISS-008 resolved 2026-05-26 (PR #21 — pod-manager allowance auto-recovery).
- ISS-009 open (high, prompt-bug) — recurred 2026-05-27 as 3rd occurrence;
  PR #24 prompt-tightening + PR #27 workflow-level grep guard both insufficient
  because chain-runner's `on_error=fail-fast` branch uses bash `continue`
  (skips to next loop iter) instead of `break` (aborts the chain). Trading-agent
  still SKIPped today on missing fenced reppo-plan block.
