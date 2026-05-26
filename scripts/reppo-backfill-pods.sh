#!/usr/bin/env bash
# Backfill Reppo platform metadata for pods that were minted on chain
# BEFORE the metadata-registration phase landed in postprocess-reppo.sh
# (PR adding REPPO_AGENT_ID / REPPO_AGENT_API_KEY env vars and the
# phase-2 register loop).
#
# Without metadata, a pod exists as a bare ERC-721 on chain but does
# not appear in https://reppo.ai/subnets/<cuid> — the UI populates
# from the platform DB row that this script creates.
#
# Run LOCALLY once (or any time you find an orphaned mint tx):
#
#   REPPO_AGENT_ID=cm...
#   REPPO_AGENT_API_KEY=...
#   ./scripts/reppo-backfill-pods.sh
#
# Both env vars are also available as GH Actions secrets — for a
# one-shot CI invocation, dispatch via `gh workflow run` with the
# secrets injected.
set -euo pipefail

if [ -z "${REPPO_AGENT_ID:-}" ] || [ -z "${REPPO_AGENT_API_KEY:-}" ]; then
  echo "reppo-backfill: REPPO_AGENT_ID and REPPO_AGENT_API_KEY must be set" >&2
  echo "  set them in your shell or use \`gh secret set\` and dispatch the workflow" >&2
  exit 1
fi

API="https://reppo.ai/api/v1/agents/${REPPO_AGENT_ID}/pods"

# Each pod is one record: txHash + subnet + name + description + url.
# Extend this array (or replace) for ad-hoc backfills.
PODS_JSON='[
  {
    "txHash": "0x77f1386fb6fe3209bbf1a380b2be64f1f1c2c557416c9c7c0d31486a7e48a61f",
    "subnetId": 9,
    "podName": "ETH perp 1h Supertrend+ADX trend-follow",
    "podDescription": "Entry: ETH/USDT 1h, Supertrend(10, 3) flips long AND ADX(14) >= 25 (trend strength filter). Exit: Supertrend flips short OR ADX drops below 20. Symmetric short side on the inverse signals. Trades only when the trend filter is active to avoid chop. Strategy hash: 8d47851b7762a319 — first end-to-end mint from the Aeon reppo-swarm chain (run 17, 2026-05-26).",
    "url": "",
    "platform": "Aeon",
    "category": "Trading Strategy",
    "agreeToTerms": true,
    "imageURL": "",
    "thumbnailURL": "",
    "pdfURL": "",
    "videoURL": ""
  },
  {
    "txHash": "0x832db6832018891d3846997591ce127815e26e28ac51b1ac116265c036d91f21",
    "subnetId": 9,
    "podName": "ETH/USDT perp 4H Ichimoku cloud breakout",
    "podDescription": "Entry: ETH/USDT 4h, price closes above the Ichimoku cloud (Senkou Span A and B), Tenkan-sen crosses above Kijun-sen, and Chikou Span is above price 26 bars back (classic Ichimoku long confirmation). Exit: price re-enters the cloud OR Tenkan crosses below Kijun. Symmetric short on the inverse setup. Strategy hash: da7a36f4094a24f9 — second mint from the Aeon reppo-swarm chain (run 19, 2026-05-26).",
    "url": "",
    "platform": "Aeon",
    "category": "Trading Strategy",
    "agreeToTerms": true,
    "imageURL": "",
    "thumbnailURL": "",
    "pdfURL": "",
    "videoURL": ""
  }
]'

mkdir -p .reppo-cache
echo "reppo-backfill: posting metadata for $(echo "$PODS_JSON" | jq 'length') pod(s) to $API"

echo "$PODS_JSON" | jq -c '.[]' | while read -r pod; do
  tx="$(echo "$pod" | jq -r '.txHash')"
  name="$(echo "$pod" | jq -r '.podName')"
  echo "  - $tx ($name)"

  cache=".reppo-cache/register-backfill-${tx:0:18}.json"
  if curl -fsS -X POST "$API" \
       -H "Authorization: Bearer ${REPPO_AGENT_API_KEY}" \
       -H "Content-Type: application/json" \
       --data "$pod" \
       > "$cache" 2>&1; then
    echo "    ✓ registered (response cached at $cache)"
  else
    echo "    ✗ failed:" >&2
    # Compact whitespace and trim to 300 chars for legibility.
    tr -s '[:space:]' ' ' < "$cache" 2>/dev/null | cut -c1-300 >&2
    echo "" >&2
  fi
done

echo "reppo-backfill: done"
