#!/usr/bin/env bash
# Pre-fetch Hyperliquid public data OUTSIDE the Claude sandbox.
# Runs before Claude. Writes JSON to .hl-cache/ so reppo-trading-agent
# can read cached data instead of calling the network (which the sandbox
# may block intermittently).
#
# Endpoints used (all public, no auth):
#   - https://stats-data.hyperliquid.xyz/Mainnet/leaderboard
#   - https://api.hyperliquid.xyz/info  (POST userFills / candleSnapshot)
#
# On any read failure an error-marker JSON is written so the skill
# detects the failure and degrades gracefully via its WebFetch fallback.

set -euo pipefail

CACHE_DIR=".hl-cache"
mkdir -p "$CACHE_DIR"

# Tunable knobs (env-overridable so the workflow can dial them).
HL_TOP_N="${HL_TOP_N:-10}"               # how many leaderboard wallets to pull fills for
HL_WINDOW="${HL_WINDOW:-week}"           # leaderboard window: day|week|month|allTime
HL_OHLCV_COINS="${HL_OHLCV_COINS:-BTC ETH SOL}"  # coins to snapshot
HL_OHLCV_INTERVAL="${HL_OHLCV_INTERVAL:-1h}"
HL_OHLCV_DAYS="${HL_OHLCV_DAYS:-30}"

error_marker() {
  printf '{"error":%s,"code":"PREFETCH_FAILED"}\n' "$(printf '%s' "$2" | jq -R -s '.')" > "$1"
}

# 1. Leaderboard.
echo "hl-prefetch: fetching leaderboard..."
if ! curl -fsS --max-time 60 \
     "https://stats-data.hyperliquid.xyz/Mainnet/leaderboard" \
     -o "$CACHE_DIR/leaderboard.json" 2>/dev/null; then
  error_marker "$CACHE_DIR/leaderboard.json" "leaderboard fetch failed"
fi

# 2. Top-N wallets by chosen window PnL.
if jq -e . "$CACHE_DIR/leaderboard.json" >/dev/null 2>&1 \
   && ! jq -e '.code == "PREFETCH_FAILED"' "$CACHE_DIR/leaderboard.json" >/dev/null 2>&1; then

  # Extract addresses ranked by the chosen window's pnl (descending, numeric).
  mapfile -t TOP_ADDRS < <(
    jq -r --arg w "$HL_WINDOW" --argjson n "$HL_TOP_N" '
      .leaderboardRows
      | map({
          addr: .ethAddress,
          pnl: ((.windowPerformances // [])
                | map(select(.[0] == $w))
                | (.[0][1].pnl // "0")
                | tonumber)
        })
      | sort_by(-.pnl)
      | .[:$n]
      | .[].addr
    ' "$CACHE_DIR/leaderboard.json" 2>/dev/null
  )

  for addr in "${TOP_ADDRS[@]}"; do
    [ -n "$addr" ] || continue
    echo "hl-prefetch: fetching userFills for $addr..."
    body=$(printf '{"type":"userFills","user":"%s","aggregateByTime":false}' "$addr")
    if ! curl -fsS --max-time 60 \
         -H 'Content-Type: application/json' \
         -d "$body" \
         "https://api.hyperliquid.xyz/info" \
         -o "$CACHE_DIR/user-fills-${addr}.json" 2>/dev/null; then
      error_marker "$CACHE_DIR/user-fills-${addr}.json" "userFills $addr failed"
    fi
  done
else
  echo "hl-prefetch: leaderboard unavailable, skipping wallet pulls"
fi

# 3. OHLCV snapshots for the configured coins.
now_ms=$(($(date +%s) * 1000))
start_ms=$((now_ms - HL_OHLCV_DAYS * 86400 * 1000))
for coin in $HL_OHLCV_COINS; do
  out="$CACHE_DIR/candles-${coin}-${HL_OHLCV_INTERVAL}.json"
  echo "hl-prefetch: fetching candles for $coin $HL_OHLCV_INTERVAL..."
  body=$(printf '{"type":"candleSnapshot","req":{"coin":"%s","interval":"%s","startTime":%d,"endTime":%d}}' \
         "$coin" "$HL_OHLCV_INTERVAL" "$start_ms" "$now_ms")
  if ! curl -fsS --max-time 60 \
       -H 'Content-Type: application/json' \
       -d "$body" \
       "https://api.hyperliquid.xyz/info" \
       -o "$out" 2>/dev/null; then
    error_marker "$out" "candleSnapshot $coin $HL_OHLCV_INTERVAL failed"
  fi
done

echo "hl-prefetch: done"
