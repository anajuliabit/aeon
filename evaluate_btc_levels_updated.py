#!/usr/bin/env python3
"""
BTC Levels Monitor evaluation script
"""
import json
from datetime import datetime

# Actual CoinGecko response from fetch
data = {
    "prices": [
        [1781913600000, 63513.65867862926],
        [1782000000000, 64240.23278038838],
        [1782048955000, 63970.22412156303]
    ],
    "market_caps": [
        [1781913600000, 1268758066935.9958],
        [1782000000000, 1287768457406.0122],
        [1782048955000, 1283568594962.9963]
    ],
    "total_volumes": [
        [1781913600000, 23172898934.025856],
        [1782000000000, 17171401473.160103],
        [1782048955000, 17534135625.696228]
    ]
}

# Current spot and previous daily close
current_spot = data["prices"][-1][1]
prev_close_price = data["prices"][-2][1]
prev_close_timestamp = data["prices"][-2][0]

# Convert timestamp to date string
dt = datetime.fromtimestamp(prev_close_timestamp / 1000)
close_date_str = dt.strftime("%Y-%m-%d")

print(f"Current spot: ${current_spot:,.2f}")
print(f"Previous UTC daily close: ${prev_close_price:,.2f}")
print(f"Close date: {close_date_str}")

# Read current state
state_path = "memory/btc-levels-state.json"
try:
    with open(state_path, "r") as f:
        state = json.load(f)
    print("\nCurrent state loaded:")
    print(json.dumps(state, indent=2))
except FileNotFoundError:
    print("\nNo state file found, initializing default state")
    state = {
        "updatedAt": datetime.utcnow().isoformat() + "Z",
        "lastSpot": current_spot,
        "lastDailyClose": prev_close_price,
        "lastDailyCloseDate": close_date_str,
        "inLeverageReviewBand": False,
        "breakdownAlertedForClose": None,
        "reclaim63500Alerted": False,
        "reclaim65900Alerted": False
    }

# Initialize alerts
alerts = []
notification_parts = []

# Leverage-review trigger (spot ≤ 45000)
if current_spot <= 45000:
    state["inLeverageReviewBand"] = True
    if current_spot >= 40000:
        msg = f"🚨 BTC spot ${current_spot:,.0f}k ≤ $45,000 — leverage-review band $40,000–$45,000 (HF ≈ 1.48–1.66)"
    else:
        msg = f"🚨 BTC spot ${current_spot:,.0f}k BELOW $40,000 — HF worse than ~1.48 — urgent"
    alerts.append("leverage-review")
    notification_parts.append(msg)
    print(f"\n⛔ Leverage-review trigger: {msg.split('—')[1].strip()}")
else:
    state["inLeverageReviewBand"] = False

# Breakdown alert (daily close < 60500)
if prev_close_price < 60500:
    if state["breakdownAlertedForClose"] != close_date_str:
        msg = f"⚠️ Daily close ${prev_close_price:,.0f}k < $60,500 — downtrend continuation signal"
        alerts.append("breakdown")
        notification_parts.append(msg)
        state["breakdownAlertedForClose"] = close_date_str
        print(f"\n⚠️ Breakdown alert: {msg}")
    else:
        print(f"\nℹ️ Breakdown already alerted for close date {close_date_str}")
else:
    # Daily close ≥ 60500 clears the flag
    state["breakdownAlertedForClose"] = None
    print(f"\nℹ️ Daily close ${prev_close_price:,.0f}k ≥ $60,500")

# Reclaim $63,500
if current_spot >= 63500:
    if not state["reclaim63500Alerted"]:
        msg = f"✅ BTC spot ${current_spot:,.0f}k reclaimed $63,500 — first stabilization signal"
        alerts.append("reclaim-63500")
        notification_parts.append(msg)
        state["reclaim63500Alerted"] = True
        print(f"\n✅ Reclaim $63,500 alert")
    else:
        print(f"\nℹ️ Reclaim $63,500 already alerted (spot: ${current_spot:,.0f}k)")

    # Re-arm if spot falls below 60500 (full round-trip)
    if current_spot < 60500:
        state["reclaim63500Alerted"] = False
else:
    print(f"\nℹ️ Spot ${current_spot:,.0f}k < $63,500")
    if state["reclaim63500Alerted"] and current_spot < 60500:
        state["reclaim63500Alerted"] = False
        print("ℹ️ Reset reclaim-63500 flag (spot below $60,500)")

# Reclaim $65,900
if current_spot >= 65900:
    if not state["reclaim65900Alerted"]:
        msg = f"✅ BTC spot ${current_spot:,.0f}k reclaimed $65,900 — stabilization confirmed"
        alerts.append("reclaim-65900")
        notification_parts.append(msg)
        state["reclaim65900Alerted"] = True
        print(f"\n✅ Reclaim $65,900 alert")
    else:
        print(f"\nℹ️ Reclaim $65,900 already alerted (spot: ${current_spot:,.0f}k)")

    # Re-arm if spot falls below 60500 (full round-trip)
    if current_spot < 60500:
        state["reclaim65900Alerted"] = False
else:
    print(f"\nℹ️ Spot ${current_spot:,.0f}k < $65,900")
    if state["reclaim65900Alerted"] and current_spot < 60500:
        state["reclaim65900Alerted"] = False
        print("ℹ️ Reset reclaim-65900 flag (spot below $60,500)")

# Update state
state["updatedAt"] = datetime.utcnow().isoformat() + "Z"
state["lastSpot"] = current_spot
state["lastDailyClose"] = prev_close_price
state["lastDailyCloseDate"] = close_date_str

# Save updated state
with open(state_path, "w") as f:
    json.dump(state, f, indent=2)
print(f"\n✅ State saved to {state_path}")

# Generate notification message if any alerts fired
if notification_parts:
    notification_message = f"₿ BTC levels: spot ${current_spot:,.0f}k. {' '.join(notification_parts)} Leveraged cbBTC position: review trigger at ≤$45k (HF ~1.48–1.66 in the 40–45k band). Advisory only — not financial advice."
    print(f"\n📤 Notification message ready:\n{notification_message}")

    # Save notification to a file for ./notify to use
    with open("/tmp/btc-notification.txt", "w") as f:
        f.write(notification_message)

    print(f"\n📝 Notification saved to /tmp/btc-notification.txt")
else:
    print(f"\n✅ No alerts triggered")

# Append to daily log
log_date = datetime.utcnow().strftime("%Y-%m-%d")
log_file = f"memory/logs/{log_date}.md"
log_entry = f"BTC-levels: spot ${current_spot:,.2f}k, close ${prev_close_price:,.2f}k, alerts: {', '.join(alerts) if alerts else 'none'} ({datetime.utcnow().isoformat()}Z)\n"

try:
    with open(log_file, "a") as f:
        f.write(log_entry)
    print(f"\n📝 Log appended to {log_file}")
except FileNotFoundError:
    # Create log file if it doesn't exist
    with open(log_file, "w") as f:
        f.write(f"# {log_date}\n\n{log_entry}")
    print(f"\n📝 Created new log file {log_file}")

print(f"\n🎯 Evaluation complete. Alerts: {len(alerts)}")