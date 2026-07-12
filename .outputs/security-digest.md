*Security Digest — 2026-07-12*
Verdict: nothing urgent today. 3 to schedule, 2 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH THIS WEEK*
- [siyuan-note 5-cve go dump](https://github.com/advisories/GHSA-hvr9-72v2-fff3) — siyuan-note/siyuan/kernel · 4 critical + 2 high coordinated 7-10 disclosure · CVSS up to 9.9 · EPSS ≤ 0.006 · no PoC referenced
  unauth admin api via chrome-extension origin allowlist (CVE-2026-54069) anchors the batch, plus 3× stored-xss → rce 9.9 (CVE-2026-50551 / -54158 / -54067) + bazaar readme xss 7.1 (-54070). 34k-star self-hosted note app, filebrowser-class blast radius.
  → upgrade kernel past commit 2d5d72223df4 (2026-06-28).
- [GHSA-g936-7jqj-mwv8](https://github.com/advisories/GHSA-g936-7jqj-mwv8) — almeidapaulopt/tsdproxy (go) · CVSS 9.0 · no cve assigned · no PoC referenced
  internal proxy auth token forwarded to backend services enables management-api escalation. tailscale-adjacent reverse proxy.
  → upgrade to 1.4.4-0.20260603142855-434819b4421e.
- [GHSA-xrmc-c5cg-rv7x](https://github.com/advisories/GHSA-xrmc-c5cg-rv7x) — safeinstall-cli (npm) · CVSS 8.8 · no cve · no PoC referenced
  safeinstall agent-guard shell parser misses raw package execution. a supply-chain-defense tool with a bypass in its own guardrail — the tell is worse than the CVSS.
  → upgrade to ≥0.10.2.

*MONITOR*
- [CVE-2026-54071](https://github.com/advisories/GHSA-m8gf-v64p-gfmg) — babeldoc (pip) · CVSS 7.8 · EPSS n/a · no fix yet
  pickle deserialization in babeldoc/pdfminer/cmapdb.py CMap parser → arbitrary code exec on load. pdf tool used in academic + llm ingest pipelines.
  → track ≥0.6.3; do not parse untrusted pdfs meanwhile.
- [GHSA-h4g2-xfmw-q2c9](https://github.com/advisories/GHSA-h4g2-xfmw-q2c9) — clauster (pip) · no CVSS · no fix
  non-loopback deployments serve dashboard unauthenticated when auth.enabled is unset. config-default trap, not a code bug.
  → set `auth.enabled: true` or bind to loopback.
