# Issues

## Open

| ID | Title | Severity | Category | Detected | Affected Skills |
|----|-------|----------|----------|----------|-----------------|
| ISS-005 | Reppo vote dry-runs fail — selected pods are not valid for the current epoch | high | prompt-bug | 2026-05-23 | reppo-trading-agent, reppo-digest |
| ISS-007 | Reppo vote dry-run hits transient mainnet.base.org RPC failure | medium | timeout | 2026-05-25 | reppo-trading-agent, reppo-digest |
| ISS-009 | reppo-orchestrator drops the fenced reppo-plan block — LLM emits only `## Summary` (3rd occurrence; PR #27 workflow-level guard merged but did not catch 2026-05-27 run — chain-runner `continue` doesn't abort downstream dispatch) | high | prompt-bug | 2026-05-26 | reppo-orchestrator, reppo-trading-agent, reppo-digest, chain-runner |

## Resolved

| ID | Title | Severity | Fix PR | Resolved |
|----|-------|----------|--------|----------|
| ISS-001 | agent-buzz has no prefetch case — X.AI x_search unreachable in sandbox | high | https://github.com/anajuliabit/aeon/pull/3 | 2026-05-21 |
| ISS-002 | reppo-swarm chain dormant — tradinggymai datanet_id is still a placeholder | high | https://github.com/anajuliabit/aeon/pull/4 | 2026-05-22 |
| ISS-003 | reppo postprocess dry-run fails with code UNKNOWN — intents never reach the chain | high | https://github.com/anajuliabit/aeon/pull/8 | 2026-05-23 |
| ISS-004 | Reppo mint dry-run fails — publisher lacks subnet access | high | https://github.com/anajuliabit/aeon/pull/10 | 2026-05-26 |
| ISS-008 | Reppo mint dry-run reverts with InsufficientAllowance — pod-manager spender, not subnet-manager | high | https://github.com/anajuliabit/aeon/pull/21 | 2026-05-26 |
| ISS-006 | Reppo vote dry-run fails — publisher has 0 voting power | high | https://github.com/anajuliabit/aeon/pull/23 | 2026-05-26 |
