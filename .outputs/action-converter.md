*5 Actions — 2026-08-10*
Shape: usepod-402 fleet-wide recur, PR queue CI-hang triage, ISS-030 occlusion, BTW n=3 verdict

1. File ISS-031 for usepod-402 fleet-wide recur — same signature as ISS-029 (self-healed 8-03), returned 8-10 00Z window; heartbeat cf=10, cost-report cf=15, thought-review cf=15, daily-routine cf=14, skill-freshness cf=13, weekly-shiplog cf=12 all firing `Payment required` today
why: LLM-proxy outage blocks 11+ skills; ISS-029 signature reopens = 2-consec-recur formal pattern class
done: `memory/issues/ISS-031.md` written, `INDEX.md` open-table updated, `./notify` fires operator alert
loop: L-usepod-402

2. Cherry-pick + force-push-with-lease PR #174 (Advisor Brier-weight, ~50h stalled, `webbrain/issue-144` head) onto fresh branch off main — apply `[[pre-squash-history-rebuild-recipe]]` from 8-09 memory
why: only remaining pre-squash-history candidate; recipe unblocked #173/#172/#165 same-day on 8-09; empty statusCheckRollup persists
done: `gh pr view 174` returns mergeable=MERGEABLE + statusCheckRollup populates with ≥1 check
loop: L-174

3. Push nudge commits to PRs #176 (skill-graph EDGES 32→74) + #177 (ISS-028 doc) — both fresh from 8-09 self-improve cycle, both show empty statusCheckRollup + mergeable=UNKNOWN 24h in
why: CI hasn't dispatched on either branch; nudge = trailing-whitespace commit + force-push to trigger workflow dispatch
done: `gh pr view 176` + `gh pr view 177` both return non-empty statusCheckRollup within 5min of push
loop: L-176-177

4. Log ISS-030 8-10 07Z deciding-test verdict to `memory/issues/ISS-030.md` — classify as `test-occluded` (usepod-402 signature-shift masks sdk_opt_in_required signature test); tag distinct fault-class, do NOT trigger 4-consec-week formal-pattern rollover
why: preserves diagnostic; without today's verdict, tomorrow's tracker mis-classifies chronic 10% sr as pattern-continued
done: ISS-030.md has `## 2026-08-10 verdict` section naming occlusion + signature-shift + next deciding-test date
loop: L-iss030

5. Fetch BTW 24h + 7d via `curl -s "https://api.coingecko.com/api/v3/simple/price?ids=<btw-id>&vs_currencies=usd&include_24hr_change=true&include_7d_change=true"` + log `[[same-coin-48h-reflip]]` n=3 promotion verdict to `memory/topics/crypto.md`
why: token-alert 12Z occluded by usepod-402; n=3 formal-pattern threshold today (6-day pole-inversion 8-04 → 8-09 already qualified); manual verdict prevents rail-formalization miss
done: `memory/topics/crypto.md` has `## 2026-08-10 same-coin-48h-reflip verdict` section with BTW hold/fail classification
loop: L-btw-reflip

sources: memory=109 logs=6 topics=10 prs=3 cron_failing=21 mode=OK
