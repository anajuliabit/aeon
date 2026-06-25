*Security Digest — 2026-06-25*
Verdict: 48 net-new npm malware drops, 1 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- 48 net-new npm malware advisories in last 48h (sustained ~24/day) — 5 KEV adds this week (Ubiquiti UniFi trio + Lantronix EDS5000 + Splunk) all deduped to prior logs, no net-new KEV today.
  notable clusters: 9× HubSpot-dev typosquats (`@su-doughnym/loginui|metrics-js|react-dlb|hubspot-loginui-poc` + `nabisco` + `signup-embedder` + `poc-publish-test-su-doughnym` + `hs-locale-management` + `two-factor-prompt-lib`); 3× `leo-*` (LeoSDK target: `leo-sdk`/`leo-cron`/`leo-logger`); popular-name spoofs `multer-express`, `vercel-api-client`, `markdownlint-cli2-fix`, `postcss-minify-selector(-parser)`, `vscode-test-web`.
  → audit any `npm install` / lockfile drift since 2026-06-23 against the [npm malware feed](https://github.com/advisories?query=type%3Amalware+ecosystem%3Anpm); on match: uninstall + rotate credentials touched by the install path.

*PATCH THIS WEEK*
- [GHSA-7fq5-7wr8-rjwj](https://github.com/advisories/GHSA-7fq5-7wr8-rjwj) — OliveTin (Go) · CVSS 7.5 · EPSS 0.004 · no public PoC
  shared `text/template.Template` instance in `service/internal/tpl/templates.go` — concurrent `tpl.Parse` overwrites the tree while another goroutine runs `Execute`, mixing one user's args into another's template. cross-user command contamination on any multi-user instance.
  → upgrade OliveTin to ≥3000.13.0 this week.
