# Robust Telegram Delivery in `notify` — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Stop `notify` silently dropping valid Telegram replies — deliver long answers (chunked, labeled) and Markdown-breaking answers (retry as plain), and log real send failures.

**Architecture:** A new pure `scripts/tg-chunk.sh` splits a message into ≤4000-char chunks on line boundaries (NUL-separated). The Telegram branch of the inline `notify` script in `messages.yml` loops over chunks, labels parts `(i/n)`, sends with `parse_mode:Markdown` then retries the same chunk as plain text if the API rejects it, and emits a `::warning::` on real failure instead of swallowing it. Discord/Slack branches unchanged.

**Tech Stack:** Bash (chunker is bash-3.2-compatible for the macOS selftest; the notify loop uses `mapfile -d ''` and runs on GitHub ubuntu bash 5), curl, jq. Offline tests in `scripts/advisor/selftest.sh`.

**Branch:** `fix/notify-telegram-delivery` off `main`. Worktree `.worktrees/notify-fix`.

---

## File Structure

- **Create** `scripts/tg-chunk.sh` — stdin → ≤`TG_CHUNK_MAX` (default 4000) char chunks on line boundaries, NUL-separated. The only real logic; unit-tested.
- **Modify** `.github/workflows/messages.yml` — replace the Telegram branch of the `notify` heredoc (currently lines ~703–707) with a chunked, Markdown→plain-retry, failure-logging loop.
- **Modify** `scripts/advisor/selftest.sh` — offline assertions for `tg-chunk.sh`.

---

## Task 1: `scripts/tg-chunk.sh`

Pure message chunker. Byte-exact: concatenating the emitted chunks reproduces the input (it only splits, never adds/removes characters).

**Files:**
- Create: `scripts/tg-chunk.sh`
- Test: `scripts/advisor/selftest.sh` (append before the final pass/fail line)

- [ ] **Step 1: Write the failing tests**

Append to `scripts/advisor/selftest.sh` before the final `[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" ...` line:

```bash
# --- tg-chunk.sh: line-boundary chunking under the Telegram limit ---
TGC="$(cd "$(dirname "$0")/.." && pwd)/tg-chunk.sh"
# Consume NUL-delimited stdin -> "<count> <maxchunklen>" (portable: read -d '').
tgstats() { local c n=0 m=0; while IFS= read -r -d '' c; do n=$((n+1)); [ "${#c}" -gt "$m" ] && m="${#c}"; done; echo "$n $m"; }

SHORT="$(printf 'alpha\nbeta\ngamma')"
check "tg-chunk short -> 1 chunk"       "$(printf '%s' "$SHORT" | bash "$TGC" | tgstats | cut -d' ' -f1)" "1"
check "tg-chunk short reassembles"      "$(printf '%s' "$SHORT" | bash "$TGC" | tr -d '\0')" "$SHORT"

# ~6100 chars across 120 lines (50 'x' + newline each) -> multiple chunks, each <=4000.
LONG="$(for i in $(seq 1 120); do printf 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n'; done)"
set -- $(printf '%s' "$LONG" | bash "$TGC" | tgstats)
check "tg-chunk long -> >=2 chunks"     "$([ "$1" -ge 2 ] && echo yes)" "yes"
check "tg-chunk long chunks <=4000"     "$([ "$2" -le 4000 ] && echo yes)" "yes"
check "tg-chunk long reassembles"       "$(printf '%s' "$LONG" | bash "$TGC" | tr -d '\0')" "$LONG"

# Single 5000-char line, no newline -> hard-split into >=2 chunks, each <=4000.
BIG="$(printf 'y%.0s' $(seq 1 5000))"
set -- $(printf '%s' "$BIG" | bash "$TGC" | tgstats)
check "tg-chunk overlong line -> >=2"   "$([ "$1" -ge 2 ] && echo yes)" "yes"
check "tg-chunk overlong line <=4000"   "$([ "$2" -le 4000 ] && echo yes)" "yes"

# Exactly 4000 chars -> 1 chunk.
B4000="$(printf 'z%.0s' $(seq 1 4000))"
check "tg-chunk exactly 4000 -> 1 chunk" "$(printf '%s' "$B4000" | bash "$TGC" | tgstats | cut -d' ' -f1)" "1"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `bash scripts/advisor/selftest.sh`
Expected: FAIL — `tg-chunk.sh` missing, so `bash "$TGC"` errors; counts/lengths are wrong. Final `selftest: FAILURES`.

- [ ] **Step 3: Create `scripts/tg-chunk.sh`**

```bash
#!/usr/bin/env bash
# scripts/tg-chunk.sh — split stdin into <= TG_CHUNK_MAX-char chunks, preferring line
# boundaries (a single overlong line is hard-split), emitted NUL-separated so a bash
# consumer can `mapfile -d ''`. The 4000 default leaves headroom under Telegram's
# 4096 limit for a "(i/n)" part label and any byte/char drift. Pure: concatenating
# the chunks reproduces the input exactly. bash-3.2 compatible (no mapfile here).
set -uo pipefail
MAX="${TG_CHUNK_MAX:-4000}"

# Read all of stdin, preserving any trailing newline (command-sub would strip it).
MSG="$(cat; printf x)"; MSG="${MSG%x}"

rest="$MSG"
while [ "${#rest}" -gt "$MAX" ]; do
  window="${rest:0:$MAX}"
  if [[ "$window" == *$'\n'* ]]; then
    head="${window%$'\n'*}"$'\n'   # up to and including the last newline in the window
  else
    head="$window"                 # no newline in range: hard-split at MAX
  fi
  printf '%s\0' "$head"
  rest="${rest:${#head}}"
done
[ -n "$rest" ] && printf '%s\0' "$rest"
exit 0
```

- [ ] **Step 4: Make it executable**

Run: `chmod +x scripts/tg-chunk.sh`
Expected: no output.

- [ ] **Step 5: Run tests to verify they pass**

Run: `bash scripts/advisor/selftest.sh`
Expected: the 8 new `tg-chunk …` checks `ok`, final `selftest: ALL PASS`.

- [ ] **Step 6: Syntax-check**

Run: `bash -n scripts/tg-chunk.sh && echo "tg-chunk.sh OK"`
Expected: `tg-chunk.sh OK`

- [ ] **Step 7: Commit**

```bash
git add scripts/tg-chunk.sh scripts/advisor/selftest.sh
git commit -m "feat(messages): tg-chunk.sh — split messages under the Telegram 4096 limit"
```

---

## Task 2: Rework the Telegram branch of `notify`

Replace the single fire-and-forget Telegram `curl` with a chunked, retrying, logging loop. The `notify` script is a quoted heredoc (`<< 'NOTIFY_SCRIPT'`) inside the YAML `run: |` block — keep the existing 10-space YAML indentation on every line so it stays in the block.

**Files:**
- Modify: `.github/workflows/messages.yml` (the Telegram branch inside the `notify` heredoc)

- [ ] **Step 1: Replace the Telegram branch**

Find this EXACT block:

```bash
          if [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
            curl -sf -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" \
              -H "Content-Type: application/json" \
              -d "$(jq -n --arg chat "$TELEGRAM_CHAT_ID" --arg text "$MSG" '{chat_id: $chat, text: $text, parse_mode: "Markdown"}')" > /dev/null || true
          fi
```

Replace with (preserve the 10-space leading indentation exactly as shown):

```bash
          if [ -n "${TELEGRAM_BOT_TOKEN:-}" ] && [ -n "${TELEGRAM_CHAT_ID:-}" ]; then
            # Telegram caps messages at 4096 chars and rejects Markdown it can't parse
            # (links/*/_ in research answers). Chunk + label parts, send Markdown then
            # retry the same chunk as plain text, and log a real failure (no silent drop).
            mapfile -d '' _CHUNKS < <(printf '%s' "$MSG" | bash scripts/tg-chunk.sh)
            _n=${#_CHUNKS[@]}; _i=0
            for _c in "${_CHUNKS[@]}"; do
              [ -n "$_c" ] || continue
              _i=$((_i+1))
              [ "$_n" -gt 1 ] && _c="($_i/$_n) $_c"
              _body="$(jq -n --arg chat "$TELEGRAM_CHAT_ID" --arg text "$_c" '{chat_id:$chat, text:$text, parse_mode:"Markdown"}')"
              _resp="$(curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -H "Content-Type: application/json" -d "$_body")"
              if [ "$(printf '%s' "$_resp" | jq -r '.ok // false')" != "true" ]; then
                _body="$(jq -n --arg chat "$TELEGRAM_CHAT_ID" --arg text "$_c" '{chat_id:$chat, text:$text}')"
                _resp="$(curl -s -X POST "https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage" -H "Content-Type: application/json" -d "$_body")"
                [ "$(printf '%s' "$_resp" | jq -r '.ok // false')" = "true" ] || echo "::warning::notify: telegram send failed: $(printf '%s' "$_resp" | jq -r '.description // "unknown"')" >&2
              fi
            done
          fi
```

Leave the Discord and Slack branches (the two `if` blocks that follow) and the `NOTIFY_SCRIPT` terminator unchanged.

- [ ] **Step 2: Verify the workflow parses**

Run: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/messages.yml')); print('yaml OK')"`
Expected: `yaml OK`

- [ ] **Step 3: Extract the generated `notify` script and syntax-check it**

The Telegram loop lives inside the `notify` heredoc, so `bash -n` of the run block alone won't validate it — extract the heredoc body and check it directly:

```bash
python3 -c "
import yaml, re
d=yaml.safe_load(open('.github/workflows/messages.yml'))
runs=[s.get('run','') for j in d['jobs'].values() for s in j.get('steps',[])]
blob=next(r for r in runs if 'NOTIFY_SCRIPT' in r and 'tg-chunk.sh' in r)
m=re.search(r\"cat > ./notify << 'NOTIFY_SCRIPT'\n(.*?)\n\s*NOTIFY_SCRIPT\", blob, re.S)
open('/tmp/notify.sh','w').write(m.group(1))
print('extracted notify body')
" && bash -n /tmp/notify.sh && echo "notify body: bash OK"
```
Expected: `extracted notify body` then `notify body: bash OK`.

- [ ] **Step 4: Confirm the wiring**

Run: `grep -n "tg-chunk.sh\|_CHUNKS\|parse_mode\|telegram send failed" .github/workflows/messages.yml`
Expected: shows the `mapfile … tg-chunk.sh` line, the `_CHUNKS` loop, the `parse_mode:"Markdown"` body, and the failure `::warning::`. The Telegram branch has exactly ONE `parse_mode` reference (the Markdown attempt); the plain-retry body has none.

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/messages.yml
git commit -m "fix(messages): chunk + Markdown-retry + log failures on Telegram delivery"
```

---

## Task 3: Full suite + final review

- [ ] **Step 1: Run the complete offline suite**

Run: `bash scripts/advisor/selftest.sh`
Expected: all `ok`, final `selftest: ALL PASS`, exit 0 (prior checks plus the 8 new `tg-chunk` checks).

- [ ] **Step 2: Sanity-check chunk labeling math by hand**

Run:
```bash
printf 'line\n%s' "$(printf 'q%.0s' $(seq 1 9000))" | bash scripts/tg-chunk.sh | { n=0; while IFS= read -r -d '' c; do n=$((n+1)); echo "chunk $n: ${#c} chars"; done; }
```
Expected: 4 chunks, each ≤4000 chars (5, 4000, 4000, 1000) — the leading `line\n` is its own chunk (line-boundary cut), then the 9000-char run hard-splits. Confirms a long reply is sent as `(1/4)…(4/4)` instead of dropped.

- [ ] **Step 3: Confirm Discord/Slack branches untouched**

Run: `git diff origin/main -- .github/workflows/messages.yml | grep -E '^[-+].*(DISCORD_WEBHOOK_URL|SLACK_WEBHOOK_URL)'`
Expected: no output (those lines unchanged — only the Telegram branch differs).

---

## Self-Review

**Spec coverage:**
- §1 tg-chunk.sh (≤4000 line-boundary split, NUL-separated, hard-split overlong line, byte-exact) → Task 1 + 8 assertions.
- §2 Markdown→plain retry → Task 2 loop (Markdown body, `.ok` check, plain re-send).
- §2 length chunking + `(i/n)` labeling → Task 2 (`mapfile` over tg-chunk, `_n>1` prefix).
- §2 surface failures (`::warning::`, not `|| true`) → Task 2 final `||` branch.
- §3 Telegram-only scope → Task 2 leaves Discord/Slack blocks; Task 3 Step 3 verifies.
- Testing (short/long/overlong/boundary) → Task 1 assertions; notify body syntax → Task 2 Step 3.

**Placeholder scan:** none — all code/commands concrete.

**Type/name consistency:** `scripts/tg-chunk.sh`, env `TG_CHUNK_MAX`, vars `_CHUNKS`/`_n`/`_i`/`_c`/`_body`/`_resp`, the `(i/n)` label, and the `::warning::notify: telegram send failed` string are consistent across the chunker, the notify loop, and the tests. The chunker emits NUL-separated output exactly as `mapfile -d ''` in notify and `read -r -d ''` in the tests consume it.
