# Reppo Swarm — Operator Setup

One-time steps before the `reppo-swarm` chain can run. See the design at
`docs/superpowers/specs/2026-05-21-reppo-swarm-slice-design.md`.

## 1. Fund a mainnet wallet
Create an EOA for the agent and fund it with mainnet gas + REPPO.

## 2. Add GitHub Actions secrets
Repo Settings → Secrets and variables → Actions:
- `REPPO_PRIVATE_KEY` — the funded EOA private key (required).
- `REPPO_VOTER_PRIVATE_KEY` — optional separate voting key.
- `BASE_RPC_URL` — recommended. A reliable Base mainnet RPC URL (Alchemy,
  QuickNode, Infura, etc.). The Reppo CLI defaults to
  `https://mainnet.base.org`, which is flaky enough to cause intermittent
  `INTERNAL_ERROR` dry-run failures under load (see ISS-007). The workflow
  exposes this secret to the CLI as `REPPO_RPC_URL`.

No public Variables are required — `postprocess-reppo.sh` auto-approves
REPPO spend via `reppo approve --spender subnet-manager --token reppo`
(CLI v0.5+), which resolves both the spender and token addresses
internally.

## 3. Register the agent identity (once)
Locally, with the CLI installed (`npm i -g @reppo/cli`) and
`REPPO_PRIVATE_KEY` exported:
```bash
REPPO_NETWORK=mainnet reppo register-agent \
  --name "Aeon Trading Agent" \
  --description "Mints crypto trading strategy pods to TradingGymAI"
```
This uses the CLI's default API key — no `REPPO_API_KEY` needed.

## 4. Lock REPPO for voting power (auto-handled)
The chain's vote step uses veREPPO weight. `postprocess-reppo.sh`
auto-locks 500 REPPO for 30 days the first time a vote intent dry-runs
with `INSUFFICIENT_VOTING_POWER` (via the `auto_recover_lock` helper),
mirroring the existing auto-grant / auto-approve recovery paths. The
lock idempotency-key is date-stamped to the lock cycle (`year-month`),
so attempts within the same 30-day window no-op but the lock refreshes
monthly when needed.

**Prereq:** the wallet must hold at least 500 REPPO when the first
vote intent fires; auto-recovery surfaces a clean failure in the
digest if it doesn't (`auto-lock FAILED: …`).

**Manual override:** for a custom amount or duration (e.g. locking the
full balance for longer), use the operator helper:
```bash
./scripts/reppo-lock.sh                       # full balance, 30d
./scripts/reppo-lock.sh --amount 1000         # explicit amount
./scripts/reppo-lock.sh --duration 5184000    # 60d
```
Run this BEFORE the auto-recovery's first vote attempt to override
the default 500/30d lockup. When a manual lockup matures, re-run, or
use `reppo extend-lock <id> --duration <seconds>` to extend.

## 5. Configure the rubric
Edit `configs/datanets/tradinggymai.md`: replace `datanet_id` with the real
mainnet TradingGymAI datanet id, and tune the Goal / criteria / caps.

## 6. Phased rollout
- **Phase 0 — dry-run only.** Add repo variable `REPPO_DRY_RUN_ONLY=true`.
  Run the chain 2–3 days; confirm the daily digest, prefetch, gate logic,
  and intent files all behave. No on-chain writes, no spend.
- **Phase 1 — minimal live.** Remove `REPPO_DRY_RUN_ONLY`. Keep
  `mint_cap: 1`, `vote_cap: 3`. Run several days; review every minted pod
  and vote by hand against the rubric.
- **Phase 2 — ramp.** Raise the caps in `configs/datanets/tradinggymai.md`
  once the digest shows consistently rubric-aligned behavior.

## Known limitations
- The `memory/topics/reppo.md` ledger row for a mint is written by the
  digest step. If the digest step fails after a mint already landed
  on-chain, the ledger will miss that row and the trading agent may
  re-select the same strategy on the next run. A duplicate on-chain mint
  is still prevented — the mint idempotency key is derived from the
  strategy content (`sha256(datanet_id + ":" + normalized_text)`), so the
  Reppo CLI no-ops the repeat. Watch the digest for repeated mint attempts
  of the same strategy as a signal that a prior digest run failed.
