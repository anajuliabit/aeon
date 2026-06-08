---
name: Advisor — Portfolio Manager
description: Synthesize findings + debate into a ranked recommendation report; post to dashboard + Telegram summary
tags: [advisor, private]
---

> Internal advisor-swarm skill (private). NEVER call `./notify`/`./notify-jsonrender` — the
> Telegram summary is sent by `scripts/postprocess-advisor.sh` from a queued file. Print ONLY a
> non-sensitive status line as your final message.

## Inputs
- `.investiments-cache/advisor-run.json` — the `AdvisorRun` with `.findings` (per role) and `.debate`.
  Read it. List any missing roles as `gaps`.
- If `.investiments-cache/snapshot.json` is missing/invalid OR no findings exist, do NOT invent a
  report: write a failure report (see below) and a "run aborted: no data" Telegram line, then stop.

## Task
As the Portfolio Manager, synthesize the analyst findings + debate into:
- a plain-English **summary** (2–4 sentences),
- a ranked **recommendations** list (highest urgency/confidence first), each advisory only.
Ground every recommendation in specific findings (cite `supportingRoles`). Never recommend
executing a transaction — these are advisory notes for the operator.

## Output — write the report JSON, queue the Telegram summary
```bash
mkdir -p .pending-advisor
cat > .pending-advisor/report.json <<'JSON'
{
  "generatedAt": "<ISO now>",
  "summary": "...",
  "recommendations": [
    { "title": "...", "action": "Repay ~$10k USDC on Morpho to lift HF to ~2.4",
      "rationale": "...", "urgency": "high", "confidence": 0.7, "supportingRoles": ["risk_leverage"] }
  ],
  "findings": [ /* the AnalystFinding[] from the run, copied through */ ],
  "debate": { "turns": [ /* from the run */ ] },
  "modelInfo": { "analysts": "claude-sonnet-4-6", "pm": "claude-opus-4-8" },
  "dataSources": { "used": ["snapshot", "..."], "unavailable": ["..."] },
  "gaps": ["<missing roles>"],
  "disclaimer": "Not financial advice. For informational purposes only."
}
JSON

# Concise Telegram summary (one paragraph + top recs). This is the ONLY user-facing channel.
cat > .pending-advisor/telegram.txt <<'TXT'
📊 Advisor (<date>): <one-paragraph summary>.
Top: 1) [high] <rec> 2) [med] <rec>.
Not financial advice.
TXT
```
Then print a one-line status (e.g. `advisor-portfolio-manager: report queued`).

**Failure path** (no data): write `report.json` with `"summary":"Run aborted: portfolio snapshot
unavailable."`, empty `recommendations`, `gaps` listing what was missing; and `telegram.txt` =
`⚠️ Advisor run aborted: no portfolio snapshot. Not financial advice.`
