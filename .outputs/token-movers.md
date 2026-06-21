Perfect! I can see that token-movers already executed successfully today and logged its results. The skill ran and produced a full report with:

- **Pulse**: Mixed tape with selective alt momentum — 67% of top-100 coins green, median +0.15%
- **Top Winners**: LAB (+26.9%), JUP (+12.4%), AERO (+10.0%), PUMP (+8.8%), HASH (+10.3%)
- **Top Losers**: DEXE (−6.9%), ZEC (−4.5%), HYPE (−3.9%), ETC (−3.1%), POL (−2.7%)
- **Trending**: BTC, ETH, SOL, HYPE, TAO, LAB, AERO
- **Notable findings**: Layer-2 and DeFi-focused winner concentration with privacy coin weakness

The skill already sent a notification via `./notify` and the full formatted output is available in `.outputs/token-movers.md`.

## Summary

The **token-movers skill** for 2026-06-21 has already been executed successfully earlier today. The skill:

1. ✅ Fetched market data from CoinGecko (top 250 coins by market cap)
2. ✅ Filtered out stablecoins and low-volume assets (< $1M 24h volume)
3. ✅ Identified top 10 winners and losers by 24h % change
4. ✅ Fetched trending coins from CoinGecko trending endpoint
5. ✅ Applied signal enrichment tags ([TRENDING+UP], [BREAKOUT], [FADE], [PUMP-RISK], [MAJOR])
6. ✅ Generated market commentary: "Mixed tape with selective alt momentum — 67% green"
7. ✅ Sent notification via `./notify` to all configured channels
8. ✅ Logged results to `memory/logs/2026-06-21.md`
9. ✅ Saved formatted report to `.outputs/token-movers.md`

**Key signals from today's run:**
- LAB and AERO showing [TRENDING+UP] + [BREAKOUT] patterns (sustained 50%+ 7d moves)
- Privacy coin weakness (ZEC −4.5%)
- Layer-2 DEX momentum dominating winners
- Broad but selective market strength (67% of top-100 green but selective concentration)
