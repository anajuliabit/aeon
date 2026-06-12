#!/usr/bin/env bash
# postprocess-picks.sh — POST staged pick records to the investiments dashboard.
# Skills write pick JSON to .pending-picks/*.json (token-pick step 6c, etc.);
# this runs after Claude finishes, with full env (sandbox-safe pattern, same
# as postprocess-farcaster.sh). 200/400 delete the payload (server upserts by
# id, validation failures are permanent); transient failures keep it for the
# next run.
set -euo pipefail

PENDING_DIR=".pending-picks"
BASE="${INVESTIMENTS_BASE_URL:-https://investiments-production.up.railway.app}"

if [ ! -d "$PENDING_DIR" ] || [ -z "$(ls -A "$PENDING_DIR" 2>/dev/null)" ]; then
  exit 0
fi

if [ -z "${INVESTIMENTS_BASIC_AUTH:-}" ]; then
  echo "postprocess-picks: INVESTIMENTS_BASIC_AUTH not set, skipping"
  exit 0
fi

for payload in "$PENDING_DIR"/*.json; do
  [ -f "$payload" ] || continue
  if ! jq -e '.source and .thesis' "$payload" >/dev/null 2>&1; then
    echo "postprocess-picks: malformed payload $(basename "$payload"), removing"
    rm -f "$payload"
    continue
  fi
  resp_file=$(mktemp)
  http_code=$(curl -s -o "$resp_file" -w "%{http_code}" --max-time 30 \
    -X POST "$BASE/api/picks" \
    -H "Authorization: Basic ${INVESTIMENTS_BASIC_AUTH}" \
    -H "Content-Type: application/json" \
    -d @"$payload") || http_code="000"
  if [ "$http_code" = "200" ]; then
    echo "postprocess-picks: posted $(basename "$payload") → id=$(jq -r '.id // "?"' "$resp_file")"
    rm -f "$payload"
  elif [ "$http_code" = "400" ]; then
    echo "postprocess-picks: rejected $(basename "$payload"): $(cat "$resp_file")"
    rm -f "$payload"
  else
    echo "postprocess-picks: HTTP $http_code for $(basename "$payload") — kept for retry"
  fi
  rm -f "$resp_file"
done

rmdir "$PENDING_DIR" 2>/dev/null || true
