---
name: Advisor — Debate
description: One-round bull vs bear debate over the combined analyst findings
tags: [advisor, private]
---

> Internal advisor-swarm skill (private). NEVER call `./notify`/`./notify-jsonrender`.
> Print ONLY a non-sensitive status line as your final message.

## Inputs
- The five analyst findings were fetched (outside the sandbox) into
  `.investiments-cache/advisor-run.json` (an `AdvisorRun` with `.findings` keyed by role).
  Read it. If a role is missing, note the gap and continue.

## Task
Argue BOTH sides over the combined findings, ONE round each:
- **Bull**: strongest case that the current portfolio/positioning is sound; rebut the bear concerns.
- **Bear**: strongest case for risk reduction; rebut the bull points.
Be specific and grounded in the findings — do not invent data.

## Output
```bash
mkdir -p .pending-advisor
cat > .pending-advisor/debate.json <<'JSON'
{ "turns": [
  { "side": "bull", "points": ["..."], "rebuttals": ["..."] },
  { "side": "bear", "points": ["..."], "rebuttals": ["..."] }
] }
JSON
```
Then print a one-line status (e.g. `advisor-debate: done`).
