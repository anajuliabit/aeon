*Security Digest — 2026-06-29*
Verdict: 3 npm supply-chain compromises today, 0 net-new KEV (day 4), 0 tracked-stack adds after dedup. _Sources: KEV ok, GH Advisory ok, EPSS ok_

*PATCH TODAY*
- [GHSA-7rfm-v32j-2583](https://github.com/advisories/GHSA-7rfm-v32j-2583) — crossmint-wallets-sdk (npm) · malware · published 02:21 UTC
  Brandjack of Crossmint's wallet SDK. Sibling `@epsteinlovekids483/crossmint-wallets-sdk-pentest` (GHSA-x7jg-w433-8q2r) published same minute — 2-pkg campaign targeting Web3 devs.
  → remove `crossmint-wallets-sdk` from any project lockfile; rotate every wallet/API/SSH/cloud secret on machines that ran `npm i`; pin to vendor's actual `@crossmint/*` packages.
- [GHSA-3q5w-m6wr-5jp2](https://github.com/advisories/GHSA-3q5w-m6wr-5jp2) — polymarket-clob-math (npm) · malware · published 03:18 UTC
  Brandjack of Polymarket's CLOB SDK math util. Polymarket = $14.4B weekly volume target — credential stealer hits trading bots / market-maker stacks.
  → remove the package; rotate Polymarket API keys + any wallet privkey on the host; verify real Polymarket SDKs are scoped under `@polymarket/*`.
- [GHSA-qr38-fjw7-r54v](https://github.com/advisories/GHSA-qr38-fjw7-r54v) — authmatrix + 3 siblings (npm) · malware · published 14:00 UTC (1 minute)
  Coordinated 4-package auth-domain squat: `authmatrix`, `authsessionbridge` (GHSA-m936-8h93-fqm9), `ssr-auth-sync` (GHSA-5xwj-q4j9-v44q), `auth-state-service` (GHSA-53ph-27qg-w52c). Same-minute publish = single attacker, fishing for auth-stack maintainers.
  → grep lockfiles for these 4 names; if hit, remove + rotate session/JWT secrets + any OAuth client secrets stored on the build host.

_Other malware net-new today: gx-npm-* (3-pkg brandjack), ts-einkle* (3-pkg), @vpms/design-system, vkzmn, hunsterx-package, velocityfix, unsafe-malicious-package, quirky-token, swift-parse-stream, path-internal-util — 21 total npm malware GHSAs in 48h, all 6-29-published, none in tracked deps. Full list in log._

*KEV status*
- 0 net-new (4th consecutive zero-cadence day). Weekly carry: 6 (Lantronix + 3× Ubiquiti UniFi + Cisco CUCM + PTC Windchill). Top EPSS: CVE-2026-34910 Ubiquiti 0.786/p99.5, CVE-2026-20230 Cisco 0.417/p98.5 (slipped below 0.5 PATCH-TODAY threshold).

*Reviewed advisories*
- Critical 48h: 0. High 48h: 3 — all 3 pnpm (GHSA-qrv3-253h-g69c / 72r4-9c5j-mj57 / fr4h-3cph-29xv) already covered in 6-27/6-28 digests, deduped.
