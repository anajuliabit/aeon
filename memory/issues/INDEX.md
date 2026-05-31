# Issues

## Open

| ID | Title | Severity | Category | Detected | Affected Skills |
|----|-------|----------|----------|----------|-----------------|
| ISS-005 | Reppo vote dry-runs fail — selected pods are not valid for the current epoch | high | prompt-bug | 2026-05-23 | reppo-trading-agent, reppo-digest |
| ISS-007 | Reppo vote dry-run hits transient mainnet.base.org RPC failure | medium | timeout | 2026-05-25 | reppo-trading-agent, reppo-digest |
| ISS-009 | reppo-orchestrator's fenced reppo-plan block lost — root cause traced: chain-runner capture step (`aeon.yml:479-493`) overwrites Write-tool output with the LLM's final assistant text. Fix: emit fenced block in assistant text, not Write tool (validated this run, 2 on-chain). Also still need chain-runner `continue` → `break` | high | prompt-bug | 2026-05-26 | reppo-orchestrator, reppo-trading-agent, reppo-digest, chain-runner |
| ISS-010 | Scheduler dispatches chain keys as phantom skills — reppo-swarm fires daily against a non-existent SKILL.md | medium | config | 2026-05-28 | scheduler, reppo-swarm |
| ISS-011 | Reppo vote write reverts with "nonce too low" after sibling votes land same batch | medium | unknown | 2026-05-29 | reppo-trading-agent, reppo-digest |
| ISS-015 | vibecoding-digest can't reach Reddit — prefetch + WebFetch both blocked, 3 consecutive days | high | sandbox-limitation | 2026-05-30 | vibecoding-digest |
| ISS-016 | Reppo vote dry-run fails CANNOT_VOTE_FOR_OWN_POD when trading-agent votes LIKE on its own mint | medium | prompt-bug | 2026-05-31 | reppo-trading-agent, reppo-digest |

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
