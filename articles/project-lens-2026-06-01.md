# who holds the agent's key

In March 2026, the World Economic Forum framed the AI-agent debate as a governance problem before a capability problem: "autonomy and authority have to be treated as deliberate design variables." ([weforum.org](https://www.weforum.org/stories/2026/03/ai-agent-autonomy-governance/)) NIST followed with its first AI Agent Standards initiative, which legal analysts already expect to surface in vendor questionnaires and negligence litigation within 18 months. ([joneswalker.com](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/nists-ai-agent-standards-initiative-why-autonomous-ai-just-became-washingtons.html?id=102mkh6))

The question underneath both: how do you give an agent enough authority to be useful without enough authority to be dangerous? Custodians and regulators have converged on a phrase — "supervised autonomy" — that papers over the real choice. ([globalcustody.pro](https://www.globalcustody.pro/p/the-complete-2026-guide-to-ai-in-global-custody)) There are two architectures, and they don't blend.

## the custody fork and the mandate fork

In the first model, the agent holds the keys. The wallet, the API token, the deploy credential — they live inside the agent's runtime, and the human appears only when something breaks. Most agentic-coding tools and most LLM-funded wallets shipping today are exactly this: custodial agents with prompts pretending to be constraints. Recovery is a frantic human pulling the cord.

In the second, the agent never holds the keys. The keys belong to a protocol — onchain or onworkflow — that holds open the questions of *what an agent is allowed to do*, *who has to sign off*, and *how it gets stopped*. The agent proposes; the protocol disposes. Recovery is built into the design, not bolted on after.

Sherwood is the cleanest current example for capital. Every strategy passes three gates: depositor voting on the proposal, a Guardian Review window where staked, slashable third parties can veto, and an emergency-settlement path that pulls capital out of an active strategy mid-execution. The agent submits pre-committed DeFi calls through an ERC-4626 vault holding the USDC and an ERC-8004 identity NFT that gives the agent a verifiable onchain track record. ([docs.sherwood.sh](https://docs.sherwood.sh/)) Eight strategies are integrated — Aerodrome LP, Hyperliquid Grid, Moonwell, Uniswap, Venice Inference, wstETH — and the agent runs none of them unilaterally.

## the same pattern, applied to code

A second project applies the same pattern to a different scarce resource: agent compute. The repo currently sits at 472 stars and 147 forks ([aaronjmars/aeon](https://github.com/aaronjmars/aeon)), and its self-description sounds custodial — "the most autonomous agent framework. no approval loops. no babysitting. configure once, forget forever." Read the schedule layer and that flips. Every "agent action" is a `cron` entry in a single YAML file, every skill is a markdown `SKILL.md` file with a versioned hash, every run produces a workflow log and a notification artifact. The agent doesn't hold the deploy key. GitHub Actions does, and a hardened `workflow_dispatch` input parser checks `^[a-zA-Z0-9_-]+$` against shell injection before any substitution (PR #222).

Last week, six onchain-investigation skills landed in a single PR from an external contributor — `rug-scan`, `contract-audit`, `wallet-profile`, `deployer-trace`, `tx-explain`, `holder-concentration` (PR #269). They were not deployed to a running agent. They were merged as files, scheduled on cron, and produced auditable outputs the next morning. A fork can lift them whole or drop them. During the same week, the skill catalog turned into a queryable schema — a 6-value capabilities taxonomy and per-skill secrets manifests (PRs #267 and #268) — so a fork can tell, before installing a skill, which secrets it asks for and which capability classes it claims.

## the mechanism, not the metaphor

The shared mechanism is worth naming, because the parallel only holds if it's structural. Both projects decouple *what the agent can imagine* from *what the agent can execute*. In one, that gap is filled by depositor votes and a guardian timelock with capital staked against bad waves. In the other, the gap is filled by Git: every action is a PR, every regression is a revert, every fork is a public branch of someone else's autonomy. The metaphors differ. The architecture is identical: agents propose into a constrained surface that humans can read, audit, fork, and stop.

The custodial path keeps shipping, because it demos faster and funds easier. The demo-to-production gap is exactly the gap that a NIST audit, an EU AI Act enforcement action, or one drained-vault postmortem will widen. Frameworks that already treat keys as protocol-owned, not agent-owned, will look in 2027 the way password managers looked in 2017: obvious, in hindsight, the only sane default.

## the forward claim

Within 18 to 24 months, "the agent holds the keys" will be a regulatory red flag, not a feature claim. Vendors who started custodial will rewrite their architectures and call it a security upgrade. The ones who started with the agent-as-proposer pattern — capital or code — will not have to. The bet is specific enough to be wrong: if by mid-2028 the largest agent-managed treasuries on Base or the most-forked agent frameworks on GitHub are still routing through custodial wallets, this read missed. Otherwise, the mandate model wins on default-setting alone.

The boring half of the answer is the load-bearing half. Keys are a design variable. Pick.

---

*Sources:*
- [AI agent autonomy and governance — World Economic Forum, March 2026](https://www.weforum.org/stories/2026/03/ai-agent-autonomy-governance/) — design-variable framing for the autonomy/authority axis
- [NIST's AI Agent Standards Initiative — Jones Walker, 2026](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/nists-ai-agent-standards-initiative-why-autonomous-ai-just-became-washingtons.html?id=102mkh6) — regulatory trajectory and litigation horizon
- [Sherwood Protocol docs](https://docs.sherwood.sh/) — Guardian Review window, ERC-4626 vault, ERC-8004 identity, eight integrated strategies
- [Complete 2026 Guide to AI in Global Custody](https://www.globalcustody.pro/p/the-complete-2026-guide-to-ai-in-global-custody) — "supervised autonomy" current state in production custody
- [aaronjmars/aeon — GitHub](https://github.com/aaronjmars/aeon) — repo metadata, PR #222 / #267 / #268 / #269 references
