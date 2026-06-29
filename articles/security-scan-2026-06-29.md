# Security Scan — 2026-06-29

**Verdict:** ATTENTION (4 persistent HIGH findings; 0 NEW, 0 RESOLVED)
**Scope:** full corpus (192 SKILL.md + 9 workflows + 19 repo scripts + 8 advisor scripts + 1 companion script = 229 files)
**Scanner mode:** inline_grep_fallback — `scan.sh` execution blocked by the sandbox approval gate (same path as 2026-05-25 / 2026-06-01 / 2026-06-15 / 2026-06-22 runs); inline Grep over `scan.sh`'s HIGH/MEDIUM/LOW pattern library + manual GitHub Actions script-injection audit of every `${{ }}` expression in `run:` blocks, per SKILL.md step 4 sandbox fallback. Never silently skipped.
**Counts:** 229 files scanned · **4 HIGH** · 15 MEDIUM · 4 LOW · **0 new** · **0 resolved** since last scan
**Exit status:** `SECURITY_SCAN_NOCHANGE`

## Needs attention (NEW high-severity this run)

None. No NEW HIGH findings.

## Resolved since last scan

None. No HIGH findings were resolved between 2026-06-22 and today.

## Persistent findings (unchanged)

| # | File | Line | Pattern | Delta | Note |
|---|------|------|---------|-------|------|
| 1 | `.github/workflows/aeon.yml` | 86 | `echo "name=${{ inputs.skill }}" >> "$GITHUB_OUTPUT"` | PERSISTENT | `inputs.skill` interpolated into `run:` block. Workflow_dispatch/workflow_call gated → requires repo write access → low real risk. Same anti-pattern as 2026-04-11 messages.yml incident. |
| 2 | `.github/workflows/aeon.yml` | 94 | `if [ -n "${{ steps.skill.outputs.name }}" ]; then` | PERSISTENT | `steps.skill.outputs.name` is the value of `inputs.skill` echoed at L86 — same risk profile. |
| 3 | `.github/workflows/aeon.yml` | 96 | `echo "label=${{ steps.skill.outputs.name }}" >> "$GITHUB_OUTPUT"` | PERSISTENT | Same chain as #2. |
| 4 | `.github/workflows/aeon.yml` | 812 | `LABEL="${{ steps.work.outputs.label }}"` | PERSISTENT (no line drift this run) | Held at `:812` for the second consecutive scan (was `:812` at 2026-06-22, `:849` at 2026-06-15, `:725` at 06-01, `:718` at baseline). Derived from `steps.skill.outputs.name` → `inputs.skill`. |

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

- **SKILL.md files**: 192 (all enabled + disabled skills under `skills/*/SKILL.md`). Every match against shell-injection, exfil, prompt-override, and destructive-command patterns landed inside threat-modeling prose or fenced code blocks documenting safe usage (e.g. `skills/sparkleware-catalog/SKILL.md:283`, `skills/research-brief/SKILL.md:111`, `skills/competitor-launch-radar/SKILL.md:424`, `skills/deep-research/SKILL.md:80`, etc. — all framing the threats the skills defend against, not payloads).
- **Workflows**: 9 (`aeon.yml`, `chain-runner.yml`, `ci-packs-json.yml`, `ci-skills-json.yml`, `investment-advisor.yml`, `messages.yml`, `replicate-oneoff.yml`, `sync-upstream.yml`, `weekly-conviction.yml`). 4 HIGH all in `aeon.yml`. Every other `${{ }}` expression in any `run:` block goes through `env:` indirection (`messages.yml` L612-616/684-685/838-863, `chain-runner.yml` L41/368, `replicate-oneoff.yml` L52-55/78) — confirmed.
- **Repo scripts**: 19 under `scripts/*.sh`. No `eval` of external data, no `curl`/`wget` piping secrets to non-intended hosts, no `rm -rf /`, no force-push to main.
- **Advisor scripts**: 8 under `scripts/advisor/`. `selftest.sh:31` (`rm -rf /` defensive test fixture, allowlist defaults to `hold`, never executed) + `selftest.sh:220,252` (`eval` extracting internal helper functions from same-repo `run.sh` / `llm-usepod.sh` for unit testing — trusted-source content) carried as known false positives; `real_risk: false`.
- **Companion scripts under `skills/*/`**: 1 (e.g. `skills/skill-security-scan/scan.sh` itself). The scanner's own regex library matches its own patterns in source (every HIGH pattern string appears) — these are HIGH-pattern strings, not HIGH-pattern code, and remain excluded from any disposition per the self-documenting-scanner exception.

## Obfuscation sweep

- **Zero-width Unicode (U+200B, U+FEFF)**: clean. No matches anywhere in scope.
- **Bidi override (U+202E / Trojan Source)**: clean.
- **`fromCharCode`**: clean.
- **`base64 -d` / `base64 --decode` piped to shell**: zero matches of the "decode-then-execute" shape. All `base64 -d` occurrences decode `gh api .../contents/*` responses (GitHub API returns base64-encoded file contents) or build a JSON payload via `jq` — none pipe to a shell.
- **SSRF/webhook hosts** (`ngrok`, `interact.sh`, `webhook.site`, `burpcollaborator`, `pipedream.net`, `requestbin.com`): no active matches. One historical README/article mention of "ngrok" as an example tunnel option; no active code uses any flagged host.

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
| `skills/*/SKILL.md` (×192) | PASS / WARN per-skill | 0 | ~9 (all in fenced code blocks → effectively informational) | ~4 |

\* `selftest.sh` HIGH counts (`rm -rf /` test fixture at L31, two `eval` helper extractions at L220/L252) are documented false positives — `real_risk: false`.

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
    {"file": "scripts/advisor/selftest.sh", "line": 252, "reason": "eval extracts internal helper function from same-repo llm-usepod.sh for unit testing. Trusted-source content."}
  ],
  "medium_persistent_note": "All `base64 -d` matches decode GitHub API contents responses (API returns base64) or chunk a Telegram message via `jq`-built JSON. None pipe to a shell — no decode-then-execute. Path-traversal / force-push MEDIUM matches are documentation or internally-computed non-user-controllable step outputs.",
  "low_persistent_note": "~4 `find / `/ `tee /` style matches in skill examples; documentation, not executed payloads."
}
```
