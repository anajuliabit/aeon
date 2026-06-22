# Security Scan — 2026-06-22

**Verdict:** ATTENTION (4 persistent HIGH findings; 0 NEW, 0 RESOLVED)
**Scope:** full corpus (191 SKILL.md + 9 workflows + 19 repo scripts + 8 advisor scripts + 1 companion script = 228 files)
**Scanner mode:** inline_grep_fallback — `scan.sh` execution blocked by the sandbox approval gate (same path as 2026-05-25 / 2026-06-01 / 2026-06-15 runs); inline Grep over `scan.sh`'s HIGH/MEDIUM/LOW pattern library + manual GitHub Actions script-injection audit of every `${{ }}` expression in `run:` blocks per SKILL.md step 4 sandbox fallback. Never silently skipped.
**Counts:** 228 files scanned · **4 HIGH** · 15 MEDIUM · 4 LOW · **0 new** · **0 resolved** since last scan
**Exit status:** `SECURITY_SCAN_NOCHANGE`

## Needs attention (NEW high-severity this run)

None. No NEW HIGH findings.

## Resolved since last scan

None. No HIGH findings were resolved between 2026-06-15 and today.

## Persistent findings (unchanged)

| # | File | Line | Pattern | Delta | Note |
|---|------|------|---------|-------|------|
| 1 | `.github/workflows/aeon.yml` | 86 | `echo "name=${{ inputs.skill }}" >> "$GITHUB_OUTPUT"` | PERSISTENT | `inputs.skill` interpolated into `run:` block. Workflow_dispatch/workflow_call gated → requires repo write access → low real risk. Same anti-pattern as 2026-04-11 messages.yml incident. |
| 2 | `.github/workflows/aeon.yml` | 94 | `if [ -n "${{ steps.skill.outputs.name }}" ]; then` | PERSISTENT | `steps.skill.outputs.name` is the value of `inputs.skill` echoed at L86 — same risk profile. |
| 3 | `.github/workflows/aeon.yml` | 96 | `echo "label=${{ steps.skill.outputs.name }}" >> "$GITHUB_OUTPUT"` | PERSISTENT | Same chain as #2. |
| 4 | `.github/workflows/aeon.yml` | 812 | `LABEL="${{ steps.work.outputs.label }}"` | PERSISTENT_LINE_DRIFT | Was `:849` at 2026-06-15 (and `:725` at 06-01, `:718` at baseline). Code drift shifted the line down 37 lines; content + pattern unchanged. Derived from `steps.skill.outputs.name` → `inputs.skill`. |

**Remediation (single canonical fix for all 4 sites)** — apply the env: indirection pattern already used by `chain-runner.yml:41,368` (ISS-017 fix) and `messages.yml:612-616, 684-685` (post-2026-04-11 fix):

```yaml
- name: Determine skill
  id: skill
  env:
    _INPUT_SKILL: ${{ inputs.skill }}
  run: |
    if [ "${{ github.event_name }}" = "workflow_dispatch" ] || [ "${{ github.event_name }}" = "workflow_call" ]; then
      echo "name=$_INPUT_SKILL" >> "$GITHUB_OUTPUT"
    elif [ "${{ github.event_name }}" = "issues" ]; then
      echo "name=feature" >> "$GITHUB_OUTPUT"
    fi
```

The same rebind pattern (`env: _SKILL_NAME: ${{ steps.skill.outputs.name }}` then read `$_SKILL_NAME`) closes all four sites. No new ISS filed — this anti-pattern has been documented and accepted as low-real-risk since baseline (workflow_dispatch/workflow_call require repo write access; no external attacker reaches `inputs.skill`).

## Additional unindirected sites in aeon.yml (informational — same risk class as the 4 PERSISTENT above)

`aeon.yml` contains additional `${{ inputs.* }}` / `${{ steps.*.outputs.* }}` expressions interpolated directly into `run:` blocks rather than via `env:` rebinding. These are downstream sites of the same `inputs.skill` chain (L86) and the same `steps.run.outputs.*` token-count chain — they share the canonical-4 risk profile (workflow_dispatch-gated, low real risk) and are listed here for completeness. They are **not** counted as additional HIGH findings (consistent with the 2026-05-25 → 2026-06-15 tracking convention of reporting only the canonical entry-point sites).

| Line | Expression | Source chain |
|------|------------|--------------|
| 132 | `SKILL_FILE="skills/${{ steps.skill.outputs.name }}/SKILL.md"` | inputs.skill |
| 178 | `SKILL="${{ steps.skill.outputs.name }}"` | inputs.skill |
| 224 | `SKILL_NAME="${{ steps.skill.outputs.name }}"` | inputs.skill |
| 229 | `INPUT_MODEL="${{ inputs.model }}"` | inputs.model (workflow_dispatch input) |
| 409 | `SKILL_NAME="${{ steps.skill.outputs.name }}"` | inputs.skill |
| 413 | `CHAIN_CTX="${{ inputs.chain_context_file }}"` | inputs.chain_context_file (workflow_call input) |
| 536-541, 559 | `INPUT="${{ steps.run.outputs.SKILL_*_TOKENS }}"` (×6) | jq-derived integers from anthropic-gateway response |
| 564, 587, 876 | `SKILL="${{ steps.skill.outputs.name }}"` (×3) | inputs.skill |
| 880 | `QUALITY_SCORE="${{ steps.analyze.outputs.QUALITY_SCORE }}"` | step-internal integer |

**Recommendation:** if/when the canonical-4 are remediated via env: indirection, apply the same fix to these downstream sites in the same PR. Until then, no action required — same risk profile as canonical-4 (privileged-dispatch only).

## Other workflows — clean

- **`.github/workflows/chain-runner.yml`** — L41 + L368 use `_CHAIN: ${{ inputs.chain }}` env: indirection; shell reads `$_CHAIN`. **ISS-017 fix held.**
- **`.github/workflows/messages.yml`** — L612-616 (`_INPUT_MESSAGE`, `_INPUT_SOURCE`, `_EVENT_NAME`, `_EVENT_ACTION`, `_PAYLOAD_MESSAGE`) and L684-685 (`_MSG_SOURCE`, `_MSG_MESSAGE`) and L838-863 (`_LOG_*`, `_COMMIT_SOURCE`) all use env: indirection. **2026-04-11 incident-class fix held across every site.**
- **`.github/workflows/replicate-oneoff.yml`** — L52-55 (`PROMPT`, `OUTPUT_PATH`, `ASPECT`, `MODEL`) and L78 (`OUTPUT_PATH`) all in `env:` blocks. Shell reads `"$PROMPT"`, `"$OUTPUT_PATH"`. Safe.
- **`.github/workflows/sync-upstream.yml`** — L66 / L73-75 interpolate `${{ steps.merge.outputs.branch }}` etc. directly into `run:`, but those step outputs are computed from internal date math and `git ... --jq` numeric counts in earlier steps (not user-controlled). Same low-real-risk anti-pattern as the aeon.yml downstream sites; informational only.
- **`.github/workflows/investment-advisor.yml`** + **`weekly-conviction.yml`** — no `${{ }}` → `run:` injection (cron-only, no inputs).
- **`.github/workflows/ci-packs-json.yml`** + **`ci-skills-json.yml`** — no `${{ }}` → `run:` injection.

## Companion + repo scripts — clean

- **`scripts/advisor/selftest.sh:31`** — `DIR_IN="rm -rf /"; case "$DIR_IN" in increase|decrease|hold|hedge) DIR_OUT="$DIR_IN" ;; *) DIR_OUT="hold" ;; esac` — defensive test fixture proving the direction sanitizer defangs malicious input. The string is never executed (allowlist case defaults to `hold`). `real_risk: false`.
- **`scripts/advisor/selftest.sh:220, :252`** — `eval "$(sed -n '/^foo() {/,/^}/p' "$..."/run.sh")"` — internal helper extraction from same-repo `run.sh`/`llm-usepod.sh` to expose private functions for unit testing. Trusted-source (same-repo) content; no external data path. Safe.
- **All other repo scripts** (`scripts/*.sh`) — no `eval` of external data, no curl/wget piping secrets to non-intended hosts (Telegram/Discord/Slack/Anthropic/CoinGecko/DefiLlama/Railway/Hyperliquid/GeckoTerminal/Replicate/Vercel/X.AI only), no `rm -rf /`, no force-push to main.

## SKILL.md curl-with-secret matches (MEDIUM after code-fence downgrade)

~80+ raw matches across `skills/*/SKILL.md` of `curl ... $VAR` patterns (e.g. `curl "...?apikey=$ETHERSCAN_API_KEY"`, `curl -H "Authorization: Bearer $XAI_API_KEY"`). **All** are inside ```` ```bash ```` fenced code blocks documenting integration patterns — the actual execution path is `scripts/prefetch-*.sh` with full env access, NOT the skill body. Per SKILL.md step 7 (code-fence downgrade), HIGH → MEDIUM. Existing baseline entries for `skills/security-digest/SKILL.md` cover the canonical fenced examples (`scan-baseline.yml` L44-53); the remaining ~75 matches are the same documentation pattern and remain at MEDIUM. No action needed.

## Obfuscation sweep — clean

- **Zero-width / bidi Unicode** (`U+200B`, `U+FEFF`, `U+202E`): no matches in any tracked file.
- **`fromCharCode`**: no matches.
- **`base64 -d` / `base64 --decode` piped to shell**: zero matches of the dangerous "decode-then-execute" shape. All `base64 -d` occurrences decode `gh api .../contents/*` responses (GitHub API returns base64-encoded file contents) or build a JSON payload via `jq` — none pipe to a shell.
- **SSRF/webhook hosts** (`ngrok`, `interact.sh`, `webhook.site`, `burpcollaborator`, `pipedream`, `requestbin`): no matches in active code; one benign README.md mention of "ngrok" as an example tunnel option, and one prose mention in `add-a2a` doc comments.

## Per-file results (summary)

| File | Status | HIGH | MEDIUM | LOW |
|------|--------|------|--------|-----|
| `.github/workflows/aeon.yml` | **FAIL** | 4 (canonical) + ~13 downstream same-chain | 2 | 1 |
| `.github/workflows/chain-runner.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/messages.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/replicate-oneoff.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/sync-upstream.yml` | WARN | 0 | 4 (step-output interpolation, internal-only) | 0 |
| `.github/workflows/investment-advisor.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/weekly-conviction.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/ci-packs-json.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/ci-skills-json.yml` | PASS | 0 | 0 | 0 |
| `scripts/*.sh` (19) | PASS (all) | 0 | 0 | 0 |
| `scripts/advisor/*.sh` (8) | PASS (incl. selftest fixture) | 0 | 0 | 0 |
| `skills/*/SKILL.md` (191) | mostly PASS; ~80 MEDIUM in fenced code-block curl examples | 0 (post code-fence downgrade) | ~80 (docs in fenced blocks) | ~3 |
| `skills/skill-security-scan/scan.sh` | PASS | 0 | 0 | 0 |

## Appendix — current finding set fingerprints

```
aeon.yml:86:inputs.skill                       — PERSISTENT
aeon.yml:94:steps.skill.outputs.name           — PERSISTENT
aeon.yml:96:steps.skill.outputs.name           — PERSISTENT
aeon.yml:812:steps.work.outputs.label          — PERSISTENT_LINE_DRIFT (was :849 on 06-15)
```

No `memory/issues/INDEX.md` updates required — all four findings have been the documented PERSISTENT set since baseline, none rise to a new ISS, and no ISS-filed finding resolved this run.
