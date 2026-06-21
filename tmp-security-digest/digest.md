*Security Digest — 2026-06-21*
verdict: 2 actively exploited, 5 to patch this week, 1 to monitor. _sources: kev, gh advisory, epss_

*PATCH TODAY*
- [CVE-2026-20253](https://nvd.nist.gov/vuln/detail/CVE-2026-20253) — splunk enterprise · kev added 2026-06-18 · epss 0.10 (95th%) · cvss n/a
  unauth file create/truncate via postgres sidecar endpoint. cisa due 2026-06-21.
  → apply svd-2026-0603 today.
- [CVE-2026-48907](https://nvd.nist.gov/vuln/detail/CVE-2026-48907) — joomla content editor (widget factory) · kev added 2026-06-16 · epss 0.07 (93rd%) · cvss n/a
  unauth php upload+exec via new editor-profile creation.
  → apply jce free patch / upgrade per joomlacontenteditor.net.
- 10 malicious npm packages flagged 2026-06-19→21 ([GHSA-chhh-8532-pg35](https://github.com/advisories/GHSA-chhh-8532-pg35) +9) — typo-squat wave incl. ethereum-gas-reporter, eth-util, mongoose-jsonify, pretty-logger-js, assert-kit, new-ecro, ts-ecro family
  newly-published malicious versions; credential-stealer pattern.
  → grep lockfiles for the 10 names; if any installed, uninstall + rotate any creds the process touched.

*PATCH THIS WEEK*
- [CVE-2026-55255](https://github.com/advisories/GHSA-qrpv-q767-xqq2) — langflow (pip) · cvss 9.9 · epss n/a
  idor on /api/v1/responses lets authed users read other users' flows.
  → upgrade langflow to ≥1.9.1.
- [CVE-2026-54051](https://github.com/advisories/GHSA-qw6v-5fcf-5666) — network-ai (npm) · cvss 9.9 · epss n/a
  os command injection.
  → upgrade network-ai to ≥5.9.1.
- [CVE-2026-55447](https://github.com/advisories/GHSA-ccv6-r384-xp75) — langflow (pip) · cvss 9.6 · epss n/a · poc in advisory
  basefilecomponent arbitrary file read chained to rce.
  → upgrade langflow to ≥1.9.2 (covers 55255 + 55447).
- [CVE-2026-48814](https://github.com/advisories/GHSA-r78r-rwrf-rjwp) — network-ai (npm) · cvss 9.1 · epss n/a
  fix for cve-2026-46701 was incomplete — empty default secret still authorizes all requests.
  → upgrade network-ai to ≥5.7.2 (or 5.9.1 to also cover 54051).
- [GHSA-x845-2f78-7v36](https://github.com/advisories/GHSA-x845-2f78-7v36) — blocky (go) · cvss 8.6 · epss n/a
  dnssec validation bypass + cache-scope pollution.
  → upgrade blocky to ≥0.32.0.

*MONITOR*
- [GHSA-wfqx-gjrf-g28r](https://github.com/advisories/GHSA-wfqx-gjrf-g28r) — crossplane (go) · cvss 9.0 · no fix yet
  signature-verification toctou: mutable tag lets attacker swap package content post-verify.
  → pin images by digest; track for patched release.
