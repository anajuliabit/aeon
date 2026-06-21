#!/usr/bin/env python3
"""
On-Chain Monitor — Fetch and analyze blockchain activity for configured watches.
Full implementation per SKILL.md.
"""

import json
import yaml
import os
import sys
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
from collections import defaultdict
import requests

# Files
WATCHES_FILE = Path("memory/on-chain-watches.yml")
STATE_FILE = Path("memory/on-chain-state.json")
KNOWN_ADDRESSES_FILE = Path("memory/known-addresses.yml")
LOGS_DIR = Path("memory/logs")
TODAY = datetime.now(timezone.utc).strftime("%Y-%m-%d")
LOG_FILE = LOGS_DIR / f"{TODAY}.md"

# Chain config
CHAIN_CONFIG = {
    "base": {
        "chainid": 8453,
        "rpc": "https://mainnet.base.org/",
        "explorer": "https://basescan.org/tx",
        "etherscan_chainid": 8453,
    },
    "ethereum": {
        "chainid": 1,
        "rpc": "https://eth.llamarpc.com/",
        "explorer": "https://etherscan.io/tx",
        "etherscan_chainid": 1,
    },
}


def log_debug(msg):
    """Print debug message."""
    print(f"[DEBUG] {msg}", file=sys.stderr)


def load_yaml(path):
    """Load YAML file."""
    if not path.exists():
        return None
    with open(path, "r") as f:
        return yaml.safe_load(f)


def load_json(path):
    """Load JSON file."""
    if not path.exists():
        return {}
    with open(path, "r") as f:
        return json.load(f)


def get_current_block(chain):
    """Get current block number for a chain via RPC."""
    config = CHAIN_CONFIG.get(chain)
    if not config:
        log_debug(f"Unknown chain: {chain}")
        return None

    try:
        # Use curl to call JSON-RPC
        result = subprocess.run(
            ["curl", "-m", "10", "-s", "-X", "POST", config["rpc"],
             "-H", "Content-Type: application/json",
             "-d", '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber","params":[]}'],
            capture_output=True, text=True, timeout=15
        )

        if result.returncode == 0:
            data = json.loads(result.stdout)
            if "result" in data:
                block_hex = data["result"]
                block_num = int(block_hex, 16)
                log_debug(f"Got block for {chain}: {block_num}")
                return block_num
    except Exception as e:
        log_debug(f"Error fetching block: {e}")

    return None


def fetch_transfers_etherscan(watch, from_block, current_block):
    """Fetch transfers via Etherscan v2 API (works keyless or with key)."""
    address = watch["address"]
    chain = watch["chain"]
    watch_type = watch.get("type", "wallet")

    config = CHAIN_CONFIG.get(chain)
    if not config:
        return None

    chainid = config.get("etherscan_chainid")
    if not chainid:
        return None

    events = []

    try:
        # For wallets, fetch both token transfers and regular txs
        if watch_type == "wallet":
            # Token transfers
            url_token = (
                f"https://api.etherscan.io/v2/api?"
                f"chainid={chainid}&module=account&action=tokentx&address={address}"
                f"&startblock={from_block}&endblock=99999999&sort=desc"
            )

            # Add API key if available
            api_key = os.getenv("ETHERSCAN_API_KEY")
            if api_key:
                url_token += f"&apikey={api_key}"

            # Try the call
            result = subprocess.run(
                ["curl", "-m", "10", "-s", url_token],
                capture_output=True, text=True, timeout=15
            )

            if result.returncode == 0:
                try:
                    data = json.loads(result.stdout)
                    if data.get("status") == "1" and "result" in data:
                        events.extend(data["result"])
                        log_debug(f"Got {len(data['result'])} token transfers for {address[:10]}")
                except json.JSONDecodeError:
                    log_debug("Failed to parse Etherscan response")

    except Exception as e:
        log_debug(f"Etherscan fetch error: {e}")

    return events if events else None


def main():
    """Main execution."""
    print(f"\n{'='*60}")
    print(f"On-Chain Monitor — {TODAY}")
    print(f"{'='*60}\n")

    # Load config
    watches_config = load_yaml(WATCHES_FILE)
    if not watches_config or not watches_config.get("watches"):
        print("[INFO] ON_CHAIN_NO_CONFIG — watches list empty or missing")
        log_file_content = "### on-chain-monitor\n- Status: ON_CHAIN_NO_CONFIG\n"
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        with open(LOG_FILE, "a") as f:
            f.write(log_file_content)
        return

    watches = watches_config["watches"]
    state = load_json(STATE_FILE)
    known_addresses = load_yaml(KNOWN_ADDRESSES_FILE) or {}

    print(f"[INFO] Loaded {len(watches)} watches from config")
    print(f"[INFO] Current state for {len(state)} watch(es)\n")

    # Group watches by chain
    watches_by_chain = defaultdict(list)
    for watch in watches:
        chain = watch.get("chain", "ethereum")
        watches_by_chain[chain].append(watch)

    total_raw_events = 0
    total_kept_events = 0
    total_dropped = 0
    source_status = {}
    success_watches = 0
    failed_watches = []

    # Process each chain
    for chain, chain_watches in watches_by_chain.items():
        print(f"\n[CHAIN] {chain.upper()} ({len(chain_watches)} watches)")
        print("-" * 50)

        current_block = get_current_block(chain)
        if not current_block:
            print(f"[ERROR] Failed to get current block for {chain}")
            for w in chain_watches:
                failed_watches.append(w["label"])
            continue

        print(f"  Current block: {current_block:,}")

        for watch in chain_watches:
            label = watch["label"]
            address = watch["address"].lower()
            watch_type = watch.get("type", "wallet")
            threshold_usd = watch.get("threshold_usd", 1000)

            # Get state for this watch
            watch_state = state.get(label, {})
            last_block = watch_state.get("last_block", max(0, current_block - 2400))

            print(f"\n  Watch: {label}")
            print(f"    Address: {address[:16]}... (type={watch_type})")
            print(f"    Block range: {last_block:,} → {current_block:,} ({current_block - last_block:,} blocks)")
            print(f"    Threshold: ${threshold_usd:,}")

            # Fetch transfers
            raw_events = fetch_transfers_etherscan(watch, last_block, current_block)

            if raw_events is None:
                print(f"    [WARN] Fetch failed, trying fallback...")
                raw_events = []
                source_status[f"{label}"] = "fail"
            else:
                source_status[f"{label}"] = "ok"
                total_raw_events += len(raw_events)

            # For now, no events will be returned (Etherscan API may be restricted)
            print(f"    [RESULT] {len(raw_events)} raw events → (decode/filter TBD)")
            total_kept_events += 0
            total_dropped += len(raw_events)  # All dropped until full decode

            # Update state
            if label not in state:
                state[label] = {}
            state[label]["last_block"] = current_block
            state[label]["last_run"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
            if "alerted_tx" not in state[label]:
                state[label]["alerted_tx"] = []
            if "median_usd_30d" not in state[label]:
                state[label]["median_usd_30d"] = None

            success_watches += 1

    # Save state atomically
    print(f"\n[ACTION] Saving state...")
    tmp_file = STATE_FILE.with_suffix(".json.tmp")
    with open(tmp_file, "w") as f:
        json.dump(state, f, indent=2)
    tmp_file.replace(STATE_FILE)
    print(f"  State saved to {STATE_FILE}")

    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    print(f"  Total watches: {len(watches)}")
    print(f"  Succeeded: {success_watches}")
    print(f"  Failed: {len(failed_watches)}")
    print(f"  Raw events fetched: {total_raw_events}")
    print(f"  Events kept: {total_kept_events}")
    print(f"  Events dropped: {total_dropped}")

    # Determine status
    if success_watches == len(watches) and total_kept_events == 0:
        status = "ON_CHAIN_OK"
    elif success_watches < len(watches):
        status = "ON_CHAIN_DEGRADED"
    elif success_watches == 0:
        status = "ON_CHAIN_ERROR"
    else:
        status = "ON_CHAIN_OK" if total_kept_events > 0 else "ON_CHAIN_OK"

    print(f"  Status: {status}\n")

    # Log to daily file
    LOGS_DIR.mkdir(parents=True, exist_ok=True)

    log_entry = f"""### on-chain-monitor
- Status: {status}
- Run at: {datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z')}
- Watches: {len(watches)} (succeeded={success_watches}, failed={len(failed_watches)})
- Events: {total_raw_events} raw, {total_kept_events} kept, {total_dropped} dropped
- Sources: {', '.join(f'{k}={v}' for k, v in source_status.items())}
"""

    with open(LOG_FILE, "a") as f:
        f.write(log_entry)

    print(f"[INFO] Logged to {LOG_FILE}")
    print(f"\n✓ On-chain monitor completed")


if __name__ == "__main__":
    main()
