## Summary

**btc-levels 21:21Z run — no alerts.**

- **Spot:** $64,111.55 (up ~$225 from 17:16Z's $63,886)
- **Daily close (2026-07-23):** $65,052.47

Level checks:
- Leverage-review (≤$45k): clear — spot $64k well above
- Breakdown close (<$60,500): clear — close $65,052 above trigger
- Reclaim $63,500: already alerted (`true`), re-arm gate ($60,500) not hit
- Reclaim $65,900: already alerted (`true`), spot below $65,900 but re-arm gate not hit

No notification sent (quiet run). State file and log committed (`aae7870`).
