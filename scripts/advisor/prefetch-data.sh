#!/usr/bin/env bash
# scripts/advisor/prefetch-data.sh
# Fetch everything the Virtuals advisor runner needs into .investiments-cache/advisor/.
#
# Best-effort: a failed feed is logged (::warning::) and skipped — it NEVER aborts the run.
# All feeds are keyless GETs EXCEPT the portfolio snapshot (Basic auth) and the optional
# X sentiment search (XAI key). Runs OUTSIDE the Claude sandbox (from the workflow step),
# so env-var-in-header auth is fine here.
set -uo pipefail

# Pinned production URL (canonical Railway domain — reaches the app; auth-guarded).
BASE="https://investiments-production.up.railway.app"
D=.investiments-cache/advisor
mkdir -p "$D"

# Keyless GET helper. Args: outfile, url
get() {
  if curl -fsS --max-time 30 "$2" -o "$D/$1"; then
    echo "ok $1"
  else
    echo "::warning::advisor-prefetch: feed failed: $1"
  fi
}

# --- Portfolio snapshot (Basic auth) ---
# Build the Basic-auth token at runtime from the dashboard creds (avoids
# pre-encoding mistakes). DASHBOARD_USER defaults to "admin" (investiments default).
DASHBOARD_USER="${DASHBOARD_USER:-admin}"
if [ -n "${DASHBOARD_PASSWORD:-}" ]; then
  AUTH=$(printf '%s:%s' "$DASHBOARD_USER" "$DASHBOARD_PASSWORD" | base64 | tr -d '\n')
  code=$(curl -sS --max-time 30 \
      -H "Authorization: Basic ${AUTH}" \
      "$BASE/api/snapshot" -o "$D/snapshot.json" -w "%{http_code}" 2>/dev/null || echo "000")
  if [ "$code" = "200" ]; then
    echo "ok snapshot.json"
  else
    # Non-200: don't leave an error page where a snapshot is expected.
    rm -f "$D/snapshot.json"
    echo "::warning::advisor-prefetch: snapshot fetch failed (HTTP $code at $BASE/api/snapshot)"
  fi
else
  echo "::warning::advisor-prefetch: DASHBOARD_PASSWORD not set, skipping snapshot"
fi

# --- Keyless market/DeFi feeds ---
get yields.json     "https://yields.llama.fi/pools"
get fees.json       "https://api.llama.fi/overview/fees?excludeTotalDataChart=true"
get protocols.json  "https://api.llama.fi/protocols"
get cg-global.json  "https://api.coingecko.com/api/v3/global"
get cg-btc.json     "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
get fng.json        "https://api.alternative.me/fng/?limit=1"
get cg-markets.json "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"

# --- Held-token fundamentals (fixes the top-100-only gap) ---
# One keyless call resolves the HELD tickers (from the snapshot) to their
# canonical CoinGecko coins (the `symbols` filter returns the highest-mcap match
# per symbol — e.g. cbbtc -> coinbase-wrapped-btc, not a same-ticker vault token),
# so held small-caps that aren't top-100 (e.g. MAMO, REPPO) get real mcap/FDV/
# supply instead of being punted to manual review. Held symbols never touch git
# (the snapshot and this cache are gitignored); only the ticker list is queried.
if [ -f "$D/snapshot.json" ]; then
  HELD_SYMS=$(jq -r '[.positions[]?.symbol, .analytics.assets[]?.symbol]
                     | map(select(. != null) | ascii_downcase) | unique | join(",")' \
                   "$D/snapshot.json" 2>/dev/null)
  if [ -n "$HELD_SYMS" ]; then
    curl -fsS --max-time 30 "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&symbols=$HELD_SYMS" \
      -o "$D/cg-held.json" && echo "ok cg-held.json ($HELD_SYMS)" \
      || echo "::warning::advisor-prefetch: cg-held fetch failed"
  fi
fi

# --- X sentiment (optional; reuses the proven Grok x_search shape from scripts/prefetch-xai.sh) ---
if [ -n "${XAI_API_KEY:-}" ]; then
  TODAY=$(date -u +%Y-%m-%d)
  YESTERDAY=$(date -u -d "yesterday" +%Y-%m-%d 2>/dev/null || date -u -v-1d +%Y-%m-%d)
  XBODY=$(jq -n \
    --arg model "grok-4-1-fast" \
    --arg prompt "Summarize the most market-moving crypto/DeFi news and X sentiment in the last 24h. Neutral, factual, cite handles." \
    --argjson tools "[{\"type\":\"x_search\",\"from_date\":\"$YESTERDAY\",\"to_date\":\"$TODAY\"}]" \
    '{model: $model, input: [{role: "user", content: $prompt}], tools: $tools}')
  if curl -fsS --max-time 180 -X POST "https://api.x.ai/v1/responses" \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $XAI_API_KEY" \
      -d "$XBODY" -o "$D/x-search.json"; then
    echo "ok x-search.json"
  else
    echo "::warning::advisor-prefetch: x_search failed"
  fi
else
  echo "advisor-prefetch: XAI_API_KEY not set, skipping x_search (optional)"
fi

# --- Advisor memory: last 7 daily reports + scorecard accuracy ---
# The advisor's own past output, distilled (summaries + structured recs), so the
# PM can hold a consistent line day-to-day instead of reasoning from scratch.
if [ -n "${DASHBOARD_PASSWORD:-}" ]; then
  MEM_REPORTS="[]"
  md=1
  while [ "$md" -le 7 ]; do
    MDAY=$(date -u -d "-${md} days" +%Y-%m-%d 2>/dev/null || date -u -v-${md}d +%Y-%m-%d)
    md=$((md + 1))
    MRUN=$(curl -fsS --max-time 30 -H "Authorization: Basic ${AUTH}"       "$BASE/api/advisor/run?date=$MDAY" 2>/dev/null || true)
    MSLIM=$(printf '%s' "$MRUN" | jq -c 'select(.report != null) | {date,
      summary: .report.summary,
      recommendations: [(.report.recommendations // [])[]
        | {title, action, urgency, confidence, symbol, direction, level, invalidateLevel, horizonDays}]}'       2>/dev/null || true)
    [ -n "$MSLIM" ] && MEM_REPORTS=$(printf '%s' "$MEM_REPORTS" | jq -c --argjson r "$MSLIM" '. + [$r]')
  done
  MACC=$(curl -fsS --max-time 30 -H "Authorization: Basic ${AUTH}" "$BASE/api/advisor/scorecard" 2>/dev/null | jq -c '.accuracy // {}' 2>/dev/null || echo '{}')
  MJOURNAL=$(curl -fsS --max-time 30 -H "Authorization: Basic ${AUTH}" "$BASE/api/journal?days=14" 2>/dev/null | jq -c '[.[]? | {ts, kind, text, symbol}]' 2>/dev/null || echo '[]')
  jq -n --argjson reports "$MEM_REPORTS" --argjson acc "$MACC" --argjson journal "$MJOURNAL" '{pastReports: $reports, scorecardAccuracy: $acc, operatorJournal: $journal}' > "$D/advisor-memory.json" && echo "ok advisor-memory.json ($(printf '%s' "$MEM_REPORTS" | jq 'length') past reports, $(printf '%s' "$MJOURNAL" | jq 'length') journal entries)"
else
  echo "advisor-prefetch: no DASHBOARD_PASSWORD, skipping advisor-memory"
fi

# NOTE (spec phase-2): DefiLlama emissions/unlocks (unlocks.json) is intentionally
# NOT fetched — api.llama.fi/emissions moved behind the paid plan (verified
# 2026-06-09: "Upgrade to the paid API plan"). Vesting for HELD tokens is already
# covered by the snapshot's analytics.vesting (Sablier). Revisit if a free
# unlock source appears.

# --- Micro-cap DEX liquidity + volume (GeckoTerminal, keyless) ---
# For held tokens outside the majors/stables, fetch top Base pools so trim
# recommendations can be sized against real daily volume. Symbols come from the
# gitignored snapshot cache — never committed.
if [ -f "$D/snapshot.json" ]; then
  MAJORS='["btc","wbtc","cbbtc","tbtc","eth","weth","wsteth","usdc","usdt","dai","usds","susds","usde","gho"]'
  # Top 4 BY POSITION VALUE (assets are one row per symbol already): `unique`
  # would sort alphabetically and let dust symbols crowd out the holdings that
  # actually need liquidity sizing (e.g. MAMO/REPPO).
  MICRO_SYMS=$(jq -r --argjson majors "$MAJORS" '
    [.analytics.assets[]? | select(.isStable | not)]
    | sort_by(-.valueUsd)
    | map(.symbol | ascii_downcase)
    | map(select(. as $s | $majors | index($s) | not)) | .[0:4] | join(" ")' \
    "$D/snapshot.json" 2>/dev/null)
  : > "$D/gt-liquidity.tmp"
  for TOK in $MICRO_SYMS; do
    curl -fsS --max-time 20 "https://api.geckoterminal.com/api/v2/search/pools?query=${TOK}&network=base&page=1" \
      -H "Accept: application/json" \
      | jq --arg t "$TOK" '{token: $t, pools: [.data[]? | {name: .attributes.name,
          liquidityUsd: (.attributes.reserve_in_usd | tonumber? // 0),
          volume24hUsd: (.attributes.volume_usd.h24 | tonumber? // 0)}]
          | sort_by(-.liquidityUsd) | .[0:5],
          totalVolume24hUsd: ([.data[]? | (.attributes.volume_usd.h24 | tonumber? // 0)] | add // 0)}' \
      >> "$D/gt-liquidity.tmp" 2>/dev/null || echo "::warning::advisor-prefetch: geckoterminal $TOK failed"
    sleep 2 # GeckoTerminal free tier: 30 calls/min
  done
  if [ -s "$D/gt-liquidity.tmp" ]; then
    jq -s '.' "$D/gt-liquidity.tmp" > "$D/gt-liquidity.json" && echo "ok gt-liquidity.json ($MICRO_SYMS)"
  fi
  rm -f "$D/gt-liquidity.tmp"
fi

# --- Hyperliquid perp funding (BTC/ETH, keyless) ---
if curl -fsS --max-time 20 -X POST "https://api.hyperliquid.xyz/info" \
    -H "Content-Type: application/json" -d '{"type":"metaAndAssetCtxs"}' \
    | jq '. as [$meta, $ctxs] | [range($meta.universe | length)
          | select($meta.universe[.].name == "BTC" or $meta.universe[.].name == "ETH")
          | {coin: $meta.universe[.].name,
             fundingHourly: ($ctxs[.].funding | tonumber? // null),
             openInterest: ($ctxs[.].openInterest | tonumber? // null),
             markPx: ($ctxs[.].markPx | tonumber? // null)}]' \
    > "$D/hl-funding.json" 2>/dev/null; then
  echo "ok hl-funding.json"
else
  echo "::warning::advisor-prefetch: hyperliquid funding failed"
fi

# --- Upcoming macro events (next 14 days, from the curated calendar) ---
ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TODAY=$(date -u +%Y-%m-%d)
UNTIL=$(date -u -d '+14 days' +%Y-%m-%d 2>/dev/null || date -u -v+14d +%Y-%m-%d)
if jq --arg today "$TODAY" --arg until "$UNTIL" \
    '{updated, coverage, events: [.events[] | select(.date >= $today and .date <= $until)]}' \
    "$ROOT/advisor/data/macro-calendar.json" > "$D/macro-upcoming.json" 2>/dev/null; then
  echo "ok macro-upcoming.json"
else
  echo "::warning::advisor-prefetch: macro calendar filter failed"
fi

echo "advisor-prefetch: done"
ls -1 "$D" 2>/dev/null || true
