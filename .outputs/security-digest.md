The scratch dir lives under the project root and only holds ephemeral fetch JSON — leaving it. Done.

## Summary

**Security Digest — 2026-06-13** executed end-to-end.

- **PATCH TODAY (3)**: CVE-2026-10520 (Ivanti Sentry KEV, unauth root RCE, EPSS 0.43, CISA due 6-14); CVE-2026-35273 (Oracle PeopleSoft KEV, **known ransomware use**, CVSS 9.8, CISA due 6-15); npm malware burst — 20 GHSAs in 3 clusters (11-pkg ecto-* CTF/exfil single-second push, 5-pkg forge-jsx + ioredis typo-squats, 4-pkg credential-stealer mix incl. chai-web3-testkit wallet-adjacent).
- **PATCH THIS WEEK (4)**: CVE-2026-48150 @budibase/server priv-esc 9.0 → ≥3.39.0; CVE-2026-48152 @budibase/server REST-cred exfil 8.1 → ≥3.39.0; GHSA-gv7w-rqvm-qjhr esbuild RCE 8.1 → ≥0.28.1; CVE-2026-11401 aws-advanced-go-wrapper Go priv-esc 8.0.
- **MONITOR**: empty (all in-stack 7.x highs had fix versions implied by `< X.Y.Z` ranges; fell off per 6-11 Baileys precedent).
- **Sources**: KEV ok · GH Advisory ok · EPSS ok. **First double-KEV PATCH TODAY** in digest history; 5 prior-week KEVs deduped against 6-11 log.
- **Notification**: staged to `.pending-notify/1781361787-security-digest.md` (2994 chars) for post-run delivery (sandbox blocks direct `./notify "$(cat ...)"`).
- **Log**: appended `### security-digest` block to `memory/logs/2026-06-13.md` with tier IDs, ranking rationale, source status, and notable signals.

Files modified: `memory/logs/2026-06-13.md`; created `.pending-notify/1781361787-security-digest.md`. Follow-up: post-run notify delivery step will fan out to Telegram/Discord/Slack.
