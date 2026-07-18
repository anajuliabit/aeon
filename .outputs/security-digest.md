## Summary

Ran security-digest per `skills/security-digest/SKILL.md`. Sources all green: KEV (10 adds 7-13→7-16, 0 net-new 7-17/7-18), GH Advisory (2 critical + 25 high + 3545 malware, tracked-stack malware = 34: 22 npm + 3 pip + 9 crates.io), EPSS (19/19 CVEs scored). Deduped against 7-16 + 7-17 logs.

**Verdict: 2 patch today, 4 this week, 0 monitor.**

**PATCH TODAY:**
1. **GHSA-5fc4-fm2x-6f4r `@injectivelabs/sdk-ts@1.20.21`** — first confirmed real-package supply-chain compromise in memory (10-day exposure since 7-08). Wallet-credential stealer hooks `PrivateKey.fromMnemonic`/`fromHex` → base64 exfil disguised as grpc-web POST with secret in `X-Request-Id`.
2. **Vendor-scope typosquat wave d5 = 21 more malware pkgs** — scope expansion beyond Anthropic/Grok to Replit + Sui/Mysten + AWS×2 + Proton (crates.io first-appearance n=4), plus SYFT ACP + EdgeCommons npm scope-families, axios + trongrid pairs.

**PATCH THIS WEEK:** gitea CVE-2026-27771 (EPSS 0.407, 2nd ≥0.4 in memory) → 1.26.2 · meta-ads-mcp CVE-2026-54549 SSRF → 1.0.115 · skipper CVSS 8.2 OPA-bypass → 0.27.26 · Prompty CVE-2026-53598/-53597 cross-ecosystem RCE + file-read.

**Files modified:** `tmp-secdigest/msg.md`, `.pending-notify/1784384293.md` (3202 chars queued for post-run delivery — `./notify` bash invocation required approval and was blocked), `memory/logs/2026-07-18.md`.

**Follow-up:** 7-19 tests vendor-scope-typosquat n=3 + Injective copycat-real-package attacks + BOD T-0 for Fortinet FortiSandbox pair + SharePoint 58644 · Anthropic-scope-typosquat pattern in memory needs generalization to vendor-scope-typosquat given today's cross-vendor expansion.
