*Security Digest — 2026-08-15*
Verdict: crypto-lib brand-jack wave holds, 2 CVSS 8+ tracked-stack to schedule, 2 no-patch to monitor. KEV quiet 3-consec-day. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- npm malware wave — 5,219+ advisories in 48h (feed-capped). Fresh fleet-adjacent brand-jacks post-yesterday cutoff: `@polymarkets/clob-client-v2`, `@mexc/shared-utils`, `@devmikets/hyperliquid-sdk`, `@lodash-js/lodash-js`, `sui-gql-lite`, `@convera/ui-shared`. New `abina-amu*/abina-amog*` namespace-flood (~50 pkgs in one burst, 2nd instance of same shape after `@zalastax/nolb-*` on 8-14).
  → audit npm installs; block/rotate creds exposed to unfamiliar `@polymarkets/*`, `@mexc/*`, `@devmikets/*` scoped names.

*PATCH THIS WEEK*
- [CVE-2026-55157](https://github.com/advisories/GHSA-49mq-fc6q-3h46) — `@ooples/token-optimizer-mcp` (npm) · CVSS 8.4 · EPSS 0 · full PoC in advisory
  OS command injection in `smart_user` tool via crafted `username` → arbitrary shell exec as MCP-server user.
  → upgrade `@ooples/token-optimizer-mcp` to ≥5.1.0.
- [CVE-2026-53657](https://github.com/advisories/GHSA-2j9v-p4xj-cjw2) — `lima-vm/lima/v2` (Go) · CVSS 8.2 · EPSS 0.001 · no public PoC
  QEMU driver: any VM user → root via `/run/lima-guestagent.sock`. Not exploitable on vz driver.
  → upgrade lima to ≥v2.1.3, or switch to vz driver (macOS default), or `--plain` to disable guest agent.

*MONITOR*
- [GHSA-29rf-f4vv-pvq6](https://github.com/advisories/GHSA-29rf-f4vv-pvq6) — `authorizer` (Go) · no CVSS · no fix · zero-click account takeover via OAuth identity linking to unverified email.
  → track patch; disable OAuth identity linking if enabled.
- [GHSA-5fpj-28rv-84r7](https://github.com/advisories/GHSA-5fpj-28rv-84r7) — `@budibase/server` (npm) · no CVSS · no fix · SSRF in Webhook/Zapier/N8N/Slack/Discord automations bypasses IP blacklist.
  → track patch; front automations with an egress proxy that filters RFC1918.
