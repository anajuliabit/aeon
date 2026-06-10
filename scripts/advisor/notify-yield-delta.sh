#!/usr/bin/env bash
# scripts/advisor/notify-yield-delta.sh — stable-yield opportunity alert.
#
# Compares the best sustainable (apyBase) USD-stable rate among deep-TVL pools
# against a proxy for our current venue's rate (best Morpho USDC pool on Base —
# where the deployed stables sit), and pings Telegram when the spread exceeds
# DELTA_MIN_PP percentage points. Best-effort venue matching: the proxy is
# approximate by design and the message says so. Reads the prefetch cache
# (yields.json from prefetch-data.sh) — run AFTER prefetch.
#
# Deterministic — no LLM. Runs OUTSIDE the Claude sandbox.
set -uo pipefail

D=.investiments-cache/advisor
DELTA_MIN_PP="${DELTA_MIN_PP:-1.5}"
MIN_TVL="${MIN_TVL:-20000000}" # $20m floor — no incentive-farm dust pools

if [ ! -f "$D/yields.json" ]; then
  echo "notify-yield-delta: no yields.json (run prefetch first) — skipping"; exit 0
fi
if [ -z "${TELEGRAM_BOT_TOKEN:-}" ] || [ -z "${TELEGRAM_CHAT_ID:-}" ]; then
  echo "notify-yield-delta: telegram not configured — skipping"; exit 0
fi

# Our venue proxy: best Morpho USDC pool on Base (where the deployed stables live).
OURS=$(jq -r '
  [.data[]? | select(.stablecoin == true and (.symbol // "" | ascii_downcase | test("usdc"))
    and (.project // "" | ascii_downcase | test("morpho")) and (.chain // "" | ascii_downcase == "base")
    and ((.tvlUsd // 0) >= 1000000))]
  | max_by(.apyBase // 0) | select(. != null) | {project, symbol, apyBase}' "$D/yields.json" 2>/dev/null || true)
OUR_APY=$(printf '%s' "$OURS" | jq -r '.apyBase // empty' 2>/dev/null || true)
if [ -z "$OUR_APY" ]; then
  echo "notify-yield-delta: could not locate our venue proxy (morpho/usdc/base) — skipping"; exit 0
fi

# Candidates restricted to battle-tested lending/savings protocols: buffer
# capital must never be benchmarked against managed "yield vaults" (opaque
# strategies, anon teams) — that comparison class is wrong by design.
LENDING_PROJECTS='["aave-v3","aave-v2","morpho","morpho-blue","morpho-v1","compound-v3","spark","sparklend","maple","fluid-lending","euler-v2"]'
BEST=$(jq -r --argjson mintvl "$MIN_TVL" --argjson allow "$LENDING_PROJECTS" '
  [.data[]? | select(.stablecoin == true and ((.tvlUsd // 0) >= $mintvl) and ((.apyBase // 0) > 0)
    and ((.project // "" | ascii_downcase) as $p | $allow | any(. == $p)))]
  | max_by(.apyBase) | select(. != null) | {project, symbol, chain, tvlUsd, apyBase}' "$D/yields.json" 2>/dev/null || true)
BEST_APY=$(printf '%s' "$BEST" | jq -r '.apyBase // empty' 2>/dev/null || true)
if [ -z "$BEST_APY" ]; then
  echo "notify-yield-delta: no qualifying pools"; exit 0
fi

DELTA=$(python3 -c "print($BEST_APY - $OUR_APY)")
echo "notify-yield-delta: ours $(printf '%.2f' "$OUR_APY")% vs best $(printf '%.2f' "$BEST_APY")% (delta $(printf '%.2f' "$DELTA")pp)"
if python3 -c "exit(0 if $DELTA >= $DELTA_MIN_PP else 1)"; then
  BEST_DESC=$(printf '%s' "$BEST" | jq -r '"\(.project) \(.symbol) on \(.chain) (\(.apyBase * 100 | floor / 100)% base, TVL $\(.tvlUsd / 1000000 | floor)m)"')
  MSG=$(printf '💧 Yield gap: best deep-TVL stable rate is %s vs ~%.1f%% at the current Morpho/Base venue (>=%.1fpp better). Sustainable apyBase only, established lending venues, TVL >= $%dm. Venue proxy is approximate — verify before moving. Not financial advice.' \
    "$BEST_DESC" "$OUR_APY" "$DELTA_MIN_PP" "$(python3 -c "print(int($MIN_TVL/1000000))")")
  curl -fsS --max-time 20 "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
    --data-urlencode "chat_id=${TELEGRAM_CHAT_ID}" \
    --data-urlencode "text=$MSG" >/dev/null 2>&1 \
    && echo "notify-yield-delta: sent" \
    || echo "::warning::notify-yield-delta: telegram send failed"
else
  echo "notify-yield-delta: spread below threshold"
fi
