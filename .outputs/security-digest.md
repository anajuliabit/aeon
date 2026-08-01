*Security Digest — 2026-08-01*
Verdict: nothing actively exploited today, 1 to patch, 3 to monitor. _Sources: KEV, GH Advisory, EPSS_

*PATCH TODAY*
- ~60 npm + ~20 pip malware advisories in 48h. Notable clusters: **@0xlr/* 10-pack saas-auth dep-confusion** (clerk-auth / stripe-checkout / supabase-db / sentry-web / prisma-client-js / vercel-analytics), **fintech corporate-scope 20-pack** (@spending-behavior-ui/*, @finance-ui/*, @cr-invested-ui-components/*, @mplay-*), **nvidia AI-tooling squats** (trtllm-subdir-test + nvtorch-oot-nightly + test-dev-* 8-pack), **mcp-server typosquat 12+** (refbase-mcp / chaos-mcp / gtm-mcp-auth / sap-mcp-facilitator / pm-claude-skills-mcp / kip-mcp-http), **ethers/solana wallet-targets** (@ethers-sdk/ethers + @ethers-sdk/wallet + @solana-sdk/web3.js + eth-bridge + kelly-stake).
  → audit npm/pip installs against these names; rotate any credentials on dev hosts that touched them.

*PATCH THIS WEEK*
- [CVE-2026-52855](https://github.com/advisories/GHSA-pfvc-3p5h-x7h6) — github.com/pterodactyl/wings (Go) · CVSS 9.9 · no public PoC · no EPSS
  wings exposes node config secrets via egg configuration-file templating. 2nd wings CVE in 3d (7-30 shipped CVE-2026-54593 fix 1.12.2). → upgrade wings to ≥1.12.3.

*MONITOR*
- [GHSA-qvv7-cg9c-w4x3](https://github.com/advisories/GHSA-qvv7-cg9c-w4x3) — nltk (pip) 4-CVE mass-disclose · max CVSS 8.6 · no fix yet
  DNS-rebinding SSRF bypass defeats ENFORCE mode + 3 path-traversals in FramenetCorpusReader/NKJPCorpusReader/ReviewsCorpusReader. → track for nltk >3.9.4; pin and restrict outbound DNS until patched.
- [GHSA-mw3h-qjxj-6xg9](https://github.com/advisories/GHSA-mw3h-qjxj-6xg9) — thumbor (pip) 6-CVE mass-disclose · max CVSS 8.2 · no fix yet
  HMAC bypass via multi-replace + ALLOWED_SOURCES regex bypass + 4 DoS in convolution/proportion filters. → track for thumbor >7.7.7; do not expose thumbor endpoints publicly.
- [GHSA-r2v3-8gwf-7ghm](https://github.com/advisories/GHSA-r2v3-8gwf-7ghm) — bank-vaults/vault-secrets-webhook (Go) · CVSS 9.6 · no fix yet
  vault-addr annotation SSRF + cluster-wide SA token theft via TokenRequest API. → track for ≥1.22.3; restrict webhook egress and audit RBAC for TokenRequest scope.
