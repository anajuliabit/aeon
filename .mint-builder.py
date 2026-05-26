import hashlib, re, json, os

strategy = (
    "ETH/BTC daily statistical-arbitrage pairs trade on perpetual futures. "
    "Refit hedge ratio beta via OLS regression of log(ETH) on log(BTC) over trailing 60 daily bars; "
    "require Engle-Granger ADF p<0.05 before opening any new position. "
    "Spread s_t = log(ETH_t) - beta*log(BTC_t); compute rolling 30-day z-score. "
    "Entry: cross of z above +2.0 -> short the spread (short 1 unit ETH perp, long beta units BTC perp); "
    "cross of z below -2.0 -> long the spread (long 1 unit ETH perp, short beta units BTC perp). "
    "Profit exit when |z| <= 0.25. Hard stop when |z| >= 3.5. "
    "Weekly re-run ADF cointegration test; exit immediately if p > 0.10. "
    "Time stop: close after 20 trading days. "
    "Risk 1 percent of account equity per trade sized from 30-day spread sigma; cap at one concurrent pair position."
)

normalized = re.sub(r"\s+", " ", strategy).strip().lower()
datanet_id = "9"
h = hashlib.sha256((datanet_id + ":" + normalized).encode("utf-8")).hexdigest()
print("normalized:", normalized)
print("full_hash:", h)
print("first16:", h[:16])

os.makedirs(".pending-reppo", exist_ok=True)

intent = {
    "cmd": "mint-pod",
    "datanet": datanet_id,
    "idempotency_key": h,
    "strategy_summary": (
        "ETH/BTC daily stat-arb pairs trade on perps: OLS log-log hedge ratio over 60d, "
        "ADF p<0.05 gate, 30d z-score entries at |z|>=2.0 (short spread when z>+2, long when z<-2), "
        "profit |z|<=0.25, hard stop |z|>=3.5, weekly ADF p>0.10 cointegration stop, "
        "20-day time stop, 1 percent equity risk per trade, 1 concurrent pair. "
        "Source: https://blog.amberdata.io/crypto-pairs-trading-why-cointegration-beats-correlation"
    ),
}

path = ".pending-reppo/mint-" + h[:16] + ".json"
with open(path, "w") as f:
    json.dump(intent, f, indent=2)
print("wrote", path)
