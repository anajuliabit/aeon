*Security Digest — 2026-06-27*
Verdict: 1 actively exploited (litellm wheel · EPSS 0.834) + 38 npm malware net-new, 5 to schedule, 1 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- [CVE-2026-42208](https://github.com/advisories/GHSA-r75f-5x8p-qvmc) — litellm (pip) · EPSS 0.834 / p99.65 · CVSS — · supply-chain credential-stealer wheel
  1.82.8 shipped a malicious `litellm_init.pth` that auto-executes on python startup and exfiltrates AWS/GCP/Azure creds + SSH keys + k8s configs + crypto wallets to `models.litellm.cloud`. semantic-router 0.1.8–0.1.14 resolved to it via unbounded transitive pin ([GHSA-98x5-vq43-vc5p](https://github.com/advisories/GHSA-98x5-vq43-vc5p), 6-26).
  → upgrade litellm to ≥1.83.7 (+ semantic-router ≥0.1.15), grep `site-packages/litellm_init.pth`, rotate any creds reachable from environments that ran the affected install.
- npm malware **38 net-new** (6-25 + 6-26 windows, post-dedup vs 6-25/6-26 logs) — weavedb-base + 4 sibling spoofs in one 43min burst (2026-06-26T05:05–05:48Z), ai-node-relay + ai-node-agent twins, hexo-shoka-swiper + hexo-deployer-wrangler, pino-zod ↔ zod-pino spoof pair, atlassian-forge-skills brand-spoof (matches 6-25 HubSpot @su-doughnym pattern — enterprise dev-tooling target now in 3rd vendor), pump-stream-logger + pump-laserstream-parser variants; 6-25 leftovers tesco-help / pathfix / easy-time-format ↔ easy-time666 twin / boardflow / ts-grok / loadninja-shared / atlassian-forge-skills / 9 more.
  → grep package-lock/pnpm-lock/yarn.lock against [type=malware feed since 6-25](https://github.com/advisories?query=type%3Amalware+published%3A%3E%3D2026-06-25); on hit, remove + rotate creds exposed to that install.

*PATCH THIS WEEK*
- [CVE-2026-49257](https://github.com/advisories/GHSA-73cv-556c-w3g6) — mcp-pinot-server (pip) · CVSS 10.0 · EPSS 0.005
  Default `oauth_enabled=False` + 0.0.0.0 bind = unauth tool invocation on any deployment. → upgrade mcp-pinot to ≥3.1.0; meantime bind to 127.0.0.1 + enable oauth.
- **Incus 7-CVE Go cluster** ([CVE-2026-48749](https://github.com/advisories/GHSA-2q3f-q5pq-g8wv)/50/51/52/53/55 + 48769) · CVSS 9.9 each · coordinated security release 2026-06-26T18:30–19:13Z
  Symlink AFW chain on host via crafted images (`rootfs/`, `exec-output`, `templates/`), restricted-project bypass → arbitrary command execution, arbitrary file write via trusted image hash, S3 multipart path traversal. → upgrade incus to ≥7.2.0.
- [CVE-2026-49252](https://github.com/advisories/GHSA-9v98-6g37-x9g6) — @deepstream/server (npm) · CVSS 9.9 · EPSS 0.003
  Prototype pollution. → upgrade @deepstream/server to ≥10.0.5.
- [CVE-2026-53519](https://github.com/advisories/GHSA-5c25-7vpj-9mqh) — nezhahq/nezha (Go) · CVSS 9.1 · EPSS 0.005
  Pre-auth path traversal via `/dashboard..` prefix confusion leaks `jwt_secret_key` = full auth bypass once exploited. → upgrade nezha to ≥2.0.13.
- **pnpm 9-CVE cluster** ([CVE-2026-55700](https://github.com/advisories/GHSA-v23m-ccfg-pq9h)/55698/55697/55487/50015/50016 + 3 unnumbered GHSAs) · CVSS max 8.8 · published 2026-06-26 → 2026-06-27
  Lockfile spoof + manifest-identity spoof + patch-remove path traversal + configDependencies env-lockfile execution — package manager itself as the supply-chain attack surface. → upgrade pnpm to ≥10.34.4 (v10) or ≥11.5.3 (v11).

*MONITOR*
- [GHSA-q6xx-5vr8-p898](https://github.com/advisories/GHSA-q6xx-5vr8-p898) — nezhahq/nezha (Go) · CVSS — · no fix yet · affects 1.14.13–1.14.14
  Cross-tenant terminal + file-manager session hijack via WebSocket stream UUID with no ownership check. → restrict admin/operator UI to trusted IPs until fix lands.
