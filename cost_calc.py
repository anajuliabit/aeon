import csv, io, math
from datetime import date, timedelta

TODAY = date(2026, 6, 24)
N = 7
CUTOFF = TODAY - timedelta(days=N)
PRIOR_CUTOFF = TODAY - timedelta(days=2*N)

RATES = {
    'claude-opus-4-7':          {'input':15.00,'output':75.00,'cache_read':1.50,'cache_write':18.75},
    'claude-sonnet-4-6':        {'input':3.00, 'output':15.00,'cache_read':0.30,'cache_write':3.75},
    'claude-haiku-4-5-20251001':{'input':0.80, 'output':4.00, 'cache_read':0.08,'cache_write':1.00},
}

data = open('/home/runner/work/aeon/aeon/memory/token-usage.csv').read()
reader = csv.DictReader(io.StringIO(data))

current_rows = []
prior_rows = []
malformed = 0
unknown_models = {}

for row in reader:
    try:
        d = date.fromisoformat(row['date'].strip())
        skill = row['skill'].strip()
        model = row['model'].strip()
        inp = int(row['input_tokens'])
        out = int(row['output_tokens'])
        cr  = int(row['cache_read'])
        cw  = int(row['cache_creation'])
    except Exception:
        malformed += 1
        continue

    if model not in RATES:
        unknown_models[model] = unknown_models.get(model, 0) + inp + out
        rates = RATES['claude-opus-4-7']
    else:
        rates = RATES[model]

    cost = (inp/1e6*rates['input'] + out/1e6*rates['output'] +
            cr/1e6*rates['cache_read'] + cw/1e6*rates['cache_write'])

    r = dict(date=d, skill=skill, model=model,
             input=inp, output=out, cache_read=cr, cache_write=cw, cost=cost)

    if d >= CUTOFF:
        current_rows.append(r)
    elif d >= PRIOR_CUTOFF:
        prior_rows.append(r)

print(f"Current window rows: {len(current_rows)}")
print(f"Prior window rows: {len(prior_rows)}")
print(f"Malformed: {malformed}")
print(f"Unknown models: {unknown_models}")

total_cost = sum(r['cost'] for r in current_rows)

def row_breakdown(rows):
    ti = to = tcr = tcw = 0.0
    for r in rows:
        rates = RATES.get(r['model'], RATES['claude-opus-4-7'])
        ti  += r['input']/1e6*rates['input']
        to  += r['output']/1e6*rates['output']
        tcr += r['cache_read']/1e6*rates['cache_read']
        tcw += r['cache_write']/1e6*rates['cache_write']
    return ti, to, tcr, tcw

ti, to, tcr, tcw = row_breakdown(current_rows)
total_runs = len(current_rows)

print(f"\nCURRENT {CUTOFF} to {TODAY}")
print(f"Total: ${total_cost:.4f}  runs={total_runs}")
print(f"  Input:${ti:.4f} Output:${to:.4f} CacheRead:${tcr:.4f} CacheWrite:${tcw:.4f}")

prior_cost = sum(r['cost'] for r in prior_rows)
print(f"\nPRIOR {PRIOR_CUTOFF} to {CUTOFF}: ${prior_cost:.4f}  runs={len(prior_rows)}")
if prior_cost > 0:
    wow = (total_cost - prior_cost) / prior_cost * 100
    print(f"WoW: {wow:+.1f}%")

# Per-skill
skill_data = {}
for r in current_rows:
    s = r['skill']
    if s not in skill_data:
        skill_data[s] = {'runs':0,'tokens':0,'cost':0.0,'costs':[],'rows':[]}
    skill_data[s]['runs'] += 1
    skill_data[s]['tokens'] += r['input']+r['output']+r['cache_read']+r['cache_write']
    skill_data[s]['cost'] += r['cost']
    skill_data[s]['costs'].append(r['cost'])
    skill_data[s]['rows'].append(r)

print("\nTOP 10 BY COST:")
top10 = sorted(skill_data.items(), key=lambda x: -x[1]['cost'])[:10]
for sk, v in top10:
    avg = v['cost']/v['runs'] if v['runs'] else 0
    print(f"  {sk}: runs={v['runs']} tok={v['tokens']:,} cost=${v['cost']:.4f} avg=${avg:.4f}")

model_data = {}
for r in current_rows:
    m = r['model']
    if m not in model_data:
        model_data[m] = {'runs':0,'tokens':0,'cost':0.0}
    model_data[m]['runs'] += 1
    model_data[m]['tokens'] += r['input']+r['output']+r['cache_read']+r['cache_write']
    model_data[m]['cost'] += r['cost']

print("\nPER MODEL:")
for m, v in sorted(model_data.items(), key=lambda x: -x[1]['cost']):
    print(f"  {m}: runs={v['runs']} tok={v['tokens']:,} cost=${v['cost']:.4f}")

# Anomaly detection
print("\nANOMALIES:")
sm_data = {}
for r in current_rows:
    key = (r['skill'], r['model'])
    if key not in sm_data:
        sm_data[key] = []
    sm_data[key].append(r)

anomaly_count = 0
for (sk, m), rows in sm_data.items():
    if len(rows) < 3:
        continue
    costs = [r['cost'] for r in rows]
    mu = sum(costs)/len(costs)
    variance = sum((c-mu)**2 for c in costs)/len(costs)
    sigma = math.sqrt(variance)
    for r in rows:
        if r['cost'] > mu + 2*sigma and r['cost'] > 0.10:
            anomaly_count += 1
            print(f"  {sk}/{m} {r['date']} cost=${r['cost']:.4f} mu=${mu:.4f} 2sig=${mu+2*sigma:.4f}")
            print(f"    inp={r['input']:,} out={r['output']:,} cw={r['cache_write']:,}")

if anomaly_count == 0:
    print("  None.")
print(f"Total anomalies: {anomaly_count}")

# WoW skill spikes
prior_skill = {}
for r in prior_rows:
    s = r['skill']
    if s not in prior_skill:
        prior_skill[s] = 0.0
    prior_skill[s] += r['cost']

print("\nSKILL WOW SPIKES (>=2x, prior>=$0.25):")
for sk, v in skill_data.items():
    if sk in prior_skill and prior_skill[sk] >= 0.25:
        ratio = v['cost'] / prior_skill[sk]
        if ratio >= 2.0:
            print(f"  {sk}: cur=${v['cost']:.4f} pri=${prior_skill[sk]:.4f} {ratio:.1f}x")

# Forecast
daily_avg = total_cost / N
monthly = daily_avg * 30
print(f"\nFORECAST: daily=${daily_avg:.4f} monthly=${monthly:.4f}")

# Optimization: model downgrade candidates
print("\nOPTIMIZATION CANDIDATES (downgrade):")
for sk, v in skill_data.items():
    rows = [r for r in current_rows if r['skill'] == sk and r['model'] == 'claude-opus-4-7']
    if not rows:
        continue
    avg_cost = v['cost'] / v['runs']
    if avg_cost <= 0.25:
        continue
    total_inp = sum(r['input'] for r in rows)
    total_out = sum(r['output'] for r in rows)
    if total_inp == 0:
        continue
    ratio = total_out / total_inp if total_inp > 0 else 999
    if ratio < 0.3:
        opus_inp_cost = total_inp/1e6*15.0
        opus_out_cost = total_out/1e6*75.0
        son_inp_cost = total_inp/1e6*3.0
        son_out_cost = total_out/1e6*15.0
        opus_total = opus_inp_cost + opus_out_cost
        son_total = son_inp_cost + son_out_cost
        if opus_total > 0:
            savings_pct = (opus_total - son_total) / opus_total
            est_weekly = v['cost'] * savings_pct
            print(f"  {sk}: avg_cost=${avg_cost:.4f} out/inp={ratio:.3f} est_savings=${est_weekly:.4f}/wk")

# Cache underuse check (direct: cache_read / (cache_read+input) < 0.2, avg cost > $0.10)
print("\nCACHE UNDERUSE:")
for sk, v in skill_data.items():
    total_inp = sum(r['input'] for r in v['rows'])
    total_cr = sum(r['cache_read'] for r in v['rows'])
    avg_cost = v['cost'] / v['runs']
    if avg_cost <= 0.10:
        continue
    denom = total_cr + total_inp
    if denom == 0:
        continue
    ratio = total_cr / denom
    if ratio < 0.2:
        print(f"  {sk}: cache_ratio={ratio:.3f} avg_cost=${avg_cost:.4f}")
