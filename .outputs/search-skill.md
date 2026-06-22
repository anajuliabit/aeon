*Search Skills — 2026-06-22*
Gap: vuln-scanner failing 7% (29 runs) — ISS-018 open, semgrep/trufflehog binaries blocked in sandbox.

Candidates (not auto-installed — all UNTRUSTED sources):
- **vulnerability-scanner** — davila7/claude-code-templates (gap-fit 5/5, sum 19/20, UNTRUSTED) — pure-python OWASP 2025 + supply-chain checklist scanner, no binary deps. Sidesteps ISS-018.
- **security-audit** — davila7/claude-code-templates (gap-fit 4/5, sum 17/20, UNTRUSTED) — workflow bundle: recon → vuln-assess → pentest → harden. Heavier than current vuln-scanner.
- **code-security** — semgrep/skills (gap-fit 3/5, sum 15/20, UNTRUSTED) — secure-coding rules across 15+ langs, prompt-only, no semgrep binary needed. Different scope (write-time rules vs scan-time).

Manual install (after review):
```
./add-skill davila7/claude-code-templates vulnerability-scanner
```

Sources: npx=ok vercel=0 anthropics=0 bankr=2(both dupes) skills.sh=ok
