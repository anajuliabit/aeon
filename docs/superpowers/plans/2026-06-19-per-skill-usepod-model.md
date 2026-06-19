# Per-skill usepod Model Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Let heavy aeon skills run a faster usepod model (`llama-4`) via a new per-skill `usepod_model:` field, so they stop hitting usepod's 120s origin timeout (524) on the slow `deepseek-v3.2` default.

**Architecture:** aeon.yml resolves a per-skill `usepod_model:` and exports `USEPOD_MODEL` before sourcing the (unchanged) `anthropic-gateway.sh`, which already honors it. Also tightens the existing greedy `SKILL_MODEL` regex so it can't capture the new `usepod_model:` value. Config sets `usepod_model: "llama-4"` on the 8 known-heavy skills.

**Tech Stack:** Bash (sed extraction in the GitHub Actions run step), the gateway helper from the prior change. Offline tests in `scripts/advisor/selftest.sh`.

**Branch:** `feat/usepod-per-skill-model` off `main`. Worktree `.worktrees/per-skill-model`.

---

## File Structure

- **Modify** `.github/workflows/aeon.yml` — tighten `SKILL_MODEL` regex (~line 228); add `usepod_model` extraction + `export USEPOD_MODEL` (before the `. scripts/anthropic-gateway.sh` source, ~line 240).
- **Modify** `aeon.yml` (config) — add `usepod_model: "llama-4"` to the 8 heavy skills.
- **Modify** `scripts/advisor/selftest.sh` — offline assertions for the resolution chain + the regex collision.

---

## Task 1: aeon.yml extraction + regex-collision fix

**Files:**
- Modify: `.github/workflows/aeon.yml` (~lines 228, 238–240)
- Test: `scripts/advisor/selftest.sh` (append before the final pass/fail line)

- [ ] **Step 1: Write the tests** (they encode the regex CONTRACT the workflow must adopt)

Append to `scripts/advisor/selftest.sh` before the final `[ "$FAIL" -eq 0 ] && echo "selftest: ALL PASS" ...` line:

```bash
# --- per-skill usepod_model: extraction regexes + resolution chain ---
GWP="$(cd "$(dirname "$0")/.." && pwd)/anthropic-gateway.sh"
PS_DIR="$(mktemp -d)"
cat > "$PS_DIR/aeon.yml" <<'EOF'
gateway:
  provider: usepod
skills:
  heavyskill: { enabled: true, schedule: "0 12 * * *", usepod_model: "llama-4" }
  bothskill: { enabled: true, model: "claude-sonnet-4-6", usepod_model: "llama-4" }
  plainskill: { enabled: true, model: "claude-sonnet-4-6" }
  bareskill: { enabled: true }
EOF
# These two sed expressions MUST match the ones used in .github/workflows/aeon.yml.
skill_model()  { grep "^  $1:" "$PS_DIR/aeon.yml" | sed -n 's/.*[ ,{]model: *"\([^"]*\)".*/\1/p'; }
usepod_model() { grep "^  $1:" "$PS_DIR/aeon.yml" | sed -n 's/.*usepod_model: *"\([^"]*\)".*/\1/p'; }
# Resolve GATEWAY_MODEL the way the workflow will: export USEPOD_MODEL if per-skill set, then source helper.
resolve() { # skill -> GATEWAY_MODEL
  local u; u="$(usepod_model "$1")"
  ( cd "$PS_DIR"; export GATEWAY=usepod USEPOD_TOKEN=T MODEL="$(skill_model "$1")"; \
    [ -n "$u" ] && export USEPOD_MODEL="$u"; . "$GWP" >/dev/null 2>&1; printf '%s' "$GATEWAY_MODEL" )
}
check "usepod_model extracted for heavyskill" "$(usepod_model heavyskill)" "llama-4"
check "usepod_model empty for plainskill"     "$(usepod_model plainskill)" ""
# Regex collision: a line with BOTH model: and usepod_model: must split correctly.
check "SKILL_MODEL not fooled by usepod_model" "$(skill_model bothskill)" "claude-sonnet-4-6"
check "usepod_model on bothskill"              "$(usepod_model bothskill)" "llama-4"
# Resolution chain via the real helper.
check "resolve heavyskill -> llama-4"   "$(resolve heavyskill)" "llama-4"
check "resolve bothskill -> llama-4"    "$(resolve bothskill)" "llama-4"
check "resolve plainskill -> deepseek"  "$(resolve plainskill)" "deepseek-v3.2"
check "resolve bareskill -> deepseek"   "$(resolve bareskill)" "deepseek-v3.2"
# Workflow var wins over default when no per-skill override.
check "resolve var-default for plainskill" "$( cd "$PS_DIR"; export GATEWAY=usepod USEPOD_TOKEN=T USEPOD_MODEL=qwen-3.5 MODEL=claude-sonnet-4-6; . "$GWP" >/dev/null 2>&1; printf '%s' "$GATEWAY_MODEL" )" "qwen-3.5"
```

- [ ] **Step 2: Run the tests**

Run: `bash scripts/advisor/selftest.sh`
Expected: these checks PASS immediately — they validate the regex strings + helper resolution, which are correct by construction. (This task is unusual: the unit under test is two sed regexes + the existing helper, so the test encodes the contract rather than driving a red→green on new code. The red→green gate is Step 4, which fails until the workflow actually adopts these exact regexes.) If any check FAILS here, a regex string is wrong — fix it before editing the workflow. Final line should read `selftest: ALL PASS`.

- [ ] **Step 3: Edit `.github/workflows/aeon.yml`**

3a. Tighten the `SKILL_MODEL` regex. Find (~line 228):
```bash
          SKILL_MODEL=$(grep "^  ${SKILL_NAME}:" aeon.yml | sed -n 's/.*model: *"\([^"]*\)".*/\1/p')
```
Replace with:
```bash
          SKILL_MODEL=$(grep "^  ${SKILL_NAME}:" aeon.yml | sed -n 's/.*[ ,{]model: *"\([^"]*\)".*/\1/p')
```

3b. Add the usepod_model extraction. Find:
```bash
          echo "Using model: $MODEL"
          echo "SKILL_MODEL=$MODEL" >> "$GITHUB_OUTPUT"

          # --- AI Gateway routing (shared resolver; sets ANTHROPIC_BASE_URL + GATEWAY_MODEL) ---
```
Insert between the `echo "SKILL_MODEL=$MODEL" ...` line and the `# --- AI Gateway routing` comment (preserve 10-space indent):
```bash
          # Per-skill usepod model override (heavy skills run a faster model to avoid
          # usepod's 120s origin timeout). Only affects the usepod gateway; direct/bankr
          # still use the per-skill `model:` (claude-*) above.
          SKILL_USEPOD_MODEL=$(grep "^  ${SKILL_NAME}:" aeon.yml | sed -n 's/.*usepod_model: *"\([^"]*\)".*/\1/p')
          [ -n "$SKILL_USEPOD_MODEL" ] && export USEPOD_MODEL="$SKILL_USEPOD_MODEL"
```

- [ ] **Step 4: Verify workflow parses + uses the exact regexes the tests validate**

Run:
```bash
python3 -c "import yaml; yaml.safe_load(open('.github/workflows/aeon.yml')); print('yaml OK')"
grep -c 's/.*\[ ,{\]model: \*"' .github/workflows/aeon.yml
grep -c 's/.*usepod_model: \*"' .github/workflows/aeon.yml
```
Expected: `yaml OK`, then `1` (tightened SKILL_MODEL regex present) and `1` (usepod_model extraction present).

- [ ] **Step 5: Re-run the suite**

Run: `bash scripts/advisor/selftest.sh`
Expected: the new checks `ok`, final `selftest: ALL PASS`.

- [ ] **Step 6: Commit**

```bash
git add .github/workflows/aeon.yml scripts/advisor/selftest.sh
git commit -m "feat(gateway): per-skill usepod_model override + fix greedy SKILL_MODEL regex"
```

---

## Task 2: Set `usepod_model: "llama-4"` on the heavy skills

**Files:**
- Modify: `aeon.yml` (config; the 8 heavy skill entries)

- [ ] **Step 1: Add the field to each heavy skill**

In `aeon.yml`, add `usepod_model: "llama-4"` inside the `{ ... }` of each entry below (insert before the closing `}`; keep existing fields and any trailing `# comment`). Example for `market-context-refresh`:
```yaml
  market-context-refresh: { enabled: true, schedule: "0 13 * * *", model: "claude-sonnet-4-6", usepod_model: "llama-4" } # fetch live crypto macro data, update memory
```
Apply to all 8:
- `market-context-refresh`
- `defi-overview`
- `defi-monitor`
- `token-movers`
- `token-pick`
- `on-chain-monitor`
- `narrative-tracker`
- `aixbt-pulse`

- [ ] **Step 2: Verify the config parses + all 8 carry the field**

Run:
```bash
python3 -c "import yaml; yaml.safe_load(open('aeon.yml')); print('aeon.yml valid')"
for s in market-context-refresh defi-overview defi-monitor token-movers token-pick on-chain-monitor narrative-tracker aixbt-pulse; do
  grep -q "^  $s:.*usepod_model: \"llama-4\"" aeon.yml && echo "$s OK" || echo "$s MISSING"
done
```
Expected: `aeon.yml valid`, then `OK` for all 8.

- [ ] **Step 3: Confirm resolution end-to-end against the real config**

Run (a real heavy skill resolves to llama-4; a non-listed one stays deepseek):
```bash
GWP="$(pwd)/scripts/anthropic-gateway.sh"
for s in market-context-refresh heartbeat; do
  u=$(grep "^  $s:" aeon.yml | sed -n 's/.*usepod_model: *"\([^"]*\)".*/\1/p')
  ( export GATEWAY=usepod USEPOD_TOKEN=T MODEL=x; [ -n "$u" ] && export USEPOD_MODEL="$u"; . "$GWP" >/dev/null 2>&1; echo "$s -> $GATEWAY_MODEL" )
done
```
Expected: `market-context-refresh -> llama-4`, `heartbeat -> deepseek-v3.2`.

- [ ] **Step 4: Commit**

```bash
git add aeon.yml
git commit -m "config(gateway): route 8 heavy skills to llama-4 on usepod"
```

---

## Task 3: Full suite + final review

- [ ] **Step 1: Run the complete offline suite**

Run: `bash scripts/advisor/selftest.sh`
Expected: all `ok`, final `selftest: ALL PASS`, exit 0.

- [ ] **Step 2: Confirm direct gateway unaffected**

Run:
```bash
GWP="$(pwd)/scripts/anthropic-gateway.sh"
( export GATEWAY=direct MODEL=claude-opus-4-7; . "$GWP" >/dev/null 2>&1; echo "direct -> $GATEWAY_MODEL" )
```
Expected: `direct -> claude-opus-4-7` (per-skill usepod_model has no effect off usepod).

- [ ] **Step 3 (operator, needs token): dry-run ONE heavy skill before trusting the set**

```bash
gh workflow run aeon.yml -f skill=market-context-refresh -R anajuliabit/aeon
# then check the run log for: ::notice::Routing through usepod (... model=llama-4) and a clean completion (no 4xx model error)
```
Expected: routes on `llama-4` and completes. If usepod rejects `llama-4` (wrong slug), the skill errors — fix the slug once in aeon.yml (or remove the lines to fall back to `deepseek-v3.2`).

---

## Self-Review

**Spec coverage:**
- §1 mechanism (export USEPOD_MODEL per-skill; helper unchanged) → Task 1 Step 3b.
- §1 SKILL_MODEL regex-collision fix → Task 1 Step 3a + collision tests.
- §2 config `usepod_model: "llama-4"` on the 8 heavy skills → Task 2.
- §3 testing (chain: per-skill→llama-4, none→deepseek, var-wins; collision) → Task 1 Step 1.
- §4 boundaries/rollback (only aeon.yml + selftest; helper/messages/advisor untouched) → Tasks 1–2 scope; Task 3 Step 2 confirms direct gateway unaffected.
- Open assumption (llama-4 slug) → Task 3 Step 3 dry-run.

**Placeholder scan:** none — concrete code/commands.

**Type/name consistency:** the two sed regexes (`s/.*[ ,{]model: *"..."` and `s/.*usepod_model: *"..."`) are identical in the test (Task 1 Step 1) and the workflow (Step 3); Step 4 greps the workflow to enforce they match. Field name `usepod_model`, value `llama-4`, env `USEPOD_MODEL`, and default `deepseek-v3.2` are consistent across tests, workflow, config, and the helper.
