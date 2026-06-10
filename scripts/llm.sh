#!/usr/bin/env bash
# scripts/llm.sh — call Virtuals free inference (OpenAI-compatible, Kimi K2).
#
# Usage:
#   echo "your prompt" | ./scripts/llm.sh
#   ./scripts/llm.sh "your prompt"
#
# Reads VIRTUALS_API_KEY from env. Prints the completion text to stdout.
# Exits non-zero (with a message on stderr) on any failure, so callers can
# detect and handle it.
#
# Override defaults via env:
#   VIRTUALS_MODEL    (default claude-opus-4-8; see GET /v1/models for options)
#   VIRTUALS_ENDPOINT (default https://compute.virtuals.io/v1/chat/completions)
#
# Sandbox note: this calls curl with VIRTUALS_API_KEY in the header, so it must
# run OUTSIDE the Claude sandbox (i.e. from a workflow step with full env, like
# the messages.yml fallback). Calling it from inside a skill would hit the
# sandbox's env-var-in-header block — use the prefetch pattern there instead.
set -euo pipefail

MODEL="${VIRTUALS_MODEL:-claude-opus-4-8}"
ENDPOINT="${VIRTUALS_ENDPOINT:-https://compute.virtuals.io/v1/chat/completions}"

if [ -z "${VIRTUALS_API_KEY:-}" ]; then
  echo "llm.sh: VIRTUALS_API_KEY not set" >&2
  exit 1
fi

# Prompt from $1 or stdin.
if [ -n "${1:-}" ]; then
  PROMPT="$1"
else
  PROMPT="$(cat)"
fi
if [ -z "${PROMPT//[[:space:]]/}" ]; then
  echo "llm.sh: empty prompt" >&2
  exit 1
fi

# Build the request body with jq so the prompt is safely JSON-encoded.
BODY=$(jq -n --arg model "$MODEL" --arg content "$PROMPT" \
  '{model: $model, messages: [{role: "user", content: $content}]}')

# Up to 3 attempts with backoff: the Virtuals gateway intermittently 504s on
# long completions; a transient gateway error must not kill a whole skill run.
ATTEMPTS="${LLM_ATTEMPTS:-3}"
attempt=1
while :; do
  RESP=$(curl -sS --max-time 180 -X POST "$ENDPOINT" \
    -H "Authorization: Bearer $VIRTUALS_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$BODY") || RESP=""

  if [ -n "$RESP" ]; then
    # Surface API-level errors. Handles both OpenAI-style {"error":{"message":...}}
    # and Virtuals-style {"message":...,"error":"...","statusCode":N}.
    ERR=$(printf '%s' "$RESP" | jq -r '.error.message? // .message? // empty' 2>/dev/null || true)
    CONTENT=$(printf '%s' "$RESP" | jq -r '.choices[0].message.content // empty' 2>/dev/null || true)
    if [ -z "$ERR" ] && [ -n "$CONTENT" ]; then
      printf '%s\n' "$CONTENT"
      exit 0
    fi
    # Retry only transient shapes: gateway error pages (5xx text) and
    # rate/overload API errors; real 4xx API errors fail fast.
    if [ -n "$ERR" ] && ! printf '%s' "$ERR" | grep -qiE 'timeout|overload|rate|too many|unavailable|gateway|5[0-9][0-9]'; then
      echo "llm.sh: API error: $ERR" >&2
      exit 1
    fi
  fi

  if [ "$attempt" -ge "$ATTEMPTS" ]; then
    echo "llm.sh: failed after $ATTEMPTS attempts: $(printf '%s' "${RESP:-<no response>}" | head -c 300)" >&2
    exit 1
  fi
  sleep $(( attempt * 15 ))
  attempt=$(( attempt + 1 ))
done
