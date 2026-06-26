*5 Actions — 2026-06-26*
Shape: verify PR-#147 selftest, cut ISS-025 PR, close SEI invalidation, document Morpho rule, dedupe MEMORY

1. run `bash scripts/advisor/selftest.sh` post-merge of PR #147 (advisor hard risk layer #140) and append result to `memory/topics/fleet.md` under an "advisor sprint" subsection
why: operator's first delivery of the 7-issue advisor sprint merged 12:44Z with no review — `CLAUDE.md` flags selftest as the CI gate
done: selftest exit code logged to topics/fleet.md with PR ref and merge timestamp
loop: pr-147-postmerge-verify

2. cut PR patching the workflow `.github/workflows/aeon.yml` capture step — fix the `output_tokens=0` response shape that signs ISS-019/020/021/024/025
why: 22 chronic-tail skills sr<0.5 still lose telemetry every cron tick; day 4 since action-converter flagged the fix at 4.6/5 quality
done: PR open on github; ISS-025 frontmatter `fix_pr:` field updated
loop: iss-025-capture-fix

3. close `.pending-picks/2026-06-25-token-pick.json` SEI HIGH 9/10 — invalidation $0.054 hit day 1 (intraday $0.054, −10.2% per token-movers 12:31Z); POST close to `/api/picks` and append outcome row to `memory/topics/crypto.md` alongside AAVE day-3 +13.4%
why: token-pick spec triggers close at invalidation; the side-by-side AAVE vs SEI row is the only carry-forward signal from a 1d stop-out
done: pick state=closed via api + crypto.md outcome row appended
loop: sei-pick-invalidation

4. draft `memory/topics/morpho-position.md` covering cbBTC/USDC at LLTV 0.86 / 14% cushion, the no-new-collateral + pay-USDC-instead rule, and the re-margin trigger LLTV <0.80 + BTC reclaim $63,500
why: operator engaged advisor leverage-freeze rec 6-25 21:08Z + 21:34Z via telegram followup; the decision rule lives in chat history, not on disk
done: file has 4 sections (position state, decision rule, re-margin trigger, link to crypto.md morpho-curator-risk lesson)
loop: morpho-position-runbook

5. prune `memory/MEMORY.md` duplicate "Recently Cleared" header at line 24 and the redundant Current Goals (sandbox-truncation, XAI quota, on-chain config, BTC hard levels appear before AND after line 10's first Recently Cleared)
why: file is read by every action-converter + morning-brief + heartbeat run; duplicate goals risk stale-vs-fresh divergence (6-19 vs 6-25 entries already drift inside the file)
done: MEMORY.md has exactly 1 Current Goals + 1 Recently Cleared section; line count drops ≥15
loop: memory-md-dedup

sources: memory=62 logs=8d topics=11 prs=0 cron_failing=0 mode=OK
