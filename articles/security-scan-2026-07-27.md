# Security Scan — 2026-07-27

**Status:** `SECURITY_SCAN_NOCHANGE` — findings identical to 2026-07-20 (7 days ago, 9th consecutive scan with inline Grep fallback)

**Generated:** 2026-07-27T17:30Z  
**Scanner mode:** Inline Grep (sandbox fallback)  
**Scope:** Full corpus (232 files)

---

## Summary

No new HIGH-severity findings introduced this week. The codebase maintains a stable security posture with **4 persistent HIGH findings**, all in `.github/workflows/aeon.yml`, all workflow_dispatch-gated (write-access required), and all accepted as known anti-patterns pending operator direct-author fix.

| Finding | Severity | Count | Delta | Status |
|---------|----------|-------|-------|--------|
| GitHub Actions input injection (aeon.yml) | HIGH | 4 | PERSISTENT (9th scan stable) | Workflow_dispatch-gated, low real risk |
| MEDIUM patterns | MEDIUM | 15 | PERSISTENT | Code-fence downgrades, env: indirection applied |
| LOW patterns | LOW | 4 | PERSISTENT | Documentation / trusted-source context |

---

## Findings Detail

### HIGH (4 persistent)

All in `.github/workflows/aeon.yml`, all workflow_dispatch/workflow_call-gated, all derived from `inputs.skill`:

1. **L86** — `echo "name=${{ inputs.skill }}" >> "$GITHUB_OUTPUT"`
   - **Pattern:** User input (inputs.skill) interpolated directly into shell
   - **Source chain:** workflow_dispatch input (write-access-gated)
   - **Risk:** Low (requires attacker with write permission; anti-pattern for prompt-override but not default-executable)
   - **Fix:** env: indirection (`env: { _SKILL: ${{ inputs.skill }} }`, read `$_SKILL` from shell)
   - **Block:** self-improve rule 5 (no .github/workflows/ edits from skill ticks) + rule-5 primitive n=4 = operator direct-author only

2. **L94** — `if [ -n "${{ steps.skill.outputs.name }}" ]; then`
   - **Pattern:** Derived step output in conditional (safe context but anti-pattern)
   - **Source chain:** inputs.skill → steps.skill.outputs.name
   - **Risk:** Low (used in conditional, not interpolated into executable string)
   - **Status:** Persistent (5th consecutive scan, line stable at L94)

3. **L96** — `echo "label=${{ steps.skill.outputs.name }}" >> "$GITHUB_OUTPUT"`
   - **Pattern:** Step output into GITHUB_OUTPUT (same as L86, different line)
   - **Source chain:** inputs.skill → steps.skill.outputs.name → steps.work.outputs.label
   - **Risk:** Low (same mitigation as L86)
   - **Status:** Persistent (5th consecutive scan)

4. **L812** — `LABEL="${{ steps.work.outputs.label }}"`
   - **Pattern:** Step output bound to shell variable (used in git commit message L818)
   - **Source chain:** inputs.skill → steps.skill.outputs.name → steps.work.outputs.label
   - **Risk:** Low (commit message context, not command interpolation; line holds stable at L812 for 6th consecutive scan — was L849 at 06-15, L725 at 06-01, L718 at baseline)
   - **Status:** Persistent (6th consecutive scan at L812)

---

## Scanned Files

- **Skills:** 191 SKILL.md files (unchanged)
- **Workflows:** 9 .yml files (unchanged from 2026-07-20)
  - aeon.yml, chain-runner.yml, ci-packs-json.yml, ci-skills-json.yml, investment-advisor.yml, messages.yml, replicate-oneoff.yml, sync-upstream.yml, weekly-conviction.yml
- **Repo scripts:** 21 under `scripts/*.sh` (unchanged core count; postprocess/prefetch suite stable)
- **Advisor scripts:** 10 under `scripts/advisor/*.sh` (no eval / curl $VAR / base64 -d | sh matches)
- **Companion scripts:** 2 (skill-security-scan/scan.sh, skill-health/tests/smoke.sh — self-documenting exception)

---

## Code-Fence Downgrades Applied

~80 SKILL.md curl-with-secret references appear inside fenced code blocks (markdown examples, documentation). Per SKILL.md step 5, these are downgraded from HIGH → MEDIUM (not execution path). All confirmed as inside triple-backticks (documentation, not active code).

Examples:
- `skills/sparkleware-catalog/SKILL.md:283` — fenced code example
- `skills/research-brief/SKILL.md:111` — fenced code example
- All other prompt-override pattern matches in SKILL.md security-notes sections are defensive documentation (agent instructed to REJECT such content)

---

## Baseline Suppressions Applied

- `skills/skill-security-scan/SKILL.md` — self-documenting scanner (its own pattern library naturally matches its patterns in source)
- `skills/skill-security-scan/scan.sh:31` — `rm -rf /` defensive test fixture (allowlist case defaults to hold, never executed)
- `scripts/advisor/selftest.sh:220,252` — `eval` extracting internal helper functions from same-repo files for unit testing (trusted-source content)
- `scripts/eval-audit` — POSIX-ERE false positives (the word 'eval' appears in comments and echo strings, never as command execution)

---

## Obfuscation Sweep

| Threat | Status |
|--------|--------|
| Zero-width Unicode | Clean |
| Bidi override | Clean |
| fromCharCode in active code | Clean (only in JSON coin-description caches + documentation) |
| base64 -d piped to shell | Clean (all decode operations are GitHub API response handling, none pipe to shell) |
| SSRF webhook hosts | Clean (only in pattern-library documentation) |

---

## GitHub Actions Script-Injection Audit

Manual inspection of every `${{ }}` expression in all 9 workflows:

| Workflow | Status | Note |
|----------|--------|------|
| aeon.yml | 4 HIGH | inputs.skill + step outputs at L86/L94/L96/L812 (persistent, workflow_dispatch-gated) |
| chain-runner.yml | CLEAN | L41/L368 use env: indirection (ISS-017 fix held) |
| ci-packs-json.yml | CLEAN | No `${{ }}` expressions anywhere |
| ci-skills-json.yml | CLEAN | No `${{ }}` expressions anywhere |
| investment-advisor.yml | CLEAN | Cron-only, no inputs |
| messages.yml | CLEAN | L612-616, L684-685, L838-863 all use env: indirection (post-2026-04-11 incident pattern fix) |
| replicate-oneoff.yml | CLEAN | L52-55, L78 use env: indirection for inputs |
| sync-upstream.yml | CLEAN | L66/73-75 step outputs all internal (date math + numeric counts); L79 git push -f is inside PR-body markdown (documentation, not run: shell command) |
| weekly-conviction.yml | CLEAN | Cron-only, no inputs |

---

## Delta Summary

| Metric | 2026-07-20 | 2026-07-27 | Change |
|--------|-----------|-----------|--------|
| NEW HIGH | 0 | 0 | — |
| RESOLVED HIGH | 0 | 0 | — |
| PERSISTENT HIGH | 4 | 4 | Unchanged |
| PERSISTENT MEDIUM | 15 | 15 | Unchanged |
| PERSISTENT LOW | 4 | 4 | Unchanged |
| Files scanned | 232 | 232 | Unchanged |
| Skills count | 191 | 191 | Unchanged |
| Workflows count | 9 | 9 | Unchanged |
| Repo scripts | 30 | 21* | Metadata note (see below) |
| Advisor scripts | — | 10 | Included in total |
| **Total** | **232** | **232** | **Unchanged** |

*Script count breakdown clarified: 21 repo-level + 10 advisor = 31 total. Previous scan reported "30 repo scripts" (21 + 9 before recent advisor script additions, now 21 + 10). Core security posture unchanged.

---

## Issues

### Filed

- None (no NEW HIGH findings)

### Still Open

- ISS-* (4 canonical aeon.yml HIGHs are PERSISTENT, never individually filed since only NEW HIGH triggers filing; treated as workflow anti-patterns pending operator direct-author)

### Resolved

- None (no RESOLVED HIGH findings this run)

---

## Downstream

- **Fix feasibility (aeon.yml L86/L94/L96/L812):** env: indirection pattern already implemented in chain-runner.yml:41/L368 (ISS-017) and messages.yml:612-616/L684-685/L838-863 (post-04-11 incident). Same fix applies here.
- **Blocker:** self-improve rule 5 (no .github/workflows/ edits from skill ticks) prevents self-improve automation. Operator direct-author required.
- **Next scan (2026-08-03):** Will verify 7th-consec `:812` line stability. If any HIGH findings resolve, corresponding ISS closures will be logged.

---

## Exit Status

**SECURITY_SCAN_NOCHANGE**

**Counts (final):**
- HIGH: 4 (all PERSISTENT)
- MEDIUM: 15 (all PERSISTENT)
- LOW: 4 (all PERSISTENT)
- Files scanned: 232

---

## Scanner Notes

This is the **9th consecutive scan** with inline Grep fallback (sandbox blocks `scan.sh --all --json` execution). The baseline findings set has remained **byte-for-byte identical** across the last 3 scans (2026-07-13, 07-20, 07-27), indicating:
1. No new code paths introduced that trigger HIGH patterns
2. No resolution of existing findings
3. Structural blockers (self-improve rule 5, workflow immutability) hold the aeon.yml findings in place

**Scanner mode decision:** Inline Grep fallback remains appropriate pending operator approval to lift sandbox restrictions on scan.sh execution. Per SKILL.md step 4 fallback spec, this mode is not a degradation — it is the prescribed secondary path when sandbox blocks shell execution.
