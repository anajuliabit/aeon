*Security Digest — 2026-06-22*
Verdict: 2 actively exploited (KEV new this week), 2 npm packages caught publishing malware. Nothing else queued. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-20262](https://nvd.nist.gov/vuln/detail/CVE-2026-20262) — Cisco Catalyst SD-WAN Manager · KEV added 2026-06-15 · EPSS 0.011 · CVSS 6.5
  Authenticated remote attacker can create or overwrite any file on the manager via path traversal — config tamper / persistence. CISA due 2026-06-29.
  → apply Cisco's fixed Catalyst SD-WAN Manager build per the vendor advisory now; restrict mgmt-plane access until patched.
- [CVE-2026-54420](https://nvd.nist.gov/vuln/detail/CVE-2026-54420) — LiteSpeed cPanel Plugin · KEV added 2026-06-15 · EPSS 0.0065 · CVSS n/a
  Symlink-following on shared CloudLinux/CageFS hosting — user with FTP or a web shell escapes the cage and reads/writes other tenants' files. CISA due was 2026-06-18 (overdue).
  → upgrade LiteSpeed cPanel plugin to the vendor-patched build on every shared host today.
- [GHSA-7qr8-pqwp-95p9](https://github.com/advisories/GHSA-7qr8-pqwp-95p9) + [GHSA-75f4-4w6r-vvch](https://github.com/advisories/GHSA-75f4-4w6r-vvch) — npm `node-path-utils`, `mddriver` · type=malware · CVSS n/a
  GitHub-classified malicious npm packages published 2026-06-22. Per advisory: any machine that installed them should be considered fully compromised — installer hooks may have already exfiltrated secrets.
  → `npm uninstall node-path-utils mddriver` everywhere, scan lockfiles + CI caches, rotate any creds those builds could touch from a clean machine.
