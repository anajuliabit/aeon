---
name: Token Alert
description: Notify on price or volume anomalies for tracked tokens
var: ""
tags: [crypto]
---
> **${var}** — Token symbol or CoinGecko ID. If empty, checks all tracked tokens.

If `${var}` is set, only check that token.


## Config

This skill reads tracked tokens from a "Tracked Tokens" section in `memory/MEMORY.md`. If the section doesn't exist AND `${var}` is empty, log `TOKEN_ALERT_NO_CONFIG` and exit silently — do not notify, do not invent tokens.

```markdown
## Tracked Tokens
| Token | CoinGecko ID | 24h % Threshold | Price Floor | Price Ceiling |
|-------|--------------|-----------------|-------------|---------------|
| ETH   | ethereum     | 10%             | 2000        | 5000          |
| SOL   | solana       | 10%             |             |               |
```

- **24h % Threshold** — overrides the default 10% from step 2 for that token. Blank → use default.
- **Price Floor / Price Ceiling** — optional absolute USD levels that drive the "threshold-cross" check in step 2. Blank → no cross check for that token.

---

Read memory/MEMORY.md for tracked tokens and alert thresholds.
Read the last 2 days of memory/logs/ for previous prices to detect changes.

Steps:
1. For each token tracked in MEMORY.md (under "Tracked Tokens"):
   - Fetch current price data using a free API:
     ```bash
     # CoinGecko API (works without key, but COINGECKO_API_KEY improves rate limits)
     if [ -n "${COINGECKO_API_KEY:-}" ]; then
       curl -s "https://pro-api.coingecko.com/api/v3/simple/price?ids=TOKEN_ID&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true" \
         -H "x-cg-pro-api-key: $COINGECKO_API_KEY"
     else
       curl -s "https://api.coingecko.com/api/v3/simple/price?ids=TOKEN_ID&vs_currencies=usd&include_24hr_change=true&include_24hr_vol=true"
     fi
     ```
   - Compare against last logged price in memory/logs/
2. Alert if any of these conditions are met (evaluate independently per token):
   - **24h price change** — `|change_24h| >= threshold` (default 10%, or the token-specific override from the Tracked Tokens table).
   - **Volume spike** — `current_volume_24h >= 3 * mean(volume_24h over the last 5 logged runs)`. **Skip this check if fewer than 5 historical points exist** in `memory/logs/` for the token — log `volume-spike: skipped (n=<count>, need 5)` and continue. Do not invent a baseline.
   - **Threshold cross** — current price `<= Price Floor` or `>= Price Ceiling` from the Tracked Tokens table AND yesterday's logged price was on the other side of the level (i.e. an actual crossing this run, not a sustained breach). Skip with `threshold-cross: skipped (no Floor/Ceiling configured)` for any token without levels.
3. If any alerts triggered, send via `./notify`:
   ```
   *Token Alert — ${today}*

   TOKEN: $X.XX (up/down Y% 24h)
   Volume: $Z (N x average)
   Trigger: reason for alert
   ```
4. Log all current prices to memory/logs/${today}.md (for next comparison).
If no anomalies detected, log "TOKEN_ALERT_OK" and end.

## Sandbox note

The sandbox may block outbound curl. Use **WebFetch** as a fallback for any URL fetch. For auth-required APIs, use the pre-fetch/post-process pattern (see CLAUDE.md).
