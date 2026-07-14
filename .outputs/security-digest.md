*Security Digest — 2026-07-14*
Verdict: npm-malware wave resurfaces after 5-day quiet (30 pkgs same-day), 2 KEV items live, DIRAC pip 4-CVE RCE cluster to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- npm-malware wave RESURFACES d1 — 30 pkgs published 05:09–14:20Z today across coordinated batches: [@sqlite-panel](https://github.com/advisories/GHSA-mq68-3vc3-ch3q) / [@sqlite-group](https://github.com/advisories/GHSA-cf6c-6x68-cf8r) / [@sqlite-clone](https://github.com/advisories/GHSA-x8m3-m829-mhc4) fake-sqlite, nodemon-plint / nodemon-delog / motion-pull typosquats, humanize-kit / string-morph / temp-cloak / clipboard-drop / dom-weave cluster, [@tonsdk/core](https://github.com/advisories/GHSA-hw5x-gw43-m4mx) + [@resolvx/core](https://github.com/advisories/GHSA-5fvj-272r-496w) crypto-scope, [@oliviamcdaniel12/safer-buffer](https://github.com/advisories/GHSA-88h2-qq8c-r5pv) safer-buffer typosquat. Breaks 5-day quiet streak clean.
  → audit npm deps for these + typosquat lookalikes; rotate any creds exposed to postinstall on affected versions.
- [CVE-2008-4128](https://nvd.nist.gov/vuln/detail/CVE-2008-4128) — Cisco IOS 12.4 CSRF · KEV added 2026-07-13 · EPSS 0.24 · BOD 26-04 due 2026-07-16
  17-year-old CVE fresh into KEV; IOS 12.4 mainline is EOL/obsolete per Cisco.
  → retire IOS 12.4 devices today, or apply Cisco mitigations before 7-16.
- [CVE-2026-48282](https://helpx.adobe.com/security/products/coldfusion/apsb26-68.html) — Adobe ColdFusion path traversal → RCE · KEV 2026-07-07 · EPSS 0.29 · due 7-10 (passed)
  Recurring KEV-week carry; federal due date already blown.
  → patch to APSB26-68 today.

*PATCH THIS WEEK*
- DIRAC (pip) 4-CVE cluster — [GHSA-m4m7](https://github.com/advisories/GHSA-m4m7-4cw8-62j6) (CVE-2026-61667, CVSS 9.9 SQL+eval RCE FileCatalog) / [GHSA-9jpv](https://github.com/advisories/GHSA-9jpv-c7p4-997x) (CVE-2026-45579, CVSS 9.9 eval RCE RequestManager) / [GHSA-7xw9](https://github.com/advisories/GHSA-7xw9-549r-8jrc) (CVSS 8.5 PilotManager SQLi + missing auth) / [GHSA-vg99](https://github.com/advisories/GHSA-vg99-gr89-qhw9) (CVE-2026-61668, CVSS 8.1 pilot code over unverified HTTPS). EPSS n/a on all 4 (too fresh). LHCb Grid computing package; one upgrade fixes the cluster.
  → upgrade DIRAC to ≥8.0.79 / 9.0.22 / 9.1.10 (whichever branch).
- [GHSA-xf7x-x43h-rpqh](https://github.com/advisories/GHSA-xf7x-x43h-rpqh) — json-repair (pip) · CVSS 7.5 · no CVE assigned
  Circular JSON Schema `$ref` → unbounded CPU DoS on untrusted input.
  → upgrade json-repair to ≥0.60.1.
