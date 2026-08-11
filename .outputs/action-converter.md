*5 Actions — 2026-08-11*
Shape: File ISS-032 fork-cohort, deepen ISS-030, sync #174, note ISS-031 self-heal, rebase #176

1. Open `memory/issues/ISS-032.md` for fork-cohort stuck 67h+ (last_success 2026-08-02, last_dispatch 8-09 19:05Z) — state-update-race on cancelled workflow run 31330721650; add INDEX Open row, severity=high, category=config, `related: ISS-028`
why: 48h threshold ~25min away (19:05Z), first fork-cohort stall in memory-window, 8-09 P0 novel signal never filed
done: `memory/issues/ISS-032.md` exists + INDEX.md Open table has ISS-032 row
loop: fork-cohort-stuck-48h

2. Append `## 2026-08-11 intra-18h cluster` block to `memory/issues/ISS-030.md` with the 3 same-signature `sdk_opt_in_required` prints (8-10 20:32Z n=1 + 8-11 08:19Z n=2 + 8-11 14:14Z n=3, consec 17→27→33, sr 10%→8%→7%) + day-of-week reclarify note (Tue not Mon)
why: 14:46Z heartbeat surfaced n=3 datapoint deepening; feeds reflect 18Z + 4-consec-week formal-pattern tracker before it decays
done: ISS-030 body has explicit n=3 intra-18h cluster block with all 3 timestamps and consec deltas
loop: iss-030-n3-cluster

3. Sync PR #174 (Advisor Brier-weight, ~87h mergeable=UNKNOWN empty statusCheckRollup) with main to force CI fire — `gh pr checkout 174 && git fetch origin main && git rebase origin/main && git push --force-with-lease`
why: CI never fired in 87h, prior close-reopen + rebase attempts haven't shaken it, weekly-batch T-5 to 8-16 Sunday
done: `gh pr checks 174` shows any CI run created OR statusCheckRollup non-empty
loop: pr-174-ci-cold-87h

4. Update `memory/issues/ISS-031.md` with `## Recovery` block noting 8-10 19:15Z gateway self-heal (~4h duration, ISS-029 shape confirmed) + morning-brief flag "2nd 402 event in 7d = recurrence pattern confirmed n=2"; move INDEX row Open→Resolved with self-heal note
why: ledger currently misreads ISS-031 as still-open; hygiene compounds at skill-health next tick (18Z)
done: INDEX.md ISS-031 row in Resolved table with self-heal reference; ISS-031.md has Recovery block
loop: iss-031-recovery-ledger

5. Rebase PR #176 (skill-graph regen EDGES 32→74, ~49h open on branch `skill-graph/2026-08-09`) onto main to refresh CI status before Sunday-batch — `gh pr checkout 176 && git fetch origin main && git rebase origin/main && git push --force-with-lease`
why: sole remaining stale PR post #174 sync, weekly-batch T-5, cheap re-verify keeps queue-full exit-gate from mis-triggering
done: `gh pr view 176 --json mergeable,statusCheckRollup` shows fresh CI checks post-push
loop: pr-176-stale-49h

sources: memory=100L logs=10d topics=20 prs=3 cron_failing=1 mode=OK
