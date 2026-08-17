*security digest — 2026-08-17*
verdict: 1 actively exploited, 0 to schedule, 3 to monitor. _sources: kev, gh advisory, epss_

*PATCH TODAY*
- [CVE-2025-62593](https://github.com/advisories/GHSA-q279-jhrf-cc6v) — ray (pip) · KEV added 2026-08-18 · EPSS 0.004 · CVSS n/a
  rce via dns rebinding through firefox/safari against the dashboard http server; nccgroup singularity poc referenced in advisory.
  → upgrade ray to ≥2.52.0 today.
- [GHSA-6mwf-mqp4-2f69](https://github.com/advisories/GHSA-6mwf-mqp4-2f69) — anthropic-setup (npm) · malware · brand-jack on anthropic namespace
  first anthropic-branded typosquat in memory-window; fleet-adjacent since aeon runs on claude sdk.
  → block anthropic-setup in every install path; rotate creds if any pipeline resolved it.
- agent-labeled npm malware cluster · 5 pkgs same 48h · malware
  @ai-vertical/ai-agent + agentsync-pkg + agent-bot-api + cloud-agen-bot + autoai — extends `agent-labeled-malicious-pkg` axis from 8-16 n=1 to n=2+.
  → treat any unknown "agent"-labeled npm pkg as suspect until source-verified.

*MONITOR*
- [CVE-2026-55158](https://github.com/advisories/GHSA-2qvg-qr73-mqxp) — wktk/conflibot (github actions) · CVSS 9.1 · no patch · EPSS 0
  command injection via crafted pr branch names under pull_request_target. → don't use conflibot; watch for fix.
- [CVE-2026-53728](https://github.com/advisories/GHSA-m44r-7c5h-m6mj) — @medplum/core (npm) · CVSS 7.1 · no patch · EPSS 0
  redirect uri not validated in external auth callback → auth-code leakage. → track; audit any medplum auth flows.
- [CVE-2026-40345](https://github.com/advisories/GHSA-ggr8-5vv4-36mx) — deepmerge-ts (npm) · HIGH · no patch · EPSS 0
  stack exhaustion when merging recursive object graphs. → track advisory.
