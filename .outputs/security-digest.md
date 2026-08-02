*Security Digest — 2026-08-02*
Verdict: 2 malware to purge, nothing else fresh. quiet-cadence returns d2. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [GHSA-6wp2-7xxw-m8c6](https://github.com/advisories/GHSA-6wp2-7xxw-m8c6) — wacve-utils (pip) · malware · published 2026-08-02 12:30Z
  encrypted infostealer, Linux/Termux targets, exfil to Telegram (files + browser data + SMS).
  → block wacve-utils in pypi mirror; rotate any credentials on hosts that resolved it.
- [GHSA-4g95-5h46-4643](https://github.com/advisories/GHSA-4g95-5h46-4643) — pp-react-worldready (npm) · malware · published 2026-08-01 15:30Z
  OpenSSF Package Analysis flag — calls known-malicious domain.
  → block pp-react-worldready in npm mirror; audit lockfiles for the string.

_KEV: 0 fresh net-new (3 this-week, all covered 7-27→7-31). Reviewed CVEs: 0 fresh (all 4 critical + 24 high in 48h shipped in 8-01 14:52Z digest). Aeon-fleet clean vs both malware IDs._
