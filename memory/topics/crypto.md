# Crypto — Research State

Consolidated from defi-overview, narrative-tracker, token-pick, token-alert and digest runs.
Latest data point wins; this file is overwritten as newer runs land.

## DeFi overview (latest: 2026-05-27)
- TVL $81.82B raw (chain-weighted derived -0.92% 24h / +0.05% 7d) vs $82.71B
  05-26 — first material drawdown after three flat days. DEX vol +20.23%
  (sharp recovery from 05-26 $5.38B), fees -5.37% (total $54.58M), stables
  +0.16% → Mixed verdict.
- Top chains: Ethereum $42.94B, BSC $5.56B, Solana $5.38B. Solana derived
  +4.5% chain-weighted is closest to mover threshold, still under 5%. Chain
  movers section dropped: no chain cleared ≥5%/≥$500M; biggest cleared-$500M
  with a negative sign was Sui -2.2%.
- Top mover up (protocol): Solstice +25.84% ($397M → $500M, Basis Trading/Solana,
  7d +32.3%). Its USX stablecoin minted +25.87% to $500M same day — paired
  signal, consistent with fresh basis-trade capital deployed into Solana, not
  rehyp or accounting flip. Cleanest single-day flow across all categories.
- Top mover down (protocol): Rocket Pool -20.95% (snapshot $791M, UP from
  yesterday's $659M; 7d flipped to +4.83% from yesterday's -37.1%) — DAY 3 of
  DeFiLlama staking-pool methodology revision (Obol +65% / Rocket Pool -36%
  on 05-26; Obol +62% / Rocket Pool -22% on 05-25). Obol drops out of top
  movers today as change_1d normalizes. Honest second-place loser is Stake DAO
  -16.38% ($131M, 7d -15.9%) — genuine sustained outflow.
- Fees leaders (24h): Tether $16.40M (flat, -0.1% vs 7d), Circle USDC $6.43M
  (-1.0% vs 7d), Hyperliquid Perps $2.31M (+45.5% vs 7d). Hyperliquid Perps
  DISPLACES Canton ($1.98M) from #3 — first appearance of a perp DEX in top 3
  fees leaders since skill started tracking. Total fees $54.58M (-5.37% 24h,
  +2.38% 7d).
- Fees beating TVL (7d): Maple (fees +293.74% / TVL -0.01%, $0.67M 24h fees,
  $2.05B TVL — Lending demand exploding without deposit growth; also today's
  #5 protocol gainer at +5.6% TVL 1d); Uniswap V4 (fees +31.61% / TVL -0.30%,
  $1.18M 24h fees, $747M TVL — V3→V4 rotation day 3, cooling from yesterday's
  +60%/-6.7% but still cleared filter). Hyperliquid Perps +45.5% fees but no
  traditional TVL (perp DEX) — cleared fees side only.
- DEX vol: $6.53B (+20.23% 24h, +22.37% 7d, +45.98% 30d). Uniswap V4 $843M
  (+3.67%), Aerodrome Slipstream $662M (+47.36% — biggest top-5 gainer),
  PancakeSwap V3 $557M (+10.45%); Uniswap V3 $429M (+12.94%, 7d +49.24%).
  V3→V4 rotation continues but V3 also bouncing — broad-based DEX recovery.
- Real-yield top 3 (all Ethereum): WBTC-USDT v3 Uniswap 21.28% NEW LEAD,
  displaces yesterday's WETH-USDT 26.4% which dropped to 15.78% apyBase
  (WETH→WBTC swap at #1). APYUSD Pendle 20.91% holds #2 (+0.1pp).
  ETH-LINK v4 Uniswap 16.89% RETURNS at #3 displacing USDC-WETH v3.
- Incentive-yield top 2: CVXCRV 28.22% via CRV/CVX/FXN rewards ($29M TVL,
  +11% relative apy lift in one day from yesterday's 25.43%);
  SDCRV 22.38% via CRV/FXN rewards ($26M TVL, flat from 21.95%).
  Curve-locker theme intensifies for the 3rd consecutive day.
- Stables: $321.16B (+0.16% 24h, +0.13% 7d — slight expansion). Notable issuer
  moves: ↑ USX Solstice +25.87% to $500M (paired with Solstice protocol mint);
  ↑ M by M0 +3.20% to $342M (day 3 of growth); ↑ RLUSD +2.23% to $1.78B;
  ↑ apxUSD +1.99% to $511M; ↑ YLDS +1.55% to $551M; ↑ rwaUSDi +1.39% to $340M
  (RWA cohort growing in unison); ↓ USDD -4.45% to $1.45B (largest outflow on
  supply ≥$100M); ↓ PYUSD -3.92% to $3.43B (deepens 05-26's -1.54%);
  ↓ USDG -1.44% to $2.59B; ↓ crvUSD -1.23% to $250M (reverses 05-26's +5.41%
  bounce — 3rd direction-flip in 4 days).
- Continuity vs 2026-05-26: Obol/Rocket Pool methodology-revision artifact
  enters day 3 (Obol normalizes out of top movers); Solstice/USX is fresh
  story; Hyperliquid Perps debuts in fees top-3 (was #5-$2.0M yesterday);
  Maple debuts in fees-beating-TVL (replaces Centrifuge); Uniswap V4 holds
  fees-beating-TVL slot for 3rd day; crvUSD reverses +5.4% with -1.2%;
  CVXCRV/SDCRV hold incentive top 2 for 3rd day with CVXCRV compounding
  (24.8% → 25.4% → 28.2%); WBTC-USDT new at real-yield #1.
- Data caveat: /v2/chains carries no change_1d/7d; chain deltas derived
  TVL-weighted from /protocols ex-CEX/ex-Chain, clamped ±75%. Staking-pool
  methodology revisions (Obol, Rocket Pool) continue distorting top movers —
  third consecutive day, washing out.

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
- Token-alert 2026-05-27: REPPO $0.01712281 -21.53% 24h → alert fired
  (>10% threshold). Second straight double-digit red day, back below 05-22
  baseline $0.02313 and below the 05-23 low $0.01937. HYPER (hyperlane)
  $0.094071 -1.67% — fifth straight red/flat day. VVV (venice-token) $17.29
  -1.69% — fourth red day of last five. Day-over-day: REPPO -22.1%, HYPER -1.9%,
  VVV -1.9%.
- Volume-spike (>3x avg) at 05-27 — 5-point baseline reached (05-22 → 05-26).
  REPPO 5d avg $2.81M vs today $2.42M (0.86x); HYPER avg $22.91M vs $26.42M
  (1.15x); VVV avg $79.39M vs $45.87M (0.58x). No spikes; VVV volume well below avg.
- Threshold-cross check still skipped — no Price Floor / Price Ceiling rows
  populated in MEMORY.md yet. PR #9 (merged 05-25) defines the columns; operator
  hasn't filled rows.

## Bitcoin
See [[last30-bitcoin]] for the 30-day narrative snapshot (baseline 2026-05-21):
Saylor/Strategy dependency, whale accumulation vs distribution, ETF flows flipped negative.
