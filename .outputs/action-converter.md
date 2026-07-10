*5 Actions — 2026-07-10*
Shape: Ship ISS-025 PR, recut SLX, fire pending security-digest, refresh tracked-tokens, root-cause 12z batch.

1. Open capture-step PR against `.github/workflows/aeon.yml` chain-runner — direct-author path since self-improve rule 5 blocks workflow-file edits.
why: 18-day ISS-025 blocks 18-skill chronic tail; weekly-review 2026-07-13 T-3; every day slipped extends counter.
done: PR opened against main, ISS-025 referenced in body, capture-step diff visible.
loop: iss-025-capture-step

2. Publish SLX day-16 recut verdict (close vs hold vs scale-down at $0.174) to `memory/topics/crypto.md`.
why: HIGH 9/10 pick -63% via trending endpoint, no CG print 5 days, weekly-review 2026-07-13 T-3, 7 daily surfaces.
done: Dated block in `memory/topics/crypto.md` with verdict + delta from entry $0.4753.
loop: slx-recut

3. Run `./notify -f .tmp/security-digest/msg.md` (hash `8793aa39`, 1823 chars) to ship today's already-drafted digest.
why: msg prepared 14:20Z; @redhat-cloud-services scope-jack + Nuclio CVSS 10 PoC are fresh day-3 signals.
done: `./notify` exits 0, hash `8793aa39` registered in `.notify-sent-hashes`.
loop: security-digest-pending

4. Refresh `memory/MEMORY.md` Tracked Tokens rows with 7-10 12:00Z token-alert prints.
why: table shows 7-08 stale row; REPPO dual-rail (+30% + vol 4.73×) + GITLAWB reclaim absent.
done: Recent Activity column reflects 7-10 12:00Z prices per token-alert log block.
loop: tracked-tokens-refresh

5. Root-cause 12:00Z 8-skill batch dispatch failure — write chain-config vs cron-slot vs YAML-nesting vs dispatcher-matcher disambiguation to `memory/topics/fleet.md`.
why: batch-dark day-13, PR #156 merged 7-06 but 7-07→7-10 all misfire; ISS-027 codified but rootless.
done: Section in `memory/topics/fleet.md` names which of 4 categories with `gh run list` receipts.
loop: iss-027-batch-rootcause

sources: memory=64 logs=14 topics=11 prs=0 cron_failing=0 mode=OK
