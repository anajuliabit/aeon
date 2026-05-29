# Crypto — Research State

Consolidated from defi-overview, narrative-tracker, token-pick, token-alert,
market-context-refresh, and digest runs. Latest data point wins.

## Market context (latest: 2026-05-29 13:35Z)
- Regime: chop (conviction medium)
- BTC $72,909 (-0.19% 24h, -5.81% 7d) · dominance 57.66%
- ETH $1,992 (+0.39% 24h, -6.54% 7d) · ETH/BTC 0.02732
- SOL $81.24 (+0.52% 24h, -6.79% 7d)
- Total mcap $2.54T (+0.26% 24h) · DEX vol $7.01B 24h
- Breadth: 11/20 green 24h (vs 4/20 yesterday — sharpest single-day recovery
  in this risk-off window) · 3/20 green 7d
- Fear & Greed: 23 (Extreme Fear) — yesterday 22
- Top narrative: RWA Tokenization (rising) — XLM +36.65% 7d + INJ record
  $3.57B tokenized-equity daily volume + M by M0 RWA stable DAY 5 growth
- BTC ETF outflow streak hit record 9th day: $2.8B total withdrawn since
  May 14; IBIT -$528M May 28 (2nd-largest single-day outflow since launch).

## DeFi overview (latest: 2026-05-29 12:09Z)
- TVL $79.85B raw chain snapshot (+0.35% vs 05-28 $79.57B — **first up-day
  after 2 consecutive drawdowns**). /v2/chains API change_1d/change_7d all
  null today (regression vs skill spec); used snapshot d/d as fallback.
- Top chains: Ethereum $42.04B (+0.5%), BSC $5.47B (+0.6%), Solana $5.25B
  (+0.6%) — all <1%, deltas suppressed.
- Top mover up (protocol): Kinetiq kHYPE +16.38% ($942M → $1.10B, HL liquid
  staker on Hyperliquid L1, 7d +8.62% — sustained week of growth). HYPE
  near 5-26 ATH $64.63 + BHYP ETF inflows pulling kHYPE deposits.
- Top mover down (protocol): Stacks sBTC -28.06% ($302M → $217M, BTC bridge,
  7d -31.27% — essentially all 7-day move is today). Lombard BTC.b also
  -20.46% on $177M (7d -24.21%). Cohort unwind tied to BTC weakness.
- Fees leaders (24h): Tether $16.38M, Circle USDC $6.43M, Hyperliquid Perps
  $2.43M (+14.2% vs 7d avg, strengthens from yesterday's +6.3%) — **HL Perps
  holds #3 for 3rd consecutive day**. Total fees $57.60M (+7.32% 24h).
- Fees beating TVL (7d): Fluid Lending (+69.34% / TVL -10.76%, $156k 24h),
  Jupiter Perpetual Exchange (+35.89% / TVL -5.45%, $358k 24h). Uniswap V3
  (yesterday's +62.6% leader) now -11.88% c7d — reverted entirely.
- DEX vol: $7.01B (+12.00% 24h, +8.67% 7d) — bounces hard from 05-28's
  -3.96% cooldown. Uniswap V4 $668M (-7.53% c1d, V4 cooling); **PancakeSwap
  V3 $635M (+15.79% c1d, +33.42% c7d — NEW #2, displaces Aerodrome**);
  Uniswap V3 $609M (-1.14% c1d, momentum slowing).
- Real-yield top 3: USDC-WETH v3 ETH **21.0% apyBase NEW LEAD** ($97M TVL);
  APYUSD Pendle ETH 21.0% ($15M TVL — returns to top 3); ETH-LINK V4 ETH
  18.0% apyBase ($14M TVL — first V4 pool in real-yield top 3). **Yesterday's
  entire top 3 rotated out** (USDC-CBBTC halved, WETH-USDT outlier flag,
  WBTC-USDT collapsed to 5%) — unusual full one-day rotation.
- Incentive-yield top 2: CVXCRV 25% ($30M TVL — DAY 2 of decline from
  27.18%); USDC-AERO Aerodrome Base 17% ($27M TVL — fills SDCRV's vacated
  slot, SDCRV apyReward stream stopped today, filter drops).
- Stables: $319.01B (-0.25% 24h, continues yesterday's -0.21% drift). Up
  cohort: GUSD +90.28% to $318M (large consolidation event ~$150M issuance);
  M by M0 +4.99% to $362M (DAY 5 streak unbroken: $332→$336→$342→$351→$362);
  FRAX +4.81%; rwaUSDi +1.16% (DAY 6 RWA growth); USDS Sky +1.42% (~$124M
  new supply). Down cohort extends: PYUSD -7.90% to $3.03B (DAY 4
  cumulative ~-19%); USDD -2.99% to $1.40B (DAY 3 cumulative ~-14%); USDf
  -5.05% to $1.50B (DAY 3 cumulative ~-12%).
- Continuity vs 05-28: TVL reverses (+0.35% first up-day); DEX vol +12%
  bounces -3.96% cooldown; PancakeSwap V3 enters DEX top 3 displacing
  Aerodrome; HL Perps c7d strengthens +6.3%→+14.2%, holds #3 3rd day;
  Uniswap V3 fees lead reverses entirely; full real-yield top-3 rotation;
  PYUSD/USDf/USDD continue multi-day declines; M by M0 / rwaUSDi / RLUSD /
  USDS continue gains.

## Narrative tracker
- RIDE: Agent-payment infra (AWS Bedrock AgentCore Payments, Coinbase, Stripe).
  Updated 05-28: x402 → 169M machine-native payments, $73M settled
  May 2025–April 2026, USDC 98.6% share; AI crypto sector $9B → $22.6–27B
  mcap. Base shipped MCP Agent Gateway 05-26 (Moonwell/Morpho/Uniswap/
  Aerodrome/Virtuals plugins).
- RIDE: Stablecoin payment rails.
- RIDE: RWA tokenization on Stellar — DTCC + Stellar Development Foundation
  announced 2026-05-27 plan to tokenize DTC-custodied assets (Russell 1000
  equities, ETFs, US Treasuries) on Stellar with H1 2027 rollout.
  **Broadening 05-29**: INJ record $3.57B tokenized-equity daily vol on
  Injective (2026-05-27), M by M0 RWA stable DAY 5 streak, 3+ distinct
  vectors firing.
- RIDE (NEW 05-29): Prediction Markets (RAIN) — RAIN +93.03% 7d, rank #14
  by mcap ($9.0B, new top-20 entrant). Rain Protocol V2 + $100M foundation
  liquidity + joined top-3 global prediction markets by TVL ahead of
  2026 FIFA WC.
- WATCH: Hyperliquid/DEX Infrastructure — HYPE rank #11 ($13.8B mcap, near
  ATH $64.63 from 05-26), HL Perps fees holds #3 3rd day, kHYPE TVL +16%
  to $1.10B. Builder Program $20M, Grayscale HYPE $800M ARR projection,
  BHYP ETF inflows.
- WATCH (NEW 05-29): AI Data Networks (ALLORA) — ALLO trending +176% 24h,
  $103M 24h vol. Decentralized AI model coordination network. No top-50
  position yet; single-token signal only.
- WATCH: Institutional BTC / corporate treasuries.
- FADE: AI-agent token basket (PHALA pump example).
- FADE (NEW 05-29): Privacy Coins — ZEC -16.91% 7d, XMR -6.24% 7d; small
  24h bounce not converting to sustained bid, 5th consecutive fading session.
- Reflexivity flagged: AI-agent tokens, Hyperliquid FDV, Solana "underlayer".
- Note: Kaito Yaps/Yapper leaderboards shut Jan 15 2026 — no live public
  mindshare leaderboard reference.

## Token signals
- Token-pick **2026-05-29: INJ** $6.01 (+12.8% 24h / +11.8% 7d), HIGH 9/10.
  Thesis: Injective record $3.57B daily on-chain tokenized-equity vol
  2026-05-27 + 21Shares (TINJ) and Canary staked-INJ ETF filings advancing
  post-March commodity classification; vmc 0.33, outperforming BTC -5.1% /
  ETH -5.5% on 7d. Risk: HYPE ($10B/day perp vol, BHYP/GHYP/THYP spot ETFs
  already on NYSE Arca) starves INJ's burn-deflation fee flow.
- **LAB skip 05-29** — scored 10/10 but skipped on integrity grounds:
  ZachXBT flagged 95% insider supply and 100M LAB ($480M) moved from
  Bitget to fresh wallets, active manipulation investigation with $10K
  bounty out. Score-rubric doesn't capture active-fraud risk; the kind
  of named risk that overrides score.
- Polymarket **NBA Thunder 2026 Finals** YES 43¢, HIGH ~11pp edge (fair
  ~54%). Bookmaker devig: OKC -155 to advance past Spurs (60.7%) × NYK ~88%
  to win East after sweeping Cavs 4-0 ≈ 53.4%. Mispricing concentrated on
  Game-7-leg, not Finals-leg. Liquidity gate: $156k 24h vol, well >$50k.
- Token-pick 2026-05-28: XLM (Stellar) $0.1818 (+21.6% 24h / +26.6% 7d),
  HIGH 10/10. Strengthened to $0.1978 by afternoon re-fire (suppressed
  by once-per-day rule).
- Token-pick 2026-05-21: LIT (Lighter) $1.32 +45.1% 7d, HIGH 10/10.
- Token-alert **2026-05-29**: REPPO $0.01824888 (+12.13%) — **alert
  triggered**, snaps 3-day red streak, claws back through 05-27 low
  $0.01712; HYPER $0.086631 (-2.91%, 7th straight red/flat, breaks $0.089
  floor); VVV $15.60 (flat hold +0.1%). Volume-spike check: no spikes.
- Token-alert 2026-05-28: REPPO $0.01635 (-5.32%, 3rd straight red);
  HYPER $0.089451 (-4.93%, 6th straight red/flat); VVV $15.59 (-9.81%).

## Bitcoin
See [[last30-bitcoin]] for the 30-day narrative snapshot (baseline 2026-05-21,
still stale). Last30 has not re-run.
