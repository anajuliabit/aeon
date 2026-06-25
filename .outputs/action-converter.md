*5 Actions — 2026-06-25*
Shape: ship sandbox-fix PR, document HYPE cross-slate + phishing kit, log AAVE +7.7%

1. ship `.github/workflows/aeon.yml` capture-step fix as PR — patch the heredoc near L600 that reads + truncates skill output; current path loses long stdout and emits `output_tokens=0` in usage JSON, tag body with ISS-025/019/020/021/024
why: 22 chronic-tail skills sr<0.5 share the same `output_tokens=0` signature; one capture-path fix clears the cluster
done: PR opened against main, body lists the 22-skill tail + links cluster issues
loop: iss-025-workflow-capture

2. append HYPE cross-slate consensus block to `memory/topics/crypto.md` — @NOIRSINGULARIS selective-liquidity slate (TAO/WLD/HYPE/ONDO/PENDLE) + @ct_hoppy value-accruing slate (BNB/JUP/HYPE/AERO) both publish HYPE; track 24-48h cross-correlation, flag double-bid coordination risk
why: narrative-tracker 6-25 reflexivity flag #1 — published slates IS the trade, HYPE is the only ticker in both
done: ≥5-bullet entry under a "HYPE cross-slate" heading with both handle attributions, slate rosters, and a falsifier
loop: hype-double-bid-coordination

3. add a Morpho cbBTC `type: position` entry to `memory/on-chain-watches.yml` — W1→Morpho GeneralAdapter1 $7,105 cbBTC supply confirmed on-chain 6-24 14:51Z, defi-monitor still NO_CONFIG day 18
why: on-chain activity now names the actual position; ends 18-day NO_CONFIG carry without waiting on operator
done: yaml entry committed with market address + collateral=cbBTC + protocol=morpho-blue + label, next defi-monitor run reads it
loop: defi-monitor-no-config

4. log AAVE position update in `memory/topics/crypto.md` — entry $76.09 (6-24 HIGH 8/10), spot $81.99 (+7.69%), day-2 [TRENDING+UP] in 4/20-breadth tape; decide hold-for-$87 vs trail stop to break-even
why: only large-cap DeFi sustaining bid through risk-off; today's UTC close < $60,500 is binary catalyst against
done: position note appended with current spot, decision recorded, and BTC-close-conditional unwind rule
loop: aave-pick-management

5. write `memory/topics/onchain-phishing-patterns.md` — codify kit progression from 6-23 single cyrillic ÚSDС bait to 6-25 3-bait kit (zero-value real USDC + real cbBTC + value-matched cyrillic ÚSDС), attacker contract `0xC3236716cbDC725b518AC0A5d830FBaDcfd05032`, signer EOAs `0x3959E4…` + `0xcd8b9A…`, lookalike `0x98E57e6799…`
why: detection baseline for future on-chain-monitor runs; same kit already escalated twice in 2 days, third escalation likely
done: file exists with ≥5 sections (kit-progression timeline, attacker contract methodology, lookalike pattern, cyrillic value-match technique, mitigation rules)
loop: phishing-kit-postmortem

sources: memory=55 logs=7 topics=11 prs=0 cron_failing=0 mode=OK
