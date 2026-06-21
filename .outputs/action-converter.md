*5 Actions — 2026-06-21*
Shape: Unblock failing XAI-dependent skills, fix critical cron failures, seed on-chain config

1. **Top up XAI API credits for team 3a8b4c1e**  
why: Monthly credit limit hit on 6-16 blocks 10+ skills (token-pick, agent-buzz, list-digest, etc.)  
done: XAI dashboard shows refreshed quota and skill runs resume successfully  
loop: xai-quota-exhausted

2. **Fix btc-levels skill's 27 consecutive failures**  
why: BTC hard-level alerts critical for Capital‑2× program; 27 straight failures indicate root cause  
done: btc-levels skill completes without error in next cron run  
loop: btc-levels-failed

3. **Seed memory/on-chain-watches.yml with at least 3 DeFi positions**  
why: on-chain-monitor and defi-monitor stuck 14 days with NO_CONFIG status  
done: watches.yml contains ≥3 watch entries with addresses and thresholds  
loop: on-chain-watches-missing

4. **Review and merge PR #112 (skill-graph docs)**  
why: Stalled 4 days; skill-graph updates block fleet documentation  
done: PR #112 merged to main branch  
loop: pr-112-stalled

5. **Investigate 14:29Z cluster dispatch lag (narrative-tracker, market-context-refresh, security-digest)**  
why: Batch dispatched 6-16 without success; likely GitHub Actions cron congestion  
done: Identify root cause in workflow logs and implement fix  
loop: 1429z-batch-stuck

sources: memory=70 logs=3 topics=12 prs=3 cron_failing=17 mode=OK
