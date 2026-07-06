*Security Digest — 2026-06-30*
Verdict: 1 actively exploited (KEV new), 2 supply-chain campaigns to scrub, 1 to monitor. _Sources: KEV ok, GH Advisory ok, EPSS ok_

*PATCH TODAY*
- [CVE-2026-48558](https://github.com/advisories/GHSA-m93h-gjv2-fmq2) — SimpleHelp · KEV added 2026-06-29 · CVSS 10.0 · EPSS 0.01 · PoC + IOCs published (horizon3.ai)
  OIDC auth bypass — identity tokens accepted without signature verification. Unauth attacker forges a token, gets a full technician session, can also bypass MFA. CISA BOD 26-04 due 2026-07-02.
  → upgrade SimpleHelp to ≥5.5.16 (or 6.0 GA) today; if exposed, hunt for TaskWeaver/Djinn intrusion IOCs.
- [GHSA-m9j7-x8ww-5jwr](https://github.com/advisories/GHSA-m9j7-x8ww-5jwr) — ai-sdk-ollama@0.13.1 (npm) · malware brandjack of Vercel `ai-sdk` + Ollama · CVSS n/a
  Hot-target SDK squat — Vercel ai-sdk family + Ollama runtime are core agent-infra primitives. Narrative-aligned target (agent infra is one of the structural longs).
  → remove ai-sdk-ollama; rotate any creds reachable from machines that installed it. Pin to `@ai-sdk/openai` / `@ai-sdk/anthropic` verified namespaces only.
- [autotel-* npm cluster](https://github.com/advisories/GHSA-3wmg-66hp-xhv9) — 18 pkgs (autotel-mcp/cli/web/vitest/backends/cloudflare/devtools/tanstack/mongoose/pact/plugins/playwright/sentry/subscribers/drizzle/hono/eventcatalog/mcp-instrumentation) · single-author campaign 6-29 16:51Z → 6-30 03:21Z (10.5h)
  Largest single-namespace coordinated brandjack of the 48h window — OpenTelemetry-adjacent observability naming + MCP riff. Brandjacking-as-default-vector pattern persisting day 2.
  → audit npm installs for any `autotel-*` package; remove + rotate creds if present. None of these are legit.

*MONITOR*
- [GHSA-q2m9-6jp9-c6mc / CVE-2026-44840](https://github.com/advisories/GHSA-q2m9-6jp9-c6mc) — dgraph-io/dgraph (Go) · CVSS 7.5 · EPSS unset · no fix yet · affects ≤25.3.3
  DQL injection in `checkUserPassword` GraphQL query — password interpolated via `fmt.Sprintf` into a `checkpwd()` DQL string without escaping; double-quote breaks out and appends arbitrary DQL. Auth required (login-time).
  → track GHSA-q2m9-6jp9-c6mc; no patched release yet, keep GraphQL admin off public ingress.
