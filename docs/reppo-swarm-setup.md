# Reppo Swarm — Operator Setup

One-time steps before the `reppo-swarm` chain can run. See the design at
`docs/superpowers/specs/2026-05-21-reppo-swarm-slice-design.md`.

## 1. Fund a mainnet wallet
Create an EOA for the agent and fund it with mainnet gas + REPPO.

## 2. Add GitHub Actions secrets
Repo Settings → Secrets and variables → Actions:
- `REPPO_PRIVATE_KEY` — the funded EOA private key (required).
- `REPPO_VOTER_PRIVATE_KEY` — optional separate voting key.

## 3. Register the agent identity (once)
Locally, with the CLI installed (`npm i -g @reppo/cli`) and
`REPPO_PRIVATE_KEY` exported:
```bash
REPPO_NETWORK=mainnet reppo register-agent \
  --name "Aeon Trading Agent" \
  --description "Mints crypto trading strategy pods to TradingGymAI"
```
This uses the CLI's default API key — no `REPPO_API_KEY` needed.

## 4. Configure the rubric
Edit `configs/datanets/tradinggymai.md`: replace `datanet_id` with the real
mainnet TradingGymAI datanet id, and tune the Goal / criteria / caps.

## 5. Phased rollout
- **Phase 0 — dry-run only.** Add repo variable `REPPO_DRY_RUN_ONLY=true`.
  Run the chain 2–3 days; confirm the daily digest, prefetch, gate logic,
  and intent files all behave. No on-chain writes, no spend.
- **Phase 1 — minimal live.** Remove `REPPO_DRY_RUN_ONLY`. Keep
  `mint_cap: 1`, `vote_cap: 3`. Run several days; review every minted pod
  and vote by hand against the rubric.
- **Phase 2 — ramp.** Raise the caps in `configs/datanets/tradinggymai.md`
  once the digest shows consistently rubric-aligned behavior.
