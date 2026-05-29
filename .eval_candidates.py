#!/usr/bin/env python3
import json, os, math, hashlib, sys

CACHE = ".hl-cache"
WALLETS = sorted({
    "0x0ddf9bae2af4b874b96d287a5ad42eb47138a902",
    "0x2b3349ff0c4cf96f7df87fd5f3d583ee625733f7",
    "0x32008fcb6bbd16532afc83ca8b6c920dde22c407",
    "0x675462411d40a169c3397ac1dc00786dc9c7d3a1",
    "0x577ae91c7b74f04ddb3a5b399ded8318e9895fd2",
    "0x477296b8f5f5525be26e5c0a82eb0dd24da3949f",
    "0x71dfc07de32c2ebf1c4801f4b1c9e40b76d4a23d",
    "0x7fdafde5cfb5465924316eced2d3715494c517d1",
    "0x856c35038594767646266bc7fd68dc26480e910d",
    "0x8def9f50456c6c4e37fa5d3d57f108ed23992dae",
    "0xa8dc22b6cc18fc27dc695bbc6e9a17603b9b095b",
    "0x9a1500b41519868039b1f95c447ba50b76d837e6",
    "0x9e875bd28ee5001478c16cb0c8329116a3c3e816",
    "0x953c5152e2f8b5ed9d92976cad478a837749182a",
    "0xb798aef79972ce8f73d47b9ebbcda6bbb7ec4fbf",
    "0xbb10bda01f56b1604f2f024f2d18fcaf5d2b20b0",
    "0xbdfa4f4492dd7b7cf211209c4791af8d52bf5c50",
    "0xd47587702a91731dc1089b5db0932cf820151a91",
    "0xebe126adabe1a8f08d3ce53b45e7cc994ca14070",
    "0xecb63caa47c7c4e77f60f1ce858cf28dc2b82b00",
    "0xa9b95f2a2e7ef219021efc5c04c32761b8553bbd",
    "0x87f9cd15f5050a9283b8896300f7c8cf69ece2cf",
    "0x4ec8fe22a531a96c8a846aaf5cbef73202649a80",
    "0xe6111266afdcdf0b1fe8505028cc1f7419d798a7",
    "0xbdfa4f4492dd7b7cf211209c4791af8d52bf5c50",
})


def aggregate(wallet):
    path = os.path.join(CACHE, f"user-fills-{wallet}.json")
    try:
        with open(path) as f:
            fills = json.load(f)
    except Exception as e:
        return {"wallet": wallet, "error": str(e)}
    if isinstance(fills, dict) and fills.get("code"):
        return {"wallet": wallet, "error": fills.get("code")}
    if not isinstance(fills, list):
        return {"wallet": wallet, "error": "not-array"}
    if not fills:
        return {"wallet": wallet, "n_fills": 0, "error": "empty"}

    closes = [f for f in fills if "Close" in (f.get("dir") or "")]
    if len(closes) < 20:
        return {"wallet": wallet, "n_fills": len(fills), "n_closes": len(closes), "error": "lt20-closes"}

    pnls = [float(f["closedPnl"]) for f in closes]
    notionals = [float(f["px"]) * float(f["sz"]) for f in closes]
    rets = [(p / n) if n > 0 else 0.0 for p, n in zip(pnls, notionals)]

    n = len(closes)
    wins = sum(1 for p in pnls if p > 0)
    sum_pnl = sum(pnls)
    mean_pnl = sum_pnl / n

    first_ms = fills[0]["time"]
    last_ms = fills[-1]["time"]
    days_covered = max((last_ms - first_ms) / 1000 / 86400, 1/86400)

    mean_r = sum(rets) / n
    var_r = sum((r - mean_r) ** 2 for r in rets) / max(n - 1, 1)
    std_r = math.sqrt(var_r)
    if std_r > 0 and days_covered > 0:
        sharpe = (mean_r / std_r) * math.sqrt(n * 365.0 / days_covered)
    else:
        sharpe = 0.0

    cum = 0.0
    peak = 0.0
    max_dd_abs = 0.0
    for p in pnls:
        cum += p
        if cum > peak:
            peak = cum
        dd = peak - cum
        if dd > max_dd_abs:
            max_dd_abs = dd
    max_dd_pct = (max_dd_abs / peak * 100) if peak > 0 else 0.0

    coins = sorted({f["coin"] for f in fills})

    canonical = f"trades:9:{wallet}:{fills[0]['time']}:{fills[-1]['time']}:{n}"
    h = hashlib.sha256(canonical.encode()).hexdigest()

    return {
        "wallet": wallet,
        "n_fills": len(fills),
        "n_closes": n,
        "win_rate": wins / n,
        "sum_pnl": sum_pnl,
        "mean_pnl": mean_pnl,
        "sharpe_ann": sharpe,
        "max_dd_pct": max_dd_pct,
        "max_dd_abs": max_dd_abs,
        "days_covered": days_covered,
        "first_ms": first_ms,
        "last_ms": last_ms,
        "coins": coins,
        "canonical": canonical,
        "hash": h,
        "hash16": h[:16],
    }


results = [aggregate(w) for w in WALLETS]
for r in results:
    if r.get("error"):
        print(f"{r['wallet']}: skip ({r.get('error')})")
    else:
        print(
            f"{r['wallet']}: n={r['n_closes']} pnl=${r['sum_pnl']:.0f} win={r['win_rate']:.3f} "
            f"sharpe={r['sharpe_ann']:.2f} mdd={r['max_dd_pct']:.2f}% days={r['days_covered']:.3f} "
            f"hash16={r['hash16']} coins={','.join(r['coins'][:5])}"
        )

valid = [r for r in results if not r.get("error") and r.get("n_closes", 0) >= 20]
valid.sort(key=lambda r: (r["sharpe_ann"], r["n_closes"]), reverse=True)
print("\n=== Ranked by Sharpe (ann) ===")
for r in valid:
    print(
        f"{r['hash16']}  {r['wallet']}  closes={r['n_closes']}  sharpe={r['sharpe_ann']:.2f}  pnl=${r['sum_pnl']:.0f}"
    )

with open("/tmp/eval_results.json", "w") as f:
    json.dump(valid, f, indent=2)
print("\nWrote /tmp/eval_results.json")
