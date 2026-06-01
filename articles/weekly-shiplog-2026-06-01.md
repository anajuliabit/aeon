# Week in Review: The Skill Catalog Becomes a Registry

*2026-06-01 — Weekly shipping update*

> The skill catalog stopped being a list and became a registry: a `capabilities` taxonomy, secrets manifests, fork-adoption metrics, and the first onchain-security pack all landed in the same seven days.

## What Shipped

### onchain security skills land as a first-class class
HoundFlow shipped six investigation skills in one PR — `rug-scan`, `contract-audit`, `wallet-profile`, `deployer-trace`, `tx-explain`, `holder-concentration` — closing the gap between *"what moved?"* (the existing monitoring set: `on-chain-monitor`, `wallet-digest`, `defi-monitor`) and *"is this safe, and who's behind it?"* (#269). +693 lines across nine files, labeled `large-ok`. Three more Hound PRs are open and one merge away: `approval-audit` (#281), `honeypot-check` (#282), `lp-lock-check` (#283).

### skill-packs get a schema worth being a registry
The pack manifest grew the two fields that turn a directory listing into something a fork can actually query: `secrets_required` / `secrets_optional` (#267, AntFleet) and a `capabilities` array bound to a locked 6-value taxonomy with `docs/CAPABILITIES.md` to enforce it (#268, AntFleet). On top of that, two new skills landed that read the registry as data: `sparkleware-catalog` enriches `skill-packs.json` with live GitHub signals (#252), `fleet-skill-adoption` ranks the upstream catalog by how many forks actually have each skill enabled (#245), and `fork-health-score` synthesizes push recency + skill count + PR throughput into one ACTIVE / WARM / STALE / QUIET tier per fork (#271). seven community packs from sparkleware (#249), plus `signa` (#254), `noelclaw` (#253), and `aeon-skill-pack-mythosforge` (#228) shipped through the new contract.

### dashboard rebuilt in aeon.fun's editorial voice
Three sequential restyle passes ported the marketing site's vocabulary into the dashboard: dark canvas (#0a0a0a), coral-red accent (#d24b40), Dela Gothic display, Inter body, Space Mono labels (#263 — 396/214 across `globals.css` and 16 files). #264 added the editorial swagger the first pass missed; #265 normalized TopBar button sizes to one 32px height and ported aeon.fun's motion. A code-quality cleanup followed: `refactor(dashboard)` deduped helpers, consolidated types, and removed 275 lines of dead code (#255).

## Fixes & Polish
- shell-injection guard on `workflow_dispatch` inputs — `INPUT_SKILL` validated against `^[a-zA-Z0-9_-]+$` before substitution (#222)
- fragile `tr -d` quoting in GATEWAY provider parsing replaced (#223)
- `v4-readiness` skill manifest references aligned with its actual read set, closing Issue #184 H1 (#226)
- 34 ported skills wired into `aeon.yml` after #219 left them unschedulable; skill count + README image synced to 156 (#230)
- new `pr-skill-triage` skill produces a structured security-scan receipt on inbound SKILL.md PRs (#259)
- default model bumped to `claude-opus-4-8` across `aeon.yml`, dispatch dropdown, dashboard header, and README (#262)

## What's Nearly Here
`liquidpad-launch` (#231) — the prefetch/postprocess shims already landed in #260 to unblock it. `approval-audit` (#281), `honeypot-check` (#282), and `lp-lock-check` (#283) extend the Hound onchain-investigation pack. `ci: capabilities taxonomy parity check` (#304) enforces the new manifest contract automatically.

---

**Stats:** 51 commits · 49 PRs merged · 1 issue closed · contributors: aaronjmars, HoundFlow, AntFleet, sparkleware, noelclaw, vritra12, ryjin111, liquidpadbot, NoctelXBT, Clint, Yehor Kaliberda, 0xShak, codexvritra
**Sources:** https://github.com/aaronjmars/aeon · commits=ok · prs=ok · releases=ok · issues=ok · open_prs=ok
