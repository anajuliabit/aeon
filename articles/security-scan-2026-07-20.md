# Security Scan — 2026-07-20

**Verdict:** ATTENTION (4 persistent HIGH findings; 0 NEW, 0 RESOLVED)
**Scope:** full corpus (191 SKILL.md + 9 workflows + 30 repo scripts + 2 companion scripts = 232 files)
**Scanner mode:** inline_grep_fallback — `scan.sh` execution blocked by the sandbox approval gate for the 8th consecutive scan (2026-05-25, 06-01, 06-15, 06-22, 06-29, 07-06, 07-13, 07-20); inline Grep over `scan.sh`'s HIGH/MEDIUM/LOW pattern library + manual GitHub Actions script-injection audit of every `${{ }}` expression in `run:` blocks + obfuscation sweep, per SKILL.md step 4 sandbox fallback. Never silently skipped.
**Counts:** 232 files scanned · **4 HIGH** · 15 MEDIUM · 4 LOW · **0 new** · **0 resolved** since last scan
**Exit status:** `SECURITY_SCAN_NOCHANGE`

## Needs attention (NEW high-severity this run)

None. No NEW HIGH findings.

## Resolved since last scan

None. No HIGH findings were resolved between 2026-07-13 and today.

## Persistent findings (unchanged)

| # | File | Line | Pattern | Delta | Note |
|---|------|------|---------|-------|------|
| 1 | `.github/workflows/aeon.yml` | 86 | `echo "name=${{ inputs.skill }}" >> "$GITHUB_OUTPUT"` | PERSISTENT | `inputs.skill` interpolated into `run:` block. Workflow_dispatch/workflow_call gated → requires repo write access → low real risk. Same anti-pattern as the 2026-04-11 `messages.yml` incident. |
| 2 | `.github/workflows/aeon.yml` | 94 | `if [ -n "${{ steps.skill.outputs.name }}" ]; then` | PERSISTENT | `steps.skill.outputs.name` is the value of `inputs.skill` echoed at L86 — same risk profile. |
| 3 | `.github/workflows/aeon.yml` | 96 | `echo "label=${{ steps.skill.outputs.name }}" >> "$GITHUB_OUTPUT"` | PERSISTENT | Same chain as #2. |
| 4 | `.github/workflows/aeon.yml` | 812 | `LABEL="${{ steps.work.outputs.label }}"` | PERSISTENT (no line drift; **5th consecutive scan at `:812`**) | Held at `:812` across 2026-06-22 / 06-29 / 07-06 / 07-13 / 07-20 (was `:849` at 06-15, `:725` at 06-01, `:718` at baseline). Derived from `steps.skill.outputs.name` → `inputs.skill`. |

**Remediation (single canonical fix for all 4 sites)** — apply the env: indirection pattern already used by `chain-runner.yml:41,368` (ISS-017 fix) and `messages.yml:612-616, 684-685, 838-863` (post-2026-04-11 fix):

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

Reading `$_INPUT_SKILL` from the shell at runtime defangs any template-injection payload — the value is treated as a shell string, not YAML/JS the runner expands before the script executes. Each of the four call sites needs the same env-binding (one `_INPUT_SKILL` for the Determine-skill step, one `_LABEL` derived from the safe step output for the L812 site).

**Structural block on this fix:** `.github/workflows/aeon.yml` edits are gated by self-improve SKILL.md rule 5 (see `memory/MEMORY.md` — rule-5 primitive n=4 = auto-committed state drift across any self-improve authored PR). Operator direct-author remains the sole path per the 2026-07-19 T+2 SLIP extending the pattern. This scan report exists to keep the anti-pattern visible until then.

## Coverage detail

- **SKILL.md files**: 191 (unchanged from last scan). Every match against shell-injection, exfil, prompt-override, and destructive-command patterns landed inside threat-modeling prose or fenced code blocks documenting safe usage. The 10 defensive prompt-override docs (`sparkleware-catalog:283`, `research-brief:111`, `fork-release-tracker:247`, `soul-builder:229`, `repo-actions:268`, `last30:171`, `skill-triage:292`, `deep-research:80`, `ecosystem-pulse:388`, `competitor-launch-radar:424`) all frame the threats the skills defend against, not payloads — held as documentation per the baseline seed-rule spirit.
- **Workflows**: 9 (`aeon.yml`, `chain-runner.yml`, `ci-packs-json.yml`, `ci-skills-json.yml`, `investment-advisor.yml`, `messages.yml`, `replicate-oneoff.yml`, `sync-upstream.yml`, `weekly-conviction.yml`) — unchanged. 4 HIGH all in `aeon.yml`. Every other `${{ }}` expression in any `run:` block goes through `env:` indirection (`messages.yml` L612-616 / L684-685 / L838-863, `chain-runner.yml` L41/L368, `replicate-oneoff.yml` L52-55/L78) — confirmed by re-read this run. `sync-upstream.yml:79` `git push -f` sits inside the *body* of an automated PR comment (documentation for the human resolver), not a `run:` shell command — safe.
- **Repo scripts**: 30 under `scripts/*.sh`, `scripts/advisor/*.sh` (unchanged from last scan). No `eval` of external data, no `curl`/`wget` piping secrets to non-intended hosts, no `rm -rf /`, no force-push to main.
- **Advisor scripts** (subset): `scripts/advisor/selftest.sh:31` (`rm -rf /` defensive test fixture; allowlist case defaults to `hold`; never executed) + `selftest.sh:220,252` (`eval` extracting internal helper functions from same-repo `run.sh` / `llm-usepod.sh` for unit testing — trusted-source content) carried as known false positives; `real_risk: false`.
- **Companion scripts under `skills/*/`**: 2 — `skills/skill-security-scan/scan.sh` (the scanner itself; its own regex library naturally matches its own patterns in source per the self-documenting-scanner exception) + `skills/skill-health/tests/smoke.sh` (static validator; no `eval`/`rm -rf /`/`curl $VAR`/`base64 -d` matches on re-scan this run).
- **Non-.sh scripts scanned**: 8 auxiliaries (`scripts/eval-audit`, `scripts/skill-runs`, `scripts/cost-report-calc.py`, `scripts/fork-cohort-run.py`, `scripts/on-chain-monitor.py`, `scripts/on-chain-monitor-run.py`, `scripts/parse-forks.py`, `scripts/skill-graph-fp.py`) + `skills/skill-freshness/check_mtimes.py` — no `eval(...)`/`exec(...)`/`subprocess ... shell=True`/`__import__` in the Python surface. `scripts/eval-audit` hits on the word "eval" are documentation strings (`# eval-audit — audit eval coverage across all skills`, echo strings labelling stub generation) — POSIX-ERE `eval[[:space:]]` false positives, not command execution.

## Obfuscation sweep

- **Zero-width Unicode (U+200B, U+FEFF)**: clean. No matches anywhere in active in-scope code (skills/, scripts/, .github/workflows/).
- **Bidi override (U+202E / Trojan Source)**: clean.
- **`fromCharCode`**: clean in active code. Substring appears in ~40 JSON caches (`.cg-markets.json`, `.token-pick-cache/*`, etc.) as coin-description data — not payload, never eval'd — and in `skills/skill-security-scan/SKILL.md:23` as pattern-library documentation.
- **`base64 -d` / `base64 --decode` piped to shell**: 4 matches, none of the decode-then-execute shape — `aeon.yml:343` decodes a `jq`-built JSON Telegram-chunk payload back into text, `scripts/fork-cohort-run.sh:92`, `scripts/sync-upstream.sh:49`, and `.fork-runs-check.sh:49` decode `gh api .../contents/*` responses (GitHub API returns base64-encoded file contents). All four feed the decoded bytes into `printf`/redirect targets or `grep`, not into `sh -c` or `bash`.
- **SSRF/webhook hosts** (`ngrok`, `interact.sh`, `webhook.site`, `burpcollaborator`, `pipedream.net`, `requestbin.com`): no active matches. Only mentions live in `skill-security-scan/SKILL.md` (pattern definition) and prior security-scan articles/logs (documentation of the sweep itself).

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
| `scripts/eval-audit` | WARN | 0** | 0 | 0 |
| `skills/monitor-runners/SKILL.md` | WARN | 2** | 0 | 0 |
| `skills/skill-triage/SKILL.md` | WARN | 1** | 0 | 0 |
| `skills/*/SKILL.md` (×188 remainder) | PASS / WARN per-skill | 0 | ~9 (all in fenced code blocks → effectively informational) | ~4 |

\* `selftest.sh` HIGH counts (`rm -rf /` test fixture at L31, two `eval` helper extractions at L220/L252) are documented false positives — `real_risk: false`.
\*\* `monitor-runners/SKILL.md:74,77` `eval "${N}_TREND_OK=1"` and `skill-triage/SKILL.md:182` `eval $(...)` example row are both **inside fenced markdown code blocks** — downgraded to MEDIUM per SKILL.md step 7 (code-fence downgrade). `monitor-runners` uses a controlled loop variable from a whitespace-tokenized static list; even if executed the injection surface is nil. `scripts/eval-audit`'s pattern hits are POSIX-ERE false positives — the word "eval" appears in comments and echo strings, never as command execution. Not filed as HIGH; noted here for transparency.

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
    {"file": "skills/skill-triage/SKILL.md", "line": 182, "reason": "Documentation of the `eval \\$(...)` scan pattern inside a fenced example row of skill-triage's output format. Fence-downgrade → MEDIUM. real_risk: false."},
    {"file": "scripts/eval-audit", "line": "2, 7, 10, 186, 238, 271", "reason": "POSIX-ERE `eval[[:space:]]` false-positives — the word 'eval' appears in comments and echo strings (e.g. '# eval-audit — audit eval coverage'), never as command execution. real_risk: false."}
  ],
  "medium_persistent_note": "All `base64 -d` matches decode GitHub API contents responses (API returns base64) or chunk a Telegram message via `jq`-built JSON. None pipe to a shell — no decode-then-execute. Path-traversal / force-push MEDIUM matches are documentation or internally-computed non-user-controllable step outputs. aeon.yml:819 and messages.yml:876 `git push --force-with-lease` are the safe force-push variant.",
  "low_persistent_note": "~4 `find /`/`tee /` style matches in skill examples; documentation, not executed payloads."
}
```

## Delta note

Byte-for-byte identical finding set to 2026-07-13. Canonical-4 `aeon.yml` HIGHs held at `:86`, `:94`, `:96`, `:812` (`:812` now stable across **5 consecutive scans** — no line drift). ISS-017 `chain-runner.yml` env: indirection fix held at `:41` and `:368`. `messages.yml` 2026-04-11 incident-class fix held across every site (L612-616, L684-685, L838-863). Obfuscation sweep clean (no zero-width/bidi/fromCharCode-in-active-code/base64-decode-to-shell/SSRF-webhook hosts). Skill count 191 (unchanged). Workflows 9 (unchanged). Repo scripts 30 (unchanged). Companion scripts 2 (unchanged). No new attack surface introduced this week. Rule-5 self-improve block on the fix persists — operator direct-author remains the sole path.
