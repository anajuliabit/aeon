# Investment Advisor Swarm (aeon-native) — Design

**Date:** 2026-06-08
**Status:** Approved — ready for implementation plan
**Hand-off note:** `docs/superpowers/specs/2026-06-07-investment-advisor-handoff.md`
**Upstream reference design:** `~/code/investiments/docs/superpowers/specs/2026-06-07-investment-advisor-swarm-design.md`
(reference for the analyst roster, debate, safety posture, and data sources — *superseded* on
host-repo and LLM-runtime choices, which this spec settles for aeon.)

## Goal

An **advisory-only** LLM swarm (TradingAgents-style) that reads the operator's crypto/DeFi
portfolio + market data and produces written recommendations — an "investment manager." It
**never holds keys, never signs, never moves funds.** Decision (2026-06-07): build it in
**aeon** (already a multi-agent platform with the data skills, scheduler, notifications, and
LLM gateway), **consuming** the portfolio snapshot from the separate `investiments` dashboard.

Runs daily and on-demand; delivers a concise notification + a saved markdown report.

## Why aeon hosts it

aeon already has almost every input as a working skill (`market-context-refresh`,
`defi-overview`, `narrative-tracker`/`fetch-tweets`, `aixbt-pulse`, plus
CoinGecko/DeFiLlama/GeckoTerminal/Fear&Greed clients), a cron scheduler (`aeon.yml`),
notifications (`./notify`), and an LLM gateway. The only missing input — **Morpho liquidation
price + health factor + per-position snapshot** — is exactly what `investiments` computes and
serves over HTTP.

## Key aeon-native reframings (vs. the upstream TS design)

The upstream spec was written for a standalone Bun/TS process where "an agent" is a function
making one `completeJSON` LLM call. In aeon the unit of composition is different, and three
things change accordingly:

1. **A skill *is* an LLM call.** Each aeon skill is a full Claude Code run inside a GitHub
   Actions job. So the swarm is a **chain of skill-jobs**, not parallel function calls in one
   process. The upstream "OpenAI-compatible provider layer + `completeJSON`" collapses to
   aeon's existing per-skill `model:` override and the Virtuals gateway/fallback already wired
   into `aeon.yml`.
2. **"Structured output" = a documented block format**, not a TS schema/validator. Each skill
   writes a fenced, clearly-delimited block to `.outputs/<skill>.md`; the next stage consumes
   it via the chain `consume:` mechanism.
3. **Failure isolation = chain `on_error: continue` + "note the gap" prompting**, not
   try/catch around function calls.

## Architecture — a chain mirroring `reppo-swarm`

A new `investment-advisor` chain in `aeon.yml`, four sequential stages (8 skill-jobs/run):

```
Stage 1  portfolio-snapshot                     fetch Railway /api/snapshot (Basic auth) → snapshot block
Stage 2  parallel:                              5 portfolio-aware analysts; each consumes the
           advisor-risk-leverage                  snapshot, emits a structured AnalystFinding
           advisor-yield-allocation
           advisor-market-macro
           advisor-fundamentals
           advisor-news-social
Stage 3  parallel:                              consume snapshot + all 5 findings → DebateTurn
           advisor-bull
           advisor-bear
Stage 4  advisor-portfolio-manager              consume findings + debate → ranked
                                                  Recommendation[] + summary; ./notify + write report
```

`chains:` definition (final form pinned by the implementation plan):

```yaml
chains:
  investment-advisor:
    schedule: "0 13 * * *"          # daily 13:00 UTC, after market-context-refresh warms memory
    on_error: continue              # per-agent failure isolation
    steps:
      - skill: portfolio-snapshot
      - parallel: [advisor-risk-leverage, advisor-yield-allocation, advisor-market-macro,
                   advisor-fundamentals, advisor-news-social]
        consume: [portfolio-snapshot]
      - parallel: [advisor-bull, advisor-bear]
        consume: [portfolio-snapshot, advisor-risk-leverage, advisor-yield-allocation,
                  advisor-market-macro, advisor-fundamentals, advisor-news-social]
      - skill: advisor-portfolio-manager
        consume: [advisor-risk-leverage, advisor-yield-allocation, advisor-market-macro,
                  advisor-fundamentals, advisor-news-social, advisor-bull, advisor-bear]
```

> **Implementation-plan verification:** confirm `chain-runner.yml` supports (a) a `parallel:`
> step that also carries `consume:`, and (b) running `scripts/prefetch-*.sh` before Claude
> (the main `aeon.yml` workflow does this; the chain runner must too). If either is missing,
> the plan adds it. Fallback for (a): if parallel-with-consume is unsupported, each analyst
> reads the cached snapshot file directly instead of relying on `consume:`.

Also add `workflow_dispatch` for manual runs.

## The data seam — `portfolio-snapshot` skill + credential

The one genuinely-new capability: an authenticated GET to
`https://investiments-production.up.railway.app/api/snapshot`.

- **Sandbox constraint:** GitHub Actions blocks `curl` with an env-var expanded into an auth
  header, and `WebFetch` cannot do HTTP Basic auth. So this uses aeon's **prefetch pattern**:
  `scripts/prefetch-portfolio-snapshot.sh` runs *before* Claude with full env, curls the URL
  with the secret, and writes `.investiments-cache/snapshot.json`. The skill reads the cache.
- **Secret:** a single var `INVESTIMENTS_BASIC_AUTH` = `base64("admin:<password>")`, stored as
  a GitHub Actions secret and in the local `.env`. Never logged, never committed. `<password>`
  comes from the Railway service vars / the operator.
- `.investiments-cache/` is added to `.gitignore`.
- The skill emits a compact, structured snapshot block to `.outputs/portfolio-snapshot.md`:
  `totalUsd`, `updatedAt`, per-position rows, and the **`analytics.btc`** block (qty, loanUsd,
  netBtcValueUsd, currentBtcPriceUsd, **liquidationPriceUsd, healthFactor, dropToLiqPct,
  lltv**), allocation (stable/other), assets, vesting.
- If the fetch fails / cache is empty → the chain **hard-stops** at the PM step with a failure
  notification (no portfolio = no advice; never invent positions).

### Snapshot response shape (advisor input)

```jsonc
{
  "totalUsd": 340533.86,
  "updatedAt": "<ISO>",
  "wallets": [{ "address", "totalUsd", "error" }],
  "positions": [{ "wallet","chain","protocol","type","symbol","name","quantity","price","valueUsd" }],
  "analytics": {
    "btc": { "btcQty","btcValueUsd","loanUsd","netBtcValueUsd","netBtcQty",
             "currentBtcPriceUsd","liquidationPriceUsd","healthFactor","dropToLiqPct","lltv" },
    "allocation": { "stableUsd","otherUsd" },
    "assets": [{ "symbol","quantity","valueUsd","isStable" }],
    "vesting": [{ "protocol","lockedUsd" }]
  }
}
```

## Analyst roster → data-source mapping

Five **new** analyst skills. They are portfolio-aware (scoped to the operator's holdings +
liquidation data) and emit structured findings — but they **reuse the proven data-fetch
recipes** (endpoints + parsing) from the existing standalone skills rather than rebuilding
them. "Reuse" = reuse the plumbing, not the standalone notifying output.

| Skill | Role | Sources (reused recipes) | Key |
|---|---|---|---|
| `advisor-risk-leverage` | Liquidation distance, HF, what-if BTC drop, deleverage, vesting/unlock liquidity | snapshot `analytics.btc` + positions + vesting | — |
| `advisor-yield-allocation` | Idle stables, rate moves, stablecoin buffer vs target | DefiLlama + Morpho (`defi-overview` recipe) | keyless |
| `advisor-market-macro` | BTC technicals, momentum/runners, macro pulse | CoinGecko + GeckoTerminal + AIXBT + CoinGecko `/global` (`market-context-refresh` + `aixbt-pulse`) | keyless |
| `advisor-fundamentals` | TVL/revenue + mcap/FDV/supply for held symbols | DefiLlama + CoinGecko | keyless |
| `advisor-news-social` | Headlines, Fear & Greed, X sentiment | crypto RSS + Fear & Greed + Grok `x_search` | `XAI_API_KEY` (in `.env`) |

Then **`advisor-bull`** + **`advisor-bear`** debate the combined findings (1 round), and
**`advisor-portfolio-manager`** produces the ranked `Recommendation[]` + plain-English summary.

## Structured block formats (between stages)

Documented, fenced blocks in each skill's `.outputs/<skill>.md` (mirrors the upstream types,
expressed as markdown the next stage parses):

- **AnalystFinding:** `role`, `thesis`, `signals[]`, `concerns[]`,
  `suggestedActions[{action, rationale, confidence 0..1}]`, optional `error` (noted gap).
- **DebateTurn:** `side` (bull|bear), `points[]`, `rebuttals[]`.
- **Recommendation:** `title`, `action` (advisory, e.g. "Repay ~$10k USDC on Morpho to lift HF
  to ~2.4"), `rationale`, `urgency` (low|medium|high), `confidence 0..1`, `supportingRoles[]`.
- **AdvisorReport** (PM output): `generatedAt`, `summary`, `recommendations[]`, `findings[]`,
  `debate[]`, `modelInfo`, `dataSources{used, unavailable}`, `gaps[]`, `disclaimer`.

## Model strategy (evidence-based)

From 2026 finance benchmarks scoped to models aeon's gateway can route to:

- **Hallucination resistance is the governing metric** for real-money advice. Gemini 3.1 Pro
  (45/100) and Qwen 3.6 (32/100) **confidently fabricate** primary financial metrics and are
  **disqualified** for any reasoning step. Claude (Opus 4.6 ≈ 78) and Kimi K2.5 (≈ 71) are the
  disciplined options; GPT-5.4 (≈ 92) leads but isn't the aeon native default.
- **Finance reasoning accuracy:** Claude Opus 4.8 (89.1%) is top *and* cheapest at the top tier;
  Claude Sonnet 4.6 (83.6%) is strong for scoped summarization.

Assignment:

- **Analysts + `advisor-bull`/`advisor-bear` → `claude-sonnet-4-6`** (accurate enough for
  scoped data-summarization, Claude-family discipline, cheap across 7 jobs).
- **`advisor-portfolio-manager` → `claude-opus-4-8`** (top finance accuracy + 2nd-best
  hallucination resistance + cheapest at the top tier; the high-judgment synthesis step).
- **Fallback (only if added later) → Kimi K2.5**; **never** Gemini/Qwen/DeepSeek for reasoning.

> **Verification:** `aeon.yml`'s comment lists `claude-opus-4-7` as a model option. The plan
> confirms the workflow's model passthrough accepts `claude-opus-4-8` for the PM step.

Sources: [aimultiple 38-LLM finance benchmark](https://aimultiple.com/finance-llm),
[JurisTech hallucination report](https://juristech.net/best-llm-tools-for-financial-analysis-2026/),
[Finance LLM Leaderboard](https://awesomeagents.ai/leaderboards/finance-llm-leaderboard/).

## Error handling — failure isolation

- **Per-feed:** any dead data source → the analyst marks that section "unavailable" and reasons
  around it; never aborts the run.
- **Per-agent:** a failed analyst job → its `.outputs/` is missing/`error`; the PM is instructed
  to synthesize from whatever findings exist and list the gap in `report.gaps`. Chain uses
  `on_error: continue`.
- **Hard stop only** if the snapshot can't be fetched (empty/missing cache) → the PM step
  notifies the failure instead of inventing data.

## Safety (non-negotiable)

- **Advisory-only** — no skill signs, drafts, or submits a transaction, ever. Primary control.
- **Untrusted external text** (RSS, X posts via Grok, AIXBT/GeckoTerminal text) is delimited and
  models are instructed to ignore embedded instructions (per aeon `CLAUDE.md` security section).
- **Data-guarding** on every analyst: "use only the provided/fetched data; if a figure is
  missing, say so — never invent." Reinforced by the hallucination research. Claude-only models
  for reasoning.
- **Reports hold real financials** → written to a **gitignored** `reports/advisor/` directory;
  every report and notification carries a clear **"not financial advice"** disclaimer.
- **No secret leakage** — `INVESTIMENTS_BASIC_AUTH` (and any other secret) never appears in
  outputs, logs, or committed files.

## Schedule + output

- **Daily** `0 13 * * *` UTC + **`workflow_dispatch`** for on-demand runs.
- The PM step calls **`./notify`** with a concise summary (top recommendations + urgency, one
  paragraph) and writes the full report to **`reports/advisor/<ISO>.md`**.

## Verification (aeon skills are Claude runs, not unit-tested code)

1. `scripts/prefetch-portfolio-snapshot.sh` fetches and caches the snapshot against the live
   Railway URL with the real `INVESTIMENTS_BASIC_AUTH` secret (and fails cleanly without it).
2. A manual `workflow_dispatch` chain run produces all 8 stage outputs, delivers a notification,
   and writes a report file.
3. **Failure isolation:** induce one feed failure and one analyst failure → the report still
   generates with the gaps noted (`unavailable` / `gaps` populated).
4. **No secret leak:** grep run logs and `.outputs/` / report for the credential — must be absent.
5. Confirm `claude-opus-4-8` is accepted by the workflow for the PM step.

## Build order (sequenced, each step independently checkable)

1. Add `INVESTIMENTS_BASIC_AUTH` to `.env` / GH secrets; `.gitignore` for `.investiments-cache/`
   and `reports/advisor/`.
2. `scripts/prefetch-portfolio-snapshot.sh` + `portfolio-snapshot` skill (reads cache, emits
   snapshot block). Verify against live Railway.
3. `chain-runner.yml` capability check (parallel-with-consume + prefetch); patch if needed.
4. Five analyst skills (`advisor-*`) — prompts, data-fetch recipes, structured `AnalystFinding`.
5. `advisor-bull` + `advisor-bear` debate skills.
6. `advisor-portfolio-manager` — synthesis, ranked recommendations, `./notify`, report write.
7. Wire the `investment-advisor` chain + `workflow_dispatch` into `aeon.yml`; set per-skill models.
8. Full verification: live dispatch run, failure-isolation test, secret-leak grep.

## Out of scope (YAGNI / later)

- Any execution, transaction drafting, or key access (advisory-only, hard rule).
- Iterative multi-round debate / convergence loops (single round in v1).
- A hierarchical risk-manager veto gate.
- Backtesting or performance tracking of past recommendations.
- An aeon dashboard (json-render) panel for the advisor — notification + report only in v1.
- FRED macro augmentation (optional `FRED_API_KEY`) — keyless macro feeds suffice for v1.
