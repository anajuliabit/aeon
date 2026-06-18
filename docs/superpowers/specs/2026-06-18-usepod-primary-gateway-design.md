# usepod as the primary LLM gateway — design

**Date:** 2026-06-18
**Status:** Approved (design); implementation pending
**Author:** Ana (with Claude Code)
**Repo:** aeon

## Problem

aeon's scheduled skill fleet (`aeon.yml`) and the chat handler (`messages.yml`) run
skills as agentic Claude Code CLI invocations (`claude -p` with tools/file access).
Both route the model through `ANTHROPIC_BASE_URL`. Today every scheduled skill fails:

```
Using direct Anthropic API → Claude rate-limited (429, weekly cap, resets Jun 22)
→ retry via Virtuals → 402 Insufficient credits → text-only fallback → exit 1
```

cron-state shows `consecutive_failures` 11–21 across the fleet (heartbeat,
fleet-control, reflect, goal-tracker, market-context-refresh, …). The advisor was
already moved to usepod, but the general fleet has no usepod path — its gateway only
knows `direct`/`bankr`/`virtuals`.

usepod is funded (`USEPOD_TOKEN` secret set) and — critically — exposes an
**Anthropic-compatible** endpoint: `ANTHROPIC_BASE_URL=https://api.usepod.ai/proxy/<token> claude`
works directly (`/v1/messages` supported). So usepod can be a first-class gateway for
the Claude Code CLI — agentic, with tools — not just a plain-completion fallback.

## Decision

Make **usepod the primary gateway for every claude-CLI surface** (operator's call:
"use pod for everything, not only advisor"). Open-weight models (default
`deepseek-v3.2`) replace Claude Opus as the default; Claude/Virtuals remain as
fallbacks where they already exist.

Settled during brainstorming:
1. **usepod primary, all claude-CLI workflows** — aeon.yml skill fleet + messages.yml
   chat primary. (Advisor + weekly-conviction use the backend-script path with
   `ADVISOR_LLM=usepod`, already usepod-capable — out of scope here; weekly to verify.)
2. **Default model `deepseek-v3.2`**, overridable per-workflow via `USEPOD_MODEL`.
3. **Shared helper (DRY)** — extract gateway resolution into one sourced script,
   replacing aeon.yml's inline block and reused by messages.yml.
4. **Single config knob** — the helper reads `gateway.provider` from `aeon.yml`, so
   flipping it to `usepod` switches every surface at once.

## Design

### 1. New `scripts/anthropic-gateway.sh` (sourced, not executed)

Resolves the gateway and exports the env the `claude` CLI needs. Sourced
(`. scripts/anthropic-gateway.sh`) so its `export`s land in the caller's shell.

Inputs (env): `MODEL` (the workflow's resolved model), optional `GATEWAY` override,
and the provider tokens. Reads `gateway.provider` from `aeon.yml` when `GATEWAY` is
unset. Outputs (exported): `GATEWAY`, `ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`,
`GATEWAY_MODEL`. Prints one redacted `::notice::`.

```bash
# resolve provider: explicit env > aeon.yml config > direct
GATEWAY="${GATEWAY:-$(grep -A1 '^gateway:' aeon.yml 2>/dev/null | grep 'provider:' | sed 's/.*provider: *//' | tr -d ' "'"'" )}"
GATEWAY="${GATEWAY:-direct}"
GATEWAY_MODEL="${MODEL:-}"   # default: unchanged; usepod overrides below
case "$GATEWAY" in
  usepod)
    [ -n "${USEPOD_TOKEN:-}" ] || { echo "::error::gateway.provider=usepod but USEPOD_TOKEN not set"; return 1 2>/dev/null || exit 1; }
    export ANTHROPIC_BASE_URL="https://api.usepod.ai/proxy/$USEPOD_TOKEN"
    export ANTHROPIC_AUTH_TOKEN="unused"   # token is in the URL path; CLI still needs a value
    unset ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN
    GATEWAY_MODEL="${USEPOD_MODEL:-deepseek-v3.2}"   # usepod serves open-weight ids, not claude-*
    echo "::notice::Routing through usepod (https://api.usepod.ai/proxy/<redacted>, model=$GATEWAY_MODEL)" ;;
  bankr)
    [ -n "${BANKR_LLM_KEY:-}" ] || { echo "::error::gateway.provider=bankr but BANKR_LLM_KEY not set"; return 1 2>/dev/null || exit 1; }
    export ANTHROPIC_BASE_URL="https://llm.bankr.bot"; export ANTHROPIC_AUTH_TOKEN="$BANKR_LLM_KEY"
    unset ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN
    echo "::notice::Routing through Bankr Gateway (https://llm.bankr.bot)" ;;
  virtuals)
    [ -n "${VIRTUALS_API_KEY:-}" ] || { echo "::error::gateway.provider=virtuals but VIRTUALS_API_KEY not set"; return 1 2>/dev/null || exit 1; }
    export ANTHROPIC_BASE_URL="https://compute.virtuals.io"; export ANTHROPIC_AUTH_TOKEN="$VIRTUALS_API_KEY"
    unset ANTHROPIC_API_KEY CLAUDE_CODE_OAUTH_TOKEN
    echo "::notice::Routing through Virtuals Gateway (https://compute.virtuals.io)" ;;
  *)
    echo "::notice::Using direct Anthropic API" ;;
esac
export GATEWAY GATEWAY_MODEL
```

Token redaction is load-bearing (the usepod token sits in `ANTHROPIC_BASE_URL`): the
notice prints `<redacted>`, and GitHub masks `USEPOD_TOKEN` as a secret in all logs.
Never `set -x` around this. `bankr`/`virtuals`/`direct` reproduce today's behavior
exactly so nothing regresses.

### 2. `aeon.yml`

- Config: `gateway.provider: direct` → **`usepod`**.
- Replace the inline `GATEWAY=…` detection + `if bankr/elif virtuals/else` block
  (current ~lines 239–266) with `. scripts/anthropic-gateway.sh`.
- The skill `claude -p` call uses `--model "$GATEWAY_MODEL"` (was `$MODEL`).
- Add `USEPOD_TOKEN: ${{ secrets.USEPOD_TOKEN }}` and `USEPOD_MODEL: ${{ vars.USEPOD_MODEL }}`
  to the job env.
- The existing "Claude rate-limited → Virtuals LiteLLM shim" Layer-1 fallback stays as
  a deeper safety net (now rarely hit, since usepod is primary).

### 3. `messages.yml` (chat primary)

- Before the primary `claude -p`, `. scripts/anthropic-gateway.sh`; call with
  `--model "$GATEWAY_MODEL"`. Chat becomes **agentic on usepod** (real tools), strictly
  better than the text-only `llm-usepod.sh` fallback, which remains as deeper safety.
- Add `USEPOD_TOKEN`/`USEPOD_MODEL` to the chat job env if not already present (they
  were added for the fallback in a prior change — reuse).

### 4. Boundaries

- Only the claude-CLI gateway surfaces change: `scripts/anthropic-gateway.sh` (new),
  `aeon.yml` (config + gateway block + `--model`), `messages.yml` (primary routing).
- Advisor (`run.sh`) and weekly-conviction (`run-weekly.sh`) use the backend-script
  path (`llm-*.sh` via `ADVISOR_LLM=usepod`) — unchanged here. Verify weekly-conviction
  honors `ADVISOR_LLM`; if it doesn't, that's a separate small follow-up.
- `bankr`/`virtuals`/`direct` paths preserved for fallback/rollback (flip the config
  knob back to roll back instantly).

## Testing (`scripts/advisor/selftest.sh`, offline, no network)

Source the helper in a subshell with controlled env and assert the exports:

- `GATEWAY=usepod USEPOD_TOKEN=SECRET MODEL=claude-opus-4-7` → `ANTHROPIC_BASE_URL`
  equals `https://api.usepod.ai/proxy/SECRET`, `GATEWAY_MODEL=deepseek-v3.2`,
  `ANTHROPIC_AUTH_TOKEN=unused`.
- `GATEWAY=usepod USEPOD_TOKEN=SECRET USEPOD_MODEL=qwen-3.5` → `GATEWAY_MODEL=qwen-3.5`.
- **Redaction:** the captured `::notice::` for usepod contains `<redacted>` and does NOT
  contain `SECRET`.
- `GATEWAY=usepod` with `USEPOD_TOKEN` unset → returns non-zero / emits the `::error::`.
- `GATEWAY=direct MODEL=claude-opus-4-7` → no `ANTHROPIC_BASE_URL` set, `GATEWAY_MODEL=claude-opus-4-7`.
- `GATEWAY=bankr BANKR_LLM_KEY=k` → `ANTHROPIC_BASE_URL=https://llm.bankr.bot`;
  `GATEWAY=virtuals VIRTUALS_API_KEY=k` → `https://compute.virtuals.io` (no regression).
- Provider-from-config: with no `GATEWAY` env and a temp `aeon.yml` containing
  `gateway:\n  provider: usepod`, the helper resolves `GATEWAY=usepod`.

(The `claude -p` agentic runs themselves are exercised at workflow runtime, not in the
offline suite.)

## Out of scope

- Advisor/weekly backend-script path (already usepod via `ADVISOR_LLM`).
- Removing the Virtuals LiteLLM shim or Bankr support (kept for fallback/rollback).
- Per-skill model tiers (single `USEPOD_MODEL` default; per-workflow override via the
  var is available but no per-skill matrix).

## Open assumption (verify with a dry run before trusting the fleet)

usepod's `/v1/messages` Anthropic proxy must (a) accept `deepseek-v3.2` as the model
and (b) drive Claude Code's tool-use loop adequately. Open-weight models may have
weaker tool-calling than Opus. Confirm with one real skill run
(`gh workflow run aeon.yml` for a simple skill, or a manual dispatch) before relying on
the scheduled fleet; if tool-use is weak, bump `USEPOD_MODEL` to a stronger usepod id
or keep tool-light skills only on usepod.
