# usepod Primary Gateway Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Route the agentic Claude Code CLI surfaces (aeon skill fleet + chat primary) through usepod's Anthropic-compatible endpoint, so the fleet runs on a funded provider instead of failing on Claude's weekly limit + Virtuals' empty credits.

**Architecture:** A new sourced `scripts/anthropic-gateway.sh` resolves `gateway.provider` (from `aeon.yml`, env-overridable) and exports `ANTHROPIC_BASE_URL`/`ANTHROPIC_AUTH_TOKEN`/`GATEWAY_MODEL` for the `claude` CLI — adding a `usepod` branch (token-in-URL, redacted, model→`deepseek-v3.2`) while reproducing `bankr`/`virtuals`/`direct` exactly. `aeon.yml` and `messages.yml` source it; flipping `gateway.provider: usepod` switches both.

**Tech Stack:** Bash (helper is bash-3.2-safe for the macOS selftest), GitHub Actions, the `claude` CLI's `ANTHROPIC_BASE_URL` override. Offline tests in `scripts/advisor/selftest.sh`.

**Branch:** `feat/usepod-gateway` off `main`. Worktree `.worktrees/usepod-gateway`.

---

## File Structure

- **Create** `scripts/anthropic-gateway.sh` — sourced; resolves provider + exports gateway env. The only real logic; unit-tested.
- **Modify** `.github/workflows/aeon.yml` — replace the inline gateway block (~lines 239–267) with `. scripts/anthropic-gateway.sh`; primary skill `claude -p` uses `$GATEWAY_MODEL`; add `USEPOD_TOKEN`/`USEPOD_MODEL` env.
- **Modify** `aeon.yml` (config) — `gateway.provider: direct` → `usepod`.
- **Modify** `.github/workflows/messages.yml` — source the helper before the primary `claude -p`; use `$GATEWAY_MODEL`.
- **Modify** `scripts/advisor/selftest.sh` — offline assertions for the helper.

---

## Task 1: `scripts/anthropic-gateway.sh`

Sourced gateway resolver. Exports env for the `claude` CLI; redacts the usepod token in its notice.

**Files:**
- Create: `scripts/anthropic-gateway.sh`
- Test: `scripts/advisor/selftest.sh` (append before the final pass/fail line)

- [ ] **Step 1: Write the failing tests**

Append to `scripts/advisor/selftest.sh` before the final `[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" ...` line:

```bash
# --- anthropic-gateway.sh: provider resolution + usepod routing (sourced) ---
GW="$(cd "$(dirname "$0")/.." && pwd)/anthropic-gateway.sh"
# Source in a subshell with controlled env; echo the resolved exports.
gw() { # GATEWAY, USEPOD_TOKEN, USEPOD_MODEL, MODEL  -> "BASEURL|MODEL|AUTH"
  ( export GATEWAY="$1" USEPOD_TOKEN="${2-}" USEPOD_MODEL="${3-}" MODEL="${4-}" \
      BANKR_LLM_KEY="" VIRTUALS_API_KEY=""
    . "$GW" >/dev/null 2>&1
    printf '%s|%s|%s' "${ANTHROPIC_BASE_URL:-}" "${GATEWAY_MODEL:-}" "${ANTHROPIC_AUTH_TOKEN:-}" )
}
check "gw usepod base url"   "$(gw usepod SECRET '' claude-opus-4-7 | cut -d'|' -f1)" "https://api.usepod.ai/proxy/SECRET"
check "gw usepod model default" "$(gw usepod SECRET '' claude-opus-4-7 | cut -d'|' -f2)" "deepseek-v3.2"
check "gw usepod model override" "$(gw usepod SECRET qwen-3.5 claude-opus-4-7 | cut -d'|' -f2)" "qwen-3.5"
check "gw usepod auth literal" "$(gw usepod SECRET '' x | cut -d'|' -f3)" "unused"
check "gw direct no base url" "$(gw direct '' '' claude-opus-4-7 | cut -d'|' -f1)" ""
check "gw direct keeps model" "$(gw direct '' '' claude-opus-4-7 | cut -d'|' -f2)" "claude-opus-4-7"
check "gw bankr base url"     "$( ( export GATEWAY=bankr BANKR_LLM_KEY=k USEPOD_TOKEN='' VIRTUALS_API_KEY='' MODEL=m; . "$GW" >/dev/null 2>&1; printf '%s' "${ANTHROPIC_BASE_URL:-}") )" "https://llm.bankr.bot"
check "gw virtuals base url"  "$( ( export GATEWAY=virtuals VIRTUALS_API_KEY=k USEPOD_TOKEN='' BANKR_LLM_KEY='' MODEL=m; . "$GW" >/dev/null 2>&1; printf '%s' "${ANTHROPIC_BASE_URL:-}") )" "https://compute.virtuals.io"
# Redaction: the usepod notice must NOT leak the token.
GW_NOTICE="$( ( export GATEWAY=usepod USEPOD_TOKEN=SUPERSECRET MODEL=x; . "$GW" 2>/dev/null ) )"
check "gw usepod notice redacted" "$(printf '%s' "$GW_NOTICE" | grep -c 'SUPERSECRET')" "0"
check "gw usepod notice has marker" "$(printf '%s' "$GW_NOTICE" | grep -c '<redacted>')" "1"
# Missing token -> non-zero.
( export GATEWAY=usepod USEPOD_TOKEN='' MODEL=x; . "$GW" >/dev/null 2>&1 ); check "gw usepod missing token fails" "$?" "1"
# Provider from aeon.yml config when GATEWAY unset.
GW_CFG_DIR="$(mktemp -d)"; printf 'gateway:\n  provider: usepod\n' > "$GW_CFG_DIR/aeon.yml"
check "gw reads provider from aeon.yml" "$( cd "$GW_CFG_DIR" && ( export USEPOD_TOKEN=T MODEL=x; unset GATEWAY; . "$GW" >/dev/null 2>&1; printf '%s' "${GATEWAY:-}") )" "usepod"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `bash scripts/advisor/selftest.sh`
Expected: FAIL — helper missing, `. "$GW"` errors; assertions mismatch. Final `selftest: FAILURES`.

- [ ] **Step 3: Create `scripts/anthropic-gateway.sh`**

```bash
#!/usr/bin/env bash
# scripts/anthropic-gateway.sh — resolve the LLM gateway for the Claude Code CLI.
# SOURCE this (`. scripts/anthropic-gateway.sh`); it EXPORTS GATEWAY,
# ANTHROPIC_BASE_URL, ANTHROPIC_AUTH_TOKEN, and GATEWAY_MODEL into the caller.
#
# Provider precedence: $GATEWAY env override > aeon.yml `gateway.provider` > direct.
# usepod is Anthropic-compatible (`/v1/messages`) with the token IN THE URL PATH, so
# the token never goes in a header — and the notice redacts it (GitHub also masks the
# USEPOD_TOKEN secret). Never `set -x` around this. Returns non-zero (when sourced) on
# a misconfigured provider so the caller can fail the step.
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
```

- [ ] **Step 4: Make it executable**

Run: `chmod +x scripts/anthropic-gateway.sh`
Expected: no output.

- [ ] **Step 5: Run tests to verify they pass**

Run: `bash scripts/advisor/selftest.sh`
Expected: the new `gw …` checks all `ok`, final `selftest: ALL PASS`.

- [ ] **Step 6: Syntax-check**

Run: `bash -n scripts/anthropic-gateway.sh && echo "anthropic-gateway.sh OK"`
Expected: `anthropic-gateway.sh OK`

- [ ] **Step 7: Commit**

```bash
git add scripts/anthropic-gateway.sh scripts/advisor/selftest.sh
git commit -m "feat(gateway): anthropic-gateway.sh — sourced provider resolver with usepod branch"
```

---

## Task 2: Wire `aeon.yml` to the helper + flip provider to usepod

**Files:**
- Modify: `.github/workflows/aeon.yml` (gateway block ~239–267; primary claude call ~449; job env)
- Modify: `aeon.yml` (config `gateway.provider`)

- [ ] **Step 1: Add USEPOD env to the aeon.yml job**

In `.github/workflows/aeon.yml`, find the env block of the skill-running job (it already has `VIRTUALS_API_KEY: ${{ secrets.VIRTUALS_API_KEY }}`). Add immediately after that line:

```yaml
          USEPOD_TOKEN: ${{ secrets.USEPOD_TOKEN }}
          USEPOD_MODEL: ${{ vars.USEPOD_MODEL }}
```
(Match the existing indentation of the surrounding env keys.)

- [ ] **Step 2: Replace the inline gateway block with the helper**

Find this EXACT block (preserve 10-space YAML indentation):

```bash
          # --- AI Gateway routing ---
          GATEWAY=$(grep -A1 '^gateway:' aeon.yml | grep 'provider:' | sed 's/.*provider: *//' | tr -d ' "'"'" || echo "direct")
          GATEWAY="${GATEWAY:-direct}"
          echo "Gateway: $GATEWAY"

          echo "GATEWAY=$GATEWAY" >> "$GITHUB_OUTPUT"

          if [ "$GATEWAY" = "bankr" ]; then
            if [ -z "${BANKR_LLM_KEY:-}" ]; then
              echo "::error::gateway.provider=bankr but BANKR_LLM_KEY secret is not set"
              exit 1
            fi
            export ANTHROPIC_BASE_URL="https://llm.bankr.bot"
            export ANTHROPIC_AUTH_TOKEN="$BANKR_LLM_KEY"
            unset ANTHROPIC_API_KEY
            unset CLAUDE_CODE_OAUTH_TOKEN
            echo "::notice::Routing through Bankr Gateway (https://llm.bankr.bot)"
          elif [ "$GATEWAY" = "virtuals" ]; then
            if [ -z "${VIRTUALS_API_KEY:-}" ]; then
              echo "::error::gateway.provider=virtuals but VIRTUALS_API_KEY secret is not set"
              exit 1
            fi
            export ANTHROPIC_BASE_URL="https://compute.virtuals.io"
            export ANTHROPIC_AUTH_TOKEN="$VIRTUALS_API_KEY"
            unset ANTHROPIC_API_KEY
            unset CLAUDE_CODE_OAUTH_TOKEN
            echo "::notice::Routing through Virtuals Gateway (https://compute.virtuals.io)"
          else
            echo "::notice::Using direct Anthropic API"
          fi
```

Replace with:

```bash
          # --- AI Gateway routing (shared resolver; sets ANTHROPIC_BASE_URL + GATEWAY_MODEL) ---
          # MUST use `|| exit 1`: set -e does NOT abort on a sourced script's return,
          # so without this a misconfigured provider would run against a bad base URL.
          . scripts/anthropic-gateway.sh || exit 1
          echo "Gateway: $GATEWAY"
          echo "GATEWAY=$GATEWAY" >> "$GITHUB_OUTPUT"
```

- [ ] **Step 3: Use `$GATEWAY_MODEL` for the primary skill call**

Find (the primary skill invocation, ~line 449):

```bash
          CLAUDE_OUTPUT=$(echo "$PROMPT" | claude -p - \
            --model "$MODEL" --allowedTools "$ALLOWED" \
```

Change `--model "$MODEL"` to `--model "$GATEWAY_MODEL"` on that call ONLY. Do NOT change the Virtuals LiteLLM-shim call (`--model "${VIRTUALS_MODEL:-claude-opus-4-8}"`, ~line 484) or the hardcoded-haiku analysis scorer (`--model claude-haiku-4-5-20251001`, ~line 661) — those are intentional.

- [ ] **Step 4: Flip the config provider to usepod**

In `aeon.yml` (the config file at repo root), change:

```yaml
gateway:
  provider: direct
```
to:
```yaml
gateway:
  provider: usepod
```

- [ ] **Step 5: Verify workflow parses + gateway env reachable**

Run:
```bash
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/aeon.yml')); print('yaml OK')"
GATEWAY=usepod USEPOD_TOKEN=T MODEL=claude-opus-4-7 bash -c '. scripts/anthropic-gateway.sh >/dev/null 2>&1; echo "$ANTHROPIC_BASE_URL $GATEWAY_MODEL"'
```
Expected: `yaml OK`, then `https://api.usepod.ai/proxy/T deepseek-v3.2`.

- [ ] **Step 6: Confirm config flipped**

Run: `grep -A1 '^gateway:' aeon.yml | grep provider`
Expected: `  provider: usepod`

- [ ] **Step 7: Commit**

```bash
git add .github/workflows/aeon.yml aeon.yml
git commit -m "feat(gateway): route aeon skill fleet through usepod (shared resolver, provider=usepod)"
```

---

## Task 3: Route `messages.yml` chat primary through the helper

**Files:**
- Modify: `.github/workflows/messages.yml` (MODEL resolution ~688–689; primary `claude -p` ~771)

- [ ] **Step 1: Ensure USEPOD env present in the chat job**

Confirm the chat job's env block has `USEPOD_TOKEN`/`USEPOD_MODEL` (added in the prior research-fallback change). If absent, add after `VIRTUALS_API_KEY`:

```yaml
          USEPOD_TOKEN: ${{ secrets.USEPOD_TOKEN }}
          USEPOD_MODEL: ${{ vars.USEPOD_MODEL }}
```
Run to check: `grep -c 'USEPOD_TOKEN' .github/workflows/messages.yml` — expect ≥1.

- [ ] **Step 2: Source the gateway after MODEL is resolved**

Find:

```bash
          CONFIG_MODEL=$(grep -E '^model:' aeon.yml | sed 's/^model: *//' | tr -d ' ')
          MODEL="${CONFIG_MODEL:-claude-opus-4-7}"
```

Add immediately after those two lines:

```bash
          # Route the primary agentic chat through the shared gateway (usepod = agentic
          # on usepod with tools; far better than the text-only fallback below).
          # `|| exit 1`: set -e won't abort on a sourced return (see helper header).
          . scripts/anthropic-gateway.sh || exit 1
```

- [ ] **Step 3: Use `$GATEWAY_MODEL` for the primary chat call**

Find (~line 771):

```bash
          CLAUDE_OUTPUT=$(echo "$PROMPT" | claude -p - \
            --model "$MODEL" --allowedTools "$ALLOWED" \
```

Change `--model "$MODEL"` to `--model "$GATEWAY_MODEL"`.

- [ ] **Step 4: Verify**

Run:
```bash
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/messages.yml')); print('yaml OK')"
python3 -c "
import yaml, re
d=yaml.safe_load(open('.github/workflows/messages.yml'))
runs=[s.get('run','') for j in d['jobs'].values() for s in j.get('steps',[])]
blob=next(r for r in runs if 'CLAUDE_OK' in r and 'anthropic-gateway.sh' in r)
print('sourced + GATEWAY_MODEL used' if 'GATEWAY_MODEL' in blob else 'MISSING')
"
```
Expected: `yaml OK` then `sourced + GATEWAY_MODEL used`.

- [ ] **Step 5: Commit**

```bash
git add .github/workflows/messages.yml
git commit -m "feat(gateway): route chat primary through usepod (agentic, shared resolver)"
```

---

## Task 4: Full suite + final review

- [ ] **Step 1: Run the complete offline suite**

Run: `bash scripts/advisor/selftest.sh`
Expected: all `ok`, final `selftest: ALL PASS`, exit 0 (prior checks + the new `gw` checks).

- [ ] **Step 2: Confirm direct/bankr/virtuals unregressed**

Run:
```bash
for p in direct bankr virtuals; do
  GATEWAY=$p BANKR_LLM_KEY=k VIRTUALS_API_KEY=k MODEL=claude-opus-4-7 \
    bash -c '. scripts/anthropic-gateway.sh >/dev/null 2>&1; echo "'"$p"': base=[${ANTHROPIC_BASE_URL:-none}] model=$GATEWAY_MODEL"'
done
```
Expected: `direct: base=[none] model=claude-opus-4-7`, `bankr: base=[https://llm.bankr.bot] …`, `virtuals: base=[https://compute.virtuals.io] …`.

- [ ] **Step 3: Confirm token never prints unredacted**

Run: `GATEWAY=usepod USEPOD_TOKEN=LEAKCHECK MODEL=x bash -c '. scripts/anthropic-gateway.sh 2>&1' | grep -c LEAKCHECK`
Expected: `0` (the notice shows `<redacted>`; the token is only ever in the exported `ANTHROPIC_BASE_URL`, never echoed).

---

## Self-Review

**Spec coverage:**
- §1 helper (provider precedence, usepod branch, redaction, exports) → Task 1 + assertions.
- §2 aeon.yml (config flip, source helper, `$GATEWAY_MODEL`, env) → Task 2.
- §3 messages.yml chat primary → Task 3.
- §4 boundaries (bankr/virtuals/direct preserved; advisor/weekly untouched; Virtuals shim + haiku scorer left) → Task 2 Steps 2–3 explicitly exclude lines 484/661; no run.sh/run-weekly changes.
- Testing (usepod base/model/auth, redaction, missing-token, direct/bankr/virtuals, config-read) → Task 1 + Task 4.

**Placeholder scan:** none — concrete code/commands throughout.

**Type/name consistency:** `scripts/anthropic-gateway.sh`, exported `GATEWAY`/`ANTHROPIC_BASE_URL`/`ANTHROPIC_AUTH_TOKEN`/`GATEWAY_MODEL`, env `USEPOD_TOKEN`/`USEPOD_MODEL`, default `deepseek-v3.2`, and the `<redacted>` marker are identical across the helper, both workflows, and the tests. Both workflows source the helper after `MODEL` is set and call `claude -p --model "$GATEWAY_MODEL"`.
