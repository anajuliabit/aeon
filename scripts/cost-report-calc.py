import csv
import math
import sys
import os
from collections import defaultdict
from datetime import date

TODAY = date(2026, 6, 1)
N = 7
CUTOFF = date(2026, 5, 25)

RATES = {
    "claude-opus-4-7": {"input": 15.00, "output": 75.00, "cache_read": 1.50, "cache_write": 18.75},
    "claude-sonnet-4-6": {"input": 3.00, "output": 15.00, "cache_read": 0.30, "cache_write": 3.75},
    "claude-haiku-4-5-20251001": {"input": 0.80, "output": 4.00, "cache_read": 0.08, "cache_write": 1.00},
}

rows = []
malformed = 0
unknown_models = defaultdict(lambda: {"tokens": 0, "count": 0})

with open("memory/token-usage.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            d = date.fromisoformat(row["date"])
            in_window = d >= CUTOFF
            row["_date"] = d
            row["_in_window"] = in_window
            row["input_tokens"] = int(row["input_tokens"])
            row["output_tokens"] = int(row["output_tokens"])
            row["cache_read"] = int(row["cache_read"])
            row["cache_creation"] = int(row["cache_creation"])

            model = row["model"]
            if model in RATES:
                r = RATES[model]
            else:
                r = RATES["claude-opus-4-7"]
                if in_window:
                    unknown_models[model]["tokens"] += row["input_tokens"] + row["output_tokens"]
                    unknown_models[model]["count"] += 1

            row["_rates"] = r
            ic = row["input_tokens"] / 1e6 * r["input"]
            oc = row["output_tokens"] / 1e6 * r["output"]
            crc = row["cache_read"] / 1e6 * r["cache_read"]
            cwc = row["cache_creation"] / 1e6 * r["cache_write"]
            row["_cost"] = ic + oc + crc + cwc
            row["_cost_input"] = ic
            row["_cost_output"] = oc
            row["_cost_cache_read"] = crc
            row["_cost_cache_write"] = cwc
            rows.append(row)
        except Exception as e:
            malformed += 1

in_rows = [r for r in rows if r["_in_window"]]
print("IN_WINDOW_ROWS=" + str(len(in_rows)))
print("MALFORMED=" + str(malformed))

total_cost = sum(r["_cost"] for r in in_rows)
total_input_cost = sum(r["_cost_input"] for r in in_rows)
total_output_cost = sum(r["_cost_output"] for r in in_rows)
total_cr_cost = sum(r["_cost_cache_read"] for r in in_rows)
total_cw_cost = sum(r["_cost_cache_write"] for r in in_rows)

print("TOTAL_COST=" + str(round(total_cost, 4)))
print("COST_INPUT=" + str(round(total_input_cost, 4)))
print("COST_OUTPUT=" + str(round(total_output_cost, 4)))
print("COST_CACHE_READ=" + str(round(total_cr_cost, 4)))
print("COST_CACHE_WRITE=" + str(round(total_cw_cost, 4)))
print("TOTAL_RUNS=" + str(len(in_rows)))

skill_data = defaultdict(lambda: {"cost": 0.0, "runs": 0, "tokens": 0})
for r in in_rows:
    sk = r["skill"]
    skill_data[sk]["cost"] += r["_cost"]
    skill_data[sk]["runs"] += 1
    skill_data[sk]["tokens"] += r["input_tokens"] + r["output_tokens"] + r["cache_read"] + r["cache_creation"]

print("\nTOP_SKILLS:")
sorted_skills = sorted(skill_data.items(), key=lambda x: -x[1]["cost"])
for skill, d in sorted_skills[:10]:
    avg = d["cost"] / d["runs"]
    print("  SKILL|" + skill + "|" + str(d["runs"]) + "|" + str(d["tokens"]) + "|" + str(round(d["cost"], 4)) + "|" + str(round(avg, 4)))

model_data = defaultdict(lambda: {"cost": 0.0, "runs": 0, "tokens": 0})
for r in in_rows:
    m = r["model"]
    model_data[m]["cost"] += r["_cost"]
    model_data[m]["runs"] += 1
    model_data[m]["tokens"] += r["input_tokens"] + r["output_tokens"] + r["cache_read"] + r["cache_creation"]

print("\nPER_MODEL:")
for model, d in sorted(model_data.items(), key=lambda x: -x[1]["cost"]):
    print("  MODEL|" + model + "|" + str(d["runs"]) + "|" + str(d["tokens"]) + "|" + str(round(d["cost"], 4)))

daily_avg = total_cost / N
projected_monthly = daily_avg * 30
print("\nDAILY_AVG=" + str(round(daily_avg, 4)))
print("PROJECTED_MONTHLY=" + str(round(projected_monthly, 2)))

all_dates = sorted(set(r["_date"] for r in rows))
print("DATE_RANGE=" + str(all_dates[0]) + " to " + str(all_dates[-1]) + " (" + str(len(all_dates)) + " days)")
print("WOW_POSSIBLE=" + str(len(all_dates) >= 14))

# Anomaly detection: per (skill, model) pairs with >= 3 runs
print("\nANOMALY_DETECTION:")
sm_rows = defaultdict(list)
for r in in_rows:
    key = (r["skill"], r["model"])
    sm_rows[key].append(r)

anomalies = []
for (skill, model), rlist in sm_rows.items():
    if len(rlist) < 3:
        continue
    costs = [r["_cost"] for r in rlist]
    mu = sum(costs) / len(costs)
    variance = sum((c - mu) ** 2 for c in costs) / len(costs)
    sigma = math.sqrt(variance)
    for r in rlist:
        if r["_cost"] > mu + 2 * sigma and r["_cost"] > 0.10:
            anomalies.append({
                "skill": skill,
                "model": model,
                "date": str(r["_date"]),
                "cost": round(r["_cost"], 4),
                "mu": round(mu, 4),
                "sigma": round(sigma, 4),
                "input_tokens": r["input_tokens"],
                "output_tokens": r["output_tokens"],
                "cache_write": r["cache_creation"],
            })

if anomalies:
    for a in anomalies:
        print("  ANOMALY|" + a["skill"] + "|" + a["model"] + "|" + a["date"] + "|" + str(a["cost"]) +
              "|mu=" + str(a["mu"]) + " sigma=" + str(a["sigma"]) +
              "|in=" + str(a["input_tokens"]) + "/out=" + str(a["output_tokens"]) + "/cw=" + str(a["cache_write"]))
else:
    print("  NONE")

# Optimization: model downgrade candidates (opus, output/input ratio < 0.3, avg cost > 0.25)
print("\nOPTIMIZATION:")
for skill, d in sorted_skills:
    skill_rows_in = [r for r in in_rows if r["skill"] == skill and r["model"] == "claude-opus-4-7"]
    if len(skill_rows_in) == 0:
        continue
    avg_cost = d["cost"] / d["runs"]
    ratios = [r["output_tokens"] / max(r["input_tokens"], 1) for r in skill_rows_in]
    median_ratio = sorted(ratios)[len(ratios) // 2]
    if median_ratio < 0.3 and avg_cost > 0.25:
        opus_mix = 15.0 * 0.5 + 75.0 * 0.3 + 1.50 * 0.15 + 18.75 * 0.05
        sonnet_mix = 3.0 * 0.5 + 15.0 * 0.3 + 0.30 * 0.15 + 3.75 * 0.05
        savings_pct = 1 - sonnet_mix / opus_mix
        weekly_savings = d["cost"] * savings_pct
        print("  DOWNGRADE|" + skill + "|ratio=" + str(round(median_ratio, 3)) + "|avg_cost=$" + str(round(avg_cost, 4)) + "|weekly_savings=$" + str(round(weekly_savings, 2)))

# Cache underuse
for skill, d in sorted_skills:
    skill_rows_in = [r for r in in_rows if r["skill"] == skill]
    if len(skill_rows_in) == 0:
        continue
    avg_cost = d["cost"] / d["runs"]
    if avg_cost < 0.10:
        continue
    total_cache_read = sum(r["cache_read"] for r in skill_rows_in)
    total_input = sum(r["input_tokens"] for r in skill_rows_in)
    denom = total_cache_read + total_input
    if denom > 0 and total_cache_read / denom < 0.2:
        ratio = total_cache_read / denom
        print("  CACHE_UNDERUSE|" + skill + "|cache_ratio=" + str(round(ratio, 3)) + "|avg_cost=$" + str(round(avg_cost, 4)))

print("\nUNKNOWN_MODELS:")
if unknown_models:
    for m, d in unknown_models.items():
        print("  UNKNOWN|" + m + "|tokens=" + str(d["tokens"]) + "|rows=" + str(d["count"]))
else:
    print("  NONE")
