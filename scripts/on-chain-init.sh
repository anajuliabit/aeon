#!/bin/bash
set -e

# Base RPC endpoint
BASE_RPC="https://mainnet.base.org/"

# Get current block
echo "Fetching current Base block..."
current_block_hex=$(curl -m 10 -s -X POST "$BASE_RPC" \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"eth_blockNumber","params":[]}' | jq -r '.result')

current_block=$((16#${current_block_hex#0x}))
echo "Current Base block: $current_block (0x$current_block_hex)"

# Set starting block (2400 blocks = ~8 hours on Base)
start_block=$((current_block - 2400))
echo "Starting block (8h back): $start_block"

# Update state file with current block
echo "Updating memory/on-chain-state.json..."
jq --arg block "$current_block" \
   '(.[] | .last_block) |= ($block | tonumber) |
    (.[] | .last_run) |= now | fromdate | strftime("%Y-%m-%dT%H:%M:%SZ")' \
   memory/on-chain-state.json > memory/on-chain-state.json.tmp
mv memory/on-chain-state.json.tmp memory/on-chain-state.json

cat memory/on-chain-state.json | jq '.' | head -20
