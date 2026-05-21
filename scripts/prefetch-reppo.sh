#!/usr/bin/env bash
# Pre-fetch Reppo CLI reads OUTSIDE the Claude sandbox.
# Runs before Claude. Writes JSON to .reppo-cache/ so skills read cached
# data instead of calling the network (which the sandbox may block).
#
# On any read failure an error-marker JSON is written so downstream skills
# detect the failure and degrade gracefully instead of crashing.
set -euo pipefail

CACHE_DIR=".reppo-cache"
CONFIG_DIR="configs/datanets"
mkdir -p "$CACHE_DIR"

# Ensure the CLI is available.
if ! command -v reppo >/dev/null 2>&1; then
  echo "reppo-prefetch: installing @reppo/cli..."
  npm i -g @reppo/cli >/dev/null 2>&1 || {
    echo "reppo-prefetch: CLI install failed, skipping prefetch"
    exit 0
  }
fi

# Write an error marker to a cache file. Args: file, message.
error_marker() {
  printf '{"error":%s,"code":"PREFETCH_FAILED"}\n' "$(printf '%s' "$2" | jq -R -s '.')" > "$1"
}

# Read a frontmatter scalar from a markdown file. Args: file, key.
frontmatter() {
  awk -v k="$2" '
    /^---[[:space:]]*$/ { f++; next }
    f==1 && index($0, k ":")==1 {
      sub(/^[^:]+:[[:space:]]*/, ""); gsub(/["'\'']/, ""); gsub(/[[:space:]]+$/, "");
      print; exit
    }
  ' "$1"
}

# 1. Live mainnet datanet catalog (validity checks + new-datanet discovery).
echo "reppo-prefetch: fetching datanet catalog..."
if ! REPPO_NETWORK=mainnet reppo list datanets --status ACTIVE --json \
     > "$CACHE_DIR/datanets.json" 2>/dev/null; then
  error_marker "$CACHE_DIR/datanets.json" "list datanets failed"
fi

# 2. Per-rubric datanet detail + pods.
if [ -d "$CONFIG_DIR" ]; then
  for cfg in "$CONFIG_DIR"/*.md; do
    [ -f "$cfg" ] || continue
    name="$(basename "$cfg" .md)"
    datanet_id="$(frontmatter "$cfg" datanet_id)"
    if [ -z "$datanet_id" ] || [ "$datanet_id" = "REPLACE_WITH_MAINNET_TRADINGGYMAI_DATANET_ID" ]; then
      echo "reppo-prefetch: $name has no real datanet_id, skipping"
      error_marker "$CACHE_DIR/pods-$name.json" "datanet_id not configured"
      error_marker "$CACHE_DIR/datanet-$name.json" "datanet_id not configured"
      continue
    fi
    echo "reppo-prefetch: fetching state for $name ($datanet_id)..."
    if ! REPPO_NETWORK=mainnet reppo query datanet "$datanet_id" --json \
         > "$CACHE_DIR/datanet-$name.json" 2>/dev/null; then
      error_marker "$CACHE_DIR/datanet-$name.json" "query datanet $datanet_id failed"
    fi
    if ! REPPO_NETWORK=mainnet reppo list pods --all --datanet "$datanet_id" --json \
         > "$CACHE_DIR/pods-$name.json" 2>/dev/null; then
      error_marker "$CACHE_DIR/pods-$name.json" "list pods $datanet_id failed"
    fi
  done
fi

echo "reppo-prefetch: done"
