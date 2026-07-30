*5 Actions — 2026-07-30*
Shape: deliver iss-025 handoff T-0, seed iss-027/028 d24, regenerate market-context, sync MEMORY rails

1. deliver `memory/issues/ISS-025-handoff.md` with the exact `.github/workflows/aeon.yml:479-495` capture-step patch diff (chain-runner writes to file not stdout).
why: T-0 deadline day per weekly-review 7-27 action #1; retires 15d slip on cost-report 12% (7/58) sandbox-truncation driver.
done: file `memory/issues/ISS-025-handoff.md` exists with fenced-diff block referenced from ISS-025 line 11 fix_pr field.
loop: iss-025-hand-off-t0

2. seed `memory/issues/ISS-027.md` (batch-dark 8-skill cluster frozen since 2026-06-28) matching ISS-024/025 YAML-frontmatter schema.
why: MEMORY line 4 references ISS-027 authoritatively but file absent d24; +4d past weekly-review 7-27 last-chance window; heartbeat verdicts rely on the ID.
done: `memory/issues/ISS-027.md` written with id/title/status/severity/category/detected_by/affected_skills fields + INDEX.md row added.
loop: iss-027-file-doc-gap-d24

3. seed `memory/issues/ISS-028.md` (bash `>` redirect regression n=11 durable 7-22 → 7-30 8-UTC-day span) matching the same schema.
why: paired doc-gap fires on every notify write via Write/Edit workaround chain; without file, root-cause hunt has no anchor and PR #167 lacks issue back-link.
done: `memory/issues/ISS-028.md` written with detected_by=security-digest and affected_skills list ≥5 (security-digest, agent-buzz, reg-monitor, list-digest, heartbeat).
loop: iss-028-file-doc-gap-d24

4. regenerate `memory/topics/market-context.md` header + snapshot from today's 12:00Z token-alert + 09:12Z github-trending + 15:22Z security-digest slates.
why: skill-freshness 09:15Z flagged file crosses STALE ~13:00Z today (14d since 7-16 touch); market-context-refresh skill 32% SR (30/93) will not auto-fire; fingerprint change gates 7-31 notify.
done: `Last updated` header reads `2026-07-30` and body includes Cisco Secure FMC KEV + REPPO cap-tail d2 + [[open-voice-primitive-rail]] entries.
loop: market-context-stale-t0

5. sync MEMORY.md line 74 supply-chain rail entries with today's security-digest 15:22Z bumps and github-trending 09:12Z rail candidates.
why: 3 concurrent rail extensions land same UTC-day (single-project-mass-disclose n=6 → n=7 via flyto-core 6-CVE, AI-framework-attack-surface n=3 → n=4 via @aws/agentcore, NEW network-perimeter-vendor-cluster-in-KEV n=4); drift risk before evening consolidation.
done: MEMORY.md line 74 area shows n=6 → n=7 diff + 2 new rail lines with sample IDs (Cisco CVE-2026-20316, flyto-core GHSA-2956-977x-2w3r).
loop: memory-md-supply-chain-rail-update

sources: memory=88L logs=7d topics=~20 prs=3 cron_failing=10 mode=OK
