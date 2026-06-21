# Robust Telegram delivery in `notify` — design

**Date:** 2026-06-17
**Status:** Approved (design); implementation pending
**Author:** Ana (with Claude Code)
**Repo:** aeon

## Problem

The `notify` helper (generated inline in `.github/workflows/messages.yml`) sends a
reply to Telegram with:

```bash
curl -sf ... sendMessage -d '{chat_id, text:$MSG, parse_mode:"Markdown"}' >/dev/null || true
```

Two failure modes silently drop valid replies:

1. **Length** — Telegram rejects messages over 4096 characters (HTTP 400). `-f` makes
   curl fail and `|| true` swallows it → no delivery, no log.
2. **Markdown** — `parse_mode:"Markdown"` makes Telegram reject any text with
   unbalanced `*`/`_`/`[`/backticks or stray characters (HTTP 400, "can't parse
   entities"). Research-grounded replies (links, prices, `$`, bullets) trip this
   routinely → same silent drop.

Observed: the chat run at 2026-06-17 19:53 logged `research-prefetch returned 3489
chars` then `Replied via text fallback` — usepod produced a research answer — yet
the operator received nothing, because `notify` dropped the long/Markdown reply.

## Decisions (settled during brainstorming)

1. **Markdown:** send with `parse_mode:"Markdown"`; if the API response is not `ok`,
   resend the **same** text without `parse_mode`. Keeps formatting when valid,
   guarantees delivery when not.
2. **Length:** split into ≤4000-char chunks on line boundaries (headroom under
   Telegram's 4096 for the part label + multibyte safety); send sequentially.
3. **Multi-part labeling:** when a reply splits into n>1 chunks, prefix each with
   `(i/n)` so ordering is clear. Single-chunk replies get no label.
4. **Surface failures:** on a real send failure (both Markdown and plain rejected),
   emit `::warning::notify: telegram send failed: <description>` to stderr instead of
   swallowing it (same diagnosability lesson as the advisor/prefetch fixes).
5. **Scope: Telegram branch only.** Discord/Slack branches are unchanged.

## Design

### 1. New `scripts/tg-chunk.sh` (pure, unit-tested)

The only piece with real logic, isolated so it can be tested offline.

- Reads the message on stdin. Splits into chunks of at most `${TG_CHUNK_MAX:-4000}`
  characters, preferring line boundaries: accumulate lines (with their `\n`) until
  adding the next line would exceed the max, then emit the accumulated chunk. A
  single line longer than the max is hard-split into max-sized pieces.
- Emits chunks **NUL-separated** on stdout (so a bash consumer can `mapfile -d ''`).
- Character counting uses bash parameter expansion under the runner's UTF-8 locale;
  the 4000 cap (vs the 4096 hard limit) absorbs label length and any byte/char
  drift.

### 2. Rework the Telegram branch of `notify` (`messages.yml`)

Replace the single `curl -sf … || true` with a chunked, retrying loop:

```bash
if [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
  mapfile -d '' _CHUNKS < <(printf '%s' "$MSG" | bash scripts/tg-chunk.sh)
  _n=${#_CHUNKS[@]}
  _i=0
  for _c in "${_CHUNKS[@]}"; do
    [ -n "$_c" ] || continue
    _i=$((_i+1))
    if [ "$_n" -gt 1 ]; then _c="($_i/$_n) $_c"; fi
    _md=$(jq -n --arg chat "$TELEGRAM_CHAT_ID" --arg text "$_c" '{chat_id:$chat, text:$text, parse_mode:"Markdown"}')
    _resp="$(curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -H "Content-Type: application/json" -d "$_md")"
    if [ "$(printf '%s' "$_resp" | jq -r '.ok // false')" != "true" ]; then
      _plain=$(jq -n --arg chat "$TELEGRAM_CHAT_ID" --arg text "$_c" '{chat_id:$chat, text:$text}')
      _resp="$(curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -H "Content-Type: application/json" -d "$_plain")"
      [ "$(printf '%s' "$_resp" | jq -r '.ok // false')" = "true" ] \
        || echo "::warning::notify: telegram send failed: $(printf '%s' "$_resp" | jq -r '.description // "unknown"')" >&2
    fi
  done
fi
```

(`set -euo pipefail` is active in the generated `notify`; the loop must not abort the
script on a single failed send — the `||` guards above handle that, and no bare
failing command is left to trip `-e`.)

### 3. Boundaries

- Only the Telegram branch changes. Discord (`DISCORD_WEBHOOK_URL`) and Slack
  (`SLACK_WEBHOOK_URL`) branches are untouched. `notify`'s arg interface (`-f <file>`
  / positional, empty-message skip) is unchanged.
- `scripts/tg-chunk.sh` is reachable from the runtime `./notify` because both run
  from the repo root (the workflow writes `./notify` and runs in the checkout).

## Testing (`scripts/advisor/selftest.sh`, offline, no network)

`tg-chunk.sh` only (the curl loop is I/O — covered by `bash -n` + yaml parse):

- **Short multi-line** (3 short lines) → exactly 1 chunk; reassembles to the input.
- **Long multi-line** (~5000 chars across many lines) → ≥2 chunks, each ≤4000 chars;
  concatenation of chunks equals the original.
- **Single overlong line** (5000 chars, no newline) → hard-split into ≥2 chunks, each
  ≤4000.
- **Boundary** (exactly 4000 chars) → 1 chunk.
- Chunk count and max-chunk-length asserted by piping NUL-separated output through
  `tr '\0' '\n'` and measuring with `awk` (max line length) plus a chunk count.

## Out of scope

- Discord/Slack length handling (Discord's 2000-char limit is a separate follow-up).
- The advisor and primary `claude -p` chat paths.
- Changing the `notify` invocation interface or its Discord/Slack bodies.
- Markdown-to-Telegram-safe escaping (we degrade to plain text instead of escaping).
