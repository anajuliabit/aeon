## Summary

Ran the security-digest skill for 2026-07-23. Pulled CISA KEV (9 entries added in the 7-day window), GH Advisory Database (9 critical / 98 high / 100+ malware in 48h), and EPSS enrichment. Deduplicated against last 2 days of logs (13 CVEs + 25 GHSAs already covered).

**Ranked 3/5/3 tiers:**

- **PATCH TODAY** — 2 fresh KEV adds (SharePoint deserialization RCE CVE-2026-50522 EPSS 0.21 + Check Point SmartConsole auth bypass CVE-2026-16232, both CISA-due 2026-07-25) + npm `ethers-wallet-package` malware trio (wallet-stealer typosquat, all 3 published today 01:01Z).
- **PATCH THIS WEEK** — 2 fresh next-auth criticals published today (fail-open + homoglyph @ bypass, 15min apart), postcss arbitrary file read (fix 8.5.12), svgo removeScripts XSS 8.2, JupyterLab XSS pair.
- **MONITOR** — pyasn1 3-CVE DoS cluster (fix 0.6.4, transitive under `cryptography`), immutable.js List trie DoS, malware feed volume (100+/48h, 61 pip + 38 npm + 1 composer).

**Notable pattern surface:** SharePoint dual-KEV week (CVE-2026-50522 6 days after CVE-2026-58644, same product), npm-auth-primitive same-day-double (2 next-auth crits within 15min), ethers-wallet trio extends `[[wallet-credential-stealer-supply-chain]]` rail from n=1 (injective 6-27) to n=4.

**Delivery:** Digest is 3120 chars (under 4000 cap), queued at `.pending-notify/1784820704.md` for post-run delivery — bash `>` redirect regression continued today (n=3 same-week), `./notify` script exec blocked, so wrote the pending file directly and let the post-run step ship it.

**Files:** `.pending-notify/1784820704.md` (digest), `memory/logs/2026-07-23.md` (log entry appended with tier counts, IDs, source status, notable patterns, and full skill summary). Log line: `SECURITY_DIGEST_OK`.

**Follow-up:** SharePoint dual-KEV suggests ongoing ToolShell-class exploit chain worth naming; next-auth `[[same-day-double-critical]]` is a fresh pattern candidate; T-2 Friday 7-25 = both KEV due dates + H unlock cliff = triple-signal day.
