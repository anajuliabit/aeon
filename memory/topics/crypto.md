# Crypto — Research State

Consolidated from defi-overview, narrative-tracker, token-pick, token-alert and digest runs.
Latest data point wins; this file is overwritten as newer runs land.

## DeFi overview (latest: 2026-05-26)
- TVL $82.71B raw (+0.15% 24h chain-weighted derived, -0.10% 7d) vs $82.50B 05-25 —
  essentially flat. DEX vol +14.42% (snap back from 05-25's -20.95% crater),
  fees +14.56% (recover from -8.6%), stables +0.18% → Mixed verdict.
- Top chains: Ethereum $43.30B, BSC $5.62B, Solana $5.46B (all 1d deltas under
  the 1% threshold — suppressed). Chain-movers section dropped: biggest mover
  ≥$500M was Polygon +0.35%. Smaller chains Near +8.4% / TON +4.7% under $500M.
- Protocol movers: Obol +64.85% ($496M → $818M, ETH staking pool) — same
  data-revision artifact flagged 05-25 (+62.16%) and 05-24 (loser slot).
  Snapshot value $873M → $818M DOWN day-over-day while change_1d says +65% —
  confirmed methodology revision, third day in a row. Rocket Pool -35.52%
  ($1.02B → $659M) on the down side — 7d -37.1% IMPROVED from yesterday's -49.1%
  which is impossible unless methodology shifted (confirmed artifact).
  World Chain +23.94% (7d +52.3%) was the cleanest sustained gainer but didn't
  take the up slot. Superstate USTB -17.56% (7d -22.3%) the cleanest sustained loser.
- DEX vol $5.38B (+14.42% 24h, -18.03% 7d). Uniswap V4 $768M (+40.94%) holds top,
  PancakeSwap V3 $505M (+9.91%), Aerodrome Slipstream $473M (-10.12%). Uniswap V3
  also bounced +22.28% to $381M — V3↔V4 rotation now both sides bouncing.
- Fees leader: Tether $16.40M/24h (flat 7d); Circle USDC $6.43M (flat, -0.3%);
  Canton $2.02M (flat, -0.5%) — displaced Uniswap V4 from #3 since V4 fees fell
  from $4.18M to $1.37M (-67%). Total fees $57.62M (+14.56% 24h, +5.51% 7d).
- Fees beating TVL (7d): Uniswap V4 (fees +60% / TVL -6.70%, $1.37M 24h fees,
  $698M TVL — V3→V4 rotation continues paying); Centrifuge Protocol (fees +41.60% /
  TVL -5.76%, $0.61M 24h, $1.46B TVL — RWA fee growth despite NAV drift).
  Extreme-growth outliers (Sanctum Validator LSTs, Jupiter Staked SOL) excluded
  as new-tracking bootstrap noise.
- Real-yield top 3 (all Ethereum): WETH-USDT v3 Uniswap 26.4% (+0.4pp vs 05-25),
  APYUSD Pendle 21.0% (holds #2), USDC-WETH v3 Uniswap 19.7% (new at #3,
  displaces ETH-LINK v4 which dropped to 12.6%).
- Incentive-yield top 2: CVXCRV 25.43% via CRV/CVX rewards ($33M TVL, holds #1);
  SDCRV 21.95% via CRV rewards ($27M TVL, new at #2, displaces USDC-AERO 21.38%
  which fell to #3). Curve-locker theme intensifies — both top incentive pools
  now CRV-staking variants.
- Stables: $321.47B (+0.18% 24h vs $320.89B 05-25). Notable single-issuer:
  ↑ crvUSD +5.41% to $253M (reverses 05-25's -10.06% day-2 outflow; back above
  05-22 baseline $245M), ↑ RLUSD +1.59% to $1.77B, ↑ YLDS +1.99% to $551M,
  ↑ M by M0 +1.68% to $336M, ↑ rwaUSDi +1.47% to $338M; ↓ Falcon USDf -2.00%
  to $1.58B (2nd day same -2.00%), ↓ PYUSD -1.54% to $3.55B.
- Continuity vs 05-25: Obol +65% day 2 as gainer (methodology revision); Rocket
  Pool -36% day 2 as loser (same artifact); World Chain +24% sustained 7d +52%;
  Superstate USTB -18% sustained outflow; DEX volume +14% snaps back; V3↔V4
  both bouncing today; fees +15% recovery; Canton replaces V4 in fees #3;
  crvUSD reverses outflow; SDCRV displaces USDC-AERO in incentive #2.
- Data caveat: /v2/chains carries no change_1d/7d — chain deltas derived
  TVL-weighted from /protocols ex-CEX/ex-Chain ex-borrowed/staking/vesting subkeys,
  clamped ±75%. Staking-pool methodology revisions (Obol, Rocket Pool) continue
  distorting top movers — third consecutive day. 12:39Z scheduled run failed
  on foundry-toolchain action download (GH Actions infra flake); manual re-run
  is the day's data.

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
- Token-alert 2026-05-26: REPPO $0.02197417 -11.32% 24h → alert fired (>10%
  threshold). Erases 2 days of recovery, back below 05-22 baseline $0.02313.
  HYPER (hyperlane, rank 584 — NOT HYPE/Hyperliquid) $0.095897 -7.47% — breaks
  4-day flat band ~$0.103-0.104. VVV (venice-token) $17.63 -5.91% — third red day
  of last four. Day-over-day: REPPO -10.6%, HYPER -7.5%, VVV -6.2%. All three red.
- Volume-spike baseline still under-sized: 4 historical points (05-22 → 05-25),
  below the ~5-point convention. For the record at 05-26: REPPO 4d avg $2.96M
  vs $3.21M (1.08x), HYPER avg $22.64M vs $23.90M (1.06x), VVV avg $84.67M vs
  $58.29M (0.69x). No spikes.
- Threshold-cross check still skipped — no Price Floor / Price Ceiling rows
  populated in MEMORY.md yet. PR #9 (merged 05-25) defines the columns; operator
  hasn't filled rows.

## Bitcoin
See [[last30-bitcoin]] for the 30-day narrative snapshot (baseline 2026-05-21):
Saylor/Strategy dependency, whale accumulation vs distribution, ETF flows flipped negative.
