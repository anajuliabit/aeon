# Research prefetch for the chat fallback — design

**Date:** 2026-06-17
**Status:** Approved (design); implementation pending
**Author:** Ana (with Claude Code)
**Repo:** aeon

## Problem

When the primary chat model (Claude Code CLI, `claude -p` with `WebFetch`/`WebSearch`
tools) is rate-limited, the Telegram/Discord/Slack chat handler in
`.github/workflows/messages.yml` falls back to a single text-only completion via
`scripts/llm-usepod.sh` (usepod → Virtuals). That fallback has no tools, and its
prompt tells the model to say it will "handle it once full capacity is restored."
So research questions ("find undervalued Polymarket bets; research X/internet for
insights people haven't noticed") get refused instead of answered.

Claude's weekly limit resets 2026-06-22, so until then every chat hits this
degraded fallback. We want the fallback to answer research questions with real,
fresh data.

## Decision

Keep usepod as the answering "brain", but **prefetch live research** and inject it
into the usepod prompt (the operator chose usepod-synthesizes over Grok-answers).
The fetch primitive reuses the existing Grok/xAI pattern already in the repo
(`.xai-buzz.sh`): the xAI Responses API with live search tools. `XAI_API_KEY` is
already wired into the `messages.yml` chat job env.

Settled during brainstorming:
1. **usepod + prefetch** (not Grok-answers-directly, not text-only reword).
2. **Prefetch on every fallback message** — no intent classifier. The fallback only
   fires when Claude is down (rare), so one xAI call per message is acceptable;
   wasted on a `note:`-style capture but harmless.
3. **Sources: X + web** — enable both `x_search` and `web_search` tools on the Grok
   call for broadest coverage.

## Design

### 1. New `scripts/research-prefetch.sh`

Single-purpose fetch primitive. Contract: query on `$1` or stdin → a compact text
digest of findings on stdout; empty output + non-zero exit on any failure (so the
caller can treat it as best-effort and never block the reply).

```bash
set -uo pipefail
[ -n "${XAI_API_KEY:-}" ] || { echo "research-prefetch.sh: XAI_API_KEY not set" >&2; exit 1; }
QUERY from $1/stdin; empty -> exit 1
MODEL="${XAI_RESEARCH_MODEL:-grok-4-1-fast}"
```

- POST `https://api.x.ai/v1/responses` with `Authorization: Bearer $XAI_API_KEY`,
  `--max-time 120`, body:
  ```json
  {"model":"<model>",
   "input":[{"role":"user","content":"<research instruction + QUERY>"}],
   "tools":[{"type":"x_search"},{"type":"web_search"}]}
  ```
  Instruction: "Research the operator's question using live X and web search. Return
  the 5–8 most decision-relevant findings as terse bullets, each with a source link
  and a date. Surface non-obvious / under-noticed angles. If you find nothing solid,
  say so."
- Extract the assistant text from the Responses payload (jq over
  `.output[]?.content[]?.text // .output_text // empty`, joined). Print to stdout.
- On curl failure, HTTP error, empty/`.error` payload, or empty extracted text →
  print nothing to stdout, exit 1.
- No `set -x`. `XAI_API_KEY` is a bearer header (not in the URL), so no redaction
  needed beyond not echoing the request body on error.

### 2. Wire into the `messages.yml` fallback

In the `if [ "$CLAUDE_OK" = false ]` block (added in PR #125), before selecting the
usepod backend:

```bash
chmod +x scripts/research-prefetch.sh 2>/dev/null || true
RESEARCH="$(printf '%s' "$MESSAGE" | bash scripts/research-prefetch.sh 2>/dev/null || true)"
```

Then build `FB_PROMPT` in two modes:

- **RESEARCH non-empty** — research-grounded prompt:
  > "You are Aeon replying to your operator on ${SOURCE}. The primary model hit its
  > usage limit, so you are on a text backend — BUT you have fresh live research
  > gathered just now from X and the web (below). Answer the operator's question
  > concretely using ONLY this research; cite the source links; surface the
  > non-obvious angles. Do NOT say you cannot research or to wait for capacity.
  >
  > LIVE RESEARCH:
  > \<RESEARCH digest\>
  >
  > Operator question:
  > \"$MESSAGE\""

- **RESEARCH empty** (prefetch failed/unconfigured) — keep the current degraded
  prompt unchanged (best-effort reasoning, honest about no live data).

Then pipe `FB_PROMPT` to `scripts/llm-usepod.sh` exactly as today (usepod → Virtuals
cascade unchanged). Reuse the existing reply/exit/notify handling.

### 3. Workflow env

`XAI_API_KEY` is already present in the chat job's env block — no change needed.
Add `scripts/research-prefetch.sh` to the job's `chmod +x` list (alongside the
backend scripts) so the `bash scripts/...` call and any direct exec succeed.

### 4. Boundaries

- Only the chat fallback path in `messages.yml` changes. The primary `claude -p`
  path (already tool-capable) is untouched. The advisor (`run.sh`) is untouched.
- Prefetch is strictly best-effort: any failure leaves the existing fallback
  behavior intact (usepod answers without live data using the degraded prompt).

## Testing (`scripts/advisor/selftest.sh`, offline, no network)

- **research-prefetch.sh unconfigured:** with `XAI_API_KEY` unset, the script exits
  non-zero and prints nothing (no crash, safe for `|| true`).
- **research-prefetch.sh empty query:** empty/whitespace input → exit 1, no output.
- **FB_PROMPT mode selection:** extract the prompt-building branch logic; assert that
  a non-empty `RESEARCH` yields the research-grounded template (contains "LIVE
  RESEARCH" and forbids the "cannot research" line) and an empty `RESEARCH` yields
  the degraded template. (Stub `$MESSAGE`/`$RESEARCH`; no network.)

These run in the existing `selftest.sh` harness (the advisor selftest is the repo's
offline shell-logic test runner; the chat scripts have no other suite).

## Out of scope

- Grok answering directly (operator chose usepod-synthesizes).
- A general agentic tool loop on usepod (single text completion only).
- Search providers other than xAI; the advisor and primary chat paths.
- Intent gating of prefetch (decided: run on every fallback message).

## Open assumption (verify during implementation)

The xAI Responses API tool types: `.xai-buzz.sh` uses `x_search`. This design also
enables `web_search`. If the live API rejects `web_search` as a tool type, fall back
to `x_search` only and note it in the script comment — do not fail the prefetch over
an unsupported tool. Confirm the response JSON shape for text extraction against a
real `XAI_API_KEY` (the `.output[].content[].text` path) before relying on it; adjust
the jq if the shape differs.
