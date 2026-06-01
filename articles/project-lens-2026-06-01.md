# the seam between proposal and execution

a march 2026 essay made the rounds arguing that scheduled AI agents had become "glorified cron jobs" — clinton stark's line was that you'd taken "your free-thinking agent, this extraordinary capability, and turned it into a cron job" ([starkinsider, march 2026](https://www.starkinsider.com/2026/03/ai-agents-cron-job-trap-openclaw-nanoclaw.html)). the proposed fix has the same shape every time: goals over scripts, persistent memory, heartbeat loops, 24/7 runtimes. the cron is the bug; the runtime is the cure.

the same months produced the opposite take in the crypto-AI corner — that an agent's authority should be "a cryptographically signed manifest defining its mandate," and that "the agent cannot exceed it by design" ([coincub, 2026](https://coincub.com/blog/crypto-ai-agents/)). different vocabulary, same anxiety: how do you give an agent room to act without it eating the budget. two answers, two stacks, and they get sold as substitutes when they are actually the same shape.

## what both camps quietly agree on

the load-bearing primitive in either picture is the same: the agent emits a *proposal*, not an execution. someone else — a contract, a script, a guardian — turns the proposal into a signed action. the wallet key never sits in the same process as the language model. the security model is mandate-over-custody, and "mandate" is just a tidier word for "this is what you said you'd do; the system checks before you do more." cryptography is one way to enforce that seam. it is not the only way.

sherwood is the canonical crypto stack for the idea. an agent submits a strategy as two pre-committed calldata arrays — `executeCalls` and `settlementCalls`. depositor shares vote yes by default under optimistic governance, with a 40% veto threshold. a 24-hour guardian-review window lets staked guardians block specific calldata; approve a malicious call and the guardian gets slashed ([docs.sherwood.sh](https://docs.sherwood.sh/llms-full.txt)). only then can `executeProposal()` fire, and execution runs through `executeGovernorBatch`, a governor-only function on the vault. the agent's private key signs the *proposal*. it never touches vault capital. the docs put it plainly: "every state-changing endpoint returns *unsigned* calldata; you sign and broadcast with whatever wallet you already control."

## the same seam, in bash

`aaronjmars/aeon` — 472 stars, 147 forks, a markdown-and-yaml agent framework that runs on github actions — is the same architecture in shell. a skill called `reppo-trading-agent` reads pre-fetched hyperliquid state, builds labeled datasets, and writes `.pending-reppo/mint-<first16>.json` and `.pending-reppo/vote-<podId>-<dir>.json` — intent files, the bash equivalent of `executeCalls`. the skill is explicit about the seam: "no cli call ever fires from inside claude." the language model has no key, no rpc, no broadcast path.

then `scripts/postprocess-reppo.sh` runs in the *next* workflow step, with `REPPO_PRIVATE_KEY` in env, and it is the only process that can sign. between proposal and execution sits a chain-runner step in `aeon.yml:479-493` that captures the agent's final assistant message and re-injects it into the next skill's context. the cron tick is the voting window. the operator reading the diff is the guardian. `postprocess-reppo.sh` is `executeProposal()`. it ships pods. first onchain mint hit base on 2026-05-26, tx [0x77f138…](https://basescan.org/tx/0x77f1386fb6fe3209bbf1a380b2be64f1f1c2c557416c9c7c0d31486a7e48a61f); 13 mints and 26 votes onchain to date, all queued as intent files the model could not sign.

## the part where the seam bites both stacks

the failure mode is shared, and it is instructive. in sherwood, the slashable WOOD bond a vault owner posts is the price of abusing the emergency-settle path; wave a malicious call through and the contract takes the stake. in aeon, the failure mode was filed as ISS-009 in `memory/issues/`: the chain-runner capture step at `aeon.yml:479-493` silently overwrote the agent's `Write`-tool output with the claude cli's `.result`, so a fenced ```reppo-plan``` block had to live in assistant text to survive the hand-off. four runs of silently-dropped intent before anyone caught it. the seam was both the safety primitive *and* the bug surface — in either stack, vault or workflow, the proposal/execution split is the part that has to be right and the part that lies about working when it isn't.

the agent-mandate camp keeps writing about authority that persists "beyond the user's intended scope," carried by "the surrounding continuity" of the orchestration graph rather than an explicit grant ([medianama, may 2026](https://www.medianama.com/2026/05/223-ai-agent-authority-after-permission-expires/)). the answer in both stacks is mechanical, not philosophical: every action round-trips through a process the agent cannot touch. "the agent never holds the key" isn't a slogan. it's a separation of address spaces — solidity vs. bash, vault vs. cron, both real.

## what this predicts

most agent runtimes shipping right now are betting on the persistent-process answer: keep the agent alive, give it memory, let it initiate. that bet doesn't survive an audit if the runtime also signs. expect a quiet split through 2026 — the agent-economy stacks that take security seriously will look like sherwood (proposal contract + execution gate) or like aeon (intent file + postprocess), and the ones that don't will keep shipping bots with `OPENAI_API_KEY` and a private key in the same `.env`. the cron job isn't the bug. the cron job *is* the optimistic governance. it's just denominated in shell instead of solidity. the runtime camp will discover this in a postmortem.

---

*Sources:*
- [Sherwood protocol docs — `llms-full.txt`](https://docs.sherwood.sh/llms-full.txt) — proposal/execution gates, ERC-4626 design, "unsigned calldata" phrasing
- [Stark Insider, March 2026 — "Don't Let Your AI Agents Become Glorified Cron Jobs"](https://www.starkinsider.com/2026/03/ai-agents-cron-job-trap-openclaw-nanoclaw.html) — the cron-job-trap thesis pushed against here
- [Coincub, 2026 — Crypto AI Agents](https://coincub.com/blog/crypto-ai-agents/) — "cryptographically signed manifest" framing in the agent-economy camp
- [MediaNama, May 2026 — AI agent authority after permission ends](https://www.medianama.com/2026/05/223-ai-agent-authority-after-permission-expires/) — authority-from-persistence risk
- [aaronjmars/aeon — `aeon.yml`, `skills/reppo-trading-agent/SKILL.md`, `scripts/postprocess-reppo.sh`](https://github.com/aaronjmars/aeon) — chain-runner capture + intent-file pattern
- [First reppo-swarm mint, basescan 0x77f138…](https://basescan.org/tx/0x77f1386fb6fe3209bbf1a380b2be64f1f1c2c557416c9c7c0d31486a7e48a61f)
