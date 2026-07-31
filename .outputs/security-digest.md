*Security Digest — 2026-07-31*
Verdict: 3 supply-chain campaigns to purge, 4 to schedule, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [ethers.js typosquat cluster (7 npm pkgs)](https://github.com/advisories/GHSA-q64r-f9q5-x6m3) — malware · crypto-dev-targeted
  ethers.json, ethers.jsonn, ethe.json, eth.json, ethersss, ethers-io-ethers, ethe. Credential stealers impersonating ethers.js.
  → `npm rm` any of these, audit lockfiles, rotate any wallet/RPC keys touched by dev machines.
- [fs-extra typosquat cluster (3 npm pkgs)](https://github.com/advisories/GHSA-cg95-x585-4q9p) — malware
  fs-extra-master, node-fs-extra-master, fsextrra. Impersonating one of the top-40M-weekly-downloads npm utilities.
  → `npm rm` and audit CI/build images; rotate any secrets present during install.
- [socket.io typosquat cluster (5 npm pkgs)](https://github.com/advisories/GHSA-9gmr-4p5m-j5vr) — malware
  socketi, soccketio, socktio, scketio, socktio. Broad-impact utility impersonation.
  → `npm rm` and grep `package.json` across the org.

*PATCH THIS WEEK*
- [GHSA-hf3j-86p7-mfw8](https://github.com/advisories/GHSA-hf3j-86p7-mfw8) — @aws-amplify/codegen-ui-react (npm) · critical · EPSS 0.009 · no CVSS
  Auth'd user runs arbitrary JS during Amplify Studio component build. → upgrade to ≥2.20.4.
- [GHSA-jq8w-8q2f-ffm9](https://github.com/advisories/GHSA-jq8w-8q2f-ffm9) — zitadel (Go) · CVE-2026-54693 · high · EPSS 0.003
  Users self-verify email/phone via API. → upgrade to ≥4.15.1 (v4 line) / ≥3.4.11 (v3).
- [GHSA-cg4g-m8jx-vjv2](https://github.com/advisories/GHSA-cg4g-m8jx-vjv2) — dssrf (npm) · CVE-2026-54722 · high · EPSS 0.003
  SSRF bypass via `remove_at_symbol_in_string`. → upgrade to >1.0.3.
- [GHSA-xpxj-f2fm-rqch](https://github.com/advisories/GHSA-xpxj-f2fm-rqch) — OliveTin (Go) · CVE-2026-67437 · CVSS 7.5 · EPSS 0.004
  Unauth'd DoS via OAuth2 state map growth. → upgrade past commit ec114e95d297 (2026-07-08 tip).

*MONITOR*
- [GHSA-xvg2-cgv6-6h7v](https://github.com/advisories/GHSA-xvg2-cgv6-6h7v) — netfoil (Go) · high · no CVE
  Incorrect block responses → localhost traffic. → upgrade to ≥0.4.0 when adopted; not in Aeon deps today.

_KEV added this week: 3 (Cisco FMC, Fortinet FortiOS, Arista VeloCloud) — all covered in 7-29/7-30 digests, dedup'd._
