Per CLAUDE.md, ending with a Summary.

## Summary

Bootstrapped `skill-security-scan` on first run.

**Created:**
- `skills/security/scan-baseline.yml` — 8 seed suppressions (6 prompt-override patterns in skill-security-scan/SKILL.md Threat Categories + 2 fenced-code curl examples in security-digest/SKILL.md)
- `memory/state/security-scan.json` — structured per-file finding counts; serves as delta baseline for next run
- `articles/security-scan-2026-05-25.md` — full report
- `.pending-notify/1780099200-skill-security-scan.md` — operator notification (staged; sandbox blocks direct `./notify`, post-run step delivers)

**Modified:** `memory/logs/2026-05-25.md` — appended `### skill-security-scan` entry

**Scan results (142 files: 122 SKILL.md + 4 workflows + 9 scripts + scan.sh):**
- Exit status: `SECURITY_SCAN_BOOTSTRAPPED`
- 781 raw HIGH → 8 post-filter → **5 real HIGH after manual triage**
- All 5 are the same workflow-injection anti-pattern (same class as 2026-04-11 incident): `messages.yml:578` (`${{ github.event.action }}`), `aeon.yml:86/94/96/718` (`${{ inputs.skill }}` and derivatives). Auth-gated so low live exposure; preemptive env-var indirection fix recommended.
- Scanner ran via inline Grep fallback because `bash scan.sh --all --json` required interactive approval — the SKILL.md sandbox-fallback path was followed faithfully.

**Notable known limitation:** scan.sh HIGH pattern `` `[^`]*\$ `` produces 769 false positives across SKILL.md files (matches every inline-backtick `${var}` reference like `` `memory/logs/${today}.md` ``). Per skill constraint *"Never change scan.sh's pattern library from inside this skill"*, this run does not modify it. Flagged in the report as recommended follow-up PR.

**No issues filed** — bootstrap convention (`SECURITY_SCAN_BOOTSTRAPPED` writes initial state; next scan computes true delta and files ISS for genuinely new HIGH only).

**Follow-up actions for operator:**
1. Tighten `scan.sh` backtick pattern in a separate reviewed PR (currently masks all SKILL.md signal).
2. Apply env-var indirection to the 5 workflow-injection sites (matches the existing 2026-04-11 fix shape).
