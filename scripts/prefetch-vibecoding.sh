#!/usr/bin/env bash
# Pre-fetch r/vibecoding Reddit JSON OUTSIDE the Claude sandbox.
#
# Path selection (ISS-015 fix):
# 1. If REDDIT_CLIENT_ID + REDDIT_CLIENT_SECRET are set, use oauth.reddit.com
#    via the OAuth2 client_credentials flow. Authed traffic routes through
#    different infra than anonymous old.reddit.com requests and is not subject
#    to the datacenter-IP block that took out the anonymous path 2026-05-28.
# 2. If those secrets are absent, fall back to anonymous old.reddit.com. Same
#    behavior as before — leaves error markers if Reddit still rejects the IP.
#
# Error-marker JSON on any failure so the skill detects and degrades
# gracefully instead of crashing.
set -euo pipefail

SKILL="${1:-}"
VAR="${2:-}"

# Gate: only run for the vibecoding-digest skill (or no SKILL = manual run).
case "$SKILL" in
  ""|vibecoding-digest) ;;
  *) exit 0 ;;
esac

CACHE_DIR=".vc-cache"
mkdir -p "$CACHE_DIR"

# Window for top.json. Mirrors the skill's parsing.
TIME_WINDOW="${VAR:-day}"
case "$TIME_WINDOW" in day|week|month) ;; *) TIME_WINDOW="day" ;; esac

UA="web:aeon-vibecoding-digest:1.0 (by /u/aeonbot)"

# Decide path and set the request host + auth header accordingly.
AUTH_HEADER=""
if [ -n "${REDDIT_CLIENT_ID:-}" ] && [ -n "${REDDIT_CLIENT_SECRET:-}" ]; then
  echo "vibecoding-prefetch: REDDIT_CLIENT_ID present, using oauth.reddit.com"
  TOKEN_RESPONSE=$(curl -sS --max-time 15 \
    -u "${REDDIT_CLIENT_ID}:${REDDIT_CLIENT_SECRET}" \
    -A "$UA" \
    -d "grant_type=client_credentials" \
    "https://www.reddit.com/api/v1/access_token" 2>&1) || TOKEN_RESPONSE=""

  ACCESS_TOKEN=$(printf '%s' "$TOKEN_RESPONSE" | jq -r '.access_token // empty' 2>/dev/null)

  if [ -n "$ACCESS_TOKEN" ]; then
    HOST="https://oauth.reddit.com"
    AUTH_HEADER="Authorization: Bearer $ACCESS_TOKEN"
    echo "vibecoding-prefetch: obtained oauth token (${#ACCESS_TOKEN} chars)"
  else
    echo "vibecoding-prefetch: oauth token fetch failed, response: $(printf '%s' "$TOKEN_RESPONSE" | head -c 200)"
    echo "vibecoding-prefetch: falling back to anonymous old.reddit.com"
    HOST="https://old.reddit.com"
  fi
else
  echo "vibecoding-prefetch: no REDDIT_CLIENT_ID/SECRET, using anonymous old.reddit.com"
  HOST="https://old.reddit.com"
fi

# Write an error-marker JSON to a cache file. Args: file, message.
error_marker() {
  printf '{"error":%s,"code":"PREFETCH_FAILED"}\n' \
    "$(printf '%s' "$2" | jq -R -s '.')" > "$1"
}

# Fetch one endpoint with a single retry on transient failure.
# Args: url, outfile
fetch() {
  local url="$1" outfile="$2"
  local attempt curl_out rc
  for attempt in 1 2; do
    if [ -n "$AUTH_HEADER" ]; then
      curl_out=$(curl -fsSL --max-time 20 \
        -H "User-Agent: $UA" \
        -H "Accept: application/json" \
        -H "$AUTH_HEADER" \
        "$url" -o "$outfile" 2>&1) && rc=0 || rc=$?
    else
      curl_out=$(curl -fsSL --max-time 20 \
        -H "User-Agent: $UA" \
        -H "Accept: application/json" \
        "$url" -o "$outfile" 2>&1) && rc=0 || rc=$?
    fi

    if [ "$rc" = "0" ]; then
      if jq -e '.kind == "Listing" and (.data.children | type == "array")' \
           "$outfile" >/dev/null 2>&1; then
        return 0
      fi
      echo "vibecoding-prefetch: $(basename "$outfile") not a Listing on attempt $attempt"
    else
      echo "vibecoding-prefetch: curl rc=$rc on attempt $attempt — $(printf '%s' "$curl_out" | head -c 200)"
    fi
    sleep 2
  done
  return 1
}

echo "vibecoding-prefetch: window=$TIME_WINDOW host=$HOST"

if ! fetch \
     "$HOST/r/vibecoding/top.json?t=$TIME_WINDOW&limit=30" \
     "$CACHE_DIR/top.json"; then
  echo "vibecoding-prefetch: top failed, writing error marker"
  error_marker "$CACHE_DIR/top.json" "fetch top.json failed"
fi

if ! fetch \
     "$HOST/r/vibecoding/hot.json?limit=30" \
     "$CACHE_DIR/hot.json"; then
  echo "vibecoding-prefetch: hot failed, writing error marker"
  error_marker "$CACHE_DIR/hot.json" "fetch hot.json failed"
fi

if ! fetch \
     "$HOST/r/vibecoding/rising.json?limit=15" \
     "$CACHE_DIR/rising.json"; then
  echo "vibecoding-prefetch: rising failed, writing error marker"
  error_marker "$CACHE_DIR/rising.json" "fetch rising.json failed"
fi

# Record the window so the skill can detect a stale cache mismatch.
printf '{"window":"%s","fetched_at":"%s","host":"%s"}\n' \
  "$TIME_WINDOW" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" "$HOST" \
  > "$CACHE_DIR/meta.json"

echo "vibecoding-prefetch: done"
