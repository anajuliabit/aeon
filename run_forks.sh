#!/bin/bash
# Fetch aeon.yml from all 79 forks and build JSON array
# Output goes directly to the target file

OUTPUT="/home/runner/work/aeon/aeon/memory/topics/.fork_results_tmp.json"

FORKS=(
  "nigelon11/aeon"
  "webguy-cloud/aeon"
  "Loopershot/aeon"
  "s97472091-pixel/aeon"
  "usepaxterapp/aeon"
  "penguinxbt/aeon"
  "freezerboi/aeon"
  "anajuliabit/aeon-fork"
  "madmystic/aeon"
  "SamsShow/aeon"
  "Marr554/aeon"
  "alpenflow/aeon"
  "stefrogovskyi/aeon"
  "usephylax/aeon"
  "saivarmadpr/aeon"
  "Tholynceus/aeon"
  "logbookbase/aeon"
  "maredek-bot/aeon"
  "CharonAI-code/aeon"
  "KK-OS/aeon"
  "P9LLI/aeon"
  "adlai88/aeon"
  "vladimirvalcourt/aeon"
  "clawhunter/add-clawhunter-pack"
  "hurley87/aeon"
  "runchr-org/aeon"
  "brainlabors-dot/aeon"
  "rajkaria/aeon"
  "tenequm/aeon"
  "ziyosteve/aeon"
  "zszkey/aeon-1"
  "modelcollapse/aeon"
  "wrenwealth/aeon"
  "ghostx-dev/aeon"
  "sinfronterasai/aeon"
  "gitlumen-team/aeon"
  "ashneil12/aeon-upstream"
  "AdversaLLC/aeon"
  "anondevv69/bankr-space-aeon"
  "SahilParikh03/aeon"
  "mnemedb/aeon"
  "NASTYZUNI/aeon"
  "alfahadgm/aeon"
  "dannysrod/aeon"
  "chxoky/aeon"
  "daxaur/aeon"
  "aeoncity-hub/aeon"
  "beijiangqukuailian/aeon"
  "vigilcodes/aeon"
  "yindaqiu/aeon"
  "BBridgeers/aeon"
  "swarm-ai-research/aeon-atlas"
  "TakamiyaZee/aeon"
  "xBalbinus/aeon"
  "sparkleware/aeon"
  "codexvritra/aeon"
  "UIZorrot/aeon"
  "lawbworld-tech/aeon"
  "gitlawbounty/aeon"
  "0xShak/aeon"
  "taekwonv89/aeon"
  "0xMal0u/aeon"
  "youpsla/aeon"
  "antfleet-ops/aeon"
  "damo-nu11/aeon-minebean"
  "VibeSan7/aeon"
  "anomit/aeon"
  "enzoonchain/aeon"
  "AntFleet/aeon-bench"
  "takanafur/aeon"
  "madebyshun/blueagent-aeon"
  "usiclabs/aeon"
  "Da6hkin/aeon"
  "Boodszw/Boodszw_Bread"
  "ether-btc/aeon"
  "tomscaria/aeon"
  "yugo-engineer/aeon"
  "pezetel/aeon"
  "AmithKumar1/aeon"
)

TOTAL=${#FORKS[@]}
echo "Processing $TOTAL forks..." >&2

# We'll store raw YAML content for each fork, then process with Python
CACHE_DIR="/home/runner/work/aeon/aeon/.fork_cache"
mkdir -p "$CACHE_DIR"

for i in "${!FORKS[@]}"; do
  FORK="${FORKS[$i]}"
  SAFE_NAME=$(echo "$FORK" | tr '/' '_')
  CACHE_FILE="$CACHE_DIR/${SAFE_NAME}.b64"

  echo -n "  [$((i+1))/$TOTAL] $FORK... " >&2

  # Fetch the base64-encoded content
  RESULT=$(gh api "repos/${FORK}/contents/aeon.yml?ref=main" --jq '.content' 2>/tmp/gh_err.txt)
  EXIT_CODE=$?

  if [ $EXIT_CODE -ne 0 ]; then
    ERR=$(cat /tmp/gh_err.txt 2>/dev/null)
    if echo "$ERR" | grep -qi "404\|not found"; then
      echo "no_aeon_yml" > "${CACHE_DIR}/${SAFE_NAME}.status"
    elif echo "$ERR" | grep -qi "403\|rate limit"; then
      echo "rate_limited" > "${CACHE_DIR}/${SAFE_NAME}.status"
    else
      echo "yml_unreadable" > "${CACHE_DIR}/${SAFE_NAME}.status"
    fi
    echo "SKIP ($ERR)" >&2
    continue
  fi

  if [ -z "$RESULT" ] || [ "$RESULT" = "null" ]; then
    echo "no_aeon_yml" > "${CACHE_DIR}/${SAFE_NAME}.status"
    echo "no_aeon_yml" >&2
    continue
  fi

  echo "ok" > "${CACHE_DIR}/${SAFE_NAME}.status"
  echo "$RESULT" > "$CACHE_FILE"
  echo "ok" >&2
done

echo "Fetch done. Building JSON..." >&2
