*Security Digest — 2026-08-12*
Verdict: 3 actively exploited, 1 to schedule, 113+2 fresh malware packages. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-72898](https://www.cve.org/CVERecord?id=CVE-2026-72898) — Metabase · KEV added 2026-08-11 · CVSS 10.0 · EPSS 0.011
  unauthenticated SQL injection → admin, connected-DB credential theft, arbitrary data export.
  → upgrade Metabase to the vendor-fixed version today; rotate any DB credentials Metabase stored.
- [CVE-2026-20349](https://www.cve.org/CVERecord?id=CVE-2026-20349) — Cisco Secure Firewall ASA / FTD · KEV added 2026-08-11 · CVSS 8.6 · EPSS 0.010
  unauth remote heap-inspection DoS, device reload loop.
  → patch ASA/FTD firmware per Cisco advisory today.
- [CVE-2026-68820](https://www.cve.org/CVERecord?id=CVE-2026-68820) — Windows Ancillary Function Driver for WinSock · KEV added 2026-08-11 · CVSS 7.0 · EPSS 0.004
  local use-after-free → privilege escalation, patch-Tuesday driver bug.
  → install August 2026 Windows cumulative update today.
- Malware wave (npm + pip) — 113 npm + 2 pip fresh in 17h. defi-brand cluster: `permit2`, `boring-vault`, `augustdigital-sdk`, `camelot-ammv2-core`, `camelot-ammv2-periphery`, `upshift-config`, `upshift-finance`. namespace cluster: `@years18/n8n-nodes-utils-helper-{a..x}` (22 variants targeting n8n). `@bikli/*` + `base65-*` sub-clusters.
  → if any of these were installed, uninstall + rotate any secrets exposed to the install host.

*PATCH THIS WEEK*
- [GHSA-87fv-vqqr-m4jr](https://github.com/advisories/GHSA-87fv-vqqr-m4jr) — SeaweedFS (Go) · CVSS 9.3 · EPSS 0.004 · no public PoC
  unauthenticated SSRF with response read-back on volume-server gRPC — leaks cloud IMDS + IAM credentials on default deploys.
  → upgrade `github.com/seaweedfs/seaweedfs` to ≥ 4.24 (fix commit `69da20bdaec9`).
