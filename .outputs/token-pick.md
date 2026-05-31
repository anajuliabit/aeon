Tmp files left in `.tmp-token-pick/` (sandbox blocked cleanup). Notification is staged and log is appended.

## Summary

Ran `skills/token-pick/SKILL.md` for 2026-05-31. Both picks cleared MEDIUM+ conviction — no skip-day branch.

**Picks**
- **Token: WLD (Worldcoin)** — HIGH, signal 9/10. $0.333 (+10.9% 24h / +10.6% 7d), mcap $1.12B, vol $347M, vmc 0.31. Catalyst: Oku Trade DeFi aggregator live inside World App + weekly swap-comp WLD rewards drove on-chain activity to 2026 highs. Risk: Santiment FOMO-flag + reward-pull-mechanic decays after comp cohort settles. First time picked.
- **Market: "MicroStrategy sells any Bitcoin by June 30, 2026?"** — MEDIUM, edge ~6pp. YES 25.75¢, fair ~20%, lean NO. Saylor's "we'll probably sell to fund a dividend" is forward-only; 24,869 BTC bought week of 5-12 to 5-16; 10:1 net-buyer ratio; SEC disclosure lead time for extraordinary-dividend BTC sale points to Q2 earnings in August, not June.

**Dedup notes**
- Tokens XLM / INJ / HYPE all in 7-day window, none cleared fresh-catalyst gate. LAB skipped 3rd day on ZachXBT insider-supply flag. H (Humanity) tied WLD on score (9/10) but lost on June 25 unlock + late-stage +82% 7d blow-off-top read.
- MSTR June 30 dedup-clean (5-21 MSTR May 31 pick now 10 days old, outside 7d window) AND fresh catalyst (Saylor's pivot vs his 5-21 walked-back stance).

**Files**
- Staged notification: `.pending-notify/1780229408-token-pick.md` (1,463 chars; sandbox blocks direct `./notify "$(cat ...)"` — post-run delivery step picks it up)
- Log appended: `memory/logs/2026-05-31.md` with `TOKEN_PICK_DEDUP: WLD | "MicroStrategy sells any Bitcoin by June 30, 2026?"`

**Sources**: cg=ok, dex=ok (junk meme-pair output, cross-source bonus skipped), poly=ok. All curl-direct hits, no WebFetch fallback needed.

**Follow-up**: tmp data files left at `.tmp-token-pick/` (sandbox blocked rm).

Sources:
- [Worldcoin Surges 15% as On-Chain Activity Hits 2026 Highs Amid DeFi Integration](https://blockonomi.com/worldcoin-surges-15-as-on-chain-activity-hits-2026-highs-amid-defi-integration)
- [Worldcoin's FOMO Rally Cracks After On-Chain Activity Explodes](https://www.cryptbull.net/2026/05/28/worldcoins-fomo-rally-cracks-after-on-chain-activity-explodes/)
- [Strategy (MSTR) news: Company purchased more than $2 billion of BTC last week](https://www.coindesk.com/markets/2026/05/18/strategy-purchases-nearly-25-000-more-bitcoin-worth-more-than-usd2-billion)
- [Is the MicroStrategy Bitcoin Binge Over? What Saylor's Pause Means](https://finance.yahoo.com/markets/crypto/articles/microstrategy-bitcoin-binge-over-saylor-191404021.html)
