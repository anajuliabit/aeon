`SECURITY_SCAN_NOCHANGE`

## Summary

- **Exit:** `SECURITY_SCAN_NOCHANGE` — 4 persistent HIGH, 0 new, 0 resolved, byte-for-byte identical to 2026-08-03.
- **Scanner mode:** `sandbox-blocked` — 11th consecutive scan takes inline-Grep fallback (dominant failure mode per SKILL step 4). Never silently skipped.
- **Scope:** full corpus (var empty) — 235 files (191 SKILL.md + 9 workflows + 21 repo scripts + 10 advisor scripts + 4 companion sh/py).
- **HIGH findings:** all 4 in `.github/workflows/aeon.yml` at L86 / L94 / L96 / L812. `:812` held **8th consecutive scan** with no line drift (56-day pinned coordinate 2026-06-22 → 2026-08-17). Remediation blocked by self-improve rule 5 (operator direct-author only).
- **Audited clean:** chain-runner (ISS-017 env indirection holds), messages.yml (2026-04-11 incident-class fix holds), replicate-oneoff (env indirection), sync-upstream (internal step outputs), 2 cron-only + 2 empty workflows. Obfuscation sweep clean.
- **Issue lifecycle:** 0 new ISS filed, 0 closed.
- **Files created/modified:**
  - `articles/security-scan-2026-08-17.md` (report)
  - `memory/state/security-scan.json` (fresh delta_summary + cadence_note + 11th-consec sandbox note + 8th-consec-at-:812 note)
  - `memory/logs/2026-08-17.md` (skill-security-scan section appended)
- **Notify:** skipped per SKILL step 14 (pure PERSISTENT NOCHANGE = silent per "never notify on a pure no-op week" constraint).
- **Fleet context:** 1st successful skill-security-scan fire since 2026-08-03 (mon-batch auto-clear test #4 succeeded via direct Claude Code execution bypass — 4/4 mon-batch cohort clears today, memory-window-first full-cohort natural recovery).
- **Follow-up:** next scan 2026-08-24; if operator lands env-rebind PR for aeon.yml's 4 canonical HIGH before then, expect 4 RESOLVED HIGH transitions + first notify since 2026-06-01 baseline.
