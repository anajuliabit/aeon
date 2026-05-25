#!/usr/bin/env bash
# Lock the agent's REPPO balance into veREPPO (voting power) for the swarm.
#
# One-time / occasional operator step — run LOCALLY with REPPO_PRIVATE_KEY
# exported. The chain's vote step uses veREPPO weight; without a lockup the
# agent may vote with zero power or hit insufficient-power errors.
#
# By default, locks the FULL REPPO balance of the agent's wallet for 30 days.
# Override with flags below.
#
# Usage:
#   REPPO_PRIVATE_KEY=0x... ./scripts/reppo-lock.sh
#   ./scripts/reppo-lock.sh --amount 100         # explicit amount instead of full balance
#   ./scripts/reppo-lock.sh --duration 5184000   # custom duration (default 2592000 = 30 days)
#   ./scripts/reppo-lock.sh --network 8453       # explicit chain id (default 8453 = Base)
#   ./scripts/reppo-lock.sh --dry-run            # eth_call simulation only, no on-chain write
set -euo pipefail

NETWORK="${REPPO_NETWORK_ID:-8453}"
DURATION="${REPPO_LOCK_DURATION:-2592000}"  # 30 days in seconds
AMOUNT=""
DRY_RUN=""

while [ $# -gt 0 ]; do
  case "$1" in
    --amount) AMOUNT="$2"; shift 2 ;;
    --duration) DURATION="$2"; shift 2 ;;
    --network) NETWORK="$2"; shift 2 ;;
    --dry-run) DRY_RUN="--dry-run"; shift ;;
    -h|--help)
      sed -n '2,15p' "$0"; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

if [ -z "${REPPO_PRIVATE_KEY:-}" ]; then
  echo "reppo-lock: REPPO_PRIVATE_KEY not set" >&2
  exit 1
fi

if ! command -v reppo >/dev/null 2>&1; then
  echo "reppo-lock: installing @reppo/cli..."
  npm i -g @reppo/cli >/dev/null 2>&1 || {
    echo "reppo-lock: @reppo/cli install failed" >&2
    exit 1
  }
fi

# Resolve the amount: explicit --amount, or auto-detect full REPPO balance.
if [ -z "$AMOUNT" ]; then
  echo "reppo-lock: querying REPPO balance on network $NETWORK..."
  BAL_JSON="$(reppo query balance --network "$NETWORK" --json 2>&1)" || {
    echo "reppo-lock: balance query failed:" >&2
    echo "$BAL_JSON" | head -c 500 >&2
    exit 1
  }

  # Try the JSON shapes the CLI is likely to use.
  AMOUNT="$(echo "$BAL_JSON" | jq -r '.reppo // .balances.reppo // .REPPO // .balance.reppo // ""' 2>/dev/null || true)"

  if [ -z "$AMOUNT" ] || [ "$AMOUNT" = "null" ]; then
    echo "reppo-lock: could not auto-detect REPPO balance in the CLI response." >&2
    echo "reppo-lock: raw response (truncated):" >&2
    echo "$BAL_JSON" | head -c 500 >&2
    echo "" >&2
    echo "reppo-lock: re-run with --amount <n> using the REPPO balance you see above." >&2
    exit 1
  fi

  # Keep just the leading numeric portion in case the CLI returns "12.345 REPPO".
  AMOUNT="$(echo "$AMOUNT" | grep -oE '^[0-9.]+' || true)"
fi

if [ -z "$AMOUNT" ] || [ "$AMOUNT" = "0" ]; then
  echo "reppo-lock: REPPO amount is 0 — nothing to lock."
  exit 0
fi

DAYS=$((DURATION / 86400))
echo "reppo-lock: locking $AMOUNT REPPO for $DURATION seconds (~${DAYS} days)${DRY_RUN:+ (dry-run)}..."

# Idempotency key bound to the day so a re-run on the same day is a no-op,
# but a new day (e.g. after the prior lockup matured) gets a fresh lock.
KEY="aeon-lock-$(date -u +%Y-%m-%d)"

reppo lock "$AMOUNT" \
  --duration "$DURATION" \
  --network "$NETWORK" \
  --idempotency-key "$KEY" \
  $DRY_RUN \
  --json
