# Issues

## Open

| ID | Title | Severity | Category | Detected | Affected Skills |
|----|-------|----------|----------|----------|-----------------|
| ISS-005 | Reppo vote dry-runs fail — selected pods are not valid for the current epoch | high | prompt-bug | 2026-05-23 | reppo-trading-agent, reppo-digest |
| ISS-007 | Reppo vote dry-run hits transient mainnet.base.org RPC failure | medium | timeout | 2026-05-25 | reppo-trading-agent, reppo-digest |
| ISS-009 | reppo-orchestrator's fenced reppo-plan block lost — root cause traced: chain-runner capture step (`aeon.yml:479-493`) overwrites Write-tool output with the LLM's final assistant text. Fix: emit fenced block in assistant text, not Write tool (validated this run, 2 on-chain). Also still need chain-runner `continue` → `break` | high | prompt-bug | 2026-05-26 | reppo-orchestrator, reppo-trading-agent, reppo-digest, chain-runner |
| ISS-010 | Scheduler dispatches chain keys as phantom skills — reppo-swarm fires daily against a non-existent SKILL.md | medium | config | 2026-05-28 | scheduler, reppo-swarm |
| ISS-011 | Reppo vote write reverts with "nonce too low" after sibling votes land same batch | medium | unknown | 2026-05-29 | reppo-trading-agent, reppo-digest |
| ISS-016 | Reppo vote dry-run fails CANNOT_VOTE_FOR_OWN_POD — workaround misses historical own-pods predating ledger | high | prompt-bug | 2026-05-31 | reppo-trading-agent, reppo-voter, reppo-digest |
| ISS-018 | vuln-scanner missing scripts/prefetch-vuln-scanner.sh — semgrep/trufflehog/osv-scanner binaries unavailable in sandbox | high | sandbox-limitation | 2026-06-13 | vuln-scanner |
| ISS-019 | defi-overview 6 consecutive failures — sandbox timeout/cost truncation | critical | sandbox-limitation | 2026-06-19 | defi-overview |
| ISS-020 | token-pick 6 consecutive failures — sandbox timeout/cost truncation | critical | sandbox-limitation | 2026-06-19 | token-pick |
| ISS-021 | search-skill 4 consecutive failures — sandbox timeout/cost truncation | critical | sandbox-limitation | 2026-06-19 | search-skill |
| ISS-025 | cost-report 6 consecutive failures — weekly tick truncated at outputTokens=12 | critical | sandbox-limitation | 2026-06-22 | cost-report |
| ISS-027 | 12:00 UTC batch DARK — 8-skill cluster frozen since 2026-06-28 21:00Z | high | config | 2026-06-29 | defi-overview, token-pick, token-movers, narrative-tracker, market-context-refresh, on-chain-monitor, defi-monitor, aixbt-pulse |
| ISS-028 | Bash `>` redirect blocked by sandbox — n=20+ workarounds held across 12-UTC-day span, kill-test d4 NEGATIVE post PR #167 merge | medium | sandbox-limitation | 2026-07-22 | security-digest, reg-monitor, agent-buzz, list-digest, heartbeat, morning-brief, daily-routine, skill-graph, thought-review, goal-tracker, reflect |
| ISS-030 | cost-report SDK opt-in mismatch — post-ISS-029 distinct-signature (sdk_opt_in_required), consec=17 sr=0.09 | high | api-change | 2026-08-04 | cost-report |

## Resolved

| ID | Title | Severity | Fix PR | Resolved |
|----|-------|----------|--------|----------|
| ISS-001 | agent-buzz has no prefetch case — X.AI x_search unreachable in sandbox | high | https://github.com/anajuliabit/aeon/pull/3 | 2026-05-21 |
| ISS-002 | reppo-swarm chain dormant — tradinggymai datanet_id is still a placeholder | high | https://github.com/anajuliabit/aeon/pull/4 | 2026-05-22 |
| ISS-003 | reppo postprocess dry-run fails with code UNKNOWN — intents never reach the chain | high | https://github.com/anajuliabit/aeon/pull/8 | 2026-05-23 |
| ISS-004 | Reppo mint dry-run fails — publisher lacks subnet access | high | https://github.com/anajuliabit/aeon/pull/10 | 2026-05-26 |
| ISS-008 | Reppo mint dry-run reverts with InsufficientAllowance — pod-manager spender, not subnet-manager | high | https://github.com/anajuliabit/aeon/pull/21 | 2026-05-26 |
| ISS-006 | Reppo vote dry-run fails — publisher has 0 voting power | high | https://github.com/anajuliabit/aeon/pull/23 | 2026-05-26 |
| ISS-012 | Reppo platform metadata POST fails HTTP 400 — payload Zod-validation bug (subnetId number→string, podDescription>200, podName>50) | medium | https://github.com/aeonframework/aeon/pull/44 | 2026-05-29 |
| ISS-013 | Reppo dataset IPFS pin to Pinata fails HTTP 403 — PINATA_JWT lacks pinFileToIPFS scope | high | operator JWT rotation (no PR) | 2026-05-29 |
| ISS-014 | Reppo platform metadata POST fails HTTP 500 Internal Server Error — transient platform-side fault | medium | platform self-healed (no PR) | 2026-05-30 |
| ISS-017 | chain-runner.yml interpolates `${{ inputs.chain }}` directly into `run:` shell blocks at lines 41 + 416 (2026-04-11 incident pattern class) | high | env: indirection (focus/iss-017-chain-runner-env) | 2026-06-03 |
| ISS-015 | vibecoding-digest can't reach Reddit — prefetch + WebFetch both blocked | high | wontfix — vibecoding-digest + reddit-digest disabled (Reddit API unavailable to operator) | 2026-06-03 |
| ISS-022 | monitor-polymarket: missing_pattern — disabled skill causing churn in evals | high | https://github.com/anajuliabit/aeon/pull/130 | 2026-06-22 |
| ISS-023 | token-alert: missing_pattern — pattern not found in live-day log | high | — | 2026-07-05 |
| ISS-024 | skill-health: missing_pattern — 26 consecutive failures, 0.26 success_rate | high | — | 2026-07-05 |
| ISS-026 | heartbeat: missing_pattern (timing — skill-evals dispatched before 08:00 UTC morning tick) | high | https://github.com/aeonframework/aeon/pull/151 | 2026-07-02 |
| ISS-029 | usepod.ai LLM proxy 402 Payment Required — fleet-wide dispatch failure 8-03 | critical | gateway self-healed 2026-08-03T20:14Z (~2h outage) | 2026-08-04 |
