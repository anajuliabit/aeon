*5 Actions — 2026-06-27*
Shape: Ship ISS-025 fix, escalate Agent-Reach disclosure, patch prefetch-xai, codify Morpho rule, seed pool config

1. Branch + open the aeon.yml capture-step patch as a PR — identify the step zeroing output_tokens, write the structural fix, push to a feat branch, open against main.
why: 5-day unshipped fix bleeds telemetry across 20 sr<0.5 chronic-tail skills; root-cause known since 6-24 18:14Z
done: PR opened against main, body links ISS-025/019/020/021
loop: iss-025-capture-fix

2. Draft maintainer outreach for Panniantong/Agent-Reach CWE-88 finding into .pending-disclosure/outreach.md — pull maintainer handle from gh API, write 6-line DM body naming agent_reach/transcribe.py:81-94 + safe-channel ask.
why: vuln-scanner 16:18Z deferred after PVR HTTP 403; 43k-star public repo with reachable RCE-shape path
done: .pending-disclosure/outreach.md exists with handle + DM body
loop: panniantong-vuln-disclosure

3. Patch scripts/prefetch-xai.sh to route 1 of 4 agent-buzz sub-queries to mode:"Top" + min_likes:50 — preserve 3 Latest legs for chronological tail.
why: today's agent-buzz log capped engagement floor at 13 likes / followers:null; single Top leg restores signal-scoring
done: PR opened touching scripts/prefetch-xai.sh
loop: agent-buzz-cache-quality

4. Codify the 6-26 Morpho-Blue leverage rule into memory/topics/crypto.md as a named subsection — pay USDC don't add cbBTC at LLTV 0.86 in extreme fear; re-margin trigger LLTV<0.80 AND BTC reclaim >$63,500.
why: durable policy from Telegram Q&A persists in chat scrollback only; next Morpho action needs a canonical reference
done: crypto.md has section "Morpho-Blue leverage policy" with both rules + 6-26 source line
loop: morpho-leverage-rule-doc

5. Seed memory/on-chain-watches.yml with 3 PROPOSED type: pool / type: position entries — Morpho-Blue cbBTC/USDC position, USDC-AERO Slipstream pool, Aave V3 cbBTC supply position — commented for operator review.
why: defi-monitor NO_CONFIG day 20; concrete candidates from today's defi-overview land the operator review
done: memory/on-chain-watches.yml has 3 PROPOSED-prefixed entries with TVL/yield context
loop: defi-monitor-no-config

sources: memory=50L logs=7d topics=11 prs=0 cron_failing=0 mode=OK
