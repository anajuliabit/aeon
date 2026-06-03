## Summary

Identified ISS-009 defence-in-depth subtask (a) as the highest-impact, smallest-effort fix from MEMORY.md L16-19 (Current Goals) and L99-102 (Lessons Learned). 0 open improvement PRs at branch time, so no debt to wait on.

**What changed:** `skills/reppo-orchestrator/SKILL.md` — added a named "Emit-in-assistant-text contract" block under the Output contract intro that explicitly names the chain capture step (`.github/workflows/aeon.yml` *Capture skill output*) that clobbers Write-tool output with the CLI `.result`. Renamed section 3 "Write the output" → "Emit the output (in your final assistant text)", swapped "Write a fenced..." → "Emit a fenced...".

**Why this fix:** The current "Write" wording is the exact ambiguity that caused ISS-009 run 18 regression (2026-05-26, 0 on-chain). 5 days clean since the inline fix on 2026-05-30, but the contract was never codified — convention only. This closes subtask (a). Subtask (b) (`continue` → `break` in chain-runner.yml) is a workflow file, out of self-improve scope.

**Files:**
- `skills/reppo-orchestrator/SKILL.md` — 19 insertions, 5 deletions
- `memory/logs/2026-06-03.md` — appended `## Self Improve` block
- `.pending-notify/1780513472-self-improve.md` — staged notification

**PR:** https://github.com/anajuliabit/aeon/pull/68

**Follow-ups:** Subtask (b) chain-runner.yml `continue` → `break` remains open under ISS-009 (workflow file — out of self-improve scope, file separately).
