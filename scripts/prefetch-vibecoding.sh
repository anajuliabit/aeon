#!/usr/bin/env bash
# Pre-fetch r/vibecoding Reddit JSON OUTSIDE the Claude sandbox.
# Reddit blocks the sandbox's datacenter IPs (403) and WebFetch on
# old.reddit.com also fails intermittently. This script runs on the
# runner host (full network) before Claude starts and writes JSON to
# .vc-cache/ so the vibecoding-digest skill reads cached data.
#
# Mirrors the prefetch-reppo.sh contract: error-marker JSON on any
# failure so the skill detects and degrades gracefully (quiet-day or
# error notification) instead of crashing.
set -euo pipefail

SKILL="${1:-}"
VAR="${2:-}"

# Gate: only run for the vibecoding-digest skill (or when called with
# no SKILL arg, e.g. manual invocation).
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

# Write an error-marker JSON to a cache file. Args: file, message.
error_marker() {
  printf '{"error":%s,"code":"PREFETCH_FAILED"}\n' \
    "$(printf '%s' "$2" | jq -R -s '.')" > "$1"
}

# Fetch one endpoint with a single retry on transient failure.
# Args: url, outfile
fetch() {
  local url="$1" outfile="$2"
  local attempt
  for attempt in 1 2; do
    if curl -fsSL --max-time 20 \
         -H "User-Agent: $UA" \
         -H "Accept: application/json" \
         "$url" -o "$outfile"; then
      # Sanity-check: must look like Reddit JSON (Listing kind).
      if jq -e '.kind == "Listing" and (.data.children | type == "array")' \
           "$outfile" >/dev/null 2>&1; then
        return 0
      fi
      echo "vibecoding-prefetch: $(basename "$outfile") not a Listing on attempt $attempt"
    fi
    sleep 2
  done
  return 1
}

echo "vibecoding-prefetch: window=$TIME_WINDOW"

if ! fetch \
     "https://old.reddit.com/r/vibecoding/top.json?t=$TIME_WINDOW&limit=30" \
     "$CACHE_DIR/top.json"; then
  echo "vibecoding-prefetch: top failed, writing error marker"
  error_marker "$CACHE_DIR/top.json" "fetch top.json failed"
fi

if ! fetch \
     "https://old.reddit.com/r/vibecoding/hot.json?limit=30" \
     "$CACHE_DIR/hot.json"; then
  echo "vibecoding-prefetch: hot failed, writing error marker"
  error_marker "$CACHE_DIR/hot.json" "fetch hot.json failed"
fi

if ! fetch \
     "https://old.reddit.com/r/vibecoding/rising.json?limit=15" \
     "$CACHE_DIR/rising.json"; then
  echo "vibecoding-prefetch: rising failed, writing error marker"
  error_marker "$CACHE_DIR/rising.json" "fetch rising.json failed"
fi

# Record the window so the skill can detect a stale cache mismatch.
printf '{"window":"%s","fetched_at":"%s"}\n' \
  "$TIME_WINDOW" "$(date -u +%Y-%m-%dT%H:%M:%SZ)" \
  > "$CACHE_DIR/meta.json"

echo "vibecoding-prefetch: done"
