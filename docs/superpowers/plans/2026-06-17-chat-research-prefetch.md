# Chat Research Prefetch Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** When chat falls back off rate-limited Claude, prefetch live X/web research via xAI Grok and inject it into the usepod prompt so Aeon answers research questions with real data instead of refusing.

**Architecture:** Two small, independently testable scripts — `research-prefetch.sh` (best-effort xAI Grok live search → findings digest) and `build-fallback-prompt.sh` (composes the fallback prompt, research-grounded when a digest exists, degraded otherwise). The `messages.yml` chat fallback calls them as a thin two-line wiring; the usepod→Virtuals backend cascade is unchanged.

**Tech Stack:** Bash, curl, jq, xAI Responses API (`api.x.ai/v1/responses`), GitHub Actions. Offline tests in `scripts/advisor/selftest.sh`.

**Branch:** `feat/chat-research-prefetch` off `main`. Worktree `.worktrees/research-prefetch`.

---

## File Structure

- **Create** `scripts/research-prefetch.sh` — query → live findings digest (xAI Grok, x_search+web_search). Best-effort: empty + nonzero on any failure.
- **Create** `scripts/build-fallback-prompt.sh` — reads `SOURCE`/`MESSAGE`/`RESEARCH` env → prints the fallback prompt (research-grounded vs degraded).
- **Modify** `.github/workflows/messages.yml` — in the Claude-failure block, prefetch research + build prompt via the two scripts; add them to the `chmod +x` line.
- **Modify** `scripts/advisor/selftest.sh` — offline assertions for both scripts.

---

## Task 1: `scripts/research-prefetch.sh`

Best-effort live-research fetch via xAI Grok. Contract mirrors the other backend scripts: input on `$1`/stdin, useful output on stdout, empty + nonzero on any failure.

**Files:**
- Create: `scripts/research-prefetch.sh`
- Test: `scripts/advisor/selftest.sh` (append before the final pass/fail line)

- [ ] **Step 1: Write the failing tests**

Append to `scripts/advisor/selftest.sh` before the final `[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" ...` line:

```bash
# --- research-prefetch.sh: safe failure when unusable (offline) ---
RP="$(cd "$(dirname "$0")/.." && pwd)/scripts/research-prefetch.sh"
# Unconfigured (no XAI_API_KEY) -> exit 1, no stdout.
RP_OUT="$(env -u XAI_API_KEY bash "$RP" 'find cheap polymarket bets' 2>/dev/null)"; RP_RC=$?
check "research-prefetch exits 1 without XAI_API_KEY" "$RP_RC" "1"
check "research-prefetch emits no stdout without key" "$RP_OUT" ""
# Empty query (key present but blank prompt) -> exit 1, no stdout.
RP_OUT2="$(XAI_API_KEY=dummy bash "$RP" '   ' 2>/dev/null)"; RP_RC2=$?
check "research-prefetch exits 1 on empty query" "$RP_RC2" "1"
check "research-prefetch emits no stdout on empty query" "$RP_OUT2" ""
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `bash scripts/advisor/selftest.sh`
Expected: FAIL — the script does not exist, so `bash "$RP" ...` errors; `RP_RC` is 127 (not 1) and assertions fail. Final `selftest: FAILURES`.

- [ ] **Step 3: Create `scripts/research-prefetch.sh`**

```bash
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
  curl -sS --max-time 120 -X POST "https://api.x.ai/v1/responses" \
    -H "Authorization: Bearer $XAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$body"
}

extract() { # reads RESP on stdin -> findings text or empty
  jq -r '
    ([ .output[]?.content[]? | select(has("text")) | .text ]
       | map(select(. != null and . != "")) | join("\n"))
    // .output_text // .choices[0].message.content // empty' 2>/dev/null
}

RESP="$(call_xai '[{"type":"x_search"},{"type":"web_search"}]')" || { echo "research-prefetch.sh: request failed" >&2; exit 1; }
ERR=$(printf '%s' "$RESP" | jq -r '.error.message? // (.error|strings) // empty' 2>/dev/null || true)
if printf '%s' "$ERR" | grep -qiE 'web_search|tool|unsupported|invalid'; then
  echo "research-prefetch.sh: retrying x_search only ($ERR)" >&2
  RESP="$(call_xai '[{"type":"x_search"}]')" || { echo "research-prefetch.sh: request failed" >&2; exit 1; }
  ERR=$(printf '%s' "$RESP" | jq -r '.error.message? // (.error|strings) // empty' 2>/dev/null || true)
fi
if [ -n "$ERR" ]; then echo "research-prefetch.sh: API error: $ERR" >&2; exit 1; fi

OUT="$(printf '%s' "$RESP" | extract)"
if [ -z "${OUT//[[:space:]]/}" ]; then echo "research-prefetch.sh: no text in response" >&2; exit 1; fi
printf '%s\n' "$OUT"
```

- [ ] **Step 4: Make it executable**

Run: `chmod +x scripts/research-prefetch.sh`
Expected: no output.

- [ ] **Step 5: Run tests to verify they pass**

Run: `bash scripts/advisor/selftest.sh`
Expected: `ok   research-prefetch exits 1 without XAI_API_KEY`, `ok   research-prefetch emits no stdout without key`, `ok   research-prefetch exits 1 on empty query`, `ok   research-prefetch emits no stdout on empty query`, final `selftest: ALL PASS`.

(Note: the `XAI_API_KEY=dummy` empty-query test exits 1 at the empty-query guard BEFORE any network call, so it is fully offline.)

- [ ] **Step 6: Syntax-check**

Run: `bash -n scripts/research-prefetch.sh && echo "research-prefetch.sh OK"`
Expected: `research-prefetch.sh OK`

- [ ] **Step 7: Commit**

```bash
git add scripts/research-prefetch.sh scripts/advisor/selftest.sh
git commit -m "feat(messages): research-prefetch.sh — best-effort xAI Grok live search"
```

---

## Task 2: `scripts/build-fallback-prompt.sh`

Composes the chat fallback prompt from env. With `RESEARCH` set, grounds the answer in it and forbids the "can't research" refusal; otherwise emits the existing degraded prompt.

**Files:**
- Create: `scripts/build-fallback-prompt.sh`
- Test: `scripts/advisor/selftest.sh` (append before the final pass/fail line)

- [ ] **Step 1: Write the failing tests**

Append to `scripts/advisor/selftest.sh` before the final pass/fail line:

```bash
# --- build-fallback-prompt.sh: research-grounded vs degraded prompt ---
BFP="$(cd "$(dirname "$0")/.." && pwd)/scripts/build-fallback-prompt.sh"
# With RESEARCH -> research-grounded prompt.
P_RESEARCH="$(SOURCE=telegram MESSAGE='find cheap polymarket bets' RESEARCH='- Market X underpriced (link, 2026-06-17)' bash "$BFP")"
check "research prompt includes LIVE RESEARCH" "$(printf '%s' "$P_RESEARCH" | grep -c 'LIVE RESEARCH')" "1"
check "research prompt includes the digest"    "$(printf '%s' "$P_RESEARCH" | grep -c 'Market X underpriced')" "1"
check "research prompt omits degraded line"     "$(printf '%s' "$P_RESEARCH" | grep -c 'degraded text-only fallback')" "0"
# Without RESEARCH -> degraded prompt.
P_DEGRADED="$(SOURCE=telegram MESSAGE='hi' bash "$BFP")"
check "degraded prompt has degraded line"        "$(printf '%s' "$P_DEGRADED" | grep -c 'degraded text-only fallback')" "1"
check "degraded prompt omits LIVE RESEARCH"      "$(printf '%s' "$P_DEGRADED" | grep -c 'LIVE RESEARCH')" "0"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `bash scripts/advisor/selftest.sh`
Expected: FAIL — script missing, `bash "$BFP"` errors, the `grep -c` counts are `0` where `1` is expected. Final `selftest: FAILURES`.

- [ ] **Step 3: Create `scripts/build-fallback-prompt.sh`**

```bash
#!/usr/bin/env bash
# scripts/build-fallback-prompt.sh — compose the text-fallback prompt for the chat
# handler. Reads SOURCE, MESSAGE, and optional RESEARCH from the environment and
# prints the prompt to stdout. With RESEARCH non-empty, ground the answer in it and
# forbid the "can't research" refusal; otherwise emit the honest degraded prompt.
set -uo pipefail
: "${SOURCE:=your channel}"
: "${MESSAGE:=}"

if [ -n "${RESEARCH:-}" ]; then
  cat <<EOF
You are Aeon replying to your operator on ${SOURCE}. The primary model hit its usage limit, so you are on a text backend — BUT you have fresh live research gathered just now from X and the web (below). Answer the operator's question concretely using ONLY this research; cite the source links; surface the non-obvious angles. Do NOT say you cannot research or to wait for capacity.

LIVE RESEARCH:
${RESEARCH}

Operator question:
"${MESSAGE}"
EOF
else
  cat <<EOF
You are Aeon, an autonomous assistant replying to your operator on ${SOURCE}. You are in a degraded text-only fallback (no file or tool access) because the primary model hit its usage limit. Reply helpfully and concisely in one short paragraph. If the request needs running a skill, editing files, or saving a note, say you will handle it once full capacity is restored.

Operator message:
"${MESSAGE}"
EOF
fi
```

- [ ] **Step 4: Make it executable**

Run: `chmod +x scripts/build-fallback-prompt.sh`
Expected: no output.

- [ ] **Step 5: Run tests to verify they pass**

Run: `bash scripts/advisor/selftest.sh`
Expected: the six new `*prompt*` checks all `ok`, final `selftest: ALL PASS`.

- [ ] **Step 6: Syntax-check**

Run: `bash -n scripts/build-fallback-prompt.sh && echo "build-fallback-prompt.sh OK"`
Expected: `build-fallback-prompt.sh OK`

- [ ] **Step 7: Commit**

```bash
git add scripts/build-fallback-prompt.sh scripts/advisor/selftest.sh
git commit -m "feat(messages): build-fallback-prompt.sh — research-grounded vs degraded prompt"
```

---

## Task 3: Wire prefetch + prompt builder into `messages.yml`

Replace the inline fallback prompt with: prefetch research, then build the prompt via the new scripts. Backend cascade unchanged.

**Files:**
- Modify: `.github/workflows/messages.yml` (the `if [ "$CLAUDE_OK" = false ]` block, currently lines ~753–778)

- [ ] **Step 1: Add the new scripts to the chmod line**

In `.github/workflows/messages.yml`, find (inside the Claude-failure block):

```bash
            chmod +x scripts/llm.sh scripts/llm-usepod.sh 2>/dev/null || true
```

Replace with:

```bash
            chmod +x scripts/llm.sh scripts/llm-usepod.sh scripts/research-prefetch.sh scripts/build-fallback-prompt.sh 2>/dev/null || true
```

- [ ] **Step 2: Replace the inline FB_PROMPT with prefetch + builder**

Find this exact block:

```bash
            if [ -n "$FB_LLM" ]; then
              FB_PROMPT="You are Aeon, an autonomous assistant replying to your operator on ${SOURCE}. You are in a degraded text-only fallback (no file or tool access) because the primary model hit its usage limit. Reply helpfully and concisely in one short paragraph. If the request needs running a skill, editing files, or saving a note, say you will handle it once full capacity is restored.

          Operator message:
          \"$MESSAGE\""
              if FB_REPLY=$(printf '%s' "$FB_PROMPT" | bash "$FB_LLM"); then
```

Replace with:

```bash
            if [ -n "$FB_LLM" ]; then
              # Best-effort live research (X + web via Grok); empty on any failure.
              RESEARCH="$(printf '%s' "$MESSAGE" | bash scripts/research-prefetch.sh 2>/dev/null || true)"
              if [ -n "$RESEARCH" ]; then echo "::notice::research-prefetch returned $(printf '%s' "$RESEARCH" | wc -c) chars"; else echo "::notice::research-prefetch empty — degraded prompt"; fi
              FB_PROMPT="$(SOURCE="$SOURCE" MESSAGE="$MESSAGE" RESEARCH="$RESEARCH" bash scripts/build-fallback-prompt.sh)"
              if FB_REPLY=$(printf '%s' "$FB_PROMPT" | bash "$FB_LLM"); then
```

(Leave the rest of the block — `./notify "$FB_REPLY"`, the `echo "::notice::Replied via text fallback ($FB_LLM)."`, `exit 0`, the `else` error branch, and the outer `else`/`fi` — unchanged.)

- [ ] **Step 3: Verify the workflow parses**

Run: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/messages.yml')); print('yaml OK')"`
Expected: `yaml OK`

- [ ] **Step 4: Syntax-check the embedded chat run block**

Run:
```bash
python3 -c "
import yaml
d=yaml.safe_load(open('.github/workflows/messages.yml'))
for jid,job in d['jobs'].items():
    for st in job.get('steps',[]):
        run=st.get('run','')
        if 'CLAUDE_OK' in run and 'FB_LLM' in run:
            open('/tmp/chatrun2.sh','w').write('#!/usr/bin/env bash\n'+run)
" && bash -n /tmp/chatrun2.sh && echo "chat run block: bash OK"
```
Expected: `chat run block: bash OK`

- [ ] **Step 5: Confirm wiring present**

Run: `grep -n "research-prefetch.sh\|build-fallback-prompt.sh\|RESEARCH=" .github/workflows/messages.yml`
Expected: shows the chmod entry, the `RESEARCH="$(...)"` prefetch line, and the `bash scripts/build-fallback-prompt.sh` call.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/messages.yml
git commit -m "feat(messages): prefetch live research into the chat fallback prompt"
```

---

## Task 4: Full suite + final review

- [ ] **Step 1: Run the complete offline suite**

Run: `bash scripts/advisor/selftest.sh`
Expected: all `ok`, final `selftest: ALL PASS`, exit 0 (prior advisor/usepod checks plus the new research-prefetch + build-fallback-prompt checks).

- [ ] **Step 2: Confirm the degraded path is unchanged when prefetch is unavailable**

Run:
```bash
SOURCE=telegram MESSAGE='hi' bash scripts/build-fallback-prompt.sh | head -1
```
Expected: a line beginning `You are Aeon, an autonomous assistant replying to your operator on telegram.` (the original degraded prompt, intent preserved).

- [ ] **Step 3 (optional, needs a real key): live prefetch smoke test**

Run:
```bash
XAI_API_KEY=<real> bash scripts/research-prefetch.sh 'find cheap underpriced polymarket bets with high win probability' | head -20
```
Expected: bulleted findings with source links. If empty: read stderr for the xAI error (e.g. `web_search` unsupported → it already retried x_search only; or a JSON-shape mismatch → adjust the `extract()` jq per the spec's open assumption).

---

## Self-Review

**Spec coverage:**
- §1 research-prefetch.sh (xAI Grok, x_search+web_search, best-effort, bearer auth, default model) → Task 1, incl. the web_search→x_search retry from the spec's open assumption.
- §2 wire into messages.yml fallback (prefetch before backend, two-mode prompt) → Tasks 2 (builder) + 3 (wiring).
- §3 env (`XAI_API_KEY` already present; add scripts to chmod) → Task 3, Step 1.
- §4 boundaries (only chat fallback; primary/advisor untouched) → only `messages.yml` + two new scripts modified; no run.sh / primary-path edits.
- Testing section (unconfigured, empty query, prompt mode selection) → Task 1 + Task 2 assertions.

**Placeholder scan:** none — every step has concrete code/commands.

**Type/name consistency:** script names `research-prefetch.sh` / `build-fallback-prompt.sh`, env vars `SOURCE`/`MESSAGE`/`RESEARCH`/`XAI_API_KEY`/`XAI_RESEARCH_MODEL`, the `LIVE RESEARCH` sentinel, and the `degraded text-only fallback` phrase are identical across the builder, the tests, and the wiring. The builder reads exactly the env vars the workflow exports.
