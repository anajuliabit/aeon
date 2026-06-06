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
#   VIRTUALS_MODEL    (default moonshotai/kimi-k2-0905)
#   VIRTUALS_ENDPOINT (default https://compute.virtuals.io/v1/chat/completions)
#
# Sandbox note: this calls curl with VIRTUALS_API_KEY in the header, so it must
# run OUTSIDE the Claude sandbox (i.e. from a workflow step with full env, like
# the messages.yml fallback). Calling it from inside a skill would hit the
# sandbox's env-var-in-header block — use the prefetch pattern there instead.
set -euo pipefail

MODEL="${VIRTUALS_MODEL:-moonshotai/kimi-k2-0905}"
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

RESP=$(curl -sS --max-time 120 -X POST "$ENDPOINT" \
  -H "Authorization: Bearer $VIRTUALS_API_KEY" \
  -H "Content-Type: application/json" \
  -d "$BODY") || { echo "llm.sh: curl to $ENDPOINT failed" >&2; exit 1; }

# Surface API-level errors (OpenAI-style {"error": {"message": ...}}).
ERR=$(printf '%s' "$RESP" | jq -r '.error.message // empty' 2>/dev/null || true)
if [ -n "$ERR" ]; then
  echo "llm.sh: API error: $ERR" >&2
  exit 1
fi

# Extract the assistant message (OpenAI chat-completions shape).
CONTENT=$(printf '%s' "$RESP" | jq -r '.choices[0].message.content // empty' 2>/dev/null || true)
if [ -z "$CONTENT" ]; then
  echo "llm.sh: empty/invalid response: $(printf '%s' "$RESP" | head -c 300)" >&2
  exit 1
fi

printf '%s\n' "$CONTENT"
