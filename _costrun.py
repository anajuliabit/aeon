import csv, statistics
from datetime import date, timedelta
from collections import defaultdict
TODAY=date(2026,6,15); N=7
CUTOFF=TODAY-timedelta(days=N); PRIOR_CUTOFF=TODAY-timedelta(days=2*N)
PRICING={"claude-opus-4-7":(15.0,75.0,1.5,18.75),"claude-sonnet-4-6":(3.0,15.0,0.3,3.75),"claude-haiku-4-5-20251001":(0.8,4.0,0.08,1.0)}
OPUS=PRICING["claude-opus-4-7"]
rows=[];malformed=0;unknown=defaultdict(int)
for row in csv.DictReader(open("memory/token-usage.csv")):
    try:
        d=date.fromisoformat(row["date"].strip());it=int(row["input_tokens"]);ot=int(row["output_tokens"]);cr=int(row["cache_read"]);cc=int(row["cache_creation"]);sk=row["skill"].strip();m=row["model"].strip()
    except Exception: malformed+=1;continue
    rows.append(dict(date=d,skill=sk,model=m,it=it,ot=ot,cr=cr,cc=cc))
def cost(r):
    rt=PRICING.get(r["model"])
    if rt is None: unknown[r["model"]]+=r["it"]+r["ot"]+r["cr"]+r["cc"];rt=OPUS
    ic=r["it"]/1e6*rt[0];oc=r["ot"]/1e6*rt[1];crc=r["cr"]/1e6*rt[2];cwc=r["cc"]/1e6*rt[3]
    return ic,oc,crc,cwc,ic+oc+crc+cwc
for r in rows:
    ic,oc,crc,cwc,rc=cost(r);r.update(ic=ic,oc=oc,crc=crc,cwc=cwc,rc=rc)
inw=[r for r in rows if r["date"]>=CUTOFF]
prw=[r for r in rows if PRIOR_CUTOFF<=r["date"]<CUTOFF]
has_prior=min(r["date"] for r in rows)<=PRIOR_CUTOFF
print("window",CUTOFF,"..",TODAY,"rows_total",len(rows),"malformed",malformed,"inwindow",len(inw),"prior",len(prw),"has_prior",has_prior)
total=sum(r["rc"] for r in inw);tin=sum(r["ic"] for r in inw);tout=sum(r["oc"] for r in inw);tcr=sum(r["crc"] for r in inw);tcw=sum(r["cwc"] for r in inw)
print("TOTAL %.4f runs %d | in %.4f out %.4f cr %.4f cw %.4f"%(total,len(inw),tin,tout,tcr,tcw))
sa=defaultdict(lambda:[0,0,0.0])
for r in inw:
    a=sa[r["skill"]];a[0]+=1;a[1]+=r["it"]+r["ot"]+r["cr"]+r["cc"];a[2]+=r["rc"]
print("TOPSKILLS")
for sk,(rn,tk,c) in sorted(sa.items(),key=lambda x:-x[1][2])[:10]:
    print("  %-24s runs %3d tok %10d $%.4f avg $%.4f"%(sk,rn,tk,c,c/rn))
ma=defaultdict(lambda:[0,0,0.0])
for r in inw:
    a=ma[r["model"]];a[0]+=1;a[1]+=r["it"]+r["ot"]+r["cr"]+r["cc"];a[2]+=r["rc"]
print("MODELS")
for m,(rn,tk,c) in sorted(ma.items(),key=lambda x:-x[1][2]):
    print("  %-24s runs %3d tok %11d $%.4f"%(m,rn,tk,c))
pt=sum(r["rc"] for r in prw)
if has_prior and pt>0: print("WoW this %.4f prior %.4f delta %.1f%%"%(total,pt,(total-pt)/pt*100))
else: print("WoW no baseline prior %.4f"%pt)
print("ANOMALIES")
pr=defaultdict(list)
for r in inw: pr[(r["skill"],r["model"])].append(r)
anom=[]
for (sk,m),rs in pr.items():
    if len(rs)>=3:
        cs=[x["rc"] for x in rs];mu=statistics.mean(cs);sd=statistics.pstdev(cs)
        for x in rs:
            if x["rc"]>mu+2*sd and x["rc"]>0.10: anom.append((sk,m,x,mu,sd))
csk=defaultdict(float);psk=defaultdict(float)
for r in inw: csk[r["skill"]]+=r["rc"]
for r in prw: psk[r["skill"]]+=r["rc"]
spikes=[]
if has_prior:
    for sk,c in csk.items():
        p=psk.get(sk,0)
        if p>=0.25 and c>=2*p: spikes.append((sk,c,p))
for sk,m,x,mu,sd in anom: print("  ANOM %s/%s %s $%.4f mu $%.4f sd $%.4f in %d out %d cw %d cr %d"%(sk,m,x["date"],x["rc"],mu,sd,x["it"],x["ot"],x["cc"],x["cr"]))
for sk,c,p in spikes: print("  SPIKE %s cur $%.4f prior $%.4f %.1fx"%(sk,c,p,c/p))
if not anom and not spikes: print("  none")
daily=total/N;proj=daily*30
print("BURN daily %.4f monthly %.4f %s"%(daily,proj,"WARN" if proj>50 else ""))
print("OPT")
SON=PRICING["claude-sonnet-4-6"]
for sk in csk:
    rs=[r for r in inw if r["skill"]==sk and r["model"]=="claude-opus-4-7"]
    if not rs: continue
    ratios=[r["ot"]/r["it"] if r["it"]>0 else 99 for r in rs];med=statistics.median(ratios)
    ac=sum(r["rc"] for r in rs)/len(rs);tc=sum(r["rc"] for r in rs)
    if med<0.3 and ac>0.25:
        son=sum(r["it"]/1e6*SON[0]+r["ot"]/1e6*SON[1]+r["cr"]/1e6*SON[2]+r["cc"]/1e6*SON[3] for r in rs)
        print("  DOWNGRADE %s opus_avg $%.4f med_ratio %.3f cost $%.4f sonnet $%.4f sav $%.4f"%(sk,ac,med,tc,son,tc-son))
for sk in csk:
    rs=[r for r in inw if r["skill"]==sk];tcrr=sum(r["cr"] for r in rs);tii=sum(r["it"] for r in rs)
    if tcrr+tii==0: continue
    rt=tcrr/(tcrr+tii);ac=sum(r["rc"] for r in rs)/len(rs)
    if rt<0.2 and ac>0.10: print("  CACHE %s ratio %.3f avg $%.4f runs %d"%(sk,rt,ac,len(rs)))
for sk in csk:
    rs=[r for r in inw if r["skill"]==sk]
    if len(rs)>10:
        ac=sum(r["rc"] for r in rs)/len(rs)
        if ac<0.01: print("  LONGTAIL %s runs %d avg $%.4f"%(sk,len(rs),ac))
print("UNKNOWN",dict(unknown) if unknown else "none")
print("PRIOR_TOTAL %.4f"%pt)
