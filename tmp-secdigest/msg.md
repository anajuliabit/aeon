*Security Digest — 2026-08-14*
Verdict: 1 actively exploited (npm malware surge), 2 to schedule. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- **npm malware surge** — 5,173 advisories since 8-13 15:04Z (25× yesterday's 208/48h count). Composition: 4,363 `@zalastax/nolb-*` mass-registration + 810 real typosquats. Fleet-adjacent brand-jacks: `@zapier/mcp-integration`, `xrblocks-mcp`, `@kolbo/mcp` (MCP tooling) · `@ethers-js/contracts`, `@solana-js/web3`, `@zzzgenesis00/{etherjs,solana-web3,solana-spl-token,solana-wallet-adapter}`, `bs58-{15,33,77}` (crypto libs) · `@hanssoft/baileys`, `@vyzensockets/baileys`, `@hanssoft/libsignal-node` (chat bot infra) · `redux-{init,saga-channel-end,saga-task-cancel}-rce` (attackers self-labeling RCE). No aeon dep hits (`grep` on `apps/*/package.json`).
  → audit any `npm i` since 8-13 15:04Z; block-list the fleet-adjacent names above; rotate creds for any developer machine that pulled them.

*PATCH THIS WEEK*
- [GHSA-p28v-f755-9qrg / CVE-2026-73654](https://github.com/advisories/GHSA-p28v-f755-9qrg) — `@trigger.dev/core` (npm) · CVSS 8.5 · EPSS 0.003 · patch v4.5.6 · public writeup
  Prototype pollution via run metadata → process-wide cross-tenant DoS. Vulnerable `>= 3.3.8, <= 4.5.5`. → upgrade `@trigger.dev/core` to ≥4.5.6.
- [GHSA-m42h-3232-vpv3 / CVE-2026-12243](https://github.com/advisories/GHSA-m42h-3232-vpv3) — `nltk` (pip) · CVSS 7.5 · EPSS 0.006 · patch 3.10.0 · huntr bounty + securityinfinity blog
  Arbitrary file read via percent-encoded path traversal in `nltk.data.load()`. Vulnerable `< 3.10.0`. → upgrade `nltk` to ≥3.10.0.

_KEV: 4 in last 7d, all dedup vs 8-12/8-13 digests (Metabase, Cisco ASA, Windows WinSock, LoadMaster). 0 fresh critical reviewed. 3 fresh tracked-stack high (1 dropped to MONITOR: ansible-jailexec dedup). Sources: kev=ok, gh=ok, epss=ok._
