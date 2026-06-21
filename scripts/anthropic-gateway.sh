#!/usr/bin/env bash
# scripts/anthropic-gateway.sh — resolve the LLM gateway for the Claude Code CLI.
# SOURCE this (`. scripts/anthropic-gateway.sh`); it EXPORTS GATEWAY,
# ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, and GATEWAY_MODEL into the caller.
#
# Provider precedence: $GATEWAY env override > aeon.yml `gateway.provider` > direct.
# usepod is Anthropic-compatible (`/v1/messages`) with the token IN THE URL PATH, so
# the token never goes in a header — and the notice redacts it (GitHub also masks the
# USEPOD_TOKEN secret).
#
# SOURCING CONTRACT (load-bearing): on a misconfigured provider this returns non-zero,
# but `set -e` does NOT abort a caller on a sourced script's return. Callers MUST
# source as:  . scripts/anthropic-gateway.sh || exit 1
# Relying on `set -e` alone will let the step continue with a malformed base URL.
#
# SECURITY: the usepod token is in the exported ANTHROPIC_BASE_URL. Never `set -x`
# around this, and never `echo "$ANTHROPIC_BASE_URL"` / dump `env` — that leaks it.
GATEWAY="${GATEWAY:-$(grep -A1 '^gateway:' aeon.yml 2>/dev/null | grep 'provider:' | sed 's/.*provider: *//' | tr -d ' "'"'" )}"
GATEWAY="${GATEWAY:-direct}"
GATEWAY_MODEL="${MODEL:-}"   # default: caller's model unchanged; usepod overrides below

case "$GATEWAY" in
  usepod)
    if [ -z "${USEPOD_TOKEN:-}" ]; then
      echo "::error::gateway.provider=usepod but USEPOD_TOKEN is not set" >&2
      return 1 2>/dev/null || exit 1
    fi
    export ANTHROPIC_BASE_URL="https://api.usepod.ai/proxy/$USEPOD_TOKEN"
    export ANTHROPIC_AUTH_TOKEN="unused"   # token lives in the URL path; CLI still needs a value
    unset ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN
    GATEWAY_MODEL="${USEPOD_MODEL:-deepseek-v3.2}"   # usepod serves open-weight ids, not claude-*
    echo "::notice::Routing through usepod (https://api.usepod.ai/proxy/<redacted>, model=$GATEWAY_MODEL)"
    ;;
  bankr)
    if [ -z "${BANKR_LLM_KEY:-}" ]; then
      echo "::error::gateway.provider=bankr but BANKR_LLM_KEY is not set" >&2
      return 1 2>/dev/null || exit 1
    fi
    export ANTHROPIC_BASE_URL="https://llm.bankr.bot"
    export ANTHROPIC_AUTH_TOKEN="$BANKR_LLM_KEY"
    unset ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN
    echo "::notice::Routing through Bankr Gateway (https://llm.bankr.bot)"
    ;;
  virtuals)
    if [ -z "${VIRTUALS_API_KEY:-}" ]; then
      echo "::error::gateway.provider=virtuals but VIRTUALS_API_KEY is not set" >&2
      return 1 2>/dev/null || exit 1
    fi
    export ANTHROPIC_BASE_URL="https://compute.virtuals.io"
    export ANTHROPIC_AUTH_TOKEN="$VIRTUALS_API_KEY"
    unset ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN
    echo "::notice::Routing through Virtuals Gateway (https://compute.virtuals.io)"
    ;;
  *)
    echo "::notice::Using direct Anthropic API"
    ;;
esac
export GATEWAY GATEWAY_MODEL
