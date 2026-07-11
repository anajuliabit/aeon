*5 Actions — 2026-07-11*
Shape: Author ISS-025 fix, postmortem SLX, flag PUMP unlock, patch pattern-invalidations, bisect batch scheduler.

1. Commit chain-runner capture-step fix (`.github/workflows/aeon.yml:479-493`) to a branch and open PR — preserve orchestrator's Write-tool output over CLI `.result` cp per ISS-009 root-cause.
why: day-19 sandbox-truncation systemic tail, weekly-review 2026-07-13 T-2, self-improve rule-5 blocks self-authoring — operator-direct-author only path left.
done: PR open with aeon.yml:479-493 diff preserving Write-tool output; ISS-025 fix_pr link populated.
loop: iss-025-capture-step

2. Draft SLX recut postmortem to `memory/topics/crypto.md`: entry $0.4753 → daily-routine $0.174 (-63.4%), 7 consecutive trending-endpoint surfaces, past every recut trigger, closed-pick decision anchor.
why: day-17 CATASTROPHIC, weekly-review T-2 last hygiene gate before position rolls week-4, HIGH 9/10 6-24 pick review-slot owner.
done: `memory/topics/crypto.md` diff appends "SLX postmortem" section with entry/exit/pct/date/decision bullets.
loop: slx-recut

3. Stage PUMP unlock cliff catalyst to `memory/topics/market-context.md` — 22.2% mcap (~$143M) hits float Sat 7-12, insiders vested from $0.004 ICO ($0.0015 today = -60%+), 2× recent daily volume, pre-derisking already firing (PUMP -5% today).
why: T-1 date-anchored supply event, Flowslikeosmo tokenomics lens, list-digest 7-10 top catalyst, carry-loop from 7-10 action-converter.
done: `memory/topics/market-context.md` diff appends "PUMP 7-12 unlock" section with mcap/date/insider-basis bullets.
loop: pump-unlock-cliff-t-1

4. Amend `memory/topics/crypto.md` with 4 pattern-invalidations from today's daily-routine — LAB floor thesis (d4 -32% re-arms cascade, 7d -91%), VELVET dead-cat (7d +22% → -22% overnight), CASHCAT PUMP-RISK 24-48h decay (d6 sustained +36%), GRASS FADE (d3 meme rescue +14%).
why: 4 same-day durable-pattern breaks; unpatched they carry stale predictions into narrative-tracker + list-digest cycles all week.
done: `memory/topics/crypto.md` diff includes ≥4 bullets naming each token + invalidation + 7-11 date.
loop: lab-velvet-cashcat-grass-invalidations

5. Bisect `.github/workflows/aeon.yml` scheduler for ISS-027 — diff cron-block YAML for 8 dark-batch skills (token-pick / defi-overview / token-movers / on-chain-monitor / defi-monitor / market-context-refresh / narrative-tracker / aixbt-pulse) vs firing token-alert/btc-levels; write differentiator to `memory/topics/fleet.md`.
why: batch-dark day-14, 7-10 12:00Z catch-up doesn't fix scheduler root; 8-skill last_success 2026-06-28 = ~13d stale.
done: `memory/topics/fleet.md` gets ISS-027 diagnostic section naming YAML differentiator (chain-config / cron slot / matcher).
loop: iss-027-batch-diagnostic

sources: memory=73 logs=14 topics=11 prs=0 cron_failing=0 mode=OK
