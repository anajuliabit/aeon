#!/usr/bin/env bash
# scripts/llm-usepod.sh — call usepod.ai drop-in inference (OpenAI-compatible).
#
# Same contract as scripts/llm.sh: prompt on stdin (or $1), completion on stdout,
# non-zero exit + stderr message on failure.
#
# Auth: usepod's token lives in the URL PATH, not a header. USEPOD_TOKEN is the
# drop-in token from POST https://api.usepod.ai/register (prepaid USDC balance).
# Model: USEPOD_MODEL (default deepseek-v3.2). Endpoint base: USEPOD_BASE.
#
# Fallback: if usepod is unconfigured or every attempt fails AND VIRTUALS_API_KEY
# is set, retries the same prompt through scripts/llm.sh (Virtuals), mirroring
# llm-claude.sh, so an outage degrades instead of producing a gap.
#
# NO_VIRTUALS_FALLBACK=1 disables that Virtuals fallback: on any failure the
# script returns non-zero WITHOUT retrying through Virtuals. The PM committee sets
# this so a member's output stays attributable to exactly one usepod model
# (a silent Virtuals fallback would poison per-model attribution).
#
# Cost control: USEPOD_MAX_PRICE_INPUT / USEPOD_MAX_PRICE_OUTPUT (if set) become
# X-Pod-Max-Price-Input / X-Pod-Max-Price-Output request headers — usepod is a
# marketplace with per-operator pricing plus a centralized-router fallback, so
# these ceilings cap spend (and the fallback risk) on committee calls.
# USEPOD_MAX_TIME overrides the per-request curl timeout (default 180s).
#
# Security: the token is in the URL, so ALL emitted text is piped through redact()
# before reaching stderr. Never enable `set -x` here (it would print the URL).
set -uo pipefail

MODEL="${USEPOD_MODEL:-deepseek-v3.2}"
PROXY_BASE="${USEPOD_BASE:-https://api.usepod.ai/proxy}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Replace the token path segment (proxy/<token>) with <redacted> in any text.
# Assumes the `proxy/` path segment from the default USEPOD_BASE; an override
# with a different pre-token segment would need this pattern updated to match.
redact() {
  sed 's#\(proxy/\)[^/]*#\1<redacted>#g'
}

# Prompt from $1 or stdin.
if [ -n "${1:-}" ]; then
  PROMPT="$1"
else
  PROMPT="$(cat)"
fi
if [ -z "${PROMPT//[[:space:]]/}" ]; then
  echo "llm-usepod.sh: empty prompt" >&2
  exit 1
fi

fallback() {
  if [ "${NO_VIRTUALS_FALLBACK:-0}" = "1" ]; then
    echo "llm-usepod.sh: NO_VIRTUALS_FALLBACK set — not falling back to Virtuals" >&2
    exit 1
  fi
  if [ -n "${VIRTUALS_API_KEY:-}" ] && [ -x "$ROOT/scripts/llm.sh" ]; then
    echo "llm-usepod.sh: falling back to Virtuals (llm.sh)" >&2
    printf '%s' "$PROMPT" | "$ROOT/scripts/llm.sh"
    exit $?
  fi
  exit 1
}

if [ -z "${USEPOD_TOKEN:-}" ]; then
  echo "llm-usepod.sh: USEPOD_TOKEN not set" >&2
  fallback
fi

ENDPOINT="$PROXY_BASE/$USEPOD_TOKEN/v1/chat/completions"
BODY=$(jq -n --arg model "$MODEL" --arg content "$PROMPT" \
  '{model: $model, messages: [{role: "user", content: $content}]}')

MAXTIME="${USEPOD_MAX_TIME:-180}"

# Optional per-operator price ceilings (marketplace cost guard). Built as an array
# so an unset ceiling adds no header. The `[@]+...` guard keeps this safe under
# `set -u` with an empty array (bash 3.2 on macOS included).
PRICE_HEADERS=()
[ -n "${USEPOD_MAX_PRICE_INPUT:-}" ]  && PRICE_HEADERS+=(-H "X-Pod-Max-Price-Input: ${USEPOD_MAX_PRICE_INPUT}")
[ -n "${USEPOD_MAX_PRICE_OUTPUT:-}" ] && PRICE_HEADERS+=(-H "X-Pod-Max-Price-Output: ${USEPOD_MAX_PRICE_OUTPUT}")

# Up to 3 attempts with backoff; transient gateway errors must not kill a run.
ATTEMPTS="${LLM_ATTEMPTS:-3}"
attempt=1
while :; do
  RESP=$(curl -sS --max-time "$MAXTIME" -X POST "$ENDPOINT" \
    -H "Content-Type: application/json" \
    ${PRICE_HEADERS[@]+"${PRICE_HEADERS[@]}"} \
    -d "$BODY" 2> >(redact >&2)) || RESP=""

  if [ -n "$RESP" ]; then
    ERR=$(printf '%s' "$RESP" | jq -r '.error.message? // .message? // empty' 2>/dev/null || true)
    CONTENT=$(printf '%s' "$RESP" | jq -r '.choices[0].message.content // empty' 2>/dev/null || true)
    if [ -z "$ERR" ] && [ -n "$CONTENT" ]; then
      # CONTENT is model output; the token never enters the prompt, so stdout
      # carries no secret and needs no redaction.
      printf '%s\n' "$CONTENT"
      exit 0
    fi
    # Fail fast on real 4xx (auth, insufficient balance); retry only transient shapes.
    if [ -n "$ERR" ] && ! printf '%s' "$ERR" | grep -qiE 'timeout|overload|rate|too many|unavailable|gateway|5[0-9][0-9]'; then
      printf '%s' "llm-usepod.sh: API error: $ERR" | redact >&2; echo >&2
      fallback
    fi
  fi

  if [ "$attempt" -ge "$ATTEMPTS" ]; then
    printf '%s' "llm-usepod.sh: failed after $ATTEMPTS attempts: $(printf '%s' "${RESP:-<no response>}" | head -c 300)" | redact >&2; echo >&2
    fallback
  fi
  sleep $(( attempt * 15 ))
  attempt=$(( attempt + 1 ))
done
