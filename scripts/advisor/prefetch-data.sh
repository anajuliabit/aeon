#!/usr/bin/env bash
# scripts/advisor/prefetch-data.sh
# Fetch everything the Virtuals advisor runner needs into .investiments-cache/advisor/.
#
# Best-effort: a failed feed is logged (::warning::) and skipped — it NEVER aborts the run.
# All feeds are keyless GETs EXCEPT the portfolio snapshot (Basic auth) and the optional
# X sentiment search (XAI key). Runs OUTSIDE the Claude sandbox (from the workflow step),
# so env-var-in-header auth is fine here.
set -uo pipefail

BASE="${INVESTIMENTS_BASE_URL:-https://investiments-production.up.railway.app}"
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
if [ -n "${INVESTIMENTS_BASIC_AUTH:-}" ]; then
  code=$(curl -sS --max-time 30 \
      -H "Authorization: Basic ${INVESTIMENTS_BASIC_AUTH}" \
      "$BASE/api/snapshot" -o "$D/snapshot.json" -w "%{http_code}" 2>/dev/null || echo "000")
  if [ "$code" = "200" ]; then
    echo "ok snapshot.json"
  else
    # Non-200: don't leave an error page where a snapshot is expected.
    rm -f "$D/snapshot.json"
    echo "::warning::advisor-prefetch: snapshot fetch failed (HTTP $code at $BASE/api/snapshot)"
  fi
else
  echo "::warning::advisor-prefetch: INVESTIMENTS_BASIC_AUTH not set, skipping snapshot"
fi

# --- Keyless market/DeFi feeds ---
get yields.json     "https://yields.llama.fi/pools"
get fees.json       "https://api.llama.fi/overview/fees?excludeTotalDataChart=true"
get protocols.json  "https://api.llama.fi/protocols"
get cg-global.json  "https://api.coingecko.com/api/v3/global"
get cg-btc.json     "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=30"
get fng.json        "https://api.alternative.me/fng/?limit=1"
get cg-markets.json "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=100&page=1"

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

echo "advisor-prefetch: done"
ls -1 "$D" 2>/dev/null || true
