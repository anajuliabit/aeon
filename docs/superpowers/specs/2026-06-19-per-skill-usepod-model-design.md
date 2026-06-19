# Per-skill usepod model — design

**Date:** 2026-06-19
**Status:** Approved (design); implementation pending
**Author:** Ana (with Claude Code)
**Repo:** aeon

## Problem

Since the fleet moved to the usepod gateway, every skill runs the default
`deepseek-v3.2` model (the helper hard-defaults `GATEWAY_MODEL="${USEPOD_MODEL:-deepseek-v3.2}"`
and ignores the per-skill `MODEL` aeon.yml resolves). deepseek-v3.2 is slow: heavy,
data-fetching, multi-turn skills run long enough to hit usepod's Cloudflare **120s
origin timeout (HTTP 524)**. Confirmed: `market-context-refresh` ran 33 turns / ~28 min
and died on a 524.

The per-skill `model:` field can't help here — it holds `claude-*` ids (used by the
direct/bankr fallbacks), which usepod does not serve.

## Decision

Add a per-skill **`usepod_model:`** override and route heavy skills to a faster usepod
model. Settled during brainstorming:

1. **New `usepod_model:` field** (not reuse of `model:`) — keeps the claude-* namespace
   intact for direct/bankr fallback; no clash.
2. **Apply to all known-heavy skills** (the enabled data/multi-turn ones), not just the
   one confirmed failure.
3. **Use `llama-4`** as the faster id (mid-size: faster than deepseek-v3.2/qwen-397b,
   stronger than mistral-small). The exact slug is **unverified** (catalog token-gated)
   — flagged below.

## Design

### 1. Mechanism (aeon.yml only; gateway helper unchanged)

The helper already honors `USEPOD_MODEL`. aeon.yml resolves a per-skill `usepod_model:`
and exports `USEPOD_MODEL` before sourcing the helper.

**Required fix to the existing `SKILL_MODEL` extraction (regex collision).** The current
line (aeon.yml ~228) is:
```bash
          SKILL_MODEL=$(grep "^  ${SKILL_NAME}:" aeon.yml | sed -n 's/.*model: *"\([^"]*\)".*/\1/p')
```
`.*model:` is greedy, so on a line that has BOTH `model: "..."` and `usepod_model: "..."`
it matches the LAST occurrence (`usepod_model:`) and wrongly captures the usepod id as the
claude model (breaking direct/bankr for that skill). Change it to require a delimiter
before `model:` so `usepod_model:` (preceded by `_`) can't match:
```bash
          SKILL_MODEL=$(grep "^  ${SKILL_NAME}:" aeon.yml | sed -n 's/.*[ ,{]model: *"\([^"]*\)".*/\1/p')
```

Then add, immediately before `. scripts/anthropic-gateway.sh || exit 1`:

```bash
          # Per-skill usepod model override (heavy skills run a faster model to avoid
          # usepod's 120s origin timeout). Only affects the usepod gateway; direct/bankr
          # still use the per-skill `model:` (claude-*) above. The `usepod_model:` token
          # is distinct from `model:` so the SKILL_MODEL regex above won't capture it.
          SKILL_USEPOD_MODEL=$(grep "^  ${SKILL_NAME}:" aeon.yml | sed -n 's/.*usepod_model: *"\([^"]*\)".*/\1/p')
          [ -n "$SKILL_USEPOD_MODEL" ] && export USEPOD_MODEL="$SKILL_USEPOD_MODEL"
```

**Precedence (usepod gateway):** per-skill `usepod_model:` → workflow `USEPOD_MODEL`
var → helper default `deepseek-v3.2`. For direct/bankr/virtuals this changes nothing
(`USEPOD_MODEL` is unused there).

### 2. Config — `usepod_model: "llama-4"` on the heavy set

Add `usepod_model: "llama-4"` to these enabled, data-heavy, multi-turn skills (extend
each existing entry; `market-context-refresh` already carries `model: "claude-sonnet-4-6"`,
so it gets both fields):

- `market-context-refresh` (confirmed 524)
- `defi-overview`
- `defi-monitor`
- `token-movers`
- `token-pick`
- `on-chain-monitor`
- `narrative-tracker` (was stuck)
- `aixbt-pulse`

All other skills stay on the `deepseek-v3.2` default (unchanged).

### 3. Testing (`scripts/advisor/selftest.sh`, offline)

Exercise the resolution chain end-to-end against a synthetic config:

- Write a temp `aeon.yml` with `someskill: { enabled: true, usepod_model: "llama-4" }`
  and `plainskill: { enabled: true }`. Run the extraction snippet for each `SKILL_NAME`,
  export `USEPOD_MODEL` if found, then source the real `anthropic-gateway.sh` (GATEWAY=usepod,
  USEPOD_TOKEN set) and assert `GATEWAY_MODEL`:
  - `someskill` → `GATEWAY_MODEL=llama-4`
  - `plainskill` (no field) → `GATEWAY_MODEL=deepseek-v3.2`
  - `plainskill` with a workflow `USEPOD_MODEL=qwen-3.5` env → `GATEWAY_MODEL=qwen-3.5`
    (per-skill absent, var wins over default)
- The extraction regex must NOT match a skill whose `model:` (not `usepod_model:`) is set
  — assert a skill with only `model: "claude-sonnet-4-6"` yields empty `SKILL_USEPOD_MODEL`.
- **Regex-collision (both fields):** for a line with BOTH `model: "claude-sonnet-4-6"` and
  `usepod_model: "llama-4"`, the fixed `SKILL_MODEL` regex (`s/.*[ ,{]model: ...`) yields
  `claude-sonnet-4-6` (NOT `llama-4`), and the `SKILL_USEPOD_MODEL` regex yields `llama-4`.
  This guards the greedy-match bug the new field introduces.

### 4. Boundaries / rollback

- Only `aeon.yml` (workflow extraction + config values) and `scripts/advisor/selftest.sh`
  change. The gateway helper, messages.yml, and advisor are untouched.
- **Rollback / per-skill opt-out:** delete a skill's `usepod_model:` line → it reverts to
  the `deepseek-v3.2` default. No code change needed.
- No automatic fallback if the usepod model id is wrong — the `claude` CLI errors and the
  skill fails (then its existing Virtuals-shim/text fallbacks run, as today).

## Out of scope

- Verifying the live usepod catalog (token-gated).
- messages.yml chat / advisor (single model each; not per-skill).
- Changing the default model for non-heavy skills.

## Open assumption (verify before trusting the full set)

`llama-4` is a best-effort slug from usepod's published lineup. If usepod rejects it, the
heavy skills will error (no auto-fallback to deepseek). **Recommended rollout:** after
wiring, dry-run ONE skill first — `gh workflow run aeon.yml -f skill=market-context-refresh`
— confirm it completes on `llama-4` (log: `model=llama-4`, no 4xx) BEFORE relying on the
rest. If the slug is wrong, fix the value once (or remove the lines to fall back to
deepseek-v3.2).
