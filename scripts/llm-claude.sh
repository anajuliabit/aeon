#!/usr/bin/env bash
# scripts/llm-claude.sh — call Claude Code CLI headless (subscription auth).
#
# Same contract as scripts/llm.sh: prompt on stdin (or $1), completion on stdout,
# non-zero exit + stderr message on failure.
#
# Auth: CLAUDE_CODE_OAUTH_TOKEN (Claude subscription) or ANTHROPIC_API_KEY in env.
# Model: CLAUDE_MODEL (default claude-fable-5).
#
# Fallback: if the claude CLI is missing or the call fails, retry the same prompt
# through usepod (llm-usepod.sh, funded) when USEPOD_TOKEN is set, else Virtuals
# (llm.sh). usepod-first because Virtuals tends to run dry; a CLI/limit outage
# then degrades to a working backend instead of producing a gap.
#
# Sandbox note: runs OUTSIDE the Claude sandbox (workflow step with full env),
# same as llm.sh — env-var auth works directly here.
set -uo pipefail

MODEL="${CLAUDE_MODEL:-claude-fable-5}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Prompt from $1 or stdin.
if [ -n "${1:-}" ]; then
  PROMPT="$1"
else
  PROMPT="$(cat)"
fi
if [ -z "${PROMPT//[[:space:]]/}" ]; then
  echo "llm-claude.sh: empty prompt" >&2
  exit 1
fi

fallback() {
  # Prefer usepod (funded, llm-usepod.sh cascades to Virtuals internally) over a
  # direct Virtuals call. Virtuals has historically run out of credits, so a
  # Claude outage that fell straight to Virtuals would just fail; usepod first
  # keeps the chain alive: Claude -> usepod -> (usepod's own Virtuals fallback).
  if [ -n "${USEPOD_TOKEN:-}" ] && [ -x "$ROOT/scripts/llm-usepod.sh" ]; then
    echo "llm-claude.sh: falling back to usepod (llm-usepod.sh)" >&2
    printf '%s' "$PROMPT" | "$ROOT/scripts/llm-usepod.sh"
    exit $?
  fi
  if [ -n "${VIRTUALS_API_KEY:-}" ] && [ -x "$ROOT/scripts/llm.sh" ]; then
    echo "llm-claude.sh: falling back to Virtuals (llm.sh)" >&2
    printf '%s' "$PROMPT" | "$ROOT/scripts/llm.sh"
    exit $?
  fi
  exit 1
}

if ! command -v claude >/dev/null 2>&1; then
  echo "llm-claude.sh: claude CLI not found" >&2
  fallback
fi

# Pure single-shot inference: no tools, one turn.
OUT="$(printf '%s' "$PROMPT" | claude -p --model "$MODEL" --max-turns 1 \
  --disallowedTools "Bash,Read,Write,Edit,Glob,Grep,WebFetch,WebSearch" 2>/dev/null)" || {
  echo "llm-claude.sh: claude -p failed (model=$MODEL)" >&2
  fallback
}

if [ -z "${OUT//[[:space:]]/}" ]; then
  echo "llm-claude.sh: empty completion (model=$MODEL)" >&2
  fallback
fi

printf '%s\n' "$OUT"
