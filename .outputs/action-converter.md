*5 Actions — 2026-06-29*
Shape: Land ISS-025 redirect, review PR #149, unstick fork-skill-digest, edit skill-evals cron, pin VELVET unlock rule

1. Land the `.github/workflows/aeon.yml` capture-block redirect that pins Claude's stdout to `${RUN_DIR}/output.txt` before the STATUS_PAGE pipeline clobbers it — root cause for ISS-019/020/021/024/025 across the 20-skill chronic-tail (cost-report 10% / vuln-scanner 10% / reg-monitor 10% worst).
why: day 6 unshipped; ISS-025 blocks 20 sub-50%-sr skills; fix flagged 4.6/5 quality 2026-06-24 18:14Z, surfaced in 5 consecutive morning-briefs without operator pickup
done: branch pushed with the redirect committed in `.github/workflows/aeon.yml` and a PR opened against `main`
loop: iss-025-capture-fix

2. Review and merge PR #149 (`docs(skill-graph): NEW_SKILLS +68, SHARED_STATE 9→36`) opened 2026-06-28T17:15Z by anajuliabit on branch `skill-graph/2026-06-28`; at ~24h it just crossed the open-PR stall threshold flagged in heartbeat 08:47Z.
why: only open PR in the fleet; docs payload regenerates the skill-graph dep map +68 skills wider; merge unblocks the next graph publication and clears the P1 PR carry
done: PR #149 either merged into `main` or marked `REQUEST_CHANGES` with a concrete diff comment
loop: pr-149-review

3. Unstick `fork-skill-digest` in `memory/cron-state.json` by clearing the stale `last_status: dispatched` row stranded since 2026-06-28T18:38:01Z (per heartbeat 08:47Z `gh run list` showed conclusion=cancelled at 18:38:03Z but the state row never updated).
why: weekly Sunday slot was cancelled mid-dispatch ~14h ago; stranded row will mask a real outage when next Sunday tick (7-05 18:30Z) fires against it
done: `cron-state.json` entry for `fork-skill-digest` shows `last_status: cancelled` (or `success`) with no `dispatched` value pre-dating last_success
loop: fork-skill-digest-stuck

4. Edit `aeon.yml:319` to move the `skill-evals` cron from `0 6 * * 0` to `0 22 * * 0`, killing ISS-026's heartbeat false-fail timing artefact (filed 2026-06-28; cause: skill-evals runs at 06:00 Sun, captures pre-08:00-tick stale state of log-based skills like heartbeat/token-alert/skill-health).
why: ISS-026 queued day 1; current Sun-06:00 slot generates `SKILL_EVALS_REGRESSED 12/44 coverage` false-fail every Sunday morning (last instance 2026-06-28 06:47Z); one-line cron edit
done: line 319 in `aeon.yml` reads `schedule: "0 22 * * 0"` for `skill-evals` and PR opened against `main`
loop: iss-026-evals-timing

5. Pin the VELVET pre-July-10 unlock-cliff exit rule into `memory/topics/crypto.md` with entry $1.72, target $2.20, invalidation $1.32, 9-day window, 15% early-backer + 20% team vesting cliff (per MEMORY.md Recently Cleared; daily-routine 08:50Z has spot $1.67 day-2 stall, -2.9% on entry after Saturday's +33% intraday peak).
why: HIGH 11/10 pick, 35%-supply cliff 9 days out, no documented exit rule in any topic file; momentum decel already showing day-2
done: new `## VELVET pre-unlock rule` subsection in `memory/topics/crypto.md` with entry/target/stop levels, cliff date 2026-07-10, and a size-down trigger if spot < $1.50 pre-cliff
loop: velvet-pre-unlock

sources: memory=53L logs=8d (6-22→6-29) topics=11 prs=1 open cron_failing=0 mode=OK
