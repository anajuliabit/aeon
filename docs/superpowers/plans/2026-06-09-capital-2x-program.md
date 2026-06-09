# Capital-2× Program Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the four-phase Capital-2× Program from `docs/superpowers/specs/2026-06-09-capital-2x-program-design.md`: history ledger + performance (investiments), decision-grade market data (aeon), recommendation scorecard (both), weekly conviction report (aeon) — with a multi-agent review workflow after each phase.

**Architecture:** investiments (Bun/TypeScript, Railway) owns durable data + API + dashboard; aeon (bash + Claude Code CLI on GitHub Actions) owns analysis, grading, and notifications. All new fetchers are best-effort-isolated (return empty, never throw). Each phase = its own branch + PR + review workflow + merge.

**Tech Stack:** Bun + TypeScript (investiments), bash + jq + Claude Code CLI headless (aeon), public keyless APIs (GeckoTerminal, Hyperliquid info, DefiLlama, CoinGecko), GitHub Actions.

**Conventions that apply to every task:**
- investiments tests: `bun test`; typecheck `bunx tsc --noEmit`.
- aeon scripts: `bash -n` + jq fixtures; never put wallet addresses in the aeon repo (public) — wallet-scoped data flows through the investiments API/prefetch cache.
- Branches: `2x/phase-1-ledger` (investiments), `2x/phase-2-market-data`, `2x/phase-3-scorecard` (both repos), `2x/phase-4-weekly` (aeon).
- After each phase: run the Review Workflow (Task R), fix confirmed findings, PR, merge.

---

## Phase 1 — History ledger + performance (investiments)

### Task 1.1: HistoryEntry + Performance types

**Files:** Modify: `types.ts` (append)

- [ ] Append to `types.ts`:

```ts
// One ledger line per UTC day (see history-store.ts).
export interface HistoryEntry {
  date: string; // YYYY-MM-DD (UTC)
  totalUsd: number;
  grossAssetsUsd: number;
  totalLiabilitiesUsd: number;
  stableUsd: number;
  btcQty: number;
  btcPriceUsd: number;
  healthFactor: number | null;
  topAssets: { symbol: string; valueUsd: number }[];
  vestingLockedUsd: number;
  vestingClaimableUsd: number;
}

export interface PnlWindow {
  usd: number;
  pct: number;
  fromDate: string;
}

// Computed by performance.ts from the ledger.
export interface Performance {
  baseline: { date: string; totalUsd: number; btcPriceUsd: number };
  latest: { date: string; totalUsd: number };
  pnl: {
    d1: PnlWindow | null;
    d7: PnlWindow | null;
    d30: PnlWindow | null;
    sinceBaseline: PnlWindow;
  };
  maxDrawdownPct: number;
  benchmark: { btcHoldUsd: number; vsBtcUsd: number; vsBtcPct: number };
  pace: {
    targetUsd: number;
    targetDate: string;
    trajectoryUsd: number;
    deltaUsd: number;
    onPace: boolean;
    requiredCagrPct: number;
    elapsedDays: number;
    totalDays: number;
  };
}
```

- [ ] `bunx tsc --noEmit` → clean. Commit: `feat: history + performance types`

### Task 1.2: history-store.ts (TDD)

**Files:** Create: `history-store.ts`, `history-store.test.ts`

- [ ] Write failing tests `history-store.test.ts`:

```ts
import { describe, expect, test } from "bun:test";
import { rm } from "node:fs/promises";
import { historyFromSnapshot, recordDay, readHistory } from "./history-store";
import type { Snapshot } from "./types";

const DIR = "history-store-test";
const snap = (totalUsd: number, date: string): Snapshot =>
  ({
    updatedAt: `${date}T12:00:00.000Z`,
    totalUsd,
    wallets: [],
    positions: [],
    analytics: {
      assets: [
        { symbol: "cbBTC", quantity: 1, valueUsd: totalUsd * 0.6, isStable: false },
        { symbol: "USDC", quantity: 1, valueUsd: totalUsd * 0.4, isStable: true },
      ],
      allocation: { stableUsd: totalUsd * 0.4, otherUsd: totalUsd * 0.6 },
      btc: { btcQty: 1.5, currentBtcPriceUsd: 60000, healthFactor: 1.9 },
      vesting: [{ protocol: "Sablier", symbol: "MAMO", lockedUsd: 1000, claimableUsd: 50 }],
      grossAssetsUsd: totalUsd + 100,
      totalLiabilitiesUsd: 100,
    },
  }) as unknown as Snapshot;

describe("historyFromSnapshot", () => {
  test("maps snapshot into a day entry", () => {
    const e = historyFromSnapshot(snap(1000, "2026-06-09"));
    expect(e.date).toBe("2026-06-09");
    expect(e.totalUsd).toBe(1000);
    expect(e.stableUsd).toBe(400);
    expect(e.btcQty).toBe(1.5);
    expect(e.btcPriceUsd).toBe(60000);
    expect(e.vestingLockedUsd).toBe(1000);
    expect(e.vestingClaimableUsd).toBe(50);
    expect(e.topAssets[0].symbol).toBe("cbBTC");
  });
});

describe("recordDay / readHistory", () => {
  test("appends one entry per day and upserts same-day", async () => {
    await rm(DIR, { recursive: true, force: true });
    await recordDay(snap(1000, "2026-06-08"), DIR);
    await recordDay(snap(1100, "2026-06-09"), DIR);
    await recordDay(snap(1200, "2026-06-09"), DIR); // same day → overwrite
    const h = await readHistory(DIR);
    expect(h).toHaveLength(2);
    expect(h[1].totalUsd).toBe(1200);
    await rm(DIR, { recursive: true, force: true });
  });

  test("readHistory returns [] when missing and slices ?days", async () => {
    await rm(DIR, { recursive: true, force: true });
    expect(await readHistory(DIR)).toEqual([]);
    await recordDay(snap(1, "2026-06-01"), DIR);
    await recordDay(snap(2, "2026-06-02"), DIR);
    await recordDay(snap(3, "2026-06-03"), DIR);
    expect((await readHistory(DIR, 2)).map((e) => e.date)).toEqual(["2026-06-02", "2026-06-03"]);
    await rm(DIR, { recursive: true, force: true });
  });
});
```

- [ ] Run `bun test history-store` → FAIL (module missing)
- [ ] Implement `history-store.ts`:

```ts
import { mkdir, rename, readFile } from "node:fs/promises";
import { join } from "node:path";
import type { Snapshot, HistoryEntry } from "./types";

const FILE = "history.jsonl";
let writeSeq = 0;

export function historyFromSnapshot(s: Snapshot): HistoryEntry {
  const a = s.analytics;
  return {
    date: s.updatedAt.slice(0, 10),
    totalUsd: s.totalUsd,
    grossAssetsUsd: a.grossAssetsUsd,
    totalLiabilitiesUsd: a.totalLiabilitiesUsd,
    stableUsd: a.allocation.stableUsd,
    btcQty: a.btc.btcQty,
    btcPriceUsd: (a.btc as { currentBtcPriceUsd?: number }).currentBtcPriceUsd ?? 0,
    healthFactor: a.btc.healthFactor ?? null,
    topAssets: [...a.assets]
      .sort((x, y) => y.valueUsd - x.valueUsd)
      .slice(0, 10)
      .map((x) => ({ symbol: x.symbol, valueUsd: x.valueUsd })),
    vestingLockedUsd: a.vesting.reduce((s2, v) => s2 + v.lockedUsd, 0),
    vestingClaimableUsd: a.vesting.reduce((s2, v) => s2 + (v.claimableUsd ?? 0), 0),
  };
}

export async function readHistory(dir: string, days?: number): Promise<HistoryEntry[]> {
  try {
    const text = await readFile(join(dir, FILE), "utf8");
    const all = text
      .split("\n")
      .filter((l) => l.trim())
      .map((l) => JSON.parse(l) as HistoryEntry)
      .sort((a, b) => a.date.localeCompare(b.date));
    return days && days > 0 ? all.slice(-days) : all;
  } catch (err) {
    if ((err as NodeJS.ErrnoException).code !== "ENOENT") {
      console.error("[history] read failed:", err);
    }
    return [];
  }
}

// Upsert today's entry; atomic rewrite (tmp + rename) like cache-store.
export async function recordDay(snapshot: Snapshot, dir: string): Promise<void> {
  const entry = historyFromSnapshot(snapshot);
  const existing = (await readHistory(dir)).filter((e) => e.date !== entry.date);
  existing.push(entry);
  existing.sort((a, b) => a.date.localeCompare(b.date));
  await mkdir(dir, { recursive: true });
  const tmp = join(dir, `${FILE}.${process.pid}.${writeSeq++}.tmp`);
  await Bun.write(tmp, existing.map((e) => JSON.stringify(e)).join("\n") + "\n");
  await rename(tmp, join(dir, FILE));
}
```

- [ ] `bun test history-store` → PASS. Commit: `feat: daily history ledger (history-store)`

### Task 1.3: performance.ts (TDD)

**Files:** Create: `performance.ts`, `performance.test.ts`

- [ ] Failing tests `performance.test.ts`:

```ts
import { describe, expect, test } from "bun:test";
import { computePerformance } from "./performance";
import type { HistoryEntry } from "./types";

const e = (date: string, totalUsd: number, btc = 60000): HistoryEntry =>
  ({ date, totalUsd, btcPriceUsd: btc }) as HistoryEntry;

describe("computePerformance", () => {
  test("null when fewer than 2 entries and no baseline override", () => {
    expect(computePerformance([e("2026-06-09", 100)], {})).toBeNull();
  });

  test("pnl windows, drawdown, benchmark, pace", () => {
    const ledger = [
      e("2026-01-01", 100000, 50000), // baseline
      e("2026-03-01", 140000, 50000), // peak
      e("2026-04-01", 105000, 50000), // trough → DD 25%
      e("2026-06-08", 119000, 60000),
      e("2026-06-09", 120000, 60000),
    ];
    const p = computePerformance(ledger, { now: new Date("2026-06-09T12:00:00Z"), targetDate: "2027-12-31" })!;
    expect(p.baseline.totalUsd).toBe(100000);
    expect(p.pnl.d1!.usd).toBe(1000);
    expect(p.pnl.sinceBaseline.usd).toBe(20000);
    expect(p.pnl.sinceBaseline.pct).toBeCloseTo(20);
    expect(p.maxDrawdownPct).toBeCloseTo(25);
    // BTC hold: 100k/50k = 2 BTC → $120k at 60k → equal → vsBtcUsd 0
    expect(p.benchmark.btcHoldUsd).toBeCloseTo(120000);
    expect(p.benchmark.vsBtcUsd).toBeCloseTo(0);
    // pace: target 200k at 2027-12-31; trajectory = 100k * 2^(elapsed/total)
    expect(p.pace.targetUsd).toBe(200000);
    expect(p.pace.trajectoryUsd).toBeGreaterThan(100000);
    expect(p.pace.trajectoryUsd).toBeLessThan(200000);
    expect(typeof p.pace.onPace).toBe("boolean");
  });

  test("baseline override", () => {
    const ledger = [e("2026-06-08", 110000, 60000), e("2026-06-09", 120000, 60000)];
    const p = computePerformance(ledger, {
      baselineUsd: 100000, baselineDate: "2026-01-01", baselineBtcPriceUsd: 50000,
      now: new Date("2026-06-09T12:00:00Z"),
    })!;
    expect(p.baseline.totalUsd).toBe(100000);
    expect(p.pace.targetUsd).toBe(200000);
  });
});
```

- [ ] Run → FAIL. Implement `performance.ts`:

```ts
import type { HistoryEntry, Performance, PnlWindow } from "./types";

export interface PerformanceOptions {
  baselineUsd?: number;
  baselineDate?: string;
  baselineBtcPriceUsd?: number;
  targetDate?: string; // default 2027-12-31
  now?: Date;
}

const DAY_MS = 86_400_000;
const daysBetween = (a: string, b: string): number =>
  Math.round((Date.parse(`${b}T00:00:00Z`) - Date.parse(`${a}T00:00:00Z`)) / DAY_MS);

function windowPnl(entries: HistoryEntry[], latest: HistoryEntry, days: number): PnlWindow | null {
  const cutoff = new Date(Date.parse(`${latest.date}T00:00:00Z`) - days * DAY_MS)
    .toISOString().slice(0, 10);
  const from = [...entries].reverse().find((e) => e.date <= cutoff);
  if (!from) return null;
  return {
    usd: latest.totalUsd - from.totalUsd,
    pct: from.totalUsd > 0 ? (latest.totalUsd / from.totalUsd - 1) * 100 : 0,
    fromDate: from.date,
  };
}

export function computePerformance(
  entries: HistoryEntry[],
  opts: PerformanceOptions,
): Performance | null {
  if (entries.length === 0) return null;
  if (entries.length < 2 && opts.baselineUsd === undefined) return null;
  const latest = entries[entries.length - 1];
  const baseline = opts.baselineUsd !== undefined
    ? { date: opts.baselineDate ?? entries[0].date, totalUsd: opts.baselineUsd,
        btcPriceUsd: opts.baselineBtcPriceUsd ?? entries[0].btcPriceUsd }
    : { date: entries[0].date, totalUsd: entries[0].totalUsd, btcPriceUsd: entries[0].btcPriceUsd };

  let peak = -Infinity;
  let maxDd = 0;
  for (const e of entries) {
    peak = Math.max(peak, e.totalUsd);
    if (peak > 0) maxDd = Math.max(maxDd, (1 - e.totalUsd / peak) * 100);
  }

  const btcHoldUsd = baseline.btcPriceUsd > 0
    ? (baseline.totalUsd / baseline.btcPriceUsd) * latest.btcPriceUsd
    : 0;

  const targetDate = opts.targetDate ?? "2027-12-31";
  const today = (opts.now ?? new Date()).toISOString().slice(0, 10);
  const totalDays = Math.max(1, daysBetween(baseline.date, targetDate));
  const elapsedDays = Math.min(totalDays, Math.max(0, daysBetween(baseline.date, today)));
  const targetUsd = baseline.totalUsd * 2;
  const trajectoryUsd = baseline.totalUsd * 2 ** (elapsedDays / totalDays);
  const daysLeft = Math.max(1, totalDays - elapsedDays);
  const requiredCagrPct = latest.totalUsd > 0
    ? ((targetUsd / latest.totalUsd) ** (365 / daysLeft) - 1) * 100
    : 0;

  return {
    baseline,
    latest: { date: latest.date, totalUsd: latest.totalUsd },
    pnl: {
      d1: windowPnl(entries, latest, 1),
      d7: windowPnl(entries, latest, 7),
      d30: windowPnl(entries, latest, 30),
      sinceBaseline: {
        usd: latest.totalUsd - baseline.totalUsd,
        pct: baseline.totalUsd > 0 ? (latest.totalUsd / baseline.totalUsd - 1) * 100 : 0,
        fromDate: baseline.date,
      },
    },
    maxDrawdownPct: maxDd,
    benchmark: {
      btcHoldUsd,
      vsBtcUsd: latest.totalUsd - btcHoldUsd,
      vsBtcPct: btcHoldUsd > 0 ? (latest.totalUsd / btcHoldUsd - 1) * 100 : 0,
    },
    pace: {
      targetUsd, targetDate, trajectoryUsd,
      deltaUsd: latest.totalUsd - trajectoryUsd,
      onPace: latest.totalUsd >= trajectoryUsd,
      requiredCagrPct, elapsedDays, totalDays,
    },
  };
}
```

- [ ] `bun test performance` → PASS. Commit: `feat: performance engine (pnl, drawdown, benchmark, pace)`

### Task 1.4: server wiring + endpoints

**Files:** Modify: `server.ts` (read it first; add after the snapshot write in the refresh path and new routes alongside existing API routes — auth is enforced globally at server.ts:63 before routing)

- [ ] Refresh path (after `writeSnapshot(snapshot)` succeeds):

```ts
import { recordDay, readHistory } from "./history-store";
import { computePerformance } from "./performance";

const HISTORY_DIR = process.env.HISTORY_DIR ?? "cache";
if (!process.env.HISTORY_DIR) {
  console.warn("⚠ HISTORY_DIR not set — history resets on redeploy (attach a Railway volume)");
}
// after writeSnapshot:
await recordDay(snapshot, HISTORY_DIR).catch((e) => console.error("[history] record failed:", e));
```

- [ ] Routes:

```ts
if (url.pathname === "/api/history" && req.method === "GET") {
  const days = Number(url.searchParams.get("days")) || undefined;
  return Response.json(await readHistory(HISTORY_DIR, days));
}
if (url.pathname === "/api/performance" && req.method === "GET") {
  const entries = await readHistory(HISTORY_DIR);
  const perf = computePerformance(entries, {
    baselineUsd: process.env.BASELINE_USD ? Number(process.env.BASELINE_USD) : undefined,
    baselineDate: process.env.BASELINE_DATE,
    baselineBtcPriceUsd: process.env.BASELINE_BTC_PRICE ? Number(process.env.BASELINE_BTC_PRICE) : undefined,
  });
  return Response.json(perf ?? { empty: true });
}
```

- [ ] `bun test` + `bunx tsc --noEmit` clean. Commit: `feat: /api/history + /api/performance, record day on refresh`

### Task 1.5: dashboard PERFORMANCE panel

**Files:** Modify: `public/index.html` (new readout section above VESTING), `public/app.js`

- [ ] index.html (before VESTING section):

```html
<section class="readout">
  <div class="panel-head"><span class="led"></span>PERFORMANCE — 2× BY 2027-12-31</div>
  <div id="perf-body" class="perf"></div>
  <p class="empty" id="perf-empty" hidden>Not enough history yet (needs ≥ 2 days).</p>
</section>
```

- [ ] app.js — fetch `/api/performance` in `load()` alongside the snapshot, then:

```js
function renderPerformance(p) {
  const body = document.getElementById("perf-body");
  const empty = document.getElementById("perf-empty");
  if (!p || p.empty) { body.replaceChildren(); empty.hidden = false; return; }
  empty.hidden = true;
  const pct = (n) => `${n >= 0 ? "+" : ""}${(n ?? 0).toFixed(1)}%`;
  const w = (x) => (x ? `${usd(x.usd)} (${pct(x.pct)})` : "—");
  const lines = [
    `pace: ${p.pace.onPace ? "ON" : "OFF"} — ${usd(p.latest.totalUsd)} vs trajectory ${usd(p.pace.trajectoryUsd)} (Δ ${usd(p.pace.deltaUsd)})`,
    `target ${usd(p.pace.targetUsd)} by ${p.pace.targetDate} — requires ${pct(p.pace.requiredCagrPct)}/yr from here`,
    `pnl: 1d ${w(p.pnl.d1)} · 7d ${w(p.pnl.d7)} · 30d ${w(p.pnl.d30)} · since ${p.baseline.date} ${w(p.pnl.sinceBaseline)}`,
    `vs BTC-hold: ${usd(p.benchmark.vsBtcUsd)} (${pct(p.benchmark.vsBtcPct)}) · max drawdown ${p.maxDrawdownPct.toFixed(1)}%`,
  ];
  body.replaceChildren(...lines.map((l) => { const d = document.createElement("div"); d.textContent = l; return d; }));
}
```

- [ ] Commit: `feat: dashboard performance panel (pace gauge)`

### Task 1.R: Phase-1 review → fix → PR → merge

- [ ] Review Workflow (spec-fidelity vs Phase 1; investiments conventions; logic/edge cases: date math, upsert atomicity, single-entry behavior, ephemeral-fs warning). One adversarial verifier per finding.
- [ ] Fix confirmed findings; `bun test` green; PR `2x/phase-1-ledger`; merge; probe deploy.

---

## Phase 2 — Decision-grade market data (aeon)

### Task 2.1: macro calendar data file

**Files:** Create: `advisor/data/macro-calendar.json`

- [ ] WebSearch/WebFetch the official 2026 + 2027 FOMC meeting dates (federalreserve.gov) and 2026/2027 CPI release dates (bls.gov). Do NOT invent dates; if 2027 is unpublished, include only published dates and set `"coverageThrough"` accordingly.
- [ ] File shape:

```json
{
  "sources": ["https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm",
              "https://www.bls.gov/schedule/news_release/cpi.htm"],
  "updated": "2026-06-09",
  "coverageThrough": "YYYY-MM-DD",
  "events": [
    { "date": "YYYY-MM-DD", "type": "FOMC", "note": "rate decision" },
    { "date": "YYYY-MM-DD", "type": "CPI", "note": "US CPI release" }
  ]
}
```

- [ ] Commit: `feat(advisor): macro event calendar (FOMC/CPI)`

### Task 2.2: prefetch additions

**Files:** Modify: `scripts/advisor/prefetch-data.sh` (read first; follow its fetch-into-`$D` pattern)

- [ ] Verify live response shapes with one curl per endpoint BEFORE finalizing jq, then add (each best-effort, empty on failure):

```bash
# GeckoTerminal: top Base pools (liquidity + 24h volume) for micro-cap holdings.
: > "$D/gt-liquidity.tmp"
for TOK in mamo reppo; do
  curl -fsS --max-time 20 "https://api.geckoterminal.com/api/v2/search/pools?query=${TOK}&network=base&page=1" \
    -H "Accept: application/json" \
    | jq --arg t "$TOK" '{token: $t, pools: [.data[]? | {name: .attributes.name, liquidityUsd: (.attributes.reserve_in_usd | tonumber? // 0), volume24hUsd: (.attributes.volume_usd.h24 | tonumber? // 0)}] | sort_by(-.liquidityUsd) | .[0:5]}' \
    >> "$D/gt-liquidity.tmp" 2>/dev/null || echo "prefetch: geckoterminal $TOK failed"
done
jq -s '.' "$D/gt-liquidity.tmp" > "$D/gt-liquidity.json" 2>/dev/null; rm -f "$D/gt-liquidity.tmp"

# Hyperliquid funding (BTC/ETH perps).
curl -fsS --max-time 20 -X POST "https://api.hyperliquid.xyz/info" \
  -H "Content-Type: application/json" -d '{"type":"metaAndAssetCtxs"}' \
  | jq '. as [$meta, $ctxs] | [range($meta.universe | length) as $i
        | select($meta.universe[$i].name == "BTC" or $meta.universe[$i].name == "ETH")
        | {coin: $meta.universe[$i].name,
           funding: ($ctxs[$i].funding | tonumber? // null),
           openInterest: ($ctxs[$i].openInterest | tonumber? // null),
           markPx: ($ctxs[$i].markPx | tonumber? // null)}]' \
  > "$D/hl-funding.json" 2>/dev/null || echo "prefetch: hyperliquid funding failed"

# Macro events in the next 14 days from the curated calendar.
TODAY=$(date -u +%Y-%m-%d)
UNTIL=$(date -u -d '+14 days' +%Y-%m-%d 2>/dev/null || date -u -v+14d +%Y-%m-%d)
jq --arg today "$TODAY" --arg until "$UNTIL" \
  '{updated, events: [.events[] | select(.date >= $today and .date <= $until)]}' \
  "$ROOT/advisor/data/macro-calendar.json" > "$D/macro-upcoming.json" 2>/dev/null \
  || echo "prefetch: macro filter failed"
```

- [ ] DefiLlama unlocks: probe `https://api.llama.fi/emissions`; if held tokens (MAMO/REPPO/WELL) are absent, SKIP this feed and note it in the PR body.
- [ ] `bash -n`; run live once. Commit: `feat(advisor): liquidity, funding, macro prefetch`

### Task 2.3: datablocks + prompts

**Files:** Modify: `scripts/advisor/run.sh` (role_data), `advisor/prompts/{fundamentals,yield_allocation,market_macro,risk_leverage}.md`

- [ ] role_data: fundamentals + yield_allocation get `datablock liquidity gt-liquidity.json '.'`; market_macro + risk_leverage get `datablock funding hl-funding.json '.'` and `datablock macro macro-upcoming.json '.'`.
- [ ] Prompt additions:
  - fundamentals: "When suggesting any trim/sell of a micro-cap, state the position's size in days of 24h volume (sum volume24hUsd of the token's pools in `liquidity`). If liquidity data is missing, say so and keep sizing qualitative."
  - yield_allocation: "Liquidity context is provided in `liquidity` for micro-cap holdings — use it when discussing exit feasibility."
  - market_macro: "Use `funding` for perp funding context and `macro` for upcoming FOMC/CPI events; flag any event within 7 days as a timing gate."
  - risk_leverage: "Use `funding` as carry/crowding context for leveraged positions; flag macro events within 7 days that could move BTC against the cbBTC loan."
- [ ] `bash -n scripts/advisor/run.sh`. Commit: `feat(advisor): wire liquidity/funding/macro into analysts`

### Task 2.R: review → fix → PR (include spec + plan docs) → merge → dispatch the advisor once; confirm run green and new datablocks present in logs.

---

## Phase 3 — Recommendation scorecard

### Task 3.1 (investiments): scorecard store + endpoints (TDD)

**Files:** Create: `scorecard-store.ts`, `scorecard-store.test.ts`; Modify: `types.ts`, `advisor-routes.ts` (read first — follow existing route + store patterns), `server.ts` if routes register there

- [ ] types.ts:

```ts
export interface RecGrade {
  date: string; // report date (YYYY-MM-DD)
  index: number; // rec position in that report
  title: string;
  symbol: string | null;
  direction: string;
  horizonDays: number;
  gradedAt: string; // ISO 8601
  result: "hit" | "miss" | "neutral";
  detail: string;
  analysts: string[];
}
```

- [ ] `scorecard-store.ts`: `readScorecard(dir)`, `upsertGrades(grades, dir)` (key `${date}#${index}`, JSONL + atomic rewrite — same pattern as history-store recordDay/readHistory but keyed upsert of many), `analystAccuracy(grades)` → `Record<string, {hit: number; miss: number; neutral: number}>`.
- [ ] Tests: upsert dedupes on date+index (re-grade overwrites); read [] when missing; accuracy tallies multi-analyst recs into each analyst's row.
- [ ] Routes: `GET /api/advisor/scorecard` → `{grades, accuracy}`; `POST /api/advisor/scorecard` `{grades: RecGrade[]}` → upsert. Add `GET /api/advisor/report?date=YYYY-MM-DD` if per-date report retrieval doesn't already exist.
- [ ] `bun test` green. Commit + PR `2x/phase-3-scorecard` (investiments).

### Task 3.2 (aeon): structured PM recommendations

**Files:** Modify: `advisor/prompts/portfolio_manager.md`

- [ ] Extend the recommendations contract: every recommendation object MUST include `symbol` (string|null), `direction` ("increase"|"decrease"|"hold"|"hedge"), `level` (number|null), `invalidateLevel` (number|null), `horizonDays` (30|60|90), `analysts` (contributing roles array). Keep all existing fields. Commit: `feat(advisor): structured rec fields for grading`

### Task 3.3 (aeon): grade-recs.sh

**Files:** Create: `scripts/advisor/grade-recs.sh`

- [ ] Deterministic (no LLM), runs in the weekly workflow OUTSIDE the sandbox with DASHBOARD creds:
  1. For each date D in the last 120 days: `GET /api/advisor/report?date=D`; skip missing.
  2. For each rec with `D + horizonDays <= today` not present in `GET /api/advisor/scorecard`:
     - symbol recs: CoinGecko `/coins/{id}/market_chart/range` (id via `advisor/token-refs.json`; unmapped → `neutral`, detail "unmapped symbol") → price at D and D+horizon. Direction grading: moved ≥5% in called direction → `hit`; ≥5% against → `miss`; else `neutral`. `hold`: `neutral` unless ≤ −25% → `miss`.
     - no symbol: `GET /api/history` totals at D and D+horizon vs the pace trajectory growth over the same window: beat → `hit`, trailed by >5% → `miss`, else `neutral`.
  3. `POST /api/advisor/scorecard` with the batch.
- [ ] `bash -n` + jq fixture test (synthetic report + price series exercising hit/miss/neutral). Commit: `feat(advisor): deterministic recommendation grading`

### Task 3.R: review (both diffs) → fix → merge both PRs.

---

## Phase 4 — Weekly conviction report

### Task 4.1 (investiments): weekly report type

**Files:** Modify: `advisor-store.ts` + `advisor-routes.ts` (report POST accepts optional `type: "daily"|"weekly"`, default daily; weekly stored under its own key per date; `GET /api/advisor?type=weekly` → latest weekly), `public/app.js` (render latest weekly above dailies labeled "WEEKLY CONVICTION")

- [ ] Store round-trip test for weekly type; `bun test` green; commit; PR; merge.

### Task 4.2 (aeon): weekly workflow + prompt + runner

**Files:** Create: `.github/workflows/weekly-conviction.yml`, `advisor/prompts/weekly_conviction.md`, `scripts/advisor/run-weekly.sh`

- [ ] `weekly-conviction.yml`: `0 12 * * 1` + dispatch; same env block as investment-advisor.yml; steps: checkout → install CLI → prefetch-data.sh → grade-recs.sh → run-weekly.sh.
- [ ] `run-weekly.sh` (mirror run.sh helpers: llm-claude.sh, extract_json, post, Telegram):
  - Gather: last 7 daily reports, `/api/performance`, `/api/advisor/scorecard`, phase-2 datablocks from `$D`.
  - One fable-5 call with `weekly_conviction.md` + datablocks → JSON: `{generatedAt, paceVerdict: {onPace, deltaUsd, requiredCagrPct, comment}, actions: [{thesis, symbol, direction, entry, exit, invalidate, sizeUsd, sleevePctAfter, horizonDays, wrongIf}], riskCheck: {coreUntouched, sleevePctOfNet, gates: []}, disclaimer}`.
  - Validation gate (jq): ≤3 actions; every action has numeric entry/exit/invalidate and `sleevePctAfter <= 20`; on violation retry once naming the violation, then post a degraded report with the violation flagged.
  - POST `type: "weekly"`; Telegram summary (pace verdict + action titles). Idempotent per date (re-run overwrites).
- [ ] `weekly_conviction.md`: states the goal (2× totalUsd by 2027-12-31), asymmetric envelope (core = stables reserve + cbBTC structure + locked vesting, NEVER touched; sleeve = liquid non-core, 15–20% of net cap), weekly cadence, max-3 high-conviction actions with explicit levels, scorecard humility ("your per-analyst historical accuracy is provided — weight conviction accordingly"), untrusted-data rule, advisory-only disclaimer, exact output contract.
- [ ] `bash -n` + jq fixture for the validation gate. Commit: `feat(advisor): weekly conviction report`

### Task 4.R: review → fix → PR → merge → dispatch weekly-conviction once; verify dashboard + Telegram.

---

## Final wrap

- [ ] aeon `memory/MEMORY.md`: add Capital-2× program goal (pace on dashboard, weekly Mondays, scorecard accumulating) — fold the btc-levels goal under it.
- [ ] Report to operator the manual actions: (1) attach Railway volume + set `HISTORY_DIR` (else history resets per deploy); (2) optional `BASELINE_USD`/`BASELINE_DATE`/`BASELINE_BTC_PRICE` to pin the baseline.
