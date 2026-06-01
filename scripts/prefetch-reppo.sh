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

# Ensure the CLI is available.
if ! command -v reppo >/dev/null 2>&1; then
  echo "reppo-prefetch: installing @reppo/cli..."
  npm i -g @reppo/cli >/dev/null 2>&1 || {
    echo "reppo-prefetch: CLI install failed, writing error markers"
    error_marker "$CACHE_DIR/datanets.json" "reppo CLI unavailable"
    if [ -d "$CONFIG_DIR" ]; then
      for cfg in "$CONFIG_DIR"/*.md; do
        [ -f "$cfg" ] || continue
        name="$(basename "$cfg" .md)"
        error_marker "$CACHE_DIR/datanet-$name.json" "reppo CLI unavailable"
        error_marker "$CACHE_DIR/pods-$name.json" "reppo CLI unavailable"
      done
    fi
    exit 0
  }
fi

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

    # Vote-filter state: derives `current_epoch` (max validityEpoch across
    # all pods on this datanet — voting epochs roll forward on Reppo as
    # new pods land) and `voted_pod_ids` (union of: pods we've voted on
    # successfully per the ledger + pods THIS wallet has minted, since
    # the contract reverts CANNOT_VOTE_FOR_OWN_POD on any self-vote
    # attempt). The trading-agent reads this to skip out-of-epoch pods
    # (POD_NOT_VALID_FOR_EPOCH reverts) and any pod it's already
    # interacted with (ISS-005 + ISS-016).
    current_epoch=$(jq -r 'if .code == "PREFETCH_FAILED" then ""
                           else [.pods[]?.validityEpoch | tonumber? // empty] | if length > 0 then max | tostring else "" end
                           end' "$CACHE_DIR/pods-$name.json" 2>/dev/null || echo "")
    # Parse the markdown ledger for successfully-voted podIds. A vote row
    # looks like:
    #   | 2026-05-26 | 9 | 373 | DISLIKE | success — tx 0x… |
    # We want podId from column 4, only when datanet (column 3) == this
    # rubric's datanet AND status (column 5) contains "success". Skip
    # failed/reverted rows so the filter doesn't permanently block re-tries
    # of a pod where the tx itself failed.
    #
    # CRITICAL: scope to the "## Votes cast" section ONLY. The "## Minted
    # strategies" table has the SAME row shape (| date | 9 | X | … | success |)
    # but its column 4 is a sha256 strategy HASH, not a podId. Without the
    # section guard the awk scooped mint hashes into voted_pod_ids — junk
    # that never matches a numeric podId, silently weakening the own-mint
    # vote guard (surfaced 2026-06-01: vote-filter held hashes like
    # dce17be300855e07 instead of podIds 462/463/478).
    voted_pod_ids="[]"
    if [ -f memory/topics/reppo.md ]; then
      voted_pod_ids=$(awk -F '|' -v dn="$datanet_id" '
        /^## Votes cast/ { invotes=1; next }
        /^## / { invotes=0 }
        invotes && /^\| [0-9]{4}-[0-9]{2}-[0-9]{2} +\|/ {
          dnet=$3; pod=$4; status=$6
          gsub(/^ +| +$/, "", dnet); gsub(/^ +| +$/, "", pod); gsub(/^ +| +$/, "", status)
          if (dnet == dn && index(status, "success") > 0) print pod
        }' memory/topics/reppo.md | sort -u | jq -R . | jq -s . 2>/dev/null || echo "[]")
    fi
    # Add THIS wallet's own pods (owner-scope, no --all) — the contract
    # reverts on any self-vote attempt regardless of direction. Without
    # this, trading-agent occasionally selects its own prior-day mint as
    # a LIKE candidate (rubric-aligned HL perp dataset) and the vote
    # fails CANNOT_VOTE_FOR_OWN_POD (ISS-016, surfaced 2026-05-31 on the
    # 11th-mint pod 462). Requires REPPO_PRIVATE_KEY in prefetch env.
    own_pod_ids="[]"
    if [ -n "${REPPO_PRIVATE_KEY:-}" ]; then
      if REPPO_NETWORK=mainnet reppo list pods --datanet "$datanet_id" --json \
           > "$CACHE_DIR/own-pods-$name.json" 2>/dev/null; then
        own_pod_ids=$(jq '[.pods[]?.podId]' "$CACHE_DIR/own-pods-$name.json" 2>/dev/null || echo "[]")
      else
        error_marker "$CACHE_DIR/own-pods-$name.json" "list own pods $datanet_id failed"
      fi
    fi
    jq -n --arg epoch "$current_epoch" --argjson voted "$voted_pod_ids" --argjson own "$own_pod_ids" \
      '{current_epoch: (if $epoch == "" then null else $epoch end),
        voted_pod_ids: (($voted + $own) | unique)}' \
      > "$CACHE_DIR/vote-filter-$name.json"
  done
fi

echo "reppo-prefetch: done"
