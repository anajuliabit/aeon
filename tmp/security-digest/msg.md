*Security Digest — 2026-07-02*
Verdict: 1 actively exploited, 2 supply-chain live, 5 to schedule. Agent-infra & MCP dominate. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-45659](https://nvd.nist.gov/vuln/detail/CVE-2026-45659) — Microsoft SharePoint Server · KEV added 2026-07-01 · CVSS 9.6
  Deserialization RCE, authorized-attacker. Exploited per CISA · BOD 26-04 due 2026-07-04.
  → patch SharePoint 2016 ≥16.0.5552.1002 / 2019 ≥16.0.10417.20128 / Subscription ≥16.0.19725.20280 today.
- [GHSA-w2r4-4x6j-3h5x](https://github.com/advisories/GHSA-w2r4-4x6j-3h5x) — vitest-agent (npm) · malware · agent-infra brandjack
  Full host compromise on install. Extends agent-infra brandjack wave into testing frameworks (day 6).
  → uninstall vitest-agent; rotate every secret from a clean machine.
- [GHSA-3cr6-gpr8-pjfm](https://github.com/advisories/GHSA-3cr6-gpr8-pjfm) — tailwind-animates + kin (npm) · malware · Tailwind cluster
  3-pkg same-day publish: tailwind-animates, animatecss-postcss-plugin, tailwind-typography-stylecss.
  → grep package-lock; block install of Tailwind look-alikes.

*PATCH THIS WEEK*
- [GHSA-84hp-mqvj-3p8h](https://github.com/advisories/GHSA-84hp-mqvj-3p8h) — mcp-memory-service (pip) · CVSS 9.8 · public PoC
  Missing auth on document API — unauth read/write/delete of every stored memory.
  → upgrade mcp-memory-service ≥10.67.1.
- [GHSA-xr65-5cpm-g36x](https://github.com/advisories/GHSA-xr65-5cpm-g36x) — rancher/fleet (Go) · CVSS 9.9 · no PoC
  Cross-namespace secret disclosure via unvalidated `valuesFrom`.
  → upgrade Fleet ≥0.15.2 / 0.14.6 / 0.13.11 / 0.12.15.
- [GHSA-mhc6-2gfq-xx62](https://github.com/advisories/GHSA-mhc6-2gfq-xx62) — rancher (Go) · CVSS 9.6 · EPSS 0.011
  YAML command injection at cluster import.
  → upgrade Rancher ≥2.14.2 / 2.13.6 / 2.12.10 / 2.11.14 / 2.10.12.
- [GHSA-62q6-4hv4-vjrw](https://github.com/advisories/GHSA-62q6-4hv4-vjrw) — ghost (npm) · CVSS 9.6 · no PoC
  Cache-poisoning XSS via `x-ghost-preview` header. → upgrade Ghost ≥6.37.0.
- [GHSA-9mm9-rqhj-j5mx](https://github.com/advisories/GHSA-9mm9-rqhj-j5mx) — repomix (npm) · CVSS 8.8 · public PoC
  `--remote-branch` argument-injection RCE in the AI-coding packer. → upgrade repomix ≥1.14.1.
