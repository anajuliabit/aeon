# Add `usepod` LLM provider to the advisor — design

**Date:** 2026-06-17
**Status:** Approved (design); implementation pending
**Author:** Ana (with Claude Code)
**Repo:** aeon
**Branch:** stacks on `fix/advisor-llm-diagnostics` (PR #123)

## Problem

The investment-advisor pipeline (`scripts/advisor/run.sh`) calls an LLM through a
swappable backend: `llm-claude.sh` (Claude Code CLI, primary) with `llm.sh`
(Virtuals, fallback). Add [usepod.ai](https://usepod.ai/) as a third, **opt-in**
backend an operator can select without changing the default priority.

usepod is a decentralized, OpenAI-compatible inference marketplace (open-weight
models — Llama 4, Qwen 3.5, DeepSeek, Mistral, GLM — served by independent hosts via
TEE enclaves). The drop-in path is plain HTTP, no SDK required.

## Integration surface (verified against docs.usepod.ai)

- **OpenAI-compatible, drop-in.** Chat completions:
  `POST https://api.usepod.ai/proxy/<token>/v1/chat/completions`
- **Auth is a token in the URL PATH, not a bearer header.** The `Authorization`
  header / `api_key` is ignored. Token obtained once via
  `POST https://api.usepod.ai/register` (returns token + USDC deposit address;
  prepaid balance, each response carries an `X-Balance-Remaining` header).
- **Model ids are canonical, free-text.** Marketplace catalog is token-specific; no
  fixed list to hardcode. Default `deepseek-v3.2`; operator overrides via
  `USEPOD_MODEL`.
- **Drop-in prepaid-token path only.** The wallet-native x402 / Solana per-call
  settlement path (separate Solana key + signing client) is OUT OF SCOPE.

This is the same request shape as `llm.sh` (Virtuals), with two real differences:
the **token lives in the URL path** (not the header), and that URL **must be
redacted** wherever it can surface.

## Decisions (settled during brainstorming)

1. **Opt-in third backend.** Default selection (Claude-if-token-else-Virtuals) is
   unchanged. usepod is reached only when explicitly selected.
2. **Selection via `ADVISOR_LLM` env.** Values `usepod` | `claude` | `virtuals` |
   `auto` (default). `auto` preserves today's behavior exactly.
3. **usepod → Virtuals fallback.** When usepod is selected and a call fails,
   `llm-usepod.sh` falls back to `llm.sh` (Virtuals) if `VIRTUALS_API_KEY` is set —
   mirroring how `llm-claude.sh` falls back today. Keeps a run alive through a
   usepod outage.
4. **Default model `deepseek-v3.2`.** Strong reasoning + JSON adherence among
   open-weight models; fits the analyst/PM structured-output prompts. Override via
   `USEPOD_MODEL`.
5. **Secret-in-URL redaction is load-bearing.** The `/proxy/<token>/` segment is
   redacted before any text reaches stderr/logs.

## Design

### 1. New script `scripts/llm-usepod.sh`

Mirrors the existing backend contract exactly: prompt on `$1` or stdin → completion
on stdout; non-zero exit + stderr message on failure. Because the contract matches,
`run.sh`'s `complete()` calls it unchanged.

```bash
set -uo pipefail
MODEL="${USEPOD_MODEL:-deepseek-v3.2}"
PROXY_BASE="${USEPOD_BASE:-https://api.usepod.ai/proxy}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Redact the token path segment from any text we emit. Defense-in-depth on top of
# GitHub Actions secret masking.
redact() { sed 's#\(proxy/\)[^/]*#\1<redacted>#g'; }

fallback() {  # usepod down -> Virtuals, matching llm-claude.sh's degrade path
  if [ -n "${VIRTUALS_API_KEY:-}" ] && [ -x "$ROOT/scripts/llm.sh" ]; then
    echo "llm-usepod.sh: falling back to Virtuals (llm.sh)" >&2
    printf '%s' "$PROMPT" | "$ROOT/scripts/llm.sh"; exit $?
  fi
  exit 1
}

# Fail fast if unconfigured.
[ -n "${USEPOD_TOKEN:-}" ] || { echo "llm-usepod.sh: USEPOD_TOKEN not set" >&2; fallback; }

ENDPOINT="$PROXY_BASE/$USEPOD_TOKEN/v1/chat/completions"
BODY=$(jq -n --arg model "$MODEL" --arg content "$PROMPT" \
  '{model: $model, messages: [{role:"user", content:$content}]}')
```

Retry loop is the same 3-attempt backoff as `llm.sh`:
- Success: `.choices[0].message.content` non-empty and no `.error` → print, exit 0.
- 4xx API errors (401, insufficient balance) that are NOT transient → fail fast.
- Transient (`timeout|overload|rate|too many|unavailable|gateway|5xx`) → retry with
  `attempt*15`s backoff.
- After all attempts → emit a **redacted** failure summary to stderr, then
  `fallback`.
- Every diagnostic/error line is piped through `redact` before reaching stderr.
  Never use `set -x` (would print the unredacted URL).

### 2. Backend selection in `run.sh` (current lines 37–43)

Replace the two-way if with an explicit selector; `auto` keeps current behavior:

```bash
case "${ADVISOR_LLM:-auto}" in
  usepod)
    LLM="$ROOT/scripts/llm-usepod.sh"
    MODEL_LABEL="${USEPOD_MODEL:-deepseek-v3.2} (usepod)" ;;
  claude)
    LLM="$ROOT/scripts/llm-claude.sh"
    MODEL_LABEL="${CLAUDE_MODEL:-claude-fable-5} (Claude subscription)" ;;
  virtuals)
    LLM="$ROOT/scripts/llm.sh"
    MODEL_LABEL="${VIRTUALS_MODEL:-claude-opus-4-8} (Virtuals)" ;;
  auto|*)
    if [ -n "${CLAUDE_CODE_OAUTH_TOKEN:-}" ] || [ -n "${ANTHROPIC_API_KEY:-}" ]; then
      LLM="$ROOT/scripts/llm-claude.sh"
      MODEL_LABEL="${CLAUDE_MODEL:-claude-fable-5} (Claude subscription)"
    else
      LLM="$ROOT/scripts/llm.sh"
      MODEL_LABEL="$VIRTUALS_MODEL (Virtuals)"
    fi ;;
esac
```

To make this block testable in isolation, factor it into a helper
`select_backend()` that reads the env vars and echoes `LLM|MODEL_LABEL`, called once
near the top of `run.sh`. (Mirrors how `complete()` was made testable in PR #123.)

### 3. Workflow plumbing (`.github/workflows/investment-advisor.yml`)

Add to the `env:` block so the backend can be flipped with no code change:

```yaml
USEPOD_TOKEN: ${{ secrets.USEPOD_TOKEN }}
USEPOD_MODEL: ${{ vars.USEPOD_MODEL }}   # optional; defaults to deepseek-v3.2
ADVISOR_LLM:  ${{ vars.ADVISOR_LLM }}    # set repo var to "usepod" to enable
```

Empty `ADVISOR_LLM` → `auto` → unchanged behavior. Operator enables by setting the
repo **variable** `ADVISOR_LLM=usepod` and the **secret** `USEPOD_TOKEN`.

### 4. Docs

Document `USEPOD_TOKEN`, `USEPOD_MODEL`, `ADVISOR_LLM` in `.env.example` (and README
if it lists advisor env): the drop-in token from `POST https://api.usepod.ai/register`
(prepaid USDC; OpenAI-compatible; text models only).

## Testing (`scripts/advisor/selftest.sh`, offline, no creds)

- **Redactor:** `https://api.usepod.ai/proxy/SECRETTOKEN/v1/chat/completions` →
  token replaced with `<redacted>`; a non-usepod URL is untouched.
- **Backend selection** (via the extracted `select_backend` helper):
  - `ADVISOR_LLM=usepod` → `llm-usepod.sh` + `deepseek-v3.2 (usepod)` label;
    `USEPOD_MODEL=qwen-3.5` overrides the label.
  - `ADVISOR_LLM=auto` with `CLAUDE_CODE_OAUTH_TOKEN` set → `llm-claude.sh`.
  - `ADVISOR_LLM=auto` with no Claude token → `llm.sh`.
  - `ADVISOR_LLM=virtuals` → `llm.sh` regardless of Claude token.
- **usepod fallback:** with `USEPOD_TOKEN` unset and `VIRTUALS_API_KEY` set, a stub
  proves `llm-usepod.sh` defers to `llm.sh` (assert via a stubbed `llm.sh` on PATH
  echoing a sentinel).
- Reuses the stub-`$LLM` and stub-script patterns already in `selftest.sh`.

## Files

- **New:** `scripts/llm-usepod.sh`
- **Edit:** `scripts/advisor/run.sh` (extract `select_backend`, add usepod case),
  `.github/workflows/investment-advisor.yml` (env plumbing),
  `scripts/advisor/selftest.sh` (tests), `.env.example` (docs).

## Out of scope

- Wallet-native x402 / Solana per-call settlement (drop-in prepaid token only).
- Making usepod the default/primary backend (opt-in only).
- Other workflows that call `llm.sh` (weekly-conviction, aeon, messages) — advisor
  only.
- A live dashboard/`/v1/models` catalog fetch (free-text `USEPOD_MODEL` covers it).

## Open assumption (confirm with a real token)

usepod's live catalog is token-gated; `deepseek-v3.2` is a best-effort canonical id
from usepod's published lineup. Confirm the exact slug + that it returns strict JSON
for the PM prompt via `GET https://api.usepod.ai/proxy/<token>/v1/models` and a dry
run (`ADVISOR_DRY_RUN=1 ADVISOR_LLM=usepod ./scripts/advisor/run.sh`) before relying
on it in the scheduled job.
