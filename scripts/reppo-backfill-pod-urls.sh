#!/usr/bin/env bash
# Backfill Reppo platform `url` for the 4 dataset-bearing pods that were
# registered BEFORE PR #50 took effect. Those pods went through Phase 2
# with the old projection: `url = LLM-supplied hypurrscan link, pdfURL =
# IPFS gateway`. The platform UI uses `url` as the "view content" link,
# so those pods open to a wallet history page instead of the actual
# labeled dataset.
#
# PR #50 fixed the projection going forward (skip POST when no
# dataset_uri; otherwise `url = .dataset_uri`). This script re-POSTs the
# 4 affected pods with the corrected body. Whether the platform treats
# it as an update-by-txHash or creates a duplicate is what we're
# testing — run on ONE pod first to find out.
#
# Run LOCALLY:
#
#   REPPO_AGENT_ID=cm...
#   REPPO_API_KEY=...
#   ./scripts/reppo-backfill-pod-urls.sh                 # all 4
#   ./scripts/reppo-backfill-pod-urls.sh 06e7715d81cdedca # just one
#
# Sister to scripts/reppo-backfill-pods.sh (which targets a different
# set of orphans — pre-Phase-2 mints that never had platform rows).
set -euo pipefail

if [ -z "${REPPO_AGENT_ID:-}" ] || [ -z "${REPPO_API_KEY:-}" ]; then
  echo "reppo-backfill-urls: REPPO_AGENT_ID and REPPO_API_KEY must be set" >&2
  echo "  set them in your shell and re-run" >&2
  exit 1
fi

API="https://reppo.ai/api/v1/agents/${REPPO_AGENT_ID}/pods"
SUBNET_UUID="cmnhuowns000bic04e16t6735"

# Each entry: pod hash (first 16) | txHash | IPFS CID | podName | podDescription
# Hashes from the trading-agent Execution Results across runs 9-11 and
# today's first run-4 mint. Pod metadata kept terse — full evaluable
# content lives in the pinned IPFS dataset, this body is just the UI
# teaser.
PODS_TSV='0d4b168331d58f61	0x602307948c7d73a8f7e61342b107134147784f252c31f502088d8492b6a8ae6c	QmY4yHDoVD93ScArDTiGaRVWNjsZHFQ3YgcwyhRtLL9KfY	HL ultra-HFT multi-mkt: 1152 close-longs	Wallet 0x2b3349 multi-market HFT (BTC/ETH/XYZ/NATGAS), 1152 close-long fills, Sharpe 7866, +$70k PnL. Labeled HL perp dataset, fills verifiable on hypurrscan.
a3ea5a0973858464	0x1a0dbea16bdfe70eed104978b4c71778155be2d2b9909eea4cd058f687d1dc46	QmSjHNJBhETakKpE7UmXvAG2DFeYewCsvGxkjeEB5Y4ZTs	HL CHIP perp close-short, 0x71dfc07d, 6.64d	Wallet 0x71dfc07d HL CHIP perp close-short strategy, Sharpe 805, +$24,780 PnL over 6.64d span. Labeled HL perp dataset, fills verifiable on hypurrscan.
e02fef4e76668a31	0x639cbc39356466c48a0b7e0678214ba5aa733271243855f592d588d6b774d486	QmRCqejoTkcoZuYo3x3kJ2qUjngUeSPGsudteRq9pvnuFQ	HL multi-mkt 0x7fdafde5: 1723 close fills	Wallet 0x7fdafde5 HL perp multi-market strategy across 10 markets, 1723 close fills, Sharpe 4603, +$76k PnL, MDD 0.003%. Labeled HL perp dataset.
06e7715d81cdedca	0x12ecfbdde461ef308963f2f30923bdabf8d3a90e11d4244d0177407f2a43cc11	QmRmiU2gAHG3CozZhCzP2QiyTnoTEmodjZUb2xXRXW1Lmb	HL ETH+ZEC close-short, 0xd4758770, 5.28h	Wallet 0xd4758770 HL ETH+ZEC close-short strategy, 812 fills over 5.28h, Sharpe 10.27. Labeled HL perp dataset, fills verifiable on hypurrscan.'

FILTER="${1:-}"
mkdir -p .reppo-cache
echo "reppo-backfill-urls: target = ${FILTER:-all 4 pods} (API: $API)"

# Process each TSV row.
echo "$PODS_TSV" | while IFS=$'\t' read -r pod_hash tx cid name desc; do
  [ -n "$pod_hash" ] || continue
  if [ -n "$FILTER" ] && [ "$FILTER" != "$pod_hash" ]; then continue; fi

  gateway="https://ipfs.io/ipfs/${cid}"
  cache=".reppo-cache/backfill-url-${pod_hash}.json"
  body=$(jq -n \
    --arg tx "$tx" \
    --arg subnet "$SUBNET_UUID" \
    --arg name "$name" \
    --arg desc "$desc" \
    --arg url "$gateway" \
    '{txHash:$tx, subnetId:$subnet, podName:$name, podDescription:$desc,
      url:$url, platform:"Aeon", category:"Trading Strategy",
      agreeToTerms:true, imageURL:"", thumbnailURL:"",
      pdfURL:$url, videoURL:""}')

  echo ""
  echo "  - $pod_hash · tx ${tx:0:18}… · dataset $gateway"

  http_code=$(curl -sS -X POST "$API" \
       -H "Authorization: Bearer ${REPPO_API_KEY}" \
       -H "Content-Type: application/json" \
       -d "$body" \
       -w "%{http_code}" \
       -o "$cache" 2>/dev/null || echo 000)

  if [ "${http_code:0:1}" = "2" ]; then
    echo "    ✓ HTTP $http_code — body cached at $cache"
    echo "      next step: open https://reppo.ai/subnets/${SUBNET_UUID} and confirm pod ${pod_hash}'s view-content link"
    echo "      → if link now opens IPFS: platform updates by txHash. safe to backfill the rest."
    echo "      → if a duplicate pod appears: don't run on the other 3. need a different endpoint."
  else
    echo "    ✗ HTTP $http_code — response body:" >&2
    tr -s '[:space:]' ' ' < "$cache" 2>/dev/null | cut -c1-600 >&2
    echo "" >&2
  fi
done

echo ""
echo "reppo-backfill-urls: done"
