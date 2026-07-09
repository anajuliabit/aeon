*Security Digest — 2026-07-09*
Verdict: 1 actively exploited (Nuclio 10.0, public PoC) + npm malware wave day-2. 5 to schedule, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-52831](https://github.com/advisories/GHSA-v5px-423j-pf7p) — nuclio (Go) · CVSS 10.0 · public PoC
  Unsanitized cron-trigger headers/body injected into K8s CronJob shell → root RCE.
  → upgrade nuclio to ≥1.16.4 today.
- *npm malware wave day-2* — 27 fresh advisories in 24h; AI/coding-tool brand-jack cluster
  `myclaude-code`, `clavue`, `clavue-agent-sdk`, `calvuepro`, `clavuepro`, `n8n-nodes-mcputils`, `gitlens`, `nodemon-sudo`, `tailwind-core`, `@vite-ln/build-ts` — Claude Code / n8n / Vue / nodemon / Tailwind typosquats.
  → audit last 24h npm installs; rotate any creds exposed to these packages.

*PATCH THIS WEEK*
- [CVE-2026-53649](https://github.com/advisories/GHSA-xqhv-chqm-fhcc) — joro (Go) · CVSS 9.6 · no public PoC
  Unauth cross-origin plugin upload via loopback API lacking CORS → RCE. → upgrade joro past commit 5c0ca35db828 (2026-06-01).
- [CVE-2026-53513](https://github.com/advisories/GHSA-5rr4-8452-hf4v) — @better-auth/sso (npm) · CVSS 9.6 · no PoC
  OIDC endpoint URL unvalidated on provider registration → SSRF to internal services, potential account takeover. → upgrade to ≥1.6.11.
- [CVE-2026-50197](https://github.com/advisories/GHSA-659f-rgp5-w4wf) — skipper (Go) · CVSS 8.7 · public PoC
  `opaAuthorizeRequestWithBody` skips OPA on `Transfer-Encoding: chunked` / HTTP/2. → upgrade skipper to ≥0.26.10.
- [CVE-2026-49471](https://github.com/advisories/GHSA-37h2-6p4f-mp3q) — serena-agent (pip) · CVSS 8.3 · public PoC
  LLM coding agent's unauth Flask dashboard on port 24282 → DNS-rebind → memory-poison → `subprocess.Popen(shell=True)` RCE. → upgrade serena-agent to ≥1.5.2.
- [CVE-2026-49825](https://github.com/advisories/GHSA-4jhm-jv67-739f) — lxml_html_clean (pip) · CVSS 8.2 · no PoC
  `Cleaner` doesn't strip `javascript:` URLs from namespaced URL attributes → XSS bypass. → upgrade lxml_html_clean to ≥0.4.5.

*MONITOR*
- [GHSA-52vm-mxx8-f227](https://github.com/advisories/GHSA-52vm-mxx8-f227) — phantom-audio (pip) · CVSS 7.7 · no fix line yet
  Unconfined MCP tool paths → arb file write + decode-bomb DoS. → watch MCP tool sandboxing pattern.
- [GHSA-836r-79rf-4m37](https://github.com/advisories/GHSA-836r-79rf-4m37) + [GHSA-2wc2-fm75-p42x](https://github.com/advisories/GHSA-2wc2-fm75-p42x) — soupsieve (pip) · CVSS 7.5 × 2
  ReDoS + memory exhaustion in BeautifulSoup selector dep. → pin scrapers to patched line when released.
- [GHSA-fqf6-gxhh-2xhw](https://github.com/advisories/GHSA-fqf6-gxhh-2xhw) — uucore (rust) · silent data loss
  `--suffix` alone doesn't enable backup mode in cp/mv/install/ln (silent divergence from GNU). → watch for uutils patch.
