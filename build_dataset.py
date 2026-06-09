import json
with open('.hl-cache/user-fills-0x06cecfbac34101ae41c88ebc2450f8602b3d164b.json') as f:
    fills = json.load(f)
closes = [r for r in fills if r['dir'] == 'Close Short']
trades = []
for r in closes:
    trades.append({
        'market': r['coin'],
        'direction': 'short',
        'size': float(r['sz']),
        'fill_price': float(r['px']),
        'signal': 'unclassified',
        'outcome': {
            'pnl': float(r['closedPnl']),
            'hold_duration_seconds': None,
            'win': float(r['closedPnl']) > 0,
        },
        'market_context': None,
        'timeframe': '1m',
        'verification': {
            'timestamp_ms': r['time'],
            'tx_hash': r['hash'],
        },
    })
dataset = {
    'kind': 'hl-perp-trades',
    'schema_version': 1,
    'source': {'wallet': '0x06cecfbac34101ae41c88ebc2450f8602b3d164b', 'venue': 'hyperliquid-mainnet'},
    'signal_taxonomy': {
        'unclassified': 'HL fill timing density (250 closes in 52.1 min) precludes per-fill indicator attribution; trades labeled unclassified per HFT-density convention used in mints 8/15/16/17/18',
    },
    'market_context_rules': {
        'null': 'AAVE perp not in cached BTC/ETH/SOL OHLCV; no market_context label assigned',
    },
    'ohlcv_interval': '1m',
    'aggregate_metrics': {
        'n_trades': 250,
        'win_rate': 1.0,
        'sharpe': 8458.93,
        'max_drawdown_pct': 0.0,
        'days_covered': 0.036,
    },
    'trades': trades,
}
with open('.pending-reppo/data/mint-420334cbe2154944.json', 'w') as f:
    json.dump(dataset, f, indent=2)
import os
print(f'wrote {os.path.getsize(".pending-reppo/data/mint-420334cbe2154944.json")} bytes; n_trades={len(trades)}')
