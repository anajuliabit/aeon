#!/usr/bin/env python3
"""On-chain monitor — decode Blockscout token-transfer / transaction caches
into filtered, categorized, USD-priced events; build alert; persist state.

Usage:
  python3 scripts/on-chain-monitor-run.py <data_dir> <today_iso> <now_iso> <current_block>

<data_dir> must contain w{1..5}-tt.json and w{1..5}-tx.json from Blockscout v2.
"""

import json
import os
import shutil
import sys
import tempfile
from pathlib import Path

STATE_PATH = Path("memory/on-chain-state.json")
KNOWN_ADDR_PATH = Path("memory/known-addresses.yml")

CHAIN_EXPLORERS = {
    "ethereum": "https://etherscan.io",
    "base": "https://basescan.org",
    "arbitrum": "https://arbiscan.io",
    "optimism": "https://optimistic.etherscan.io",
    "polygon": "https://polygonscan.com",
}

CEX_NAMES = ("binance", "coinbase", "kraken", "okx", "bybit", "bitfinex")
DEX_NAMES = ("uniswap", "1inch", "curve", "sushi", "aerodrome", "cowswap", "matcha", "paraswap", "kyber")
BRIDGE_NAMES = ("across", "stargate", "synapse", "wormhole", "celer", "layerzero", "axelar", "relay.link")
LENDING_NAMES = ("morpho", "moonwell", "aave", "compound", "spark")


def load_known_addresses():
    if not KNOWN_ADDR_PATH.exists():
        return {}
    out = {}
    in_labels = False
    for line in KNOWN_ADDR_PATH.read_text().splitlines():
        s = line.strip()
        if s.startswith("labels:"):
            in_labels = True
            continue
        if not in_labels or not s or s.startswith("#"):
            continue
        if ":" not in s:
            continue
        k, v = s.split(":", 1)
        k = k.strip().strip('"').lower()
        v = v.strip().strip('"')
        if k.startswith("0x"):
            out[k] = v
    return out


def label_for(cp_addr, cp_obj, known):
    if cp_addr in known:
        return known[cp_addr]
    parts = []
    impls = cp_obj.get("implementations") or []
    if impls:
        impl = impls[0].get("name")
        if impl:
            parts.append(impl)
    name = cp_obj.get("name")
    if name and (not parts or name != parts[0]):
        parts.append(name)
    for t in (cp_obj.get("public_tags") or []):
        if isinstance(t, dict):
            lbl = t.get("label") or t.get("display_name") or t.get("name")
            if lbl:
                parts.append(lbl)
        elif isinstance(t, str):
            parts.append(t)
    return " | ".join(parts) if parts else None


def categorize(direction, cp_label, cp_addr, token_addr):
    s = (cp_label or "").lower()
    if any(c in s for c in CEX_NAMES):
        return "CEX-IN" if direction == "in" else "CEX-OUT"
    if any(d in s for d in DEX_NAMES):
        return "DEX-SWAP"
    if any(b in s for b in BRIDGE_NAMES):
        return "BRIDGE"
    if any(l in s for l in LENDING_NAMES):
        return "LEND-IN" if direction == "in" else "LEND-OUT"
    if cp_addr == "0x0000000000000000000000000000000000000000" or (token_addr and cp_addr == token_addr):
        return "MINT" if direction == "in" else "BURN"
    return "UNKNOWN-IN" if direction == "in" else "UNKNOWN-OUT"


def decode_tt(items, watch, from_block, known):
    out = []
    watch_l = watch.lower()
    for it in items:
        try:
            block = int(it.get("block_number") or 0)
            if block < from_block:
                continue
            tot = it.get("total") or {}
            value_raw = tot.get("value")
            token = it.get("token") or {}
            decimals = int(tot.get("decimals") or token.get("decimals") or 0)
            if value_raw is None:
                continue
            value_token = int(value_raw) / (10 ** decimals) if decimals else int(value_raw)
            to_h = ((it.get("to") or {}).get("hash") or "").lower()
            from_h = ((it.get("from") or {}).get("hash") or "").lower()
            direction = "in" if to_h == watch_l else "out"
            cp = from_h if direction == "in" else to_h
            cp_obj = (it.get("from") if direction == "in" else it.get("to")) or {}
            cp_label = label_for(cp, cp_obj, known)
            ex_rate = token.get("exchange_rate")
            ex_rate_f = float(ex_rate) if ex_rate else None
            value_usd = value_token * ex_rate_f if ex_rate_f is not None else None
            token_addr = (token.get("address_hash") or "").lower()
            tag = categorize(direction, cp_label, cp, token_addr)
            out.append({
                "tx_hash": it.get("transaction_hash"),
                "block": block,
                "timestamp": it.get("timestamp"),
                "category": {"ERC-20": "erc20", "ERC-721": "erc721", "ERC-1155": "erc1155"}.get(it.get("token_type"), "log"),
                "direction": direction,
                "token_symbol": token.get("symbol") or "?",
                "token_address": token_addr,
                "token_decimals": decimals,
                "value_token": value_token,
                "value_usd": value_usd,
                "exchange_rate": ex_rate_f,
                "counterparty": cp,
                "counterparty_label": cp_label,
                "is_scam": cp_obj.get("is_scam", False),
                "method": it.get("method"),
                "tag": tag,
            })
        except (KeyError, ValueError, TypeError) as e:
            sys.stderr.write(f"skip tt event: {e}\n")
    return out


def decode_tx(items, watch, from_block, known):
    out = []
    watch_l = watch.lower()
    for it in items:
        try:
            block = int(it.get("block_number") or 0)
            if block < from_block:
                continue
            val = it.get("value")
            if not val or int(val) == 0:
                continue
            value_eth = int(val) / 1e18
            to_h = ((it.get("to") or {}).get("hash") or "").lower()
            from_h = ((it.get("from") or {}).get("hash") or "").lower()
            if watch_l not in (to_h, from_h):
                continue
            direction = "in" if to_h == watch_l else "out"
            cp = from_h if direction == "in" else to_h
            cp_obj = (it.get("from") if direction == "in" else it.get("to")) or {}
            cp_label = label_for(cp, cp_obj, known)
            ex_rate_raw = it.get("exchange_rate")
            ex_rate_f = float(ex_rate_raw) if ex_rate_raw else None
            value_usd = value_eth * ex_rate_f if ex_rate_f else None
            tag = categorize(direction, cp_label, cp, "")
            out.append({
                "tx_hash": it.get("hash"),
                "block": block,
                "timestamp": it.get("timestamp"),
                "category": "external_eth",
                "direction": direction,
                "token_symbol": "ETH",
                "token_address": "",
                "token_decimals": 18,
                "value_token": value_eth,
                "value_usd": value_usd,
                "exchange_rate": ex_rate_f,
                "counterparty": cp,
                "counterparty_label": cp_label,
                "is_scam": cp_obj.get("is_scam", False),
                "method": it.get("method"),
                "tag": tag,
            })
        except (KeyError, ValueError, TypeError) as e:
            sys.stderr.write(f"skip tx event: {e}\n")
    return out


def filter_event(e, threshold_usd, alerted_set):
    if e["tx_hash"] in alerted_set:
        return "dedup"
    if e.get("is_scam"):
        return "scam_filter"
    v = e.get("value_usd")
    if v is None:
        return "unpriced"
    if v < 0.10:
        return "dust"
    if v < threshold_usd:
        return "below_threshold"
    return None


def humanize_usd(v):
    if v is None:
        return "?"
    if v >= 1_000_000:
        return f"${v/1_000_000:.2f}M"
    if v >= 1_000:
        return f"${v/1_000:.1f}k"
    return f"${v:.0f}"


def humanize_amount(amount, symbol):
    if amount is None:
        return "?"
    if amount >= 1_000_000:
        s = f"{amount/1_000_000:.2f}M"
    elif amount >= 1_000:
        s = f"{amount/1_000:.2f}k"
    elif amount >= 1:
        s = f"{amount:.4f}"
    else:
        s = f"{amount:.6f}"
    return f"{s} {symbol}"


WATCHES = [
    ("Wallet 1 (primary)", "0x98e5f932a264bce0a37f3d87accaab5f5bf7c0a9", "base", 1000, "w1"),
    ("Wallet 2", "0xf595346efb499f35b390f324d1655b4cd9751d9b", "base", 1000, "w2"),
    ("Wallet 3", "0x0f2570ab0638621cd97071fcc9de4a84787531b1", "base", 1000, "w3"),
    ("Wallet 4", "0xa958f3856b434445c1fcf54766d9431579e2c454", "base", 1000, "w4"),
    ("Wallet 5", "0x3e6385a81386ccf65674c791757b44601209d931", "base", 1000, "w5"),
]


def main():
    # Hardcoded for the 2026-06-23 run; pre-fetched Blockscout v2 caches live
    # in tmp/onchain/ (non-hidden so the sandbox can read them).
    data_dir = Path("tmp/onchain")
    today = "2026-06-23"
    now_iso = "2026-06-23T13:14Z"
    current_block = 47715479  # fetched live 2026-06-23T13:11Z from blockscout main-page

    known = load_known_addresses()
    state = json.loads(STATE_PATH.read_text()) if STATE_PATH.exists() else {}

    all_events = []
    per_watch = []
    for label, addr, chain, threshold, slug in WATCHES:
        ws = state.get(label, {})
        from_block = int(ws.get("last_block") or (current_block - 2400))
        alerted_tx = ws.get("alerted_tx", [])
        alerted_set = set(alerted_tx)

        tt_path = data_dir / f"{slug}-tt.json"
        tx_path = data_dir / f"{slug}-tx.json"
        try:
            tt = json.loads(tt_path.read_text()).get("items", [])
        except Exception as e:
            sys.stderr.write(f"{label} tt read fail: {e}\n")
            per_watch.append({"label": label, "status": "fail", "reason": "tt-read-fail"})
            continue
        try:
            tx = json.loads(tx_path.read_text()).get("items", [])
        except Exception as e:
            sys.stderr.write(f"{label} tx read fail: {e}\n")
            per_watch.append({"label": label, "status": "fail", "reason": "tx-read-fail"})
            continue

        events = decode_tt(tt, addr, from_block, known) + decode_tx(tx, addr, from_block, known)

        dropped = {"below_threshold": 0, "dust": 0, "dedup": 0, "unpriced": 0, "scam_filter": 0}
        kept = []
        new_tx = []
        for e in events:
            reason = filter_event(e, threshold, alerted_set)
            if reason:
                dropped[reason] += 1
            else:
                kept.append(e)
                if e["tx_hash"] not in alerted_set:
                    new_tx.append(e["tx_hash"])

        for e in kept:
            e["_watch"] = label
            e["_chain"] = chain
            all_events.append(e)

        merged = list(dict.fromkeys(new_tx + alerted_tx))[:200]
        priced = [e["value_usd"] for e in kept if e.get("value_usd")]
        if len(priced) >= 5:
            priced.sort()
            median = priced[len(priced) // 2]
        else:
            median = ws.get("median_usd_30d")

        state[label] = {
            "last_block": current_block,
            "last_run": now_iso,
            "alerted_tx": merged,
            "median_usd_30d": median,
        }
        per_watch.append({
            "label": label,
            "status": "ok",
            "raw": len(events),
            "kept": len(kept),
            "dropped": dropped,
            "from_block": from_block,
            "to_block": current_block,
            "block_span": current_block - from_block,
        })

    (data_dir / "all-events.json").write_text(json.dumps(all_events, indent=2, default=str))
    (data_dir / "per-watch.json").write_text(json.dumps(per_watch, indent=2))

    if all_events:
        all_events.sort(key=lambda e: -(e.get("value_usd") or 0))
        groups = {}
        for e in all_events:
            groups.setdefault(e["_watch"], []).append(e)

        biggest = all_events[0]
        bigusd = humanize_usd(biggest["value_usd"])
        cp_disp = biggest.get("counterparty_label") or biggest["counterparty"][:10] + "…" + biggest["counterparty"][-4:]
        action_word = {
            "CEX-OUT": "sent", "CEX-IN": "received from",
            "DEX-SWAP": "swapped", "BRIDGE": "bridged",
            "MINT": "minted", "BURN": "burned",
            "LEND-IN": "deposited to", "LEND-OUT": "withdrew from",
            "UNKNOWN-IN": "received from", "UNKNOWN-OUT": "sent to",
        }.get(biggest["tag"], "moved")
        tldr = f"{biggest['_watch']} {action_word} {bigusd} {biggest['token_symbol']} → {cp_disp} ({biggest['tag']})"

        lines = [
            f"*On-Chain Alert — {today}*",
            f"TL;DR: {tldr}",
            "",
        ]
        cap = 10
        emitted = 0
        for label, evs in groups.items():
            if emitted >= cap:
                break
            chain = evs[0]["_chain"]
            lines.append(f"*{label}* ({chain})")
            for e in evs:
                if emitted >= cap:
                    break
                exp = CHAIN_EXPLORERS.get(e["_chain"], "")
                cp_disp = e.get("counterparty_label") or e["counterparty"][:10] + "…" + e["counterparty"][-4:]
                amt = humanize_amount(e["value_token"], e["token_symbol"])
                usd = humanize_usd(e["value_usd"])
                arrow = "→" if e["direction"] == "out" else "←"
                lines.append(f"• {e['tag']} {usd} ({amt}) {arrow} {cp_disp} — [tx]({exp}/tx/{e['tx_hash']})")
                emitted += 1
            lines.append("")

        if len(all_events) > cap:
            lines.append(f"+{len(all_events) - cap} more — see memory/logs/{today}.md")
            lines.append("")

        fail_watches = [w for w in per_watch if w["status"] != "ok"]
        src = "alchemy=skip(no-key), etherscan=skip(free-tier-blocks-base), blockscout=ok, coingecko=skip(blockscout-inline-price)"
        footer = f"{len(all_events)} events on {len(groups)} watches | sources: {src} | last_block→{current_block}"
        if fail_watches:
            footer += f" | failed: {','.join(w['label'] for w in fail_watches)}"
        lines.append(footer)
        (data_dir / "alert.md").write_text("\n".join(lines))
    else:
        (data_dir / "alert.md").write_text("")

    fd, tmp = tempfile.mkstemp(dir=STATE_PATH.parent, prefix=".state-", suffix=".json")
    os.close(fd)
    Path(tmp).write_text(json.dumps(state, indent=2))
    shutil.move(tmp, STATE_PATH)

    total_raw = sum(w.get("raw", 0) for w in per_watch if w["status"] == "ok")
    summary = {
        "today": today,
        "now_iso": now_iso,
        "current_block": current_block,
        "watches": per_watch,
        "total_raw": total_raw,
        "total_kept": len(all_events),
        "groups": len(set(e["_watch"] for e in all_events)),
    }
    (data_dir / "summary.json").write_text(json.dumps(summary, indent=2))
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
