reppo-swarm · 20th run · datanet 9 · 0 on-chain

reverted
  chain · ISS-009 recurrence — orchestrator dropped the fenced reppo-plan block again; trading-agent gated and SKIPped. PR #24's prompt-tightening held for exactly one run (19th) before drifting on the 20th.
         action: ship the workflow-level grep guard from ISS-009's escalation path — fail the orchestrator step in chain-runner.yml if `.outputs/reppo-orchestrator.md` is missing the fenced block, so the chain doesn't propagate a silent SKIP.

14 datanets unassigned.
