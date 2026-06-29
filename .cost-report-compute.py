import csv
from collections import defaultdict
import math
from datetime import date, timedelta

today_d = date(2026, 6, 29)
N = 7
cutoff_d = today_d - timedelta(days=N)       # 2026-06-22
prior_cutoff_d = today_d - timedelta(days=2*N)  # 2026-06-15

PRICING = {
    "claude-opus-4-7":           {"input": 15.00, "output": 75.00, "cache_read": 1.50,  "cache_write": 18.75},
    "claude-sonnet-4-6":         {"input":  3.00, "output": 15.00, "cache_read": 0.30,  "cache_write":  3.75},
    "claude-haiku-4-5-20251001": {"input":  0.80, "output":  4.00, "cache_read": 0.08,  "cache_write":  1.00},
}

def calc_cost(model, inp, out, cr, cw):
    rates = PRICING.get(model)
    is_unknown = False
    if rates is None:
        rates = PRICING["claude-opus-4-7"]
        is_unknown = True
    c = (inp * rates["input"] + out * rates["output"] + cr * rates["cache_read"] + cw * rates["cache_write"]) / 1e6
    return c, is_unknown

with open("memory/token-usage.csv", "r") as f:
    reader = csv.DictReader(f)
    rows = list(reader)

malformed = 0
unknown_models = defaultdict(lambda: {"inp": 0, "out": 0})
in_window = []
prior_window = []

for r in rows:
    try:
        d = date.fromisoformat(r["date"])
        inp = int(r["input_tokens"])
        out = int(r["output_tokens"])
        cr = int(r["cache_read"])
        cw = int(r["cache_creation"])
        model = r["model"]
        skill = r["skill"]
    except (ValueError, KeyError):
        malformed += 1
        continue

    cost, is_unknown = calc_cost(model, inp, out, cr, cw)
    if is_unknown:
        unknown_models[model]["inp"] += inp
        unknown_models[model]["out"] += out

    entry = {"date": d, "skill": skill, "model": model, "inp": inp, "out": out, "cr": cr, "cw": cw, "cost": cost}

    if d >= cutoff_d:
        in_window.append(entry)
    elif d >= prior_cutoff_d:
        prior_window.append(entry)

print("IN_WINDOW_ROWS=%d" % len(in_window))
print("PRIOR_WINDOW_ROWS=%d" % len(prior_window))
print("MALFORMED=%d" % malformed)

total_cost = sum(e["cost"] for e in in_window)
prior_cost = sum(e["cost"] for e in prior_window)
print("TOTAL_COST=%.6f" % total_cost)
print("PRIOR_COST=%.6f" % prior_cost)

def get_rates(model):
    return PRICING.get(model, PRICING["claude-opus-4-7"])

total_inp_cost = sum(e["inp"] * get_rates(e["model"])["input"] / 1e6 for e in in_window)
total_out_cost = sum(e["out"] * get_rates(e["model"])["output"] / 1e6 for e in in_window)
total_cr_cost  = sum(e["cr"]  * get_rates(e["model"])["cache_read"] / 1e6 for e in in_window)
total_cw_cost  = sum(e["cw"]  * get_rates(e["model"])["cache_write"] / 1e6 for e in in_window)
print("COMP_INP=%.6f" % total_inp_cost)
print("COMP_OUT=%.6f" % total_out_cost)
print("COMP_CR=%.6f"  % total_cr_cost)
print("COMP_CW=%.6f"  % total_cw_cost)

skill_stats = defaultdict(lambda: {"runs": 0, "inp": 0, "out": 0, "cr": 0, "cw": 0, "cost": 0.0, "rows": []})
for e in in_window:
    s = e["skill"]
    skill_stats[s]["runs"] += 1
    skill_stats[s]["inp"] += e["inp"]
    skill_stats[s]["out"] += e["out"]
    skill_stats[s]["cr"]  += e["cr"]
    skill_stats[s]["cw"]  += e["cw"]
    skill_stats[s]["cost"] += e["cost"]
    skill_stats[s]["rows"].append(e)

top_skills = sorted(skill_stats.items(), key=lambda x: x[1]["cost"], reverse=True)[:10]
print("\nTOP10_SKILLS:")
for sk, st in top_skills:
    total_tok = st["inp"] + st["out"] + st["cr"] + st["cw"]
    avg = st["cost"] / st["runs"] if st["runs"] > 0 else 0
    print("  %-28s runs=%-3d tokens=%-12d cost=%.4f avg=%.4f" % (sk, st["runs"], total_tok, st["cost"], avg))

model_stats = defaultdict(lambda: {"runs": 0, "inp": 0, "out": 0, "cost": 0.0})
for e in in_window:
    m = e["model"]
    model_stats[m]["runs"] += 1
    model_stats[m]["inp"] += e["inp"]
    model_stats[m]["out"] += e["out"]
    model_stats[m]["cost"] += e["cost"]
print("\nMODEL_STATS:")
for m, st in sorted(model_stats.items()):
    total_tok = st["inp"] + st["out"]
    print("  %-35s runs=%-3d tokens=%-12d cost=%.4f" % (m, st["runs"], total_tok, st["cost"]))

if prior_cost > 0:
    delta_pct = (total_cost - prior_cost) / prior_cost * 100
    print("\nWOW_DELTA=%.1f" % delta_pct)
else:
    print("\nWOW_DELTA=NONE")

daily_avg = total_cost / N
projected_monthly = daily_avg * 30
print("DAILY_AVG=%.6f" % daily_avg)
print("PROJ_MONTHLY=%.6f" % projected_monthly)

print("\nANOMALIES:")
anomalies = []
for sk, st in skill_stats.items():
    models_used = set(e["model"] for e in st["rows"])
    for m_key in models_used:
        runs_pair = [e for e in st["rows"] if e["model"] == m_key]
        if len(runs_pair) < 3:
            continue
        costs = [e["cost"] for e in runs_pair]
        mu = sum(costs) / len(costs)
        variance = sum((c - mu)**2 for c in costs) / len(costs)
        sigma = math.sqrt(variance)
        for e in runs_pair:
            if e["cost"] > mu + 2*sigma and e["cost"] > 0.10:
                anomalies.append({
                    "skill": sk, "model": m_key, "date": e["date"],
                    "cost": e["cost"], "mu": mu, "sigma": sigma,
                    "inp": e["inp"], "out": e["out"], "cw": e["cw"]
                })
                print("  ANOMALY: skill=%s model=%s date=%s cost=%.4f mu=%.4f sigma=%.4f inp=%d out=%d cw=%d" % (
                    sk, m_key, e["date"], e["cost"], mu, sigma, e["inp"], e["out"], e["cw"]))
if not anomalies:
    print("  NONE")

print("\nSPIKE_SKILLS:")
prior_skill_cost = defaultdict(float)
for e in prior_window:
    prior_skill_cost[e["skill"]] += e["cost"]
spike_count = 0
for sk, st in skill_stats.items():
    pc = prior_skill_cost.get(sk, 0)
    if pc >= 0.25 and st["cost"] >= 2 * pc:
        print("  SPIKE: skill=%s cur=%.4f prior=%.4f ratio=%.1fx" % (sk, st["cost"], pc, st["cost"]/pc))
        spike_count += 1
if spike_count == 0:
    print("  NONE")

print("\nOPT_CANDIDATES:")
opt_count = 0
for sk, st in sorted(skill_stats.items(), key=lambda x: x[1]["cost"], reverse=True):
    opus_rows = [e for e in st["rows"] if e["model"] == "claude-opus-4-7"]
    if not opus_rows:
        continue
    avg_cost = sum(e["cost"] for e in opus_rows) / len(opus_rows)
    total_inp_sk = sum(e["inp"] for e in opus_rows)
    total_out_sk = sum(e["out"] for e in opus_rows)
    if total_inp_sk > 0 and (total_out_sk / total_inp_sk) < 0.3 and avg_cost > 0.25:
        total_cost_sk = sum(e["cost"] for e in opus_rows)
        sonnet_cost = sum((e["inp"]*3 + e["out"]*15 + e["cr"]*0.30 + e["cw"]*3.75)/1e6 for e in opus_rows)
        savings = total_cost_sk - sonnet_cost
        print("  DOWNGRADE: skill=%s ratio=%.3f avg_run=%.4f opus_cost=%.4f sonnet_cost=%.4f savings=%.4f" % (
            sk, total_out_sk/total_inp_sk, avg_cost, total_cost_sk, sonnet_cost, savings))
        opt_count += 1
        if opt_count >= 5:
            break

print("\nCACHE_UNDERUSE:")
cache_count = 0
for sk, st in sorted(skill_stats.items(), key=lambda x: x[1]["cost"], reverse=True):
    total_inp_sk = sum(e["inp"] for e in st["rows"])
    total_cr_sk  = sum(e["cr"] for e in st["rows"])
    avg_cost = st["cost"] / st["runs"]
    denom = total_cr_sk + total_inp_sk
    if denom > 0:
        ratio = total_cr_sk / denom
        if ratio < 0.2 and avg_cost > 0.10:
            print("  CACHE_LOW: skill=%s cr_ratio=%.3f avg_run=%.4f total_cost=%.4f" % (sk, ratio, avg_cost, st["cost"]))
            cache_count += 1
            if cache_count >= 5:
                break

print("\nUNKNOWN_MODELS:")
if unknown_models:
    for m, tok in unknown_models.items():
        print("  UNKNOWN: model=%s inp=%d out=%d" % (m, tok["inp"], tok["out"]))
else:
    print("  NONE")

print("\nTOTAL_RUNS=%d" % len(in_window))
