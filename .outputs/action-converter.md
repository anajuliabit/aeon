*5 Actions — 2026-08-07*
Shape: close-reopen PR#173 CI, ship cost-report fix, file ISS-031+032, amend #171 range

1. close-reopen PR #173 via `gh pr close 173 && gh pr reopen 173` to force a fresh CI trigger on branch `fix/self-improve-2026-08-03`.
why: CI cold 84h+ blocks 3-PR self-improve queue at 8-10 Sunday-batch T-2; empty statusCheckRollup + mergeable=UNKNOWN since 8-03; reopen fires `pull_request.reopened` event.
done: `gh pr view 173 --json statusCheckRollup` returns non-empty check-runs list within 10min.
loop: close-reopen-PR-173-CI

2. Open PR removing `model: claude-sonnet-4-6` override at `aeon.yml:276` on branch `fix/cost-report-iss-030-model-drop`.
why: ISS-030 fleet-worst chronic sr=10% signature is `sdk_opt_in_required` under sonnet-4-6; drop lets 8-10 Mon 07Z deciding-test T-3 fire clean and auto-close the ticket.
done: `gh pr view` shows a new PR opened with body linking ISS-030 + ci-skills-json check passing.
loop: iss-030-cost-report-model-drop

3. File `memory/issues/ISS-031.md` for `[[morning-08Z-slot-dark]]` formal-pattern n=4-consec (heartbeat + skill-freshness 08Z co-miss 8-04→8-07) + add row to `memory/issues/INDEX.md` Open table.
why: today's 09:15Z heartbeat promoted the rail candidate n=3 → n=4-consec = crosses another 24h durability gate; formal-pattern threshold reached = ledger entry gates skill-repair path.
done: `memory/issues/ISS-031.md` exists with YAML frontmatter (severity medium, category config, detected_by heartbeat 8-07 09:15Z) + INDEX Open row present.
loop: file-iss-031-morning-08z-slot-dark

4. File `memory/issues/ISS-032.md` for `[[heartbeat-dispatch-lag]]` rail n=5 magnitude flat at 75min (60min-warn breach 2nd consecutive UTC-day).
why: heartbeat 8-07 09:15Z surfaced sequence 31→50→50→75→75min = breach-plateau distinct from 08Z-slot-dark cause; symptom is delay-on-fire not co-miss, warrants its own ledger entry.
done: `memory/issues/ISS-032.md` exists with YAML frontmatter (severity medium, category config, detected_by heartbeat 8-07 09:15Z, root_cause pending) + INDEX Open row present.
loop: file-iss-032-heartbeat-dispatch-lag

5. Amend PR #171 body via `gh pr edit 171 --body-file -` to bump asserted cap from 12-17 → 12-18 (8-05 github-trending fetched n=18 top-edge, breaks assertion +1).
why: 8-consec-day sub-25 fetch pattern's observed range is 12-18 not 12-17; reviewer misread risk on 8-10 batch if body still claims 12-17; single-file line edit.
done: `gh pr view 171 --json body` shows "12-18" range assertion in body text.
loop: amend-pr-171-range

sources: memory=101 logs=10 topics=19 prs=4 cron_failing=0 mode=OK
