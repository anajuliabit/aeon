*5 Actions — 2026-07-09*
Shape: route iss-025 authoring, draft rule-5 relax pr, close slx day-15, codify iss-027/028

1. Update memory/issues/ISS-025.md with routing_decision: operator-direct-author + blocked_by: self-improve-rule-5; cross-link entry in memory/topics/fleet.md
why: T-4 to weekly-review 2026-07-13; 7-07 self-improve run confirmed structural rule-5 block on workflow-file edits, no re-route persisted
done: ISS-025.md frontmatter has routing_decision + blocked_by fields; fleet.md has iss-025-authoring-block entry
loop: iss-025-routing-decision

2. Draft PR against skills/self-improve/SKILL.md rule 5 to whitelist .github/workflows/aeon.yml chain-runner capture-step edits (lines 561-575 per 7-07 self-improve log correction)
why: parallel unblock path — if operator prefers rule-relax over direct-author, PR is ready for T-4 weekly-review
done: PR draft opened citing ISS-009 root_cause + ISS-025 blocked-authoring loop, adding rule 5a whitelist
loop: iss-025-routing-decision-alt

3. Stamp SLX open pick CLOSED in memory/topics/crypto.md — entry $0.4753 → last CG $0.256 (-46% day-15) + trending $0.174 (-63%); move from open-picks to closed
why: 6th consecutive daily-routine surface, position past every recut trigger, T-4 weekly-review deadline, no fresh CG print 4 days
done: SLX section marked CLOSED with 15-day drawdown verdict; entry appears in closed-picks list
loop: slx-recut-blown

4. Create memory/issues/ISS-027.md (12z batch dark scheduler never-run, 8-skill 6-28 cluster) + ISS-028.md (aixbt-pulse dead-slot d11 twice-daily 09/21Z); add rows to INDEX.md Open table
why: 7-08 action-converter claimed filing but files don't exist; d12 + d11 loops need codified diagnostic-path separation
done: two YAML-frontmatter issue files exist; INDEX.md has 2 new Open rows citing affected_skills
loop: iss-027-iss-028-codify

5. Poll memory/cron-state.json at 20:00Z heartbeat for 8-skill 6-28 cluster; write verdict into ISS-027.md observation log
why: 7-09 12:00Z tick still un-dispatched at 14:17Z (2h past slot); 20:00Z is codification checkpoint before end-of-day
done: ISS-027.md has 7-09 12:00Z outcome line (dispatched-catch-up | missed → d13 extension)
loop: 12z-batch-dark

sources: memory=61 logs=14 topics=11 prs=0 cron_failing=0 mode=OK
