#!/usr/bin/env python3
import json
import datetime
import sys

data = {
    "prices": [
        [1781654400000, 65598.9439666077],
        [1781740800000, 64422.57366477588],
        [1781812581000, 62920.70233016583]
    ]
}

spot = data['prices'][-1][1]
prev_close = data['prices'][-2][1]
prev_close_ts = data['prices'][-2][0]
prev_close_date = datetime.datetime.fromtimestamp(prev_close_ts/1000, datetime.timezone.utc).date()
# close date is day BEFORE the timestamp's date (since 00:00 UTC snapshot is close of prior day)
close_date = prev_close_date - datetime.timedelta(days=1)

print(f'spot={spot:.2f}')
print(f'prev_close={prev_close:.2f}')
print(f'prev_close_ts={prev_close_ts}')
print(f'prev_close_date={prev_close_date.isoformat()}')
print(f'close_date={close_date.isoformat()}')
print(f'leverage_trigger={spot <= 45000}')
print(f'breakdown={prev_close < 60500}')
print(f'reclaim63500={spot >= 63500}')
print(f'reclaim65900={spot >= 65900}')