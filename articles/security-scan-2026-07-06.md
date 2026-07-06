# Security Scan — 2026-07-06

**Verdict:** ATTENTION (4 persistent HIGH findings; 0 NEW, 0 RESOLVED)
**Scope:** full corpus (191 SKILL.md + 9 workflows + 30 repo scripts + 1 companion script = 231 files)
**Scanner mode:** inline_grep_fallback — `scan.sh` execution blocked by the sandbox approval gate (same path as 2026-05-25 / 2026-06-01 / 2026-06-15 / 2026-06-22 / 2026-06-29 runs); inline Grep over `scan.sh`'s HIGH/MEDIUM/LOW pattern library + manual GitHub Actions script-injection audit of every `${{ }}` expression in `run:` blocks, per SKILL.md step 4 sandbox fallback. Never silently skipped.
**Counts:** 231 files scanned · **4 HIGH** · 15 MEDIUM · 4 LOW · **0 new** · **0 resolved** since last scan
**Exit status:** `SECURITY_SCAN_NOCHANGE`

## Needs attention (NEW high-severity this run)

None. No NEW HIGH findings.

## Resolved since last scan

None. No HIGH findings were resolved between 2026-06-29 and today.

## Persistent findings (unchanged)

| # | File | Line | Pattern | Delta | Note |
|---|------|------|---------|-------|------|
| 1 | `.github/workflows/aeon.yml` | 86 | `echo "name=${{ inputs.skill }}" >> "$GITHUB_OUTPUT"` | PERSISTENT | `inputs.skill` interpolated into `run:` block. Workflow_dispatch/workflow_call gated → requires repo write access → low real risk. Same anti-pattern as 2026-04-11 messages.yml incident. |
| 2 | `.github/workflows/aeon.yml` | 94 | `if [ -n "${{ steps.skill.outputs.name }}" ]; then` | PERSISTENT | `steps.skill.outputs.name` is the value of `inputs.skill` echoed at L86 — same risk profile. |
| 3 | `.github/workflows/aeon.yml` | 96 | `echo "label=${{ steps.skill.outputs.name }}" >> "$GITHUB_OUTPUT"` | PERSISTENT | Same chain as #2. |
| 4 | `.github/workflows/aeon.yml` | 812 | `LABEL="${{ steps.work.outputs.label }}"` | PERSISTENT (no line drift; 3rd consecutive scan at `:812`) | Held at `:812` for the third consecutive scan (2026-06-22, 2026-06-29, 2026-07-06 all at `:812`; was `:849` at 2026-06-15, `:725` at 06-01, `:718` at baseline). Derived from `steps.skill.outputs.name` → `inputs.skill`. |

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

Reading `$_INPUT_SKILL` from the shell at runtime defangs any template-injection payload — the value is treated as a shell string, not as YAML/JS that the runner expands before the script executes. Each of the four call sites needs the same env-binding (one `_INPUT_SKILL` for the Determine-skill step, one `_LABEL` derived from the safe step output for the L812 site).

## Coverage detail

- **SKILL.md files**: 191 (all enabled + disabled skills under `skills/*/SKILL.md`; down 1 from 192 at last scan — `skills/security/` remains the only non-SKILL.md-carrying dir, hosting the baseline + trusted-sources catalog). Every match against shell-injection, exfil, prompt-override, and destructive-command patterns landed inside threat-modeling prose or fenced code blocks documenting safe usage (e.g. `skills/sparkleware-catalog/SKILL.md:283`, `skills/research-brief/SKILL.md:111`, `skills/competitor-launch-radar/SKILL.md:424`, `skills/deep-research/SKILL.md:80`, etc. — all framing the threats the skills defend against, not payloads).
- **Workflows**: 9 (`aeon.yml`, `chain-runner.yml`, `ci-packs-json.yml`, `ci-skills-json.yml`, `investment-advisor.yml`, `messages.yml`, `replicate-oneoff.yml`, `sync-upstream.yml`, `weekly-conviction.yml`). 4 HIGH all in `aeon.yml`. Every other `${{ }}` expression in any `run:` block goes through `env:` indirection (`messages.yml` L612-616/684-685/838-863, `chain-runner.yml` L41/368, `replicate-oneoff.yml` L52-55/78) — confirmed by re-read this run.
- **Repo scripts**: 30 under `scripts/*.sh` and `scripts/advisor/*.sh` (up 3 from prior 27 — no new HIGH surfaces introduced). No `eval` of external data, no `curl`/`wget` piping secrets to non-intended hosts, no `rm -rf /`, no force-push to main.
- **Advisor scripts** (subset of the 30 above): `scripts/advisor/selftest.sh:31` (`rm -rf /` defensive test fixture, allowlist defaults to `hold`, never executed) + `selftest.sh:220,252` (`eval` extracting internal helper functions from same-repo `run.sh` / `llm-usepod.sh` for unit testing — trusted-source content) carried as known false positives; `real_risk: false`.
- **Companion scripts under `skills/*/`**: 1 (`skills/skill-health/tests/smoke.sh`; `skills/skill-security-scan/scan.sh` is the scanner itself and its own regex library naturally matches its own patterns in source — HIGH-pattern strings, not HIGH-pattern code, per self-documenting-scanner exception).

## Obfuscation sweep

- **Zero-width Unicode (U+200B, U+FEFF)**: clean. No matches anywhere in scope.
- **Bidi override (U+202E / Trojan Source)**: clean.
- **`fromCharCode`**: clean (only appears in `skills/skill-security-scan/SKILL.md:23` as pattern-library documentation).
- **`base64 -d` / `base64 --decode` piped to shell**: zero matches of the "decode-then-execute" shape. All `base64 -d` occurrences decode `gh api .../contents/*` responses (GitHub API returns base64-encoded file contents) or build a JSON payload via `jq` — none pipe to a shell.
- **SSRF/webhook hosts** (`ngrok`, `interact.sh`, `webhook.site`, `burpcollaborator`, `pipedream.net`, `requestbin.com`): no active matches. Historical scan-baseline reference to "ngrok" as an example tunnel; no active code uses any flagged host.

## Per-file results

| File | Status | HIGH | MEDIUM | LOW |
|------|--------|------|--------|-----|
| `.github/workflows/aeon.yml` | FAIL | 4 | 3 | 0 |
| `.github/workflows/chain-runner.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/messages.yml` | PASS | 0 | 1 | 0 |
| `.github/workflows/replicate-oneoff.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/sync-upstream.yml` | PASS | 0 | 1 | 0 |
| `.github/workflows/investment-advisor.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/weekly-conviction.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/ci-packs-json.yml` | PASS | 0 | 0 | 0 |
| `.github/workflows/ci-skills-json.yml` | PASS | 0 | 0 | 0 |
| `scripts/advisor/selftest.sh` | WARN | 3* | 0 | 0 |
| `scripts/sync-upstream.sh` | WARN | 0 | 1 | 0 |
| `skills/monitor-runners/SKILL.md` | WARN | 2** | 0 | 0 |
| `skills/skill-triage/SKILL.md` | WARN | 1** | 0 | 0 |
| `skills/*/SKILL.md` (×188 remainder) | PASS / WARN per-skill | 0 | ~9 (all in fenced code blocks → effectively informational) | ~4 |

\* `selftest.sh` HIGH counts (`rm -rf /` test fixture at L31, two `eval` helper extractions at L220/L252) are documented false positives — `real_risk: false`.
\*\* `monitor-runners/SKILL.md:74,77` `eval "${N}_TREND_OK=1"` and `skill-triage/SKILL.md:182` `eval $(...)` example row are both **inside fenced markdown code blocks** — downgraded to MEDIUM per SKILL.md step 7 (code-fence downgrade). `monitor-runners` uses a controlled loop variable from a whitespace-tokenized static list; even if executed the injection surface is nil. Not filed as HIGH; noted here for transparency.

## Per-finding remediation hint

| Finding | Fix |
|---|---|
| `aeon.yml:86` | Bind `inputs.skill` to `env:` (`_INPUT_SKILL`) on the `Determine skill` step, read `$_INPUT_SKILL` from the shell (see canonical snippet above). |
| `aeon.yml:94` | Source from the safe step output via env: indirection. After step output is safe (no template injection at write-time), `[ -n "$_NAME" ]` in shell works the same way. |
| `aeon.yml:96` | Same fix as L86 — env-bind, then `echo "label=$_INPUT_SKILL" >> "$GITHUB_OUTPUT"`. |
| `aeon.yml:812` | Bind `steps.work.outputs.label` to an env key on that step (`_LABEL: ${{ steps.work.outputs.label }}`), then `LABEL="$_LABEL"`. |

## Appendix — all current findings

```json
{
  "high": [
    {"file": ".github/workflows/aeon.yml", "line": 86, "pattern": "inputs.skill interpolated into run: block", "delta": "PERSISTENT", "fingerprint": "aeon.yml:86:inputs.skill"},
    {"file": ".github/workflows/aeon.yml", "line": 94, "pattern": "steps.skill.outputs.name interpolated into run: block", "delta": "PERSISTENT", "fingerprint": "aeon.yml:94:steps.skill.outputs.name"},
    {"file": ".github/workflows/aeon.yml", "line": 96, "pattern": "steps.skill.outputs.name interpolated into run: block", "delta": "PERSISTENT", "fingerprint": "aeon.yml:96:steps.skill.outputs.name"},
    {"file": ".github/workflows/aeon.yml", "line": 812, "pattern": "steps.work.outputs.label interpolated into run: block", "delta": "PERSISTENT", "fingerprint": "aeon.yml:812:steps.work.outputs.label"}
  ],
  "high_documented_false_positives": [
    {"file": "scripts/advisor/selftest.sh", "line": 31, "reason": "rm -rf / inside case allowlist default-to-hold direction sanitizer test. Never executed."},
    {"file": "scripts/advisor/selftest.sh", "line": 220, "reason": "eval extracts internal helper function from same-repo run.sh for unit testing. Trusted-source content."},
    {"file": "scripts/advisor/selftest.sh", "line": 252, "reason": "eval extracts internal helper function from same-repo llm-usepod.sh for unit testing. Trusted-source content."},
    {"file": "skills/monitor-runners/SKILL.md", "line": "74,77", "reason": "eval \"${N}_TREND_OK=1\" inside a fenced markdown code block; N is a controlled loop variable from a static whitespace-tokenized list. Fence-downgrade → MEDIUM. real_risk: false."},
    {"file": "skills/skill-triage/SKILL.md", "line": 182, "reason": "Documentation of the `eval \\$(...)` scan pattern inside a fenced example row of skill-triage's output format. Fence-downgrade → MEDIUM. real_risk: false."}
  ],
  "medium_persistent_note": "All `base64 -d` matches decode GitHub API contents responses (API returns base64) or chunk a Telegram message via `jq`-built JSON. None pipe to a shell — no decode-then-execute. Path-traversal / force-push MEDIUM matches are documentation or internally-computed non-user-controllable step outputs. aeon.yml:819 and messages.yml:876 `git push --force-with-lease` are the safe force-push variant.",
  "low_persistent_note": "~4 `find / `/ `tee /` style matches in skill examples; documentation, not executed payloads."
}
```
