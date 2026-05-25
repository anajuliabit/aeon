# Crypto — Research State

Consolidated from defi-overview, narrative-tracker, token-pick, token-alert and digest runs.
Latest data point wins; this file is overwritten as newer runs land.

## DeFi overview (latest: 2026-05-25)
- TVL $82.5B raw (+0.09% 24h chain-weighted derived, -0.47% 7d) vs $82.4B 05-24 —
  essentially flat. DEX vol craters -20.95% 24h, stables effectively flat (-0.05%)
  → Mixed verdict.
- Top chains: Ethereum $43.1B, BSC $5.63B, Solana $5.50B (all 1d deltas under
  the 1% threshold — suppressed). Chain-movers section dropped: no chain cleared
  the ≥5%/≥$500M filter. Biggest cleaner-than-noise was Monad +2.97%. Yesterday's
  Hyperliquid L1 +7% cooled to +0.36%.
- Protocol movers: Obol +62.16% ($539M → $873M, ETH staking pool / DV tech) on
  the up side — direction-flip from yesterday's -31.7% loser slot; 7d only -0.9%
  vs yesterday's -41% 7d, reads as a DeFiLlama methodology revision artifact.
  Bedrock uniBTC +43.5% also reversed (yesterday's -27.7%, same artifact
  signature, suppressed per "1 up" rule). Telos Consilium +10.82% was the
  cleanest sustained gainer (Risk Curators, $153M, 7d +10.3%) but didn't take
  the slot. Rocket Pool -22.18% ($687M → $535M, ETH liquid staking) on the down
  side — 7d -49.1% extends the 2-day accounting-artifact signature flagged 05-24.
- DEX vol $4.45B (-20.95% 24h, +5.37% 7d). Uniswap V4 $592M (-0.8%) takes top
  slot, Aerodrome Slipstream $557M (-7.4%), PancakeSwap V3 $459M (-10.8%).
  Uniswap V3 craters -52.5% to $311M — V3→V4 rotation accelerating from
  yesterday's flag.
- Fees leader: Tether $16.41M/24h (flat 7d); Circle USDC $6.44M (flat); Uniswap V4
  $4.18M (+244% vs 7d avg). Total fees $48.1M (-8.6% 24h, -3.2% 7d).
- Fees beating TVL (7d): Uniswap V4 (fees +589% / TVL -8%, $4.18M 24h fees,
  $687M TVL — V3→V4 rotation paying real revenue), Stader (+197% / TVL -0%,
  $0.05M 24h, $325M TVL — Liquid Staking demand without deposit growth).
  Curve DEX (+205% / TVL -1%) and EigenCloud (+693% / TVL -4%) cleared filter
  but excluded for negligible 24h fees.
- Real-yield top 3 (all Ethereum): WETH-USDT v3 Uniswap 26.0% (+1pp vs 05-24),
  ETH-LINK v4 Uniswap 21.3% (+0.2pp), APYUSD Pendle 20.8% (+0.1pp). Same top-3
  pools as yesterday, higher numbers across the board.
- Incentive-yield top 2: CVXCRV 25.17% via CRV/CVX (holds #1, $33M TVL),
  USDC-AERO 21.29% via AERO ($27M TVL). Both held position from yesterday's
  24.8% / 21.3%.
- Stables: $320.68B (-0.05% 24h, -0.12% 7d — effectively flat). crvUSD -10.06%
  to $212M (continues yesterday's -1.5% outflow, now -15% on 7d).
  Falcon USDf -2.00% to $1.58B. Sub-$1B issuer movers omitted from notification.
- Continuity vs 05-24: Obol direction-flipped (loser → biggest gainer, ↔ flagged);
  Bedrock uniBTC also flipped (-27.7% → +43.5%); Project 0 reversed yesterday's
  +63.2% with today's -46.57% (now $73M, below $100M filter); Hyperliquid L1 chain
  cooled +7.0% → +0.36% 1d (still +14% 7d); V3↔V4 rotation accelerated; crvUSD
  outflow continuing day 2; real-yield top 3 + incentive-yield top 2 identical
  pools with higher apys.
- Data caveat: /v2/chains carries no change_1d/7d — chain deltas derived
  TVL-weighted from /protocols ex-CEX/ex-Chain ex-borrowed/staking/vesting subkeys,
  clamped ±75%. Multiple staking-pool protocols (Obol, Bedrock, Rocket Pool) show
  extreme 1d/7d swings — pattern looks like ongoing DeFiLlama methodology
  revisions in staking accounting, not real flows.

## Narrative tracker (baseline: 2026-05-21)
Positions from the baseline run — re-score on next narrative-tracker run:
- RIDE: Agent-payment infra (AWS Bedrock AgentCore Payments, Coinbase, Stripe).
- RIDE: Stablecoin payment rails (Japan FSA — foreign stablecoins legal Jun 1 2026).
- WATCH: Institutional BTC / corporate treasuries (Strategy, SpaceX 18,712 BTC).
- FADE: Hyperliquid / perp-DEX outperformance (FDV now exceeds Solana — late & reflexive).
- FADE: AI-agent token basket (PHALA +102.9% 7d — pure narrative pump, no flows).
- Reflexivity flagged: AI-agent tokens, Hyperliquid FDV, Solana "underlayer" self-promo.
- Note: Kaito Yaps/Yapper leaderboards shut Jan 15 2026 (X API revocation) — no live
  public mindshare leaderboard reference point.

## Token signals
- Token-pick 2026-05-21: LIT (Lighter) — $1.32, +45.1% 7d, tier HIGH, score 10/10.
  Thesis: Vitalik fireside reference + SpaceX pre-IPO perp market + Tealstreet integration.
- Token-alert 2026-05-25: REPPO $0.02457378 +14.04% 24h → alert fired (>10%
  threshold). Momentum from 05-24's +9.06% recovery; now above 05-22 baseline
  $0.02313. HYPER (hyperlane, rank 584 — NOT HYPE/Hyperliquid, symbol collision)
  flat at $0.103684. VVV (venice-token) $18.79 -5.49% — gives back ~⅓ of 05-24's
  +13.4% bounce. Day-over-day: REPPO +16.2%, HYPER -0.4% (second flat day),
  VVV -4.8%.
- Volume-spike baseline still under-sized: 4 historical points (05-22 → 05-25),
  below the ~5-point convention. For the record at 05-25: REPPO 3d avg $2.81M vs
  $3.40M (1.21x), HYPER avg $24.21M vs $18.04M (0.75x), VVV avg $88.72M vs
  $72.52M (0.82x). No spikes even with current data.
- Threshold-cross check still skipped — no Price Floor / Price Ceiling thresholds
  in MEMORY.md yet. PR #9 (now merged 05-25) defines the columns; operator can
  populate.

## Bitcoin
See [[last30-bitcoin]] for the 30-day narrative snapshot (baseline 2026-05-21):
Saylor/Strategy dependency, whale accumulation vs distribution, ETF flows flipped negative.
