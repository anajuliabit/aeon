*5 Actions — 2026-06-28*
Shape: Ship ISS-025 patch, reschedule skill-evals, pin Morpho rule, label REPPO staking, amend bear pattern

1. Patch the aeon.yml capture step that zeros output_tokens — edit the jq/sed line that scrapes the Claude Code run summary, preserve usage.output_tokens through the workflow capture, push branch + open PR against main linking ISS-019/020/021/024/025.
why: day 7 unshipped; 20-skill chronic-tail still bleeding output_tokens=0 (vuln-scanner 10% / reg-monitor 10% / cost-report 10%); PR #148 patches signal not structure
done: PR opened against main touching aeon.yml capture step, body links ISS-025
loop: iss-025-capture-fix

2. Reschedule skill-evals cron in aeon.yml:277 from "0 6 * * 0" to "0 22 * * 0" — moves dispatch past evening-recap and after-21:00 log batch so heartbeat/token-alert/skill-health aren't pattern-missing on fresh-morning runs.
why: ISS-026 filed 06:47Z today by skill-evals itself; action-queue head = "Schedule skill-evals after 21:00 UTC"; one-line fix, kills false-fail noise on next Sunday tick
done: PR opened touching aeon.yml:277, body cites ISS-026
loop: iss-026-skill-evals-timing

3. Pin the Morpho-Blue leverage policy as a named section in memory/topics/crypto.md — "Morpho-Blue leverage policy" header + two rules: pay down USDC at LLTV 0.86 under extreme fear instead of adding cbBTC; re-margin trigger LLTV<0.80 AND BTC reclaim >$63,500; source line "6-26 Telegram operator Q&A".
why: durable policy still lives in chat scrollback only; carry from 6-27 #4 unshipped; next Morpho action needs canonical reference
done: crypto.md has "Morpho-Blue leverage policy" section with both rules + source citation
loop: morpho-leverage-rule-doc

4. Amend MEMORY.md line 44 — replace "BREAKS the 24h-bear-half-life pattern" + "Watch 6-27/28 for persistence" with "Multi-day structural-bear pattern confirmed (day 3 persistence 6-26/6-27/6-28; Bitcoin ETF 13-day longest-ever outflow streak $107.8B→$82.8B)".
why: narrative-tracker 14:18Z today explicitly recommended this update; the half-life rule is now decisively broken with structural data; future pattern-recall will misread regimes if uncorrected
done: MEMORY.md line 44 reflects multi-day-bear pattern with 3-day confirms cited
loop: memory-bear-pattern-amend

5. Label 0xc81F...68E8 as "REPPO staking" in memory/known-addresses.yml — counterparty surfaced today 13:03Z in on-chain-monitor (W3 withdraw + W1 deposit, 1.58M REPPO migration); add lowercased-address key with "REPPO staking" value below existing 6-25 entries.
why: today's first non-zero on-chain-monitor run in 72h explicitly recommended this label; without it next REPPO-flow event reads as UNKNOWN-counterparty noise
done: known-addresses.yml has 0xc81f...68e8 entry with label "REPPO staking"
loop: onchain-counterparty-label

sources: memory=50L logs=7d topics=11 prs=2 cron_failing=0 mode=OK
