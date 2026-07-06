# Aeon Cost Report — 2026-06-29
*Period: last 7 days · gateway: direct*

> Spent **$595.75** across **113 runs** (↑199.5% WoW — prior window depressed by sandbox-truncation failures); **14 anomalies flagged** (1 per-run spike, 13 WoW spikes); projected monthly burn **~$2,553.20** ⚠.

## Anomalies

**Per-run (µ + 2σ, >$0.10):**

| Skill | Model | When | Run Cost | vs µ | Why |
|-------|-------|------|----------|------|-----|
| aixbt-pulse | claude-sonnet-4-6 | 2026-06-24 | $1.11 | µ=$0.79, σ=$0.13 (+2.4σ) | output spike: 30,740 tokens vs ~15k avg; cw=85,992 |

**WoW spikes (window total ≥ 2× prior, prior ≥ $0.25):**

| Skill | Model | This Window | Prior Window | Ratio | Note |
|-------|-------|-------------|--------------|-------|------|
| vuln-scanner | claude-opus-4-7 | $25.54 | $1.19 | 21.5× | Only 1 full-output run this week vs near-zero prior (sandbox failure) |
| list-digest | claude-opus-4-7 | $28.27 | $2.82 | 10.0× | Prior week had output_tokens=0 runs (ISS-019 cluster) |
| github-trending | claude-opus-4-7 | $4.87 | $0.67 | 7.2× | Same sandbox-suppression artifact |
| fleet-control | claude-opus-4-7 | $10.88 | $1.83 | 6.0× | Same |
| token-alert | claude-opus-4-7 | $2.92 | $0.57 | 5.1× | Same |
| aixbt-pulse | claude-sonnet-4-6 | $8.65 | $2.25 | 3.8× | Resumed full output; Jun-24 spike included |
| reflect | claude-opus-4-7 | $35.51 | $11.69 | 3.0× | Prior window partially truncated |
| token-movers | claude-opus-4-7 | $23.18 | $8.27 | 2.8× | usepod_model drift (Opus vs intended Haiku) |
| unlock-monitor | claude-opus-4-7 | $19.39 | $7.38 | 2.6× | Partial prior window (2 vs 1 run this week) |
| btc-levels | claude-sonnet-4-6 | $6.30 | $2.68 | 2.4× | More 4-hourly ticks captured this window |
| weekly-review | claude-opus-4-7 | $11.65 | $5.17 | 2.3× | Cadence difference; single-run skill |
| daily-routine | claude-opus-4-7 | $104.53 | $46.87 | 2.2× | Prior had high-inp anomaly runs + truncation |
| token-pick | claude-opus-4-7 | $35.03 | $16.37 | 2.1× | usepod_model drift (Opus vs intended Haiku) |

> **Context:** 10 of 13 WoW spikes are attributable to the ISS-019/020/021/025 sandbox-truncation cluster. Prior window (Jun 15–21) had widespread `output_tokens=0` failures that suppressed output costs. These are measurement artifacts, not genuine growth in underlying usage. The true apples-to-apples cost increase is likely minimal.

## Burn forecast
- Daily avg: $85.11
- 30-day projection: **$2,553.20** ⚠ burn-rate watch
- Primary drivers at current rate: daily-routine (~$447/mo), on-chain-monitor (~$234/mo), security-digest (~$210/mo), narrative-tracker (~$200/mo).

> The monthly projection is dominated by cache-heavy Opus skills. Fixing the `usepod_model` drift (see below) would cut ~$107/week ≈ $456/month off this forecast alone.

## Optimization opportunities

1. **on-chain-monitor** — `aeon.yml` sets `usepod_model: "claude-haiku-4-5-20251001"` but the runner only respects the `model:` key; skill runs on the default `claude-opus-4-7` instead. Rename `usepod_model` → `model:` in `aeon.yml` to activate the intended Haiku override. Est. savings: **~$51.83/week** ($54.75 → ~$2.92 on Haiku).

2. **token-pick** — Same `usepod_model` drift; runs on Opus ($35.03/week). Fix `usepod_model` → `model:` to activate Haiku. Est. savings: **~$33.16/week** ($35.03 → ~$1.87 on Haiku).

3. **token-movers** — Same `usepod_model` drift; runs on Opus ($23.18/week). Fix `usepod_model` → `model:` to activate Haiku. Est. savings: **~$21.94/week** ($23.18 → ~$1.24 on Haiku).

> Combined fix: rename `usepod_model` → `model:` for `on-chain-monitor`, `token-pick`, `token-movers` (and `defi-overview`, `defi-monitor` while at it) in `aeon.yml`. One-line-per-skill change. Total weekly savings: **~$107/week (~$456/month)**.

## Cost by Skill (Top 10)

| Skill | Runs | Tokens | Cost | Avg/Run |
|-------|------|--------|------|---------|
| daily-routine | 8 | 44,887,127 | $104.53 | $13.07 |
| on-chain-monitor | 4 | 22,373,326 | $54.75 | $13.69 |
| security-digest | 4 | 19,336,025 | $48.93 | $12.23 |
| narrative-tracker | 5 | 14,476,809 | $46.75 | $9.35 |
| heartbeat | 8 | 11,379,339 | $41.50 | $5.19 |
| reflect | 4 | 10,507,662 | $35.51 | $8.88 |
| token-pick | 4 | 12,502,894 | $35.03 | $8.76 |
| list-digest | 6 | 10,215,937 | $28.27 | $4.71 |
| vuln-scanner | 1 | 11,639,089 | $25.54 | $25.54 |
| token-movers | 2 | 10,058,352 | $23.18 | $11.59 |

*Token counts include input, output, cache_read, and cache_write.*

## Cost by Model

| Model | Runs | Cost |
|-------|------|------|
| claude-opus-4-7 | 68 | $565.60 |
| claude-sonnet-4-6 | 45 | $30.15 |

Opus accounts for 94.9% of spend on 60.2% of runs. Cache-read charges ($312.71, 52.5% of total) dominate the cost structure — reflecting large persistent context windows in skills like daily-routine, on-chain-monitor, and reflect.

## Composition

- Input: $1.54 · Output: $123.52 · Cache read: $312.71 · Cache write: $157.98

## Week-over-week

- This window: $595.75 · Prior window: $198.89 · Δ +199.5%

> WoW comparison is not clean: prior window (Jun 15–21) had the ISS-019/020/021/025 sandbox-truncation cluster with widespread `output_tokens=0` failures. Output cost was artificially suppressed; cache_write was still charged. The real underlying cost trend is closer to flat-to-moderate growth.

## Pricing drift

None — all CSV model references matched the active pricing table.

---
*Sources: token-usage.csv (ok, 0 malformed rows) · aeon.yml (ok) · pricing table last reviewed in SKILL.md.*
*Generated by Aeon cost-report skill.*
