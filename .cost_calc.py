import csv, math, sys
from collections import defaultdict

TODAY = "2026-08-11"
N = 7

CUTOFF = "2026-08-04"
PRIOR_CUTOFF = "2026-07-28"

RATES = {
    "claude-opus-4-7":           {"input": 15.00, "output": 75.00, "cache_read": 1.50, "cache_write": 18.75},
    "claude-sonnet-4-6":         {"input": 3.00,  "output": 15.00, "cache_read": 0.30, "cache_write": 3.75},
    "claude-haiku-4-5-20251001": {"input": 0.80,  "output": 4.00,  "cache_read": 0.08, "cache_write": 1.00},
}

csv_path = "memory/token-usage.csv"

rows_current = []
rows_prior = []
malformed = 0
unknown_models = set()

with open(csv_path) as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            date = row["date"].strip()
            skill = row["skill"].strip()
            model = row["model"].strip()
            inp = int(row["input_tokens"])
            out = int(row["output_tokens"])
            cr = int(row["cache_read"])
            cw = int(row["cache_creation"])
        except Exception:
            malformed += 1
            continue

        if model not in RATES:
            unknown_models.add(model)
            rates = RATES["claude-opus-4-7"]
        else:
            rates = RATES[model]

        cost = (inp / 1e6 * rates["input"] +
                out / 1e6 * rates["output"] +
                cr  / 1e6 * rates["cache_read"] +
                cw  / 1e6 * rates["cache_write"])

        record = {"date": date, "skill": skill, "model": model,
                  "inp": inp, "out": out, "cr": cr, "cw": cw, "cost": cost}

        if date >= CUTOFF:
            rows_current.append(record)
        elif date >= PRIOR_CUTOFF:
            rows_prior.append(record)

def summarize(rows):
    total_cost = 0
    input_cost = output_cost = cr_cost = cw_cost = 0
    for r in rows:
        m = r["model"] if r["model"] in RATES else "claude-opus-4-7"
        rates = RATES[m]
        ic = r["inp"] / 1e6 * rates["input"]
        oc = r["out"] / 1e6 * rates["output"]
        crc = r["cr"] / 1e6 * rates["cache_read"]
        cwc = r["cw"] / 1e6 * rates["cache_write"]
        total_cost += r["cost"]
        input_cost += ic; output_cost += oc; cr_cost += crc; cw_cost += cwc
    return total_cost, input_cost, output_cost, cr_cost, cw_cost

total, ic, oc, crc, cwc = summarize(rows_current)
prior_total, *_ = summarize(rows_prior)

print("CURRENT_TOTAL=" + str(round(total, 4)))
print("INPUT_COST=" + str(round(ic, 4)))
print("OUTPUT_COST=" + str(round(oc, 4)))
print("CR_COST=" + str(round(crc, 4)))
print("CW_COST=" + str(round(cwc, 4)))
print("PRIOR_TOTAL=" + str(round(prior_total, 4)))
if prior_total > 0:
    wow = (total - prior_total) / prior_total * 100
    print("WOW=" + str(round(wow, 1)))
else:
    print("WOW=none")

skill_data = defaultdict(lambda: {"runs": 0, "total_tokens": 0, "cost": 0.0, "costs": []})
for r in rows_current:
    s = r["skill"]
    skill_data[s]["runs"] += 1
    skill_data[s]["total_tokens"] += r["inp"] + r["out"] + r["cr"] + r["cw"]
    skill_data[s]["cost"] += r["cost"]
    skill_data[s]["costs"].append(r["cost"])

print("TOTAL_RUNS=" + str(len(rows_current)))

top10 = sorted(skill_data.items(), key=lambda x: x[1]["cost"], reverse=True)[:10]
print("TOP10_START")
for skill, d in top10:
    avg = d["cost"] / d["runs"] if d["runs"] else 0
    print(skill + "|" + str(d["runs"]) + "|" + str(d["total_tokens"]) + "|" + str(round(d["cost"], 4)) + "|" + str(round(avg, 4)))
print("TOP10_END")

model_data = defaultdict(lambda: {"runs": 0, "total_tokens": 0, "cost": 0.0})
for r in rows_current:
    m = r["model"]
    model_data[m]["runs"] += 1
    model_data[m]["total_tokens"] += r["inp"] + r["out"] + r["cr"] + r["cw"]
    model_data[m]["cost"] += r["cost"]

print("MODELS_START")
for model, d in sorted(model_data.items(), key=lambda x: x[1]["cost"], reverse=True):
    print(model + "|" + str(d["runs"]) + "|" + str(d["total_tokens"]) + "|" + str(round(d["cost"], 4)))
print("MODELS_END")

sm_groups = defaultdict(list)
for r in rows_current:
    sm_groups[(r["skill"], r["model"])].append(r)

anomalies = []
for (skill, model), group in sm_groups.items():
    if len(group) < 3:
        continue
    costs = [r["cost"] for r in group]
    mu = sum(costs) / len(costs)
    sigma = math.sqrt(sum((c - mu)**2 for c in costs) / len(costs))
    for r in group:
        if r["cost"] > mu + 2*sigma and r["cost"] > 0.10:
            anomalies.append({
                "skill": skill, "model": model, "date": r["date"],
                "cost": r["cost"], "mu": mu, "sigma": sigma,
                "inp": r["inp"], "out": r["out"], "cw": r["cw"]
            })

prior_skill_cost = defaultdict(float)
for r in rows_prior:
    prior_skill_cost[r["skill"]] += r["cost"]

print("ANOMALIES_START")
for a in anomalies:
    print(a["skill"] + "|" + a["model"] + "|" + a["date"] + "|" + str(round(a["cost"], 4)) + "|" + str(round(a["mu"], 4)) + "|" + str(round(a["sigma"], 4)) + "|" + str(a["inp"]) + "|" + str(a["out"]) + "|" + str(a["cw"]))
print("ANOMALIES_END")

print("SKILL_DOUBLES_START")
for skill, d in skill_data.items():
    prior = prior_skill_cost.get(skill, 0)
    if prior >= 0.25 and d["cost"] >= 2 * prior:
        print(skill + "|" + str(round(d["cost"], 4)) + "|" + str(round(prior, 4)))
print("SKILL_DOUBLES_END")

daily_avg = total / N
monthly_proj = daily_avg * 30
print("DAILY_AVG=" + str(round(daily_avg, 4)))
print("MONTHLY_PROJ=" + str(round(monthly_proj, 4)))

print("OPT_START")
for skill, d in skill_data.items():
    skill_rows = [r for r in rows_current if r["skill"] == skill and r["model"] == "claude-opus-4-7"]
    if not skill_rows:
        continue
    avg_cost = d["cost"] / d["runs"]
    if avg_cost <= 0.25:
        continue
    ratios = []
    for r in skill_rows:
        if r["inp"] > 0:
            ratios.append(r["out"] / r["inp"])
    if ratios:
        median_ratio = sorted(ratios)[len(ratios)//2]
        if median_ratio < 0.3:
            savings_frac = 1 - 18 / 90
            savings = d["cost"] * savings_frac
            print("DOWNGRADE|" + skill + "|" + str(round(avg_cost, 4)) + "|" + str(round(median_ratio, 3)) + "|" + str(round(savings, 4)))

for skill, d in skill_data.items():
    skill_rows = [r for r in rows_current if r["skill"] == skill]
    if not skill_rows:
        continue
    avg_cost = d["cost"] / d["runs"]
    if avg_cost <= 0.10:
        continue
    total_cr = sum(r["cr"] for r in skill_rows)
    total_inp = sum(r["inp"] for r in skill_rows)
    if total_cr + total_inp == 0:
        continue
    ratio = total_cr / (total_cr + total_inp)
    if ratio < 0.2:
        print("CACHE|" + skill + "|" + str(round(ratio, 3)) + "|" + str(round(avg_cost, 4)))
print("OPT_END")

print("UNKNOWN_MODELS=" + (",".join(unknown_models) if unknown_models else "none"))
print("MALFORMED=" + str(malformed))
