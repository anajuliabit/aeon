Notification staged and log entry written.

## Summary

Ran the **github-trending** skill for 2026-06-04.

- **Fetched:** trending?since=daily via WebFetch → 14 repos (middle of recent 7-day range).
- **Enriched:** 4 real candidates via `gh api` (created_at / stars / forks / pushed_at).
- **Kept 2/14**, single combined "ai/ml" bucket, sub-3-survivor framing (no top-pick header):
  - [opendataloader-project/opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) — 570 today / 24k total · Java · **ACCELERATING** (60/day baseline × 9.4x, pushed today). Why: Java PDF parser that keeps tables + layout intact for retrieval pipelines.
  - [lyogavin/airllm](https://github.com/lyogavin/airllm) — 208 today / 19k total · Jupyter · **RETURNING** (17.6/day baseline × 11.8x, push 86d stale → post-driven surge). Why: 70B inference on a single 4GB GPU via layered weight offload.
- **Dropped 12:** 2 dedup (chopratejas/headroom, affaan-m/ECC carrying from 6-03), 5 dedup-residuals (hermes-webui / markitdown / Scrapling / supermemory / Open-LLM-VTuber), 1 learn-X (coding-interview-university), 2 below-floor stable (trivy, odoo), 2 **suspicious-magnitude page-composition guards**: NousResearch/hermes-agent (17.1% forks/stars ratio matching ECC precedent + vague "agent that grows with you" tagline), HKUDS/Vibe-Trading (19.7% forks/stars ratio + only 1.2x baseline = manufactured velocity).
- **Files written:**
  - `.pending-notify/1780565261-github-trending.md` (715 chars, well under 4000 ceiling — post-run delivery step picks it up).
  - `memory/logs/2026-06-04.md` (appended `### github-trending` log entry).
- **Sources:** trending=ok · gh_api=ok · kept 2/14
- **Exit:** `GITHUB_TRENDING_OK`
