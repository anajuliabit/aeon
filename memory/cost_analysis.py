import csv
import math
from collections import defaultdict
from datetime import date

# Pricing (per million tokens)
PRICING = {
    "claude-opus-4-7":          {"input": 15.00, "output": 75.00, "cache_read": 1.50,  "cache_write": 18.75},
    "claude-sonnet-4-6":        {"input":  3.00, "output": 15.00, "cache_read": 0.30,  "cache_write":  3.75},
    "claude-haiku-4-5-20251001":{"input":  0.80, "output":  4.00, "cache_read": 0.08,  "cache_write":  1.00},
}

WINDOW_START = date(2026, 5, 25)
WINDOW_END   = date(2026, 5, 31)

def row_cost(row):
    p = PRICING[row["model"]]
    return (
        int(row["input_tokens"])   / 1e6 * p["input"]  +
        int(row["output_tokens"])  / 1e6 * p["output"] +
        int(row["cache_read"])     / 1e6 * p["cache_read"] +
        int(row["cache_creation"]) / 1e6 * p["cache_write"]
    )

def row_cost_breakdown(row):
    p = PRICING[row["model"]]
    ic  = int(row["input_tokens"])   / 1e6 * p["input"]
    oc  = int(row["output_tokens"])  / 1e6 * p["output"]
    rrc = int(row["cache_read"])     / 1e6 * p["cache_read"]
    wrc = int(row["cache_creation"]) / 1e6 * p["cache_write"]
    return ic, oc, rrc, wrc

# Load CSV
all_rows = []
with open("memory/token-usage.csv") as f:
    for r in csv.DictReader(f):
        r["_date"] = date.fromisoformat(r["date"])
        r["_cost"] = row_cost(r)
        all_rows.append(r)

window_rows = [r for r in all_rows if WINDOW_START <= r["_date"] <= WINDOW_END]

# 1. In-window row count
print("=" * 70)
print("1. IN-WINDOW ROW COUNT")
print("=" * 70)
print(f"   In-window rows: {len(window_rows)}")

# 2. Total cost breakdown
total_ic = total_oc = total_rrc = total_wrc = 0.0
for r in window_rows:
    ic, oc, rrc, wrc = row_cost_breakdown(r)
    total_ic  += ic
    total_oc  += oc
    total_rrc += rrc
    total_wrc += wrc

total_cost = total_ic + total_oc + total_rrc + total_wrc

print()
print("=" * 70)
print("2. TOTAL COST BREAKDOWN (in-window)")
print("=" * 70)
print(f"   input_cost:       ${total_ic:.4f}")
print(f"   output_cost:      ${total_oc:.4f}")
print(f"   cache_read_cost:  ${total_rrc:.4f}")
print(f"   cache_write_cost: ${total_wrc:.4f}")
print(f"   TOTAL:            ${total_cost:.4f}")

# 3. Total runs
print()
print("=" * 70)
print("3. TOTAL RUNS (in-window row count)")
print("=" * 70)
print(f"   Total runs: {len(window_rows)}")

# 4. Per-skill aggregates
skill_data = defaultdict(lambda: {"runs": 0, "total_tokens": 0, "total_cost": 0.0})
for r in window_rows:
    s = r["skill"]
    toks = int(r["input_tokens"]) + int(r["output_tokens"]) + int(r["cache_read"]) + int(r["cache_creation"])
    skill_data[s]["runs"] += 1
    skill_data[s]["total_tokens"] += toks
    skill_data[s]["total_cost"] += r["_cost"]

print()
print("=" * 70)
print("4. PER-SKILL AGGREGATES (sorted by total cost desc)")
print("=" * 70)
print(f"{'Skill':<30} {'Runs':>5} {'Total Tokens':>14} {'Total Cost':>12} {'Avg/Run':>10}")
print("-" * 75)
for sk, d in sorted(skill_data.items(), key=lambda x: -x[1]["total_cost"]):
    avg = d["total_cost"] / d["runs"]
    print(f"{sk:<30} {d['runs']:>5} {d['total_tokens']:>14,} ${d['total_cost']:>11.4f} ${avg:>9.4f}")

# 5. Per-model aggregates
model_data = defaultdict(lambda: {"runs": 0, "total_tokens": 0, "total_cost": 0.0})
for r in window_rows:
    m = r["model"]
    toks = int(r["input_tokens"]) + int(r["output_tokens"]) + int(r["cache_read"]) + int(r["cache_creation"])
    model_data[m]["runs"] += 1
    model_data[m]["total_tokens"] += toks
    model_data[m]["total_cost"] += r["_cost"]

print()
print("=" * 70)
print("5. PER-MODEL AGGREGATES (in-window)")
print("=" * 70)
print(f"{'Model':<35} {'Runs':>5} {'Total Tokens':>14} {'Total Cost':>12}")
print("-" * 70)
for m, d in sorted(model_data.items(), key=lambda x: -x[1]["total_cost"]):
    print(f"{m:<35} {d['runs']:>5} {d['total_tokens']:>14,} ${d['total_cost']:>11.4f}")

# 6. Daily avg and projected monthly
daily_avg = total_cost / 7
monthly_proj = daily_avg * 30

print()
print("=" * 70)
print("6. DAILY AVG AND PROJECTED MONTHLY")
print("=" * 70)
print(f"   Daily avg (total / 7):    ${daily_avg:.4f}")
print(f"   Projected monthly (* 30): ${monthly_proj:.4f}")

# 7. Date range overall
all_dates = [r["_date"] for r in all_rows]
min_date = min(all_dates)
max_date = max(all_dates)
total_days_csv = (max_date - min_date).days + 1

print()
print("=" * 70)
print("7. DATE RANGE IN CSV")
print("=" * 70)
print(f"   Min date:   {min_date}")
print(f"   Max date:   {max_date}")
print(f"   Total days: {total_days_csv}")

# 8. Anomaly detection
sm_costs = defaultdict(list)
for r in window_rows:
    sm_costs[(r["skill"], r["model"])].append((r["_cost"], r))

print()
print("=" * 70)
print("8. ANOMALY DETECTION (>=3 runs, cost > mean+2sigma AND cost > $0.10)")
print("=" * 70)
anomalies_found = False
for (sk, mo), entries in sorted(sm_costs.items()):
    if len(entries) < 3:
        continue
    costs = [c for c, _ in entries]
    mean = sum(costs) / len(costs)
    variance = sum((c - mean) ** 2 for c in costs) / len(costs)
    sigma = math.sqrt(variance)
    threshold = mean + 2 * sigma
    for c, r in entries:
        if c > threshold and c > 0.10:
            anomalies_found = True
            print(f"  ANOMALY: skill={sk}, model={mo}")
            print(f"    date={r['date']}, run_cost=${c:.4f}, mean=${mean:.4f}, sigma=${sigma:.4f}")
            print(f"    input_tokens={r['input_tokens']}, output_tokens={r['output_tokens']}, cache_creation={r['cache_creation']}")
if not anomalies_found:
    print("  No anomalies detected.")

# 9. Model downgrade candidates (opus, median ratio < 0.3, avg cost > $0.25)
opus_skill = defaultdict(list)
for r in window_rows:
    if r["model"] == "claude-opus-4-7":
        opus_skill[r["skill"]].append(r)

def median(lst):
    s = sorted(lst)
    n = len(s)
    return s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2

print()
print("=" * 70)
print("9. MODEL DOWNGRADE CANDIDATES (opus, median ratio<0.3, avg cost>$0.25)")
print("=" * 70)
candidates_found = False
for sk, rows in sorted(opus_skill.items()):
    ratios = [int(r["output_tokens"]) / max(int(r["input_tokens"]), 1) for r in rows]
    med_ratio = median(ratios)
    avg_cost = sum(r["_cost"] for r in rows) / len(rows)
    if med_ratio < 0.3 and avg_cost > 0.25:
        candidates_found = True
        print(f"  skill={sk}, median_ratio={med_ratio:.4f}, avg_cost/run=${avg_cost:.4f}, runs={len(rows)}")
if not candidates_found:
    print("  No downgrade candidates found.")

print()
print("  (All opus skills -- median output/input ratio and avg cost/run:)")
print(f"  {'Skill':<30} {'Runs':>5} {'MedianRatio':>12} {'AvgCost':>10}")
print("  " + "-" * 62)
for sk, rows in sorted(opus_skill.items(), key=lambda x: -sum(r["_cost"] for r in x[1])/len(x[1])):
    ratios = [int(r["output_tokens"]) / max(int(r["input_tokens"]), 1) for r in rows]
    med_ratio = median(ratios)
    avg_cost = sum(r["_cost"] for r in rows) / len(rows)
    print(f"  {sk:<30} {len(rows):>5} {med_ratio:>12.4f} ${avg_cost:>9.4f}")

# 10. Cache underuse candidates
cache_skill = defaultdict(lambda: {"cache_read": 0, "input_tokens": 0, "total_cost": 0.0, "runs": 0})
for r in window_rows:
    sk = r["skill"]
    cache_skill[sk]["cache_read"]    += int(r["cache_read"])
    cache_skill[sk]["input_tokens"]  += int(r["input_tokens"])
    cache_skill[sk]["total_cost"]    += r["_cost"]
    cache_skill[sk]["runs"]          += 1

print()
print("=" * 70)
print("10. CACHE UNDERUSE CANDIDATES (cache_ratio<0.2 AND avg cost/run>$0.10)")
print("=" * 70)
print(f"  {'Skill':<30} {'CacheRatio':>11} {'AvgCost/Run':>12} {'Runs':>5}")
print("  " + "-" * 63)
underuse_found = False
for sk, d in sorted(cache_skill.items(), key=lambda x: -x[1]["total_cost"]/x[1]["runs"]):
    total_denom = d["cache_read"] + d["input_tokens"]
    ratio = d["cache_read"] / total_denom if total_denom > 0 else 0.0
    avg_cost = d["total_cost"] / d["runs"]
    if ratio < 0.2 and avg_cost > 0.10:
        underuse_found = True
        print(f"  {sk:<30} {ratio:>11.4f} ${avg_cost:>11.4f} {d['runs']:>5}")
if not underuse_found:
    print("  No cache underuse candidates found.")

print()
print("  (All skills -- cache ratio and avg cost for full picture:)")
print(f"  {'Skill':<30} {'CacheRatio':>11} {'AvgCost/Run':>12} {'Runs':>5} {'Flag'}")
print("  " + "-" * 70)
for sk, d in sorted(cache_skill.items(), key=lambda x: x[1]["cache_read"]/(x[1]["cache_read"]+x[1]["input_tokens"]) if (x[1]["cache_read"]+x[1]["input_tokens"])>0 else 0):
    total_denom = d["cache_read"] + d["input_tokens"]
    ratio = d["cache_read"] / total_denom if total_denom > 0 else 0.0
    avg_cost = d["total_cost"] / d["runs"]
    flag = " << UNDERUSE" if (ratio < 0.2 and avg_cost > 0.10) else ""
    print(f"  {sk:<30} {ratio:>11.4f} ${avg_cost:>11.4f} {d['runs']:>5}{flag}")

print()
print("=" * 70)
print("DONE")
print("=" * 70)
