#!/usr/bin/env bash
# Pre-fetch Hyperliquid public data OUTSIDE the Claude sandbox.
# Runs before Claude. Writes JSON to .hl-cache/ so reppo-trading-agent
# can read cached data instead of calling the network (which the sandbox
# may block intermittently).
#
# Endpoints used (all public, no auth):
#   - https://stats-data.hyperliquid.xyz/Mainnet/leaderboard
#   - https://api.hyperliquid.xyz/info  (POST userFillsByTime / candleSnapshot)
#
# Why userFillsByTime (not userFills): HL's /info endpoint caps every
# `userFills` response at 2000 rows, returning the 2000 MOST RECENT
# fills regardless of how long ago they happened. For top-leaderboard
# wallets (often >2000 fills/day), this collapses the slice to <1 day
# of span — below the rubric's ≥7-day floor, so every wallet gets
# rejected at the gate. `userFillsByTime` accepts `startTime` (ms
# epoch) and returns fills since that timestamp, ascending by time,
# so a 7d startTime yields a full-window slice for wallets that
# trade ≤2000 fills in 7d (the rubric's target — directional
# traders, not market-makers). High-frequency MMs (>2000/7d) still
# get capped, but the resulting <7d span correctly disqualifies
# them from the rubric anyway. See reppo-swarm 2nd run digest
# (2026-05-28) for the original diagnosis.
#
# On any read failure an error-marker JSON is written so the skill
# detects the failure and degrades gracefully via its WebFetch fallback.

set -euo pipefail

CACHE_DIR=".hl-cache"
mkdir -p "$CACHE_DIR"

# Tunable knobs (env-overridable so the workflow can dial them).
HL_TOP_N="${HL_TOP_N:-3}"                # how many margin-ranked wallets to pull fills for (was 10; trimmed to fit trading-agent's 30-min Aeon timeout — 10× per-wallet jq + classification + dataset build hit the wall in run 5)
HL_WINDOW="${HL_WINDOW:-week}"           # leaderboard window: day|week|month|allTime
HL_FILLS_DAYS="${HL_FILLS_DAYS:-7}"      # userFillsByTime startTime offset (still capped at 2000 fills/response)
HL_MIN_VLM_USD="${HL_MIN_VLM_USD:-100000}"  # noise floor: skip wallets with <$100k vlm in HL_WINDOW
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

# 2. Top-N wallets ranked by margin (pnl / vlm) — biases toward
# directional alpha, away from high-frequency churn. Top-PnL alone
# surfaces mostly HFT/MM wallets that hit the 2000-row response cap
# in <1 day, so the rubric never sees the directional traders it's
# meant to evaluate. A wallet with $400k pnl on $1M vlm (40% margin)
# ranks above one with $400k pnl on $10M vlm (4% margin) — the
# former is a more concentrated directional position, the latter is
# high-turnover. HL_MIN_VLM_USD ($100k default) filters out the
# noise floor (low-vlm wallets where a small absolute pnl looks like
# extreme margin).
if jq -e . "$CACHE_DIR/leaderboard.json" >/dev/null 2>&1 \
   && ! jq -e '.code == "PREFETCH_FAILED"' "$CACHE_DIR/leaderboard.json" >/dev/null 2>&1; then

  mapfile -t TOP_ADDRS < <(
    jq -r --arg w "$HL_WINDOW" --argjson n "$HL_TOP_N" --argjson minvlm "$HL_MIN_VLM_USD" '
      .leaderboardRows
      | map({
          addr: .ethAddress,
          pnl: ((.windowPerformances // [])
                | map(select(.[0] == $w))
                | (.[0][1].pnl // "0")
                | tonumber),
          vlm: ((.windowPerformances // [])
                | map(select(.[0] == $w))
                | (.[0][1].vlm // "0")
                | tonumber)
        })
      | map(select(.vlm >= $minvlm))
      | map(. + { margin: (.pnl / .vlm) })
      | sort_by(-.margin)
      | .[:$n]
      | .[].addr
    ' "$CACHE_DIR/leaderboard.json" 2>/dev/null
  )

  # Window start for userFillsByTime — same ms epoch shared across all
  # wallet pulls so the slice is consistent within a single run.
  fills_now_ms=$(($(date +%s) * 1000))
  fills_start_ms=$((fills_now_ms - HL_FILLS_DAYS * 86400 * 1000))

  for addr in "${TOP_ADDRS[@]}"; do
    [ -n "$addr" ] || continue
    echo "hl-prefetch: fetching userFillsByTime for $addr (last ${HL_FILLS_DAYS}d)..."
    body=$(printf '{"type":"userFillsByTime","user":"%s","startTime":%d,"aggregateByTime":false}' \
                  "$addr" "$fills_start_ms")
    if ! curl -fsS --max-time 60 \
         -H 'Content-Type: application/json' \
         -d "$body" \
         "https://api.hyperliquid.xyz/info" \
         -o "$CACHE_DIR/user-fills-${addr}.json" 2>/dev/null; then
      error_marker "$CACHE_DIR/user-fills-${addr}.json" "userFillsByTime $addr failed"
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
