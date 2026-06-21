#!/usr/bin/env python3
import json
import sys
import datetime

# Data from curl
data = {
  "prices": [
    [1781654400000, 65598.9439666077],
    [1781740800000, 64422.57366477588],
    [1781812960000, 63058.607581018485]
  ],
  "market_caps": [
    [1781654400000, 1314781494836.0032],
    [1781740800000, 1291258235600.5845],
    [1781812960000, 1260939503640.9346]
  ],
  "total_volumes": [
    [1781654400000, 25567698997.885597],
    [1781740800000, 32345181752.593975],
    [1781812960000, 31819812648.685455]
  ]
}

# Parse
spot = data['prices'][-1][1]
prev_close = data['prices'][-2][1]
prev_close_ts = data['prices'][-2][0]
prev_close_date = datetime.datetime.fromtimestamp(prev_close_ts/1000, datetime.timezone.utc).date()
close_date = prev_close_date - datetime.timedelta(days=1)

print(f'spot={spot:.2f}')
print(f'prev_close={prev_close:.2f}')
print(f'close_date={close_date}')
print(f'leverage_trigger={spot <= 45000}')
print(f'breakdown={prev_close < 60500}')
print(f'reclaim63500={spot >= 63500}')
print(f'reclaim65900={spot >= 65900}')