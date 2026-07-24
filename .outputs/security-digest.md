*Security Digest — 2026-07-24*
Verdict: 3 npm-malware to check-and-purge, 5 to schedule this week, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY* — npm-malware wave (45 typosquats/attack-packages published in 24h — largest single-day batch this quarter)
- [GHSA-f246-8cf4-26v7](https://github.com/advisories/GHSA-f246-8cf4-26v7) — fs-extra-core (npm) · type=malware · typosquat of `fs-extra` (~30M weekly downloads)
  Highest-blast-radius typosquat in wave.
  → purge fs-extra-core from lockfiles today; rotate creds for any env that installed it.
- [GHSA-p53q-mf26-4h26](https://github.com/advisories/GHSA-p53q-mf26-4h26) — vue-demi-fix (npm) · type=malware · typosquat of `vue-demi`
  Vue ecosystem targeted.
  → purge vue-demi-fix from lockfiles; audit Vue projects.
- [GHSA-f99h-9jhg-jrxw](https://github.com/advisories/GHSA-f99h-9jhg-jrxw) — fastify-bundler (npm) · type=malware · Fastify-adjacent typosquat
  → purge fastify-bundler; audit Fastify projects.

*PATCH THIS WEEK*
- [CVE-2026-59822](https://github.com/advisories/GHSA-7488-6r32-c95q) — litellm (pip) · CVSS v4 8.8 · EPSS 0.002
  MCP auth bypass via OAuth2 passthrough fallback. AI-framework attack-surface signal n=2 — extends Langflow RCE KEV (7-21) rail.
  → upgrade litellm to ≥1.84.0.
- [CVE-2026-64645](https://github.com/advisories/GHSA-p9j2-gv94-2wf4) — next (npm) · CVSS v4 8.3
  SSRF in rewrites via attacker-controlled destination hostname.
  → upgrade next to ≥15.5.21 or ≥16.2.11.
- [CVE-2026-55685](https://github.com/advisories/GHSA-chx6-hx7r-mcp5) — react-router (npm) · CVSS v4 8.7
  Unauthenticated DoS via inefficient route matching.
  → upgrade react-router to ≥7.18.0.
- [CVE-2026-64649](https://github.com/advisories/GHSA-89xv-2m56-2m9x) — next (npm) · CVSS v4 8.3
  SSRF in Server Actions on custom servers.
  → upgrade next to ≥15.5.21 or ≥16.2.11.
- [CVE-2026-54673](https://github.com/advisories/GHSA-p2f4-r6v6-j797) — builder-util-runtime / electron-updater (npm) · CVSS v4 8.2
  Cross-origin redirect leaks `PRIVATE-TOKEN` + mixed-case `Authorization` headers.
  → upgrade builder-util-runtime to ≥9.7.0.

*MONITOR*
- [n8n 24-CVE mass-disclose](https://github.com/advisories?query=n8n) — npm · [[single-project-mass-disclose]] extends n=2 → n=3 (post-Pillow 7-20 / Gitea 7-21)
  Auth bypass, prototype pollution, credential leak, sandbox escape, Git-node RCE across 24 advisories in ~2h window.
  → if running n8n, upgrade to ≥1.123.67 / ≥2.32.1 / ≥2.31.5.
- [GHSA-4w2j-m93h-cj5j](https://github.com/advisories/GHSA-4w2j-m93h-cj5j) — quinn-proto (rust/crates.io) · CVSS 7.5
  Remote memory exhaustion via unbounded out-of-order stream reassembly.
  → upgrade quinn-proto to ≥0.11.15.
- [CVE-2026-59935 + CVE-2026-59936](https://github.com/advisories/GHSA-g867-7843-wf8q) — pypdf (pip) · CVSS v4 8.7
  Infinite loop on malformed inline images (ASCII85/ASCIIHex).
  → upgrade pypdf to ≥6.14.2 if processing untrusted PDFs.
