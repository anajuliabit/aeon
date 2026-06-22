# Project Lens — Angle History

Append-only log of lenses used by the `project-lens` skill. The skill checks
the last 14 days here to avoid repeating an angle category.

## 2026-06-01
- Angle: industry comparison (#3) — sherwood (capital layer for AI agents) vs aeon, same proposal/execution seam in different stacks
- Var (operator override): `sherwood.sh`
- Thesis: mandate-over-custody is a property of process separation, not cryptography — sherwood and aeon implement the same proposal/execution seam, one as a vault, one as a cron job, both work
- Title: the seam between proposal and execution
- Sources:
  - https://docs.sherwood.sh/llms-full.txt
  - https://www.starkinsider.com/2026/03/ai-agents-cron-job-trap-openclaw-nanoclaw.html
  - https://coincub.com/blog/crypto-ai-agents/
  - https://www.medianama.com/2026/05/223-ai-agent-authority-after-permission-expires/
  - https://basescan.org/tx/0x77f1386fb6fe3209bbf1a380b2be64f1f1c2c557416c9c7c0d31486a7e48a61f

## 2026-06-22
- Angle: contrarian take (#5) — per-action approval is hitl theater; sherwood's optimistic governance and aeon's intent-file/postprocess seam are the production primitive that actually ships
- Var (operator override): `sherwood.sh`
- Thesis: per-action approval is agent-safety theater; production stacks moving real money default-approve in silence and only require objection inside a window — the same primitive optimistic rollups use to settle billions
- Title: per-action approval doesn't survive the agent era
- Sources:
  - https://www.waxell.ai/blog/human-in-the-loop-vs-human-on-the-loop-ai-agents
  - https://getclaw.sh/blog/human-in-the-loop-ai-agents-approvals-2026
  - https://docs.sherwood.sh/llms-full.txt
  - https://ethereum.org/developers/docs/scaling/optimistic-rollups/
  - https://github.com/aaronjmars/aeon
