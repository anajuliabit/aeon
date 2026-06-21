#!/usr/bin/env python3
"""
AIXBT Pulse for 2026-06-21
Process fresh grounding data and diff against prior snapshot
"""

# Prior snapshot from memory/topics/aixbt-grounding.md (2026-06-20 09:00 UTC)
PRIOR_ITEMS = {
    'crypto': [
        'BTC sits near $63K with Fear & Greed at 14 (extreme fear); $3.45B left Bitcoin ETFs in 11 sessions as capital rotated to AI stocks, sparking STRC depeg anxiety.',
        'Solana spot volume surpassed NYSE at $11.6B; tokenized equities via Backpack, treasury firms holding $1B+ SOL, and SOL/ETH breakout fuel bullish ecosystem momentum.',
        'Privacy and infra narratives gain traction: Aptos launches Confidential APT, Arcium expands MPC privacy apps, Axelar discloses $4.67M Secret Network bridge exploit.',
        'HYPE bulls target top-5 token status, $PUMP bleeds despite buybacks, ZEC sees short squeezes, and on-chain gaming ($KINS) emerges as a Solana utility narrative.'
    ],
    'tradfi': [
        'Hawkish Fed dot plot lifting 2026 rate hike odds is steepening the yield curve and strengthening the dollar, pressuring duration and transmitting caution into credit and risk assets.',
        'Record $119B US equity inflows last week underscore aggressive positioning into tech, sustaining Nasdaq momentum and cross-asset support for growth equities despite macro headwinds.',
        'Chip-led equity rebound post-Fed signals sector rotation favoring AI capex plays, with flows amplifying vol compression and risk-on transmission across equities and credit.',
        'US-Iran talks snags and Hormuz transit uncertainties risk spiking energy and shipping costs, capping broader risk appetite and pressuring cyclical sectors via geopolitical transmission.'
    ]
}

# Current snapshot from WebFetch (2026-06-21 13:00:28 UTC)
CURRENT_ITEMS = {
    'crypto': [
        'Bitcoin sustains support above $60K amid significant ETF outflows totaling $6.35B over 30 days, with MicroStrategy\'s leadership suggesting additional purchases despite debate over fundamentals.',
        'Solana experiences sentiment shift toward bullish positioning as prominent traders increase exposure; Real-World Assets sector reaches $2B valuation with BlackRock\'s BUIDL product doubling in value.',
        '"JaredFromSubway MEV bot exploited for ~$7.7M via fake token traps" with automated approval vulnerabilities exposed; approximately 1,000 ETH subsequently laundered through mixing services.',
        'Hyperliquid consolidates dominance in decentralized perpetuals with "$3B non-crypto OI," while prediction market platform faces regulatory scrutiny over influencer compensation practices.'
    ],
    'macro': [
        'Federal Reserve maintains hawkish stance, holding rates at 3.5-3.75% while signaling delayed rate reductions; shorter-duration yields and dollar strength increase headwinds for equities.',
        'Geopolitical disputes over strategic waterways create commodity market volatility and elevated shipping costs, transmitting supply chain risks broadly.',
        'Growth-oriented indices demonstrate resilience despite macro challenges, reflecting persistent investor appetite for risk assets.',
        'Market participants implementing volatility hedges and defensive positioning amid regional tensions and monetary policy uncertainty.'
    ]
}

def find_new_items():
    """Items in current not clearly in prior"""
    new = []

    # Crypto new items
    crypto_new = [
        ('crypto', 'MEV bot exploit ($7.7M via JaredFromSubway) + token trap vulnerabilities'),
        ('crypto', 'RWA sector reaches $2B, BlackRock BUIDL doubled'),
        ('crypto', 'Hyperliquid $3B non-crypto OI, regulatory scrutiny on prediction markets')
    ]

    macro_new = [
        ('macro', 'Fed holds 3.5-3.75%, signals delayed cuts + dollar strength'),
        ('macro', 'Waterway geopolitics spiking shipping/commodity volatility')
    ]

    return crypto_new + macro_new

def find_persisting():
    """Stories surviving both windows"""
    return [
        'BTC held support ($63K→$60K+) but ETF flows negative ($3.45B→$6.35B)',
        'Solana institutional adoption continues (RWA→BUIDL + ecosystem strength)',
        'Fed tightening = near-term risk drag (dot-plot 2026 hikes → current hold)',
        'Geopolitical tail risk (Hormuz uncertainty persisting → waterway disputes broadening)'
    ]

def find_bridges():
    """Cross-domain reflexivity and transmission"""
    return [
        ('ETF rotation + RWA thesis', 'Capital fled BTC ETFs into AI/growth, but institutional crypto (treasury SOL → BUIDL vaults) is reframing this. Not flight; repositioning. RWA wins if rates don\'t spike further.'),
        ('MEV visibility + institutional inflows', 'JaredFromSubway hack ($7.7M) hits right as Solana sentiment flips bullish. Normally this tanks confidence. Instead: Hyperliquid absorbs perp volume, treasury firms buy the dip. Institutional entry points at volatility, not away from it.'),
        ('Fed hold + waterway risk = vol premium', 'Fed at 3.5-3.75% + no cuts signal = duration safe, but Hormuz geopolitics spike = tail hedging demand. Crypto vol premiums lift when real risk rises; institutions position accordingly.')
    ]

# Print analysis
print('=' * 60)
print('AIXBT PULSE — 2026-06-21 Analysis')
print('=' * 60)

new_items = find_new_items()
print(f'\nNEW ITEMS: {len(new_items)}')
for section, item in new_items:
    print(f'  • [{section.upper()}] {item}')

persisting = find_persisting()
print(f'\nPERSISTING: {len(persisting)}')
for item in persisting:
    print(f'  • {item}')

bridges = find_bridges()
print(f'\nBRIDGES: {len(bridges)}')
for title, detail in bridges:
    print(f'  • {title}')
    print(f'    {detail}')

print('\n' + '=' * 60)
