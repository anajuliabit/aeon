#!/usr/bin/env bash
# scripts/research-prefetch.sh — best-effort live research digest via xAI Grok.
#
# Contract: query on $1 or stdin -> compact findings digest on stdout; empty output
# + non-zero exit on ANY failure, so callers can `|| true` and never block a reply.
#
# Uses the xAI Responses API with live x_search + web_search tools (same provider as
# .xai-buzz.sh). Auth: XAI_API_KEY (bearer header — not in the URL, no redaction
# needed). Model: XAI_RESEARCH_MODEL (default grok-4-1-fast). Never `set -x`.
set -uo pipefail

[ -n "${XAI_API_KEY:-}" ] || { echo "research-prefetch.sh: XAI_API_KEY not set" >&2; exit 1; }

if [ -n "${1:-}" ]; then QUERY="$1"; else QUERY="$(cat)"; fi
if [ -z "${QUERY//[[:space:]]/}" ]; then echo "research-prefetch.sh: empty query" >&2; exit 1; fi

MODEL="${XAI_RESEARCH_MODEL:-grok-4-1-fast}"
INSTR="Research the operator's question using live X and web search. Return the 5-8 most decision-relevant findings as terse bullets, each with a source link and a date. Surface non-obvious / under-noticed angles. If you find nothing solid, say so.

Question: $QUERY"

# Try with x_search + web_search; if the API rejects web_search as a tool type,
# retry once with x_search only (don't fail the prefetch over an unsupported tool).
call_xai() { # $1 = tools JSON
  local tools="$1" body
  body=$(jq -n --arg model "$MODEL" --arg content "$INSTR" --argjson tools "$tools" \
    '{model:$model, input:[{role:"user", content:$content}], tools:$tools}')
  curl -sS --connect-timeout 10 --max-time 60 -X POST "https://api.x.ai/v1/responses" \
    -H "Authorization: Bearer $XAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$body"
}

extract() { # reads RESP on stdin -> findings text or empty
  # join("") yields a truthy "" so a plain `//` chain never reaches the
  # fallbacks; only fall back when the primary array is genuinely empty.
  jq -r '
    ([ .output[]?.content[]? | select(has("text")) | .text ]
       | map(select(. != null and . != ""))) as $t
    | if ($t | length) > 0 then ($t | join("\n"))
      else (.output_text // .choices[0].message.content // empty) end' 2>/dev/null
}

RESP="$(call_xai '[{"type":"x_search"},{"type":"web_search"}]')" || { echo "research-prefetch.sh: request failed" >&2; exit 1; }
ERR=$(printf '%s' "$RESP" | jq -r '.error.message? // (.error|strings) // empty' 2>/dev/null || true)
if printf '%s' "$ERR" | grep -qiE 'web_search|unsupported.*tool|tool.*(unsupported|not (supported|allowed))'; then
  echo "research-prefetch.sh: retrying x_search only ($ERR)" >&2
  RESP="$(call_xai '[{"type":"x_search"}]')" || { echo "research-prefetch.sh: request failed" >&2; exit 1; }
  ERR=$(printf '%s' "$RESP" | jq -r '.error.message? // (.error|strings) // empty' 2>/dev/null || true)
fi
if [ -n "$ERR" ]; then echo "research-prefetch.sh: API error: $ERR" >&2; exit 1; fi

OUT="$(printf '%s' "$RESP" | extract)"
if [ -z "${OUT//[[:space:]]/}" ]; then echo "research-prefetch.sh: no text in response" >&2; exit 1; fi
printf '%s\n' "$OUT"
