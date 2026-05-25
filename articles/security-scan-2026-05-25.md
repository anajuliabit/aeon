# Security Scan — 2026-05-25

**Verdict:** ATTENTION (bootstrap baseline established; one workflow anti-pattern class worth follow-up)
**Scope:** full corpus (122 SKILL.md + 4 workflows + 9 scripts + scan.sh)
**Counts:** 142 files scanned · 781 raw HIGH · 8 HIGH post-filter · 14 MEDIUM post-filter · 4 LOW post-filter · — new (bootstrap, no prior baseline) · 0 resolved
**Scanner mode:** inline Grep fallback (scan.sh execution blocked by sandbox approval gate; ran scan.sh's published HIGH/MEDIUM/LOW pattern library inline per SKILL.md sandbox fallback)
**Exit status:** `SECURITY_SCAN_BOOTSTRAPPED`

---

## Needs attention (real HIGH findings after suppression and code-fence downgrade)

Note: scan.sh's pattern library does NOT include the `${{ github.event.* }}` / `${{ inputs.* }}` direct-interpolation anti-pattern that the canonical 2026-04-11 incident fix targets. The findings below were surfaced via manual inspection of `.github/workflows/*.yml` `run:` blocks, in line with the SKILL.md threat category "GitHub Actions script injection". They are filed here for operator awareness; none warrant new ISS-* issues on the bootstrap run.

| File | Line | What | Fix |
|------|------|------|-----|
| `.github/workflows/messages.yml` | 578 | `TYPE="${{ github.event.action }}"` interpolated directly into `run:` | Rebind to `env:` (e.g. `_GH_EVENT_ACTION: ${{ github.event.action }}`) then read `$_GH_EVENT_ACTION` in the shell — see `articles/workflow-security-audit-2026-04-11.md` for the canonical fix shape. |
| `.github/workflows/aeon.yml` | 86 | `echo "name=${{ inputs.skill }}"` direct in `run:` | Same env-var indirection. |
| `.github/workflows/aeon.yml` | 94 | `[ -n "${{ steps.skill.outputs.name }}" ]` direct in `run:` | Same. |
| `.github/workflows/aeon.yml` | 96 | `echo "label=${{ steps.skill.outputs.name }}"` direct in `run:` | Same. |
| `.github/workflows/aeon.yml` | 718 | `LABEL="${{ steps.work.outputs.label }}"` direct in `run:` | Same. |

**Risk assessment:** all five trace back to `inputs.skill` (workflow_dispatch input) or `github.event.action` (repository_dispatch action name). Both are constrained by GitHub's auth model — exploitation requires write access or a valid PAT able to call `workflow_dispatch`/`repository_dispatch`. Real exposure is low. The anti-pattern remains because if any of these values is ever wired to a less-privileged source (e.g. a webhook bridge that accepts unauthenticated input), the injection becomes live. Fix it preemptively while the surface is small.

The legitimate-curl-with-token findings in `messages.yml` (lines 482–660) and `aeon.yml` (lines 332–680) all pass tokens in `-H "Authorization: ..."` headers with shell-quoting around the URL — these are the standard messaging API integrations, not exfiltration. No action.

---

## Resolved since last scan

n/a — bootstrap run; no prior baseline. Next scan (next Monday 16:00 UTC per cron) will compute true delta against this run's state file.

---

## Persistent findings (unchanged)

n/a on bootstrap. Counts above ARE the persistent baseline going forward.

---

## Pattern noise — known limitation, no auto-fix per skill constraints

The `` `[^`]*\$ `` HIGH pattern in `scan.sh` (intended to catch backtick command substitution with var expansion) fires on every markdown inline code reference that contains `$` — overwhelmingly false positives like `` `memory/logs/${today}.md` `` and `` `${var}` ``. This produced **769 raw matches across 122 SKILL.md files** before filtering.

Per SKILL.md constraint *"Never change scan.sh's pattern library from inside this skill. Pattern evolution happens in a separate, reviewed PR"*, this scan does NOT modify the pattern. Recommended follow-up PR: replace `` '`[^`]*\$' `` with a tighter pattern that only fires on actual backtick-command-substitution contexts (e.g. require an alpha char and parens / pipes after the `$`, or exclude markdown inline contexts). Without that fix, the scanner cannot meaningfully report on SKILL.md files — they all WARN/FAIL on noise.

Until the pattern is fixed, the operator should treat raw scan.sh HIGH counts on SKILL.md as advisory only. The code-fence downgrade rule in this skill (step 7) only applies inside triple-backtick fenced blocks, not inline backticks, so it does not mitigate this pattern.

---

## Per-file results (only files with any finding)

| File | Status | HIGH (raw) | MEDIUM (raw) | LOW (raw) | Real HIGH after filter |
|------|--------|------------|--------------|-----------|------------------------|
| `.github/workflows/messages.yml` | FAIL | 9 | 1 | 0 | 1 |
| `.github/workflows/aeon.yml` | FAIL | 11 | 1 | 0 | 4 |
| `scripts/postprocess-reppo.sh` | FAIL | 9 | 0 | 0 | 0 (echo-string FPs) |
| `scripts/prefetch-xai.sh` | FAIL | 2 | 0 | 0 | 0 (legitimate API) |
| `scripts/postprocess-admanage.sh` | FAIL | 1 | 0 | 0 | 0 (legitimate API) |
| `scripts/postprocess-admanage-create.sh` | FAIL | 2 | 0 | 0 | 0 (legitimate API) |
| `scripts/postprocess-replicate.sh` | FAIL | 2 | 0 | 0 | 0 (legitimate API) |
| `scripts/sync-upstream.sh` | WARN | 0 | 1 | 0 | 0 (base64 -d on gh-api content) |
| `notify` (generated script, scanned because present) | WARN | 0 | 1 | 0 | 0 (chunked-message reassembly) |
| `skills/skill-security-scan/scan.sh` | FAIL | 9 | 0 | 0 | 0 (self-reference) |
| `skills/skill-security-scan/SKILL.md` | FAIL | 17 | 0 | 0 | 0 (suppressed by baseline) |
| `skills/security-digest/SKILL.md` | FAIL | 5 | 0 | 0 | 0 (suppressed by baseline + fenced-code) |
| `skills/competitor-launch-radar/SKILL.md` | FAIL | 1 | 0 | 0 | 0 (security-advice quote) |
| `skills/fork-release-tracker/SKILL.md` | FAIL | 1 | 0 | 0 | 0 (security-advice quote) |
| `skills/research-brief/SKILL.md` | FAIL | 1 | 0 | 0 | 0 (security-advice quote) |
| `skills/deep-research/SKILL.md` | FAIL | 1 | 0 | 0 | 0 (security-advice quote) |
| `skills/last30/SKILL.md` | FAIL | 1 | 0 | 0 | 0 (security-advice quote) |
| `skills/repo-actions/SKILL.md` | FAIL | 1 | 0 | 0 | 0 (security-advice quote) |
| `skills/fork-skill-gap/SKILL.md` | FAIL | 1 | 0 | 0 | 0 (security advice — quoted `$(rm -rf /)` example demonstrating safe JSON parsing) |
| (122 SKILL.md files total — remainder PASS after the `` `[^`]*\$ `` noise is acknowledged as a pattern bug) | | | | | |

---

## Appendix — bootstrap state

State file written to `memory/state/security-scan.json` with structured per-file counts (NOT all 769 individual matches — that would create a 1.5MB state file with no signal). Next scan will detect any change in per-file counts as a delta. If finer-grained line-level delta is needed once the backtick pattern is tightened, the state schema can be extended in a follow-up.

Baseline file `skills/security/scan-baseline.yml` bootstrapped with 8 seed suppression entries:
- 6 prompt-override patterns in `skills/skill-security-scan/SKILL.md` (Threat Categories documentation)
- 2 curl-with-env-var patterns in `skills/security-digest/SKILL.md` (fenced-code documentation examples)

No issues filed (bootstrap run — `SECURITY_SCAN_BOOTSTRAPPED` exit code). Next run's delta against this baseline will determine whether the 5 workflow-injection anti-pattern findings warrant ISS files; they remain in the state file as known-baseline-real-findings and are documented above for the operator's awareness.

---

## Follow-up actions for operator

1. **(low urgency, high signal)** Tighten `scan.sh` HIGH pattern `` '`[^`]*\$' `` — currently produces 769 false positives, masks any genuine future findings inside SKILL.md files. Separate PR per skill constraint.
2. **(medium urgency)** Apply env-var indirection to the 5 workflow-injection sites listed above. Same fix shape as the 2026-04-11 auto-fix in `messages.yml`. Even though current exposure is low (all sources auth-gated), preemptive fix matches the codebase's existing pattern and removes the class entirely.
3. **(no action needed)** All other raw findings have been classified as documentation, self-reference, legitimate API usage, or fenced-code examples.
