# Investment Advisor Swarm — Design (two-repo, privacy-safe multi-skill)

**Date:** 2026-06-08
**Status:** Approved — ready for implementation plans
**Hand-off note:** `docs/superpowers/specs/2026-06-07-investment-advisor-handoff.md`
**Upstream reference design:** `~/code/investiments/docs/superpowers/specs/2026-06-07-investment-advisor-swarm-design.md`
(reference for the analyst roster, debate, safety posture, and data sources.)

## Goal

An **advisory-only** LLM swarm (TradingAgents-style) that reads the operator's crypto/DeFi
portfolio + market data and produces written recommendations — an "investment manager." It
**never holds keys, never signs, never moves funds.** Built as **aeon skills** (a multi-agent
swarm), **consuming** the portfolio snapshot from the separate **private** `investiments`
dashboard. Runs daily + on-demand; the finished report lands in the investiments dashboard and a
summary goes straight to Telegram.

## The governing constraint: aeon is PUBLIC, investiments is PRIVATE

- `anajuliabit/aeon` is a **PUBLIC** repo. Its skill workflow (`aeon.yml`) auto-commits the
  whole working tree (`git add -A`) to `main`, including `.outputs/*` and `dashboard/outputs/*`.
- `anajuliabit/investiments` is a **PRIVATE** Bun/TS server (already hosts the portfolio
  snapshot behind HTTP Basic auth) with a browser dashboard.

Therefore **no real financial data may ever touch the aeon working tree at commit time**, and
**cross-skill data must not pass through committed files.** Both rules are satisfied by routing
all sensitive data through the **private investiments API** and keeping every aeon-side
financial artifact **gitignored**.

This reverses two earlier ideas (a public chain passing data via committed `.outputs/`, and a
single mega-skill): the swarm stays multi-skill, but the message bus is the private API, not git.

## Architecture (two sub-projects)

```
        aeon (PUBLIC, skills run on GitHub Actions)            investiments (PRIVATE, Bun server)
        ───────────────────────────────────────────           ─────────────────────────────────
 prefetch-advisor.sh  ──GET /api/snapshot───────────────────▶  Basic-auth guarded routes
   (before Claude)     ──GET /api/advisor/run?date=──────────▶  advisor-store.ts (per-day run doc)
        │                                                          ▲   │
        ▼ writes gitignored .investiments-cache/*.json             │   ▼
   ┌─ portfolio-snapshot (gate)                                    │  public/ Advisor panel
   ├─ advisor-risk-leverage     ┐                                  │
   ├─ advisor-yield-allocation  │ 5 analysts (parallel)            │
   ├─ advisor-market-macro      │ read snapshot cache, fetch feeds │
   ├─ advisor-fundamentals      │ write finding JSON to            │
   ├─ advisor-news-social       ┘ .pending-advisor/                │
   ├─ advisor-debate    (reads run doc, writes debate JSON)        │
   └─ advisor-portfolio-manager (reads run doc, writes report+TG)  │
        │                                                          │
        ▼ after Claude:                                            │
 postprocess-advisor.sh ──POST /api/advisor/{finding,debate,report}┘
   (after Claude)        ──Telegram sendMessage (summary, direct curl)
```

Ordering is provided by aeon's **chain-runner** (it dispatches each stage and *waits* for it to
finish before the next — `wait_for_runs` barrier). We use the chain-runner **only for ordering**;
we do **not** use its `consume:` mechanism (that commits context to public main). Data flows
exclusively through the private API via prefetch (GET, before Claude) and postprocess (POST,
after Claude) — aeon's sanctioned way to reach an authed API from a sandboxed skill.

### Why this works on CI (each skill = a separate Actions job)

Separate jobs share no disk, so data must pass via an external store. The private investiments
API is that store. The two sandbox-safe hooks carry it:

| Need | Hook | When | Effect |
|---|---|---|---|
| Read snapshot | `scripts/prefetch-advisor.sh` | before Claude (full env) | GET snapshot → gitignored `.investiments-cache/snapshot.json` (every advisor job) |
| Read prior findings | `scripts/prefetch-advisor.sh` | before Claude | for `advisor-debate`/`advisor-portfolio-manager`: GET `/api/advisor/run?date=today` → `.investiments-cache/advisor-run.json` |
| Write finding/debate/report + Telegram | `scripts/postprocess-advisor.sh` | after Claude (full env) | POST `.pending-advisor/*.json` to investiments; send `.pending-advisor/telegram.txt` to Telegram |

**Run correlation = the UTC date** (daily run): investiments upserts a per-day run document;
analysts POST findings into today's run; debate/PM read today's run; PM posts the report and
flags it `latest`. `workflow_dispatch` reuses the same day key (latest-wins per role).

## aeon chain definition (`aeon.yml`)

```yaml
chains:
  investment-advisor:
    schedule: "0 13 * * *"          # daily 13:00 UTC, after market-context-refresh
    on_error: continue              # a failed analyst → noted gap; run still completes
    steps:
      - skill: portfolio-snapshot
      - parallel: [advisor-risk-leverage, advisor-yield-allocation, advisor-market-macro,
                   advisor-fundamentals, advisor-news-social]
      - skill: advisor-debate
      - skill: advisor-portfolio-manager
```

`workflow_dispatch` runs it on demand (Chain Runner workflow, `chain=investment-advisor`).
No `consume:` keys — intermediates ride the private API, not committed `.outputs/`.

## Skills (aeon side)

Each is a normal aeon skill (`skills/<name>/SKILL.md`). Analysts are **portfolio-aware** (scoped
to real holdings + liquidation data from the snapshot cache) and **reuse the proven data-fetch
recipes** from existing skills (`defi-overview`, `market-context-refresh`, `narrative-tracker`,
`aixbt-pulse`) — reuse the plumbing, not the standalone notifying output.

| Skill | Role | Data | Writes |
|---|---|---|---|
| `portfolio-snapshot` | gate: validate cache freshness | `.investiments-cache/snapshot.json` | `.pending-advisor/run.json` (init today's run) |
| `advisor-risk-leverage` | liquidation distance, HF, what-if BTC drop, deleverage, vesting liquidity | snapshot `analytics.btc` + positions + vesting | `.pending-advisor/finding-risk_leverage.json` |
| `advisor-yield-allocation` | idle stables, rate moves, buffer vs target | DefiLlama + Morpho | `.pending-advisor/finding-yield_allocation.json` |
| `advisor-market-macro` | BTC technicals, momentum, macro pulse | CoinGecko + GeckoTerminal + AIXBT + `/global` | `.pending-advisor/finding-market_macro.json` |
| `advisor-fundamentals` | TVL/revenue, mcap/FDV/supply for held symbols | DefiLlama + CoinGecko | `.pending-advisor/finding-fundamentals.json` |
| `advisor-news-social` | headlines, Fear&Greed, X sentiment | crypto RSS + Fear&Greed + Grok `x_search` | `.pending-advisor/finding-news_social.json` |
| `advisor-debate` | bull + bear over combined findings (1 round) | run doc (cache) | `.pending-advisor/debate.json` |
| `advisor-portfolio-manager` | ranked recommendations + summary | run doc (cache) | `.pending-advisor/report.json` + `.pending-advisor/telegram.txt` |

Skills **never call `./notify`** (it writes committed `dashboard/outputs/`). The PM's Telegram
summary is queued for `postprocess-advisor.sh` to send directly.

## Structured payloads (JSON, posted to the private API)

```jsonc
// finding-<role>.json
{ "role": "risk_leverage", "thesis": "...", "signals": ["..."], "concerns": ["..."],
  "suggestedActions": [{ "action": "...", "rationale": "...", "confidence": 0.0 }],
  "error": null }

// debate.json
{ "turns": [ { "side": "bull", "points": ["..."], "rebuttals": ["..."] },
             { "side": "bear", "points": ["..."], "rebuttals": ["..."] } ] }

// report.json (PM output → /api/advisor/report, served to the dashboard)
{ "generatedAt": "<ISO>", "summary": "...",
  "recommendations": [ { "title": "...", "action": "Repay ~$10k USDC on Morpho to lift HF to ~2.4",
                         "rationale": "...", "urgency": "high", "confidence": 0.0,
                         "supportingRoles": ["risk_leverage"] } ],
  "findings": [ /* AnalystFinding[] */ ], "debate": { /* turns */ },
  "modelInfo": { "analysts": "claude-sonnet-4-6", "pm": "claude-opus-4-8" },
  "dataSources": { "used": ["..."], "unavailable": ["..."] },
  "gaps": ["news_social"], "disclaimer": "Not financial advice. ..." }
```

## investiments side (private) — new endpoints + store + panel

All routes already sit behind `checkBasicAuth` (`auth.ts`), so the advisor routes inherit auth
using the same `DASHBOARD_PASSWORD` the snapshot uses.

- **`advisor-store.ts`** (mirrors `cache-store.ts`: atomic temp-then-rename, dir-injectable for
  tests): `readRun(date)`, `upsertFinding(date, role, finding)`, `setDebate(date, debate)`,
  `setReport(date, report)` (also writes `latest.json`), `readLatest()`. Per-day file
  `advisor/runs/<date>.json`; `advisor/latest.json` for the panel. `advisor/` is gitignored.
- **`server.ts`** new routes (all auth-guarded):
  - `POST /api/advisor/run` `{date}` → ensure today's run doc exists.
  - `POST /api/advisor/finding` `{date, role, finding}` → `upsertFinding`.
  - `POST /api/advisor/debate` `{date, debate}` → `setDebate`.
  - `POST /api/advisor/report` `{date, report}` → `setReport` (+ `latest.json`).
  - `GET /api/advisor/run?date=YYYY-MM-DD` (default today) → run doc (findings + debate + report).
  - `GET /api/advisor` → `latest.json` or `{ empty: true }` (dashboard panel reads this).
- **`public/`** — an "ADVISOR" panel: latest summary, ranked recommendations (urgency/confidence),
  last-run time, data-sources used/unavailable, gaps, and the disclaimer.
- **`types.ts`** — add `AnalystFinding`, `DebateTurn`, `Recommendation`, `AdvisorReport`,
  `AdvisorRun` interfaces (shapes above).

## Model strategy (evidence-based)

2026 finance benchmarks, scoped to aeon-routable models. **Hallucination resistance is the
governing metric** for real-money advice: Gemini 3.1 Pro (≈45/100) and Qwen 3.6 (≈32/100)
*confidently fabricate* financial figures → **disqualified for any reasoning step**. Claude
(Opus 4.6 ≈78) and Kimi K2.5 (≈71) are the disciplined options. Claude Opus 4.8 is also #1 on
finance reasoning accuracy (89.1%) and cheapest at the top tier.

- **`portfolio-snapshot`, 5 analysts, `advisor-debate` → `claude-sonnet-4-6`** (per-skill
  `model:` override in `aeon.yml`).
- **`advisor-portfolio-manager` → `claude-opus-4-8`** (the high-judgment synthesis).
- **Fallback (only if added later) → Kimi K2.5**; **never** Gemini/Qwen/DeepSeek for reasoning.

Sources: [aimultiple 38-LLM finance benchmark](https://aimultiple.com/finance-llm),
[JurisTech hallucination report](https://juristech.net/best-llm-tools-for-financial-analysis-2026/),
[Finance LLM Leaderboard](https://awesomeagents.ai/leaderboards/finance-llm-leaderboard/).

> **Verification:** `aeon.yml`'s model resolver greps the per-skill `model:` free-form and passes
> it to `claude --model`, so `claude-opus-4-8` works even though the dispatch dropdown only lists
> `4-7`. The plan confirms a live run accepts it.

## Privacy & safety (non-negotiable)

- **Advisory-only** — no skill signs, drafts, or submits a transaction, ever. Primary control.
- **No financials on public main.** All sensitive aeon-side artifacts are **gitignored**:
  `.investiments-cache/`, `.pending-advisor/`, `reports/advisor/`, plus
  `.outputs/portfolio-snapshot.md` and `.outputs/advisor-*.md`. The private API is the only
  cross-skill bus. Skills must not call `./notify`/`./notify-jsonrender`.
- **Secrets never expand in the sandbox.** `INVESTIMENTS_BASIC_AUTH` and Telegram tokens are used
  only inside prefetch/postprocess scripts (full-env, outside Claude). Never logged or committed.
- **Untrusted external text** (RSS, X via Grok, AIXBT/GeckoTerminal) is delimited; models are told
  to ignore embedded instructions (aeon `CLAUDE.md` security section).
- **Data-guarding** on every analyst: "use only provided/fetched data; if a figure is missing,
  say so — never invent." Claude-only models for reasoning.
- Every report + Telegram summary carries a **"not financial advice"** disclaimer.

## Error handling — failure isolation

- **Per-feed:** a dead source → analyst marks that section "unavailable" and reasons around it.
- **Per-agent:** a failed analyst job → no finding posted for that role; the run doc simply lacks
  it; PM synthesizes from present findings and lists the gap. Chain `on_error: continue`.
- **Hard stop** only if the snapshot cache is empty/missing → `portfolio-snapshot` records the
  failure and downstream analysts emit an `error` finding; PM, finding no usable data, posts a
  failure report + Telegram "advisor run aborted: no snapshot" instead of inventing positions.

## Secrets / config

- **aeon (GH Actions secrets + local `.env`):** `INVESTIMENTS_BASIC_AUTH` = `base64("admin:<DASHBOARD_PASSWORD>")`
  (pull `<DASHBOARD_PASSWORD>` from the investiments Railway vars). `XAI_API_KEY` already present.
  `TELEGRAM_BOT_TOKEN` + `TELEGRAM_CHAT_ID` already present. Add `INVESTIMENTS_BASIC_AUTH` to the
  prefetch env block and `INVESTIMENTS_BASIC_AUTH`+Telegram to the postprocess env block in `aeon.yml`.
- **investiments:** no new secret — advisor routes reuse `DASHBOARD_PASSWORD`. `INVESTIMENTS_BASE_URL`
  (aeon side) = `https://investiments-production.up.railway.app`.

## Verification

- **investiments:** `bun test` covers `advisor-store.ts` (read/write/upsert/atomic) and the new
  route handlers (auth required; finding/debate/report round-trip; GET latest). Manual: panel
  renders a posted report.
- **aeon:** `prefetch-advisor.sh` caches snapshot + run doc against live Railway with the real
  secret (and exits 0 cleanly without it / for non-advisor skills). `postprocess-advisor.sh` POSTs
  queued payloads + sends Telegram. A manual `workflow_dispatch` chain run produces a report in the
  dashboard + a Telegram summary. Failure-isolation: induce one analyst failure → report still
  posts with the gap noted. **Leak check:** after a run, `git log -p origin/main` shows no
  financial data and no secret in any committed file.

## Build order

**Plan A — investiments endpoints (build first; gives aeon a target to POST to):**
store → types → routes → panel → tests.

**Plan B — aeon skills (build second):** gitignore + secrets/env wiring → `prefetch-advisor.sh`
→ `postprocess-advisor.sh` → `portfolio-snapshot` → 5 analyst skills → `advisor-debate` →
`advisor-portfolio-manager` → chain in `aeon.yml` → live verification + leak check.

## Out of scope (YAGNI / later)

- Any execution, transaction drafting, or key access (advisory-only, hard rule).
- Iterative multi-round debate / convergence loops (single round in v1).
- A hierarchical risk-manager veto gate.
- Backtesting or performance tracking of past recommendations.
- FRED macro augmentation (optional `FRED_API_KEY`) — keyless macro feeds suffice for v1.
- An aeon-side dashboard (json-render) panel — the report lives in the investiments dashboard.
