*Security Digest — 2026-08-05*
Verdict: 3 actively exploited (2 fresh KEV + 408-pkg npm malware peak), 4 to schedule (Flowise 9-CVE researcher-drop + N-central KEV tail + Open WebUI 7-pack + Ghost XSS). memory-window malware peak (408 > 8-01's 318). _Sources: KEV, GH Advisory, EPSS._

*PATCH TODAY*
- [CVE-2026-9198](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — IBM Langflow · KEV added 2026-08-04 · EPSS 0.171 (97th pct) · unauth full RCE via code injection · CISA due 2026-08-07
  6th unauth-agent-framework-CVE in KEV; extends `[[AI-framework-attack-surface]]` to KEV-confirmed.
  → upgrade Langflow to ≥1.5.1 today, or pull internet-exposed instances offline.
- [CVE-2026-34486](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — Apache Tomcat · KEV added 2026-08-04 · **EPSS 0.812 (99.6th pct — top single-CVE score this quarter)** · EncryptInterceptor bypass · CISA due 2026-08-07
  → patch Tomcat to 9.0.109 / 10.1.44 / 11.0.10 today; audit cluster-comm channels.
- 408-package npm malware mega-batch (24h post-8-04-digest) — memory-window peak (prior 8-01 at 318). Signature: **Tinkoff mega-corp-scope 100+ pkgs** (`tinkoff-*`, `statist-browser-typed-client-*`, `tramvai-tinkoff-*`, `volna-boxy-*`, `platform-ui-*`) + **wallet-cluster extension d2** (`@zzzgenesis00/ethers-wallet`, `@zzzgenesis00/bip39-mnemonic`, `@zzzgenesis00/spl-token-utils`, `trezor-lib`, `ledger-lib`, `ckcc-protocol`, `hwi-lib`, `wallet-analytics`) + **Polymarket-sub-cluster NEW** (`polyclob-api`, `poly-provider-api`, `polymarket-toolkit`) + **@umacloud CLI multi-arch 7-variant** + **@qlik/@nebula.js BI-vendor scope** + beaver-ui-*/bigops-* continuations.
  → grep repos for direct deps of any listed prefix; if a build pulled `@zzzgenesis00/*` / `ckcc-protocol` / `ledger-lib` / `trezor-lib` in last 24h, rotate wallet seeds + revoke keys.

*PATCH THIS WEEK*
- [Flowise 9-CVE researcher-drop](https://github.com/advisories?query=flowise+2026-08-04) — npm · all no-patch, published 8-04 15:13Z–19:37Z · CSV-agent Pyodide RCE (CVE-2026-69255 "Root Shell Verified"), NodeVM sandbox escape (CVE-2026-69254), SQLite-Record-Manager RCE (CVE-2026-69259), CSV-agent prompt-injection RCE (CVE-2026-70477), Pyodide Unicode homoglyph bypass (CVE-2026-70470), OAuth2 refresh-endpoint token exfil (CVE-2026-70478), MCP env-var blocklist bypass (CVE-2026-69263, bypass of CVE-2025-8943)
  → isolate all Flowise deployments this week; assume compromise if internet-exposed since 8-04; watch upstream for coordinated release. Rail n=6.
- [CVE-2026-18556](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) — N-able N-central · KEV added 8-04 · **parent of CVE-2026-18577 (dedup'd 8-03 KEV)** · auth-bypass via alternate path · due 2026-08-07
  Incomplete-patch chain confirmed: original bug → 18556 → 18577 (incomplete-patch), `[[RMM-platform-in-KEV]]` continues.
  → confirm N-central 2026.3 HF1 covers both CVE IDs; discontinue if not.
- [Open WebUI 7-CVE cluster](https://github.com/advisories?query=open-webui+2026-08-04) — pip · published 8-04 19:40Z–21:54Z · stored XSS via KaTeX (CVE-2026-70492 8.7), same-origin XSS→ATO (70486 8.2), OAuth ATO accepts any-client tokens (70482 8.1), collab folder-delete (70494 8.1), SSRF via Playwright loader (70479 7.7), NAT64 internal-services SSRF (70485 7.1)
  → upgrade Open WebUI to ≥0.6.35 this week; disable public signup on self-hosted.
- [CVE-2026-53950](https://github.com/advisories/GHSA-xpp7-93x6-v29m) — @tryghost/activitypub (npm) · CVSS 7.5 · XSS in Ghost's ActivityPub client
  → upgrade @tryghost/activitypub to fix release.

_KEV this week: 5 (3 fresh 8-04: Langflow + Tomcat + N-central-parent; 2 dedup'd: N-central-child 8-03 + Cisco FMC 7-29). Aeon-fleet clean d7 vs digest surface._
