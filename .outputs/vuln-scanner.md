*Vuln Scanner — ChromeDevTools/chrome-devtools-mcp*
clean audit. 1 candidate reviewed, 0 confirmed. `@opentelemetry/core@1.30.1` (GHSA-8988-4f7v-96qf, moderate DoS via W3C Baggage) reaches through `lighthouse → @sentry/node`, but chrome-devtools-mcp ships no `SENTRY_DSN` so the vulnerable Baggage-parse path never runs. dropped.
scanners: semgrep=fail, trufflehog=fail, osv=ok (api). semgrep/trufflehog blocked by sandbox per ISS-018 — osv-api the only surviving leg.
report: `articles/vuln-scan-2026-07-04.md`. dedup appended.
