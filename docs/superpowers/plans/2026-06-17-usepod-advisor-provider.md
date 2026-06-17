# usepod Advisor Provider Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add usepod as an opt-in third LLM backend for the investment advisor, selectable via `ADVISOR_LLM=usepod`, with token-in-URL auth, redaction, and Virtuals fallback.

**Architecture:** A new `scripts/llm-usepod.sh` honoring the same stdin→stdout contract as `llm.sh`/`llm-claude.sh`, so `run.sh`'s `complete()` calls it unchanged. Backend choice moves into a pure, testable `select_backend()` helper in `run.sh` whose default (`auto`) preserves today's Claude→Virtuals behavior. All tests are offline assertions in `scripts/advisor/selftest.sh`.

**Tech Stack:** Bash, curl, jq, GitHub Actions. Tested via `scripts/advisor/selftest.sh` (no network, no creds).

**Branch:** stacks on `fix/advisor-llm-diagnostics` (PR #123). Work in worktree `.worktrees/advisor-llm-fix`.

---

## File Structure

- **Create** `scripts/llm-usepod.sh` — usepod drop-in backend (curl to `…/proxy/<token>/v1/chat/completions`), token redaction, Virtuals fallback.
- **Modify** `scripts/advisor/run.sh` — replace the inline backend `if` (lines ~37–43) with a `select_backend()` function supporting `ADVISOR_LLM`.
- **Modify** `scripts/advisor/selftest.sh` — add selection-matrix, redactor, and fallback assertions.
- **Modify** `.github/workflows/investment-advisor.yml` — env plumbing (`USEPOD_TOKEN`, `USEPOD_MODEL`, `ADVISOR_LLM`).
- **Modify** `.env.example` — document the three new vars.

---

## Task 1: `select_backend()` helper with `ADVISOR_LLM` selector

Makes backend choice a pure function (reads env → sets `LLM`/`MODEL_LABEL` globals), adds the `usepod` case, and keeps `auto` identical to current behavior. Implemented test-first using the same extract-via-sed pattern PR #123 used for `complete()`.

**Files:**
- Modify: `scripts/advisor/run.sh` (current lines ~33–44)
- Test: `scripts/advisor/selftest.sh` (append before the final pass/fail line)

- [ ] **Step 1: Write the failing tests**

Append to `scripts/advisor/selftest.sh` immediately BEFORE the final line
`[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" ...`:

```bash
# --- run.sh select_backend(): ADVISOR_LLM selector ---
SB_DIR="$(cd "$(dirname "$0")" && pwd)"
# Run the real select_backend() in a clean subshell with controlled env.
sb() { # ADVISOR_LLM, CLAUDE_CODE_OAUTH_TOKEN, VIRTUALS_MODEL, USEPOD_MODEL -> "LLM|LABEL"
  ADVISOR_LLM="$1" CLAUDE_CODE_OAUTH_TOKEN="$2" ANTHROPIC_API_KEY="" \
    VIRTUALS_MODEL="${3:-}" USEPOD_MODEL="${4:-}" CLAUDE_MODEL="" ROOT="/fake/root" \
    bash -c 'unset LLM MODEL_LABEL
      '"$(sed -n '/^select_backend() {/,/^}/p' "$SB_DIR/run.sh")"'
      select_backend; printf "%s|%s" "$LLM" "$MODEL_LABEL"' 2>/dev/null
}
check "select usepod -> llm-usepod.sh"      "$(sb usepod '' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm-usepod.sh"
check "select usepod default label"         "$(sb usepod '' '' '' | cut -d'|' -f2)" "deepseek-v3.2 (usepod)"
check "select usepod honors USEPOD_MODEL"   "$(sb usepod '' '' qwen-3.5 | cut -d'|' -f2)" "qwen-3.5 (usepod)"
check "select claude explicit"              "$(sb claude '' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm-claude.sh"
check "select virtuals explicit"            "$(sb virtuals 'tok' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm.sh"
check "auto + claude token -> claude"       "$(sb auto 'tok' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm-claude.sh"
check "auto + no token -> virtuals"         "$(sb auto '' 'kimi' '' | cut -d'|' -f1)" "/fake/root/scripts/llm.sh"
check "unset ADVISOR_LLM behaves as auto"   "$(sb '' 'tok' '' '' | cut -d'|' -f1)" "/fake/root/scripts/llm-claude.sh"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `bash scripts/advisor/selftest.sh`
Expected: FAIL lines for the `select …` checks (function not defined yet → empty output), e.g. `FAIL select usepod -> llm-usepod.sh: got [] want [/fake/root/scripts/llm-usepod.sh]`, and final `selftest: FAILURES` (exit 1).

- [ ] **Step 3: Replace the inline backend if-block with `select_backend()`**

In `scripts/advisor/run.sh`, find this block (currently ~lines 34–43):

```bash
# Backend: Claude subscription (claude-fable-5 via Claude Code CLI) when the
# OAuth token is present; Virtuals otherwise. llm-claude.sh itself falls back
# to llm.sh if the CLI call fails, so MODEL_LABEL reflects the primary backend.
if [ -n "${CLAUDE_CODE_OAUTH_TOKEN:-}" ] || [ -n "${ANTHROPIC_API_KEY:-}" ]; then
  LLM="$ROOT/scripts/llm-claude.sh"
  MODEL_LABEL="${CLAUDE_MODEL:-claude-fable-5} (Claude subscription)"
else
  LLM="$ROOT/scripts/llm.sh"
  MODEL_LABEL="$VIRTUALS_MODEL (Virtuals)"
fi
```

Replace it with:

```bash
# Backend selection. ADVISOR_LLM picks explicitly (usepod|claude|virtuals);
# the default "auto" keeps the historical behavior: Claude subscription
# (claude-fable-5 via Claude Code CLI) when an OAuth/API token is present,
# Virtuals otherwise. llm-claude.sh / llm-usepod.sh fall back to llm.sh on
# failure, so MODEL_LABEL reflects the primary backend. Sets LLM + MODEL_LABEL.
select_backend() {
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
}
select_backend
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `bash scripts/advisor/selftest.sh`
Expected: `ok   select usepod -> llm-usepod.sh` … through `ok   unset ADVISOR_LLM behaves as auto`, and final `selftest: ALL PASS` (exit 0).

- [ ] **Step 5: Syntax-check run.sh**

Run: `bash -n scripts/advisor/run.sh && echo "run.sh OK"`
Expected: `run.sh OK`

- [ ] **Step 6: Commit**

```bash
git add scripts/advisor/run.sh scripts/advisor/selftest.sh
git commit -m "feat(advisor): ADVISOR_LLM backend selector (auto default unchanged)"
```

---

## Task 2: `scripts/llm-usepod.sh` backend

The usepod drop-in backend. Same contract as `llm.sh`. Token in URL path; all emitted text redacted; Virtuals fallback on failure or missing token.

**Files:**
- Create: `scripts/llm-usepod.sh`
- Test: `scripts/advisor/selftest.sh` (append before the final pass/fail line)

- [ ] **Step 1: Write the failing tests**

Append to `scripts/advisor/selftest.sh` before the final pass/fail line:

```bash
# --- llm-usepod.sh: redaction + fallback (offline, stubbed) ---
UP_DIR="$(cd "$(dirname "$0")/.." && pwd)/scripts"   # repo scripts/ dir
UP_TMP="$(mktemp -d)"

# Redactor: load the real redact() from llm-usepod.sh and check it scrubs the token.
eval "$(sed -n '/^redact() {/,/^}/p' "$UP_DIR/llm-usepod.sh")"
RED_IN='curl failed for https://api.usepod.ai/proxy/SECRETTOKEN/v1/chat/completions now'
check "redact scrubs usepod token" \
  "$(printf '%s' "$RED_IN" | redact)" \
  'curl failed for https://api.usepod.ai/proxy/<redacted>/v1/chat/completions now'
check "redact leaves non-usepod text" \
  "$(printf '%s' 'no secrets here' | redact)" 'no secrets here'

# Fallback: USEPOD_TOKEN unset + a stub Virtuals llm.sh on a fake root -> usepod
# defers to Virtuals and returns the stub's output.
mkdir -p "$UP_TMP/scripts"
cp "$UP_DIR/llm-usepod.sh" "$UP_TMP/scripts/llm-usepod.sh"
cat > "$UP_TMP/scripts/llm.sh" <<'EOF'
#!/usr/bin/env bash
cat >/dev/null
echo '{"ok":"virtuals-stub"}'
EOF
chmod +x "$UP_TMP/scripts/llm.sh" "$UP_TMP/scripts/llm-usepod.sh"
FB_OUT="$(USEPOD_TOKEN='' VIRTUALS_API_KEY='present' bash "$UP_TMP/scripts/llm-usepod.sh" 'ping' 2>/dev/null)"
check "usepod falls back to Virtuals when token unset" "$FB_OUT" '{"ok":"virtuals-stub"}'
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `bash scripts/advisor/selftest.sh`
Expected: FAIL — `sed` finds no `redact()` (function undefined → empty output, `FAIL redact scrubs usepod token`), and the fallback `cp` errors because `llm-usepod.sh` does not exist yet. Final `selftest: FAILURES`.

- [ ] **Step 3: Create `scripts/llm-usepod.sh`**

```bash
#!/usr/bin/env bash
# scripts/llm-usepod.sh — call usepod.ai drop-in inference (OpenAI-compatible).
#
# Same contract as scripts/llm.sh: prompt on stdin (or $1), completion on stdout,
# non-zero exit + stderr message on failure.
#
# Auth: usepod's token lives in the URL PATH, not a header. USEPOD_TOKEN is the
# drop-in token from POST https://api.usepod.ai/register (prepaid USDC balance).
# Model: USEPOD_MODEL (default deepseek-v3.2). Endpoint base: USEPOD_BASE.
#
# Fallback: if usepod is unconfigured or every attempt fails AND VIRTUALS_API_KEY
# is set, retries the same prompt through scripts/llm.sh (Virtuals), mirroring
# llm-claude.sh, so an outage degrades instead of producing a gap.
#
# Security: the token is in the URL, so ALL emitted text is piped through redact()
# before reaching stderr. Never enable `set -x` here (it would print the URL).
set -uo pipefail

MODEL="${USEPOD_MODEL:-deepseek-v3.2}"
PROXY_BASE="${USEPOD_BASE:-https://api.usepod.ai/proxy}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Replace the token path segment (proxy/<token>) with <redacted> in any text.
redact() { sed 's#\(proxy/\)[^/]*#\1<redacted>#g'; }

# Prompt from $1 or stdin.
if [ -n "${1:-}" ]; then
  PROMPT="$1"
else
  PROMPT="$(cat)"
fi
if [ -z "${PROMPT//[[:space:]]/}" ]; then
  echo "llm-usepod.sh: empty prompt" >&2
  exit 1
fi

fallback() {
  if [ -n "${VIRTUALS_API_KEY:-}" ] && [ -x "$ROOT/scripts/llm.sh" ]; then
    echo "llm-usepod.sh: falling back to Virtuals (llm.sh)" >&2
    printf '%s' "$PROMPT" | "$ROOT/scripts/llm.sh"
    exit $?
  fi
  exit 1
}

if [ -z "${USEPOD_TOKEN:-}" ]; then
  echo "llm-usepod.sh: USEPOD_TOKEN not set" >&2
  fallback
fi

ENDPOINT="$PROXY_BASE/$USEPOD_TOKEN/v1/chat/completions"
BODY=$(jq -n --arg model "$MODEL" --arg content "$PROMPT" \
  '{model: $model, messages: [{role: "user", content: $content}]}')

# Up to 3 attempts with backoff; transient gateway errors must not kill a run.
ATTEMPTS="${LLM_ATTEMPTS:-3}"
attempt=1
while :; do
  RESP=$(curl -sS --max-time 180 -X POST "$ENDPOINT" \
    -H "Content-Type: application/json" \
    -d "$BODY" 2> >(redact >&2)) || RESP=""

  if [ -n "$RESP" ]; then
    ERR=$(printf '%s' "$RESP" | jq -r '.error.message? // .message? // empty' 2>/dev/null || true)
    CONTENT=$(printf '%s' "$RESP" | jq -r '.choices[0].message.content // empty' 2>/dev/null || true)
    if [ -z "$ERR" ] && [ -n "$CONTENT" ]; then
      printf '%s\n' "$CONTENT"
      exit 0
    fi
    # Fail fast on real 4xx (auth, insufficient balance); retry only transient shapes.
    if [ -n "$ERR" ] && ! printf '%s' "$ERR" | grep -qiE 'timeout|overload|rate|too many|unavailable|gateway|5[0-9][0-9]'; then
      printf '%s' "llm-usepod.sh: API error: $ERR" | redact >&2; echo >&2
      fallback
    fi
  fi

  if [ "$attempt" -ge "$ATTEMPTS" ]; then
    printf '%s' "llm-usepod.sh: failed after $ATTEMPTS attempts: $(printf '%s' "${RESP:-<no response>}" | head -c 300)" | redact >&2; echo >&2
    fallback
  fi
  sleep $(( attempt * 15 ))
  attempt=$(( attempt + 1 ))
done
```

- [ ] **Step 4: Make it executable**

Run: `chmod +x scripts/llm-usepod.sh`
Expected: no output.

- [ ] **Step 5: Run tests to verify they pass**

Run: `bash scripts/advisor/selftest.sh`
Expected: `ok   redact scrubs usepod token`, `ok   redact leaves non-usepod text`, `ok   usepod falls back to Virtuals when token unset`, and final `selftest: ALL PASS`.

- [ ] **Step 6: Syntax-check the new script**

Run: `bash -n scripts/llm-usepod.sh && echo "llm-usepod.sh OK"`
Expected: `llm-usepod.sh OK`

- [ ] **Step 7: Commit**

```bash
git add scripts/llm-usepod.sh scripts/advisor/selftest.sh
git commit -m "feat(advisor): usepod drop-in LLM backend with token redaction + Virtuals fallback"
```

---

## Task 3: Workflow + `.env.example` plumbing

Expose the new vars so the backend flips with a repo variable, no code change. No unit test (YAML/env docs); verified by parse + grep.

**Files:**
- Modify: `.github/workflows/investment-advisor.yml` (env block, currently lines ~17–24)
- Modify: `.env.example`

- [ ] **Step 1: Add env vars to the workflow**

In `.github/workflows/investment-advisor.yml`, find the `env:` block under the
"Prefetch + run advisor" step:

```yaml
        env:
          CLAUDE_CODE_OAUTH_TOKEN: ${{ secrets.CLAUDE_CODE_OAUTH_TOKEN }}
          VIRTUALS_API_KEY: ${{ secrets.VIRTUALS_API_KEY }}
```

Insert these three lines immediately after the `VIRTUALS_API_KEY` line:

```yaml
          USEPOD_TOKEN: ${{ secrets.USEPOD_TOKEN }}
          USEPOD_MODEL: ${{ vars.USEPOD_MODEL }}
          ADVISOR_LLM: ${{ vars.ADVISOR_LLM }}
```

- [ ] **Step 2: Verify the workflow still parses**

Run: `python3 -c "import yaml; yaml.safe_load(open('.github/workflows/investment-advisor.yml')); print('yaml OK')"`
Expected: `yaml OK`

- [ ] **Step 3: Document the vars in `.env.example`**

Append to `.env.example` (create the file if absent):

```bash
# usepod LLM provider (opt-in advisor backend). Enable by setting ADVISOR_LLM=usepod.
# USEPOD_TOKEN: drop-in token from POST https://api.usepod.ai/register
#   (prepaid USDC balance; OpenAI-compatible; text models only). Lives in the
#   request URL path — treat as a secret.
USEPOD_TOKEN=
# Optional: default deepseek-v3.2. Free-text canonical model id from usepod's catalog.
USEPOD_MODEL=
# Backend selector: usepod | claude | virtuals | auto (default). auto = current behavior.
ADVISOR_LLM=
```

- [ ] **Step 4: Verify the docs landed**

Run: `grep -cE '^(USEPOD_TOKEN|USEPOD_MODEL|ADVISOR_LLM)=' .env.example`
Expected: `3` (one assignment line per var).

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/investment-advisor.yml .env.example
git commit -m "chore(advisor): wire USEPOD_TOKEN/USEPOD_MODEL/ADVISOR_LLM into the advisor workflow"
```

---

## Task 4: Full suite + manual verification

- [ ] **Step 1: Run the complete offline suite**

Run: `bash scripts/advisor/selftest.sh`
Expected: all `ok`, final `selftest: ALL PASS`, exit 0. Includes the PR #123 `complete()` checks plus the new selection/redaction/fallback checks.

- [ ] **Step 2: Confirm `auto` is byte-for-byte unchanged behavior**

Run:
```bash
bash -c 'ROOT=/x; '"$(sed -n '/^select_backend() {/,/^}/p' scripts/advisor/run.sh)"'
  CLAUDE_CODE_OAUTH_TOKEN=tok select_backend; echo "$LLM"'
```
Expected: `/x/scripts/llm-claude.sh` (matches pre-change default when a Claude token is present).

- [ ] **Step 3 (optional, requires a real token): live dry run**

Resolve the open assumption (model slug + strict-JSON behavior) without posting:
```bash
USEPOD_TOKEN=<real-token> ADVISOR_LLM=usepod ADVISOR_DRY_RUN=1 ./scripts/advisor/run.sh
```
Expected: `----- REPORT -----` prints a populated `summary` + `recommendations` (NOT the "Report generation incomplete" fallback), and `advisor: DRY_RUN — no POST/Telegram fired (model=deepseek-v3.2 (usepod))`. If the report is empty, check the surfaced `advisor: LLM call failed — …` line (from PR #123) for a redacted reason and adjust `USEPOD_MODEL`.

---

## Self-Review

**Spec coverage:**
- Decision 1 (opt-in third backend) → Task 1 `select_backend` with `auto` default.
- Decision 2 (`ADVISOR_LLM` selector) → Task 1, Step 3 + tests.
- Decision 3 (usepod→Virtuals fallback) → Task 2 `fallback()` + fallback test.
- Decision 4 (default `deepseek-v3.2`, `USEPOD_MODEL` override) → Task 1 label tests + Task 2 `MODEL`.
- Decision 5 (redaction load-bearing) → Task 2 `redact()` + redaction tests + curl `2> >(redact >&2)`.
- Design §1 (new script, contract) → Task 2. §2 (selection) → Task 1. §3 (workflow) → Task 3. §4 (docs) → Task 3.
- Testing section → Tasks 1–2 assertions; fallback test → Task 2.

**Placeholder scan:** none — every code/step is concrete.

**Type/name consistency:** `select_backend`, `redact`, `fallback`, env names `ADVISOR_LLM`/`USEPOD_TOKEN`/`USEPOD_MODEL`/`USEPOD_BASE`, and the `…/proxy/<token>/v1/chat/completions` path are identical across spec, tasks, and tests. `LLM`/`MODEL_LABEL` globals match run.sh usage downstream.
