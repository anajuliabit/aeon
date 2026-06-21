import json
import datetime

# CoinGecko data
prices = [
    [1781913600000, 63513.65867862926],
    [1782000000000, 64240.23278038838],
    [1782047020000, 64073.30006667486]
]

# Current state
state = {
    "updatedAt": "2026-06-20T12:48:00Z",
    "lastSpot": 63568.90,
    "lastDailyClose": 63513.66,
    "lastDailyCloseDate": "2026-06-19",
    "inLeverageReviewBand": False,
    "breakdownAlertedForClose": None,
    "reclaim63500Alerted": True,
    "reclaim65900Alerted": True
}

# Current values
spot = prices[-1][1]  # 64073.30
previous_close = prices[-2][1]  # 64240.23

# Timestamp for previous close
prev_close_timestamp = prices[-2][0]  # 1782000000000 ms
# Convert to date: timestamp is midnight UTC of day D, representing close of day D-1
# So close date = D-1
dt = datetime.datetime.fromtimestamp(prev_close_timestamp / 1000, datetime.timezone.utc)
close_date = (dt - datetime.timedelta(days=1)).strftime('%Y-%m-%d')
print(f"Spot: ${spot:.2f}")
print(f"Previous UTC daily close: ${previous_close:.2f} (date: {close_date})")

# Leverage review trigger
alerts = []
inLeverageReviewBand = spot <= 45000
if spot <= 45000:
    if 40000 <= spot <= 45000:
        alerts.append("🚨 Leverage-review trigger ($45k) — HF ≈ 1.48–1.66")
    else:
        alerts.append("🚨 Leverage-review trigger ($45k) — BELOW review band, HF worse than ~1.48 — urgent")

# Breakdown alert
breakdown_alert = None
if previous_close < 60500:
    if state["breakdownAlertedForClose"] != close_date:
        breakdown_alert = f"⚠️ Daily close ${previous_close:.2f} < $60,500 — downtrend continuation signal"
        alerts.append(breakdown_alert)
        breakdown_alerted_for_close = close_date
    else:
        breakdown_alerted_for_close = state["breakdownAlertedForClose"]
else:
    breakdown_alerted_for_close = None

# Reclaim 63,500
reclaim63500Alerted = state["reclaim63500Alerted"]
if spot >= 63500 and not reclaim63500Alerted:
    alerts.append("✅ Spot reclaims $63,500 — first stabilization signal")
    reclaim63500Alerted = True
elif spot < 60500:
    # Re-arm when spot drops below breakdown level
    reclaim63500Alerted = False

# Reclaim 65,900
reclaim65900Alerted = state["reclaim65900Alerted"]
if spot >= 65900 and not reclaim65900Alerted:
    alerts.append("✅ Spot reclaims $65,900 — stabilization confirmed")
    reclaim65900Alerted = True
elif spot < 60500:
    # Re-arm when spot drops below breakdown level
    reclaim65900Alerted = False

print("\nAlerts:")
for alert in alerts:
    print(f"- {alert}")

print(f"\nNew state:")
print(f"inLeverageReviewBand: {inLeverageReviewBand}")
print(f"breakdownAlertedForClose: {breakdown_alerted_for_close}")
print(f"reclaim63500Alerted: {reclaim63500Alerted}")
print(f"reclaim65900Alerted: {reclaim65900Alerted}")

# Notification message
if alerts:
    notification = f"₿ BTC levels: spot ${spot:,.0f}k. {' '.join(alerts)} Leveraged cbBTC position: review trigger at ≤$45k (HF ~1.48–1.66 in the 40–45k band). Not financial advice."
    print(f"\nNotification:\n{notification}")
else:
    print("\nNo alerts fired.")
