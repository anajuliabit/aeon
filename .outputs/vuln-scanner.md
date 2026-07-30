## Summary

Ran `vuln-scanner` skill against `block/buzz` (11,354 stars, Rust · Nostr agent-workspace) — selected from `.outputs/github-trending.md` 7-25 top pick over `citrolabs/ego-lite` (dropped: no SECURITY.md).

**Verdict:** `VULN_SCAN_OK — clean-audit-partial-scan · 3 candidates → 0 confirmed`

**Scanner status** (ISS-018 sandbox family day-33): semgrep=fail, trufflehog=fail, osv-binary=fail, cargo-audit=fail, slither=n/a. Only osv-api reachable via `curl -o` POST. Queried ~110 top-signal cargo crates in 2 batches.

**3 dep-CVE candidates, all triaged to DROP:**
- **quick-xml 0.38.4** (RUSTSEC-2026-0194+0195 DoS) via `rust-s3`/`aws-creds` — already ignored in `deny.toml:12-21` with "trusted-input XML only" maintainer reasoning
- **quick-xml 0.39.4** (same 2 advisories) via `plist` → local macOS system data only, unreachable from untrusted input
- **opentelemetry_sdk 0.31.0** (GHSA-w9wp-h8wv-79jx MODERATE Baggage unbounded-alloc) via `mesh-llm@v0.73.1` git-pin — 0.31 lives inside mesh-llm internal LLM-inference tracing (not HTTP-baggage path; relay uses 0.32 for that), unshippable as PR (git-tag pin blocker, same as tirth8205 uv.lock)

**Hand-audit spot check** of highest-attack-surface crates found zero code-level issues: SSRF check on `call_webhook` is textbook-correct (`to_socket_addrs` → `is_private_ip` → reqwest `.resolve` DNS-pin + `.no_proxy` + `.redirect(Policy::none())`), `is_private_ip` comprehensive (CGNAT + benchmarking + IPv6 ULA + NAT64 + SIIT + Teredo + 6to4), NIP-42/NIP-98 auth with deliberate no-loopback-aliasing to preserve multi-tenant host-binding.

**Disclosure:** 0 shipped. No PVR filed, no public PR opened, no `.pending-disclosure/` draft.

**Files modified:** `articles/vuln-scan-2026-07-25.md`, `memory/vuln-scanned.json` (block/buzz added, 7 entries total), `memory/logs/2026-07-25.md`, `.pending-notify/1784998332.md` (notify sandbox-block workaround), `.tmp/vuln-scan/*` (buzz clone + osv payloads/responses + sources.txt), `.tmp/vuln-scanner/msg.md`.

**Follow-up:** [[mature-project-security-hygiene]] rail extends n=3 (chrome-devtools-mcp 7-04 + tirth8205 7-18 + block/buzz 7-25 all clean-audit-partial-scan on well-managed repos); `./notify` script blocked by sandbox this run (fallback = direct write to `.pending-notify/`); next vuln-scanner tick sat 2026-08-01.
