*Security Digest — 2026-07-26*
Verdict: 1 supply-chain compromise TODAY (52 real @antv npm packages), 4 to schedule, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [Mini Shai-Hulud @antv/* 52-pack](https://github.com/advisories/GHSA-9wwp-32v6-mhm5) — npm · type=malware · published 12:25Z today
  `atool` maintainer account takeover pushed 631 malicious versions across 314 packages in a 22-minute burst. Preinstall hook runs a 498KB obfuscated Bun script that steals AWS/GH-PAT/npm/GCP/Azure/K8s/SSH/Docker/DB/Stripe/Slack creds, exfils via GH API to Dune-themed attacker repos (`harkonnen-melange-*`), and injects CI/CD workflow persistence. Malicious versions: `2.1.46` and `2.2.46` on every @antv/* pkg (g-plugin-*, data-wizard, dw-util, f2-*, dipper-*, calendar-heatmap, chart-linter, awards, and 44 more).
  → grep every lockfile for `@antv/` at `2.1.46` or `2.2.46`; if hit, rotate every cred that touched CI or a dev shell, pin to the prior version, rebuild the lockfile.

*PATCH THIS WEEK*
- [GHSA-rjg6-39jm-rgg4](https://github.com/advisories/GHSA-rjg6-39jm-rgg4) — @better-auth/scim (npm) · CVSS 9.9 · no public PoC
  SCIM provider-id collision on magic-link / email-OTP sign-in → account takeover + stale access. → upgrade @better-auth/scim to ≥1.6.22 (or ≥1.7.0-beta.10).
- [Budibase 15-CVE mass-disclose](https://github.com/advisories/GHSA-q6x4-v3qx-85qw) — @budibase/server (npm) · 3 crit + 12 high · fix 3.40.0
  Unauth REST-datasource cred theft (GHSA-mqhr) + OIDC SSO account takeover (GHSA-hp6v) + MySQL SQLi (CVSS 9.6) + SSRF/NoSQLi/IDOR pack. Extends single-project-mass-disclose to n=5 (Pillow / Gitea / n8n / GitPython / Budibase). → upgrade @budibase/server to ≥3.40.0.
- [GHSA-vh45-f885-3848](https://github.com/advisories/GHSA-vh45-f885-3848) — sm-crypto (npm) · CVSS 9.1 · no public PoC
  Default RNG uses `Math.random` + wall clock for SM2 key generation. Any key generated with sm-crypto on Node is guessable — treat as burned. → upgrade sm-crypto to ≥0.5.0 and re-issue affected keys.
- [GHSA-w4hw-qcx7-56pr](https://github.com/advisories/GHSA-w4hw-qcx7-56pr) — shescape (npm) · critical · no CVE
  Shell injection via unescaped parentheses on Windows CMD (bypass of the prior fix). → upgrade shescape to ≥2.1.14 (v2 line) or ≥3.0.1 (v3 line).
- [GHSA-xg4h-6gfc-h4m8](https://github.com/advisories/GHSA-xg4h-6gfc-h4m8) — etcd (Go) · authz bypass · no CVSS printed
  Watch API open-ended range requests bypass authorization; sibling GHSA-6vch also patches an unbounded-goroutine TLS handshake DoS. Kubernetes-adjacent blast. → upgrade etcd to ≥3.7.1 / ≥3.6.14 / ≥3.5.33.

*MONITOR*
- [GHSA-hmj8-5xmh-5573](https://github.com/advisories/GHSA-hmj8-5xmh-5573) — libp2p (pip) · CVSS 7.5 · no fix yet
  yamux connection DoS via oversized data frame. → rate-limit inbound peer streams; watch for release.
- **@akunsansan0/* npm autopublish flood** — 184 tea.xyz reward-farming pkgs published today (11× yesterday's 20/day rate). Noise-signal, not action; autopublish-flood rail extends.
- **KEV: 0 fresh this week** — all 6 additions (CheckPoint / SharePoint / WordPress×2 / Langflow / DD-WRT) already surfaced 7-22/7-23; kev-quiet-cadence d4.
