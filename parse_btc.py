import json
import sys
from datetime import datetime, timezone, timedelta

# Get the data from stdin
raw_data = sys.stdin.read()
try:
    data = json.loads(raw_data)
except json.JSONDecodeError as e:
    print(f"Error: invalid JSON: {e}", file=sys.stderr)
    sys.exit(1)

prices = data.get('prices', [])
if len(prices) < 2:
    print("Error: insufficient price data", file=sys.stderr)
    sys.exit(1)

current_timestamp_ms, current_price = prices[-1]
prev_close_timestamp_ms, prev_close_price = prices[-2]

# Convert timestamps to datetime objects
prev_close_dt = datetime.fromtimestamp(prev_close_timestamp_ms / 1000, tz=timezone.utc)
# The close date is the calendar day BEFORE the timestamp's date
close_date = (prev_close_dt - timedelta(days=1)).date()

result = {
    "spot": current_price,
    "daily_close": prev_close_price,
    "close_date": str(close_date)
}

print(json.dumps(result))