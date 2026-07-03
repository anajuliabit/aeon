*Security Digest — 2026-07-03*
Verdict: 1 to patch today (public PoC + public secret), 5 to schedule. _Sources: KEV ok, GH Advisory ok, EPSS ok_

*PATCH TODAY*
- [CVE-2026-49352](https://github.com/advisories/GHSA-jphh-m39h-6gwx) — 9router (npm) · CVSS 9.8 · public PoC · not in KEV
  Hardcoded default JWT fallback secret `9router-default-secret-change-me` = auth bypass. Advisory ships full token-forgery PoC.
  → upgrade 9router to ≥0.4.45 today; require `JWT_SECRET` at startup; rotate any tokens issued under the default.

*PATCH THIS WEEK*
- [CVE-2026-52830](https://github.com/advisories/GHSA-rxw2-pc8j-vxwm) — fast-mcp-telegram (pip) · CVSS 9.4 · public PoC
  Bearer-token path traversal (`../fast-mcp-telegram/telegram`) bypasses reserved session guard = unauth Telegram takeover on default session file.
  → upgrade fast-mcp-telegram to ≥0.19.1.
- [CVE-2026-52735](https://github.com/advisories/GHSA-gf9r-m956-97qx) — zebrad (rust) · CVSS 9.3
  P2SH sigop undercount in pure-Rust disabled-opcode parser = Zcash consensus divergence; any tx broadcaster chain-splits Zebra miners.
  → upgrade zebrad ≥4.5.0 and zebra-script ≥7.0.0.
- [CVE-2026-49255](https://github.com/advisories/GHSA-v5ff-xmfp-p245) — electerm (npm) · CVSS 8.8
  Command injection via crafted SSH/SFTP filenames through rmrf/mv/cp = RCE as desktop user; bash + PowerShell both hit.
  → upgrade electerm to ≥3.11.11.
- [CVE-2026-49852](https://github.com/advisories/GHSA-gg9x-qcx2-xmrh) — joserfc (pip) · CVSS 8.7
  HS256/384/512 verify accepts empty/nil HMAC key → JWT forgery whenever secret sourced from unset env. Cross-lang sibling of ruby-jwt CVE-2026-45363 + PyJWT.
  → upgrade joserfc to ≥1.6.8.
- [CVE-2026-44454](https://github.com/advisories/GHSA-m3cr-vc2j-pm27) — coder (Go) · CVSS 8.1
  Crafted `dotfiles_uri` URL param + `mode=auto` workspace creation = RCE on victim click; v1 EOL.
  → upgrade coder v2 to ≥2.29.7 (ESR) or ≥2.30.2 (mainline); migrate off v1.

_23-advisory OpenClaw single-package cluster (npm 9.3-6.5, fixed 2026.4.29) + Fission-style 13-CVE openbabel batch (pip, old CVE-2022-* republish) omitted — pattern signal, niche reach._
