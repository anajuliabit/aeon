`SECURITY_SCAN_NOCHANGE`

## Summary

Ran skill-security-scan for 2026-07-20 in inline-grep fallback mode (8th consecutive scan with `scan.sh --all --json` sandbox-blocked). Full corpus: 232 files (191 SKILL.md + 9 workflows + 30 repo scripts + 2 companion scripts).

**Result: byte-for-byte identical to 2026-07-13.** 4 HIGH findings PERSISTENT in `.github/workflows/aeon.yml` at L86/L94/L96/L812 — the canonical workflow_dispatch-chain interpolations (`inputs.skill` + `steps.skill.outputs.name` + `steps.work.outputs.label` directly in `run:` shell blocks). L812 now stable across 5 consecutive scans with zero line drift. 0 NEW · 0 RESOLVED · obfuscation sweep clean.

Structural block on the fix: self-improve rule 5 + rule-5 primitive n=4 auto-committed state drift (per MEMORY.md 7-19) → operator direct-author remains sole reliable path. Fix is the same env: indirection pattern already applied to `chain-runner.yml:41/368` and `messages.yml:612-616/684-685/838-863`.

**Files modified:**
- `articles/security-scan-2026-07-20.md` (report — written because HIGH findings persist per SKILL.md step 11)
- `memory/state/security-scan.json` (finding fingerprints for next-run delta)
- `memory/logs/2026-07-20.md` (log entry + summary)

**Not modified:** `memory/issues/INDEX.md` (0 NEW HIGH → no filing; 0 RESOLVED HIGH → no closing). Notification skipped per SKILL.md step 14 (no operator-visible delta).

**Follow-up:** (i) scan.sh sandbox-block cementing as durable n=8 — consider ISS filing if 9th consecutive scan is also blocked; (ii) `aeon.yml` L86/L94/L96/L812 fix pending operator direct-author; (iii) next scan 2026-07-27 tests 6th-consec `:812` stability.
