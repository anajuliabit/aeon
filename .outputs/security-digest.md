*Security Digest — 2026-07-28*
verdict: 3 to patch today (2 fresh KEV + 1 malware digest), 2 to schedule, monitor empty. _sources: CISA KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2025-68686](https://nvd.nist.gov/vuln/detail/CVE-2025-68686) — Fortinet FortiOS · KEV added 2026-07-27 · EPSS 0.013 · CWE-200 · due 2026-08-10
  post-exploit symlink-persistency bypass, unauth remote via crafted HTTP after prior filesystem foothold. CISA lists as exploited.
  → apply Fortinet FG-IR-25-934 mitigations today; if no vendor patch available, discontinue per BOD 26-04.
- [CVE-2026-16812](https://nvd.nist.gov/vuln/detail/CVE-2026-16812) — Arista VeloCloud Orchestrator On-Prem · KEV added 2026-07-27 · EPSS 0.010 · CWE-78 · due 2026-07-30
  unauth OS-command injection reaching VCO host. two-day CISA deadline.
  → apply Arista SA-0144 patch today.
- *npm supply-chain digest* — 3 fresh campaigns + Mini Shai-Hulud d2 tail (all `type=malware`)
  - **Mini Shai-Hulud d2** — 61 fresh @antv/* GHSA IDs since 7-27 (e.g. [GHSA-hgqm-cwrq-xx84](https://github.com/advisories/GHSA-hgqm-cwrq-xx84) @antv/matrix-util). same atool-account-takeover cred-stealer chain as 7-27, more pkg/versions flagged.
  - **claude-code-base-action typosquat** — [GHSA-3x98-842h-2764](https://github.com/advisories/GHSA-3x98-842h-2764) (npm v2.0.0 + v2.2.2). masquerades as the anthropics/claude-code-base-action GitHub Action; ossf flagged for c2-domain traffic. aeon uses `@anthropic-ai/claude-code` cli — not this pkg — clean.
  - **@wagni_bot/* 25-pack** — GHSA-vr92-xmj8-jr8v @wagni_bot/eth + 24 siblings across metamask/opensea/polymarket/hyperliquid/bsc scopes. web3-bot scope-typosquat class.
  - **polymarket-* 23-pack + mcp-server/anthropic-internal 15-pack** — polymarket-trading-cli / polymarket-terminal / mcp-server-{sentry,supabase,redis,git,notion,fetch,postgres,figma,github} + fake `anthropic-internal-tools` / `claude-internal-utils` — dependency-confusion class targeting AI-tooling CI.
  → uninstall + rotate creds if any @antv/@wagni_bot/polymarket-*/mcp-server-*/claude-code-base-action pkg is in a lockfile touched in last 7d. block scopes at registry proxy.

*PATCH THIS WEEK*
- [GHSA-4pj9-g833-qx53](https://github.com/advisories/GHSA-4pj9-g833-qx53) — lettre (crates.io) · CVE-2026-46428 · CVSS v4 9.1 · EPSS 0.002 · PoC in advisory
  inverted boolean disables TLS hostname verification when built with `boring-tls`. any chain-valid cert intercepts SMTP + credentials. affects v0.10.1 through v0.11.21.
  → upgrade lettre to ≥0.11.22.
- [GHSA-w6p7-2fxx-4f44](https://github.com/advisories/GHSA-w6p7-2fxx-4f44) — Pocket ID (Go) · CVE-2026-43983 · CVSS v4 8.5 · EPSS 0.002
  OIDC refresh-token flow bypasses authorization revocation, account disabling, and group restrictions. long-lived tokens survive admin actions.
  → upgrade Pocket ID to commit ≥978ac87 (pseudo-version 20260419162744).
