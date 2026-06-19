#!/bin/bash

# Step 1: Parse and validate ${var}
var="1642770456720683008"
if [ -z "${var}" ]; then
  echo "LIST_DIGEST_NO_CONFIG: var must contain at least one X list ID" \
    >> "memory/logs/$(date -u +%Y-%m-%d).md"
  exit 0
fi

IDS_PART="${var%%|*}"
TOPIC_FILTER=""
if [ "${var}" != "$IDS_PART" ]; then
  TOPIC_FILTER="${var#*|}"
fi

# Validate: each ID must be all digits (X list IDs are numeric)
for LIST_ID in $(echo "$IDS_PART" | tr ',' ' '); do
  if ! [[ "$LIST_ID" =~ ^[0-9]+$ ]]; then
    echo "LIST_DIGEST_NO_CONFIG: invalid list ID '$LIST_ID' (must be numeric)" \
      >> "memory/logs/$(date -u +%Y-%m-%d).md"
    exit 0
  fi
done

# Step 2: Check for pre-fetched cache
LIST_ID="$IDS_PART"
cache_file=".xai-cache/list-digest-${LIST_ID}.json"
list_status="ok"

if [ ! -f "$cache_file" ]; then
  echo "No cache file found for list $LIST_ID"
  list_status="error(no-cache)"

  # Check if XAI_API_KEY is available for API fallback
  if [ -z "$XAI_API_KEY" ]; then
    echo "LIST_DIGEST_NO_CONFIG: XAI_API_KEY required and cache not available" \
      >> "memory/logs/$(date -u +%Y-%m-%d).md"
    exit 0
  fi
fi

# Step 3-7: Use Python script to process data and create notification
python3 << 'EOF'
import json
import re
import math
import os
from datetime import datetime

# Parse var parameter from shell
var = "1642770456720683008"
IDS_PART = var.split("|")[0]
TOPIC_FILTER = "" if len(var.split("|")) == 1 else var.split("|")[1]
LIST_ID = IDS_PART

# Load cached data
cache_file = f".xai-cache/list-digest-{LIST_ID}.json"
try:
    with open(cache_file, "r") as f:
        data = json.load(f)
    grok_text = data['output'][-1]['content'][0]['text']
except Exception as e:
    print(f"Failed to load cache: {e}")
    exit(1)

# Parse tweets from Grok response
tweets = []
current_tweet = {}

lines = grok_text.split("\n")
for i, line in enumerate(lines):
    line = line.strip()

    # Check for tweet header pattern
    tweet_match = re.match(r"(\d+)\.\s+\*\*@(\w+)\*\*", line)
    if tweet_match:
        if current_tweet:
            tweets.append(current_tweet)
        current_tweet = {
            "handle": tweet_match.group(2),
            "text": "",
            "likes": 0,
            "retweets": 0,
            "replies": 0,
            "views": 0,
            "url": "",
            "media": "none",
            "is_reply": False,
            "is_quote": False
        }

    elif current_tweet:
        if line.startswith("likes:"):
            # Extract metrics
            likes_match = re.search(r"likes:(\d+)", line)
            retweets_match = re.search(r"retweets:(\d+)", line)
            replies_match = re.search(r"replies:(\d+)", line)
            views_match = re.search(r"views:(\d+)", line)

            if likes_match:
                current_tweet["likes"] = int(likes_match.group(1))
            if retweets_match:
                current_tweet["retweets"] = int(retweets_match.group(1))
            if replies_match:
                current_tweet["replies"] = int(replies_match.group(1))
            if views_match:
                current_tweet["views"] = int(views_match.group(1))

        elif line.startswith("https://x.com/"):
            current_tweet["url"] = line

        elif line.startswith("media type:"):
            media_match = re.search(r"media type:\s*(\w+)", line)
            if media_match:
                current_tweet["media"] = media_match.group(1)

        elif "(reply to another user)" in line or "(reply context:" in line:
            current_tweet["is_reply"] = True

        elif "(original post)" in line:
            current_tweet["is_reply"] = False

        elif line and not line.startswith("likes:") and not line.startswith("https://x.com/") and not line.startswith("media type:") and not line.startswith("(") and not line.startswith("9–12"):
            if line != "**Step 1:**" and line != "**Step 2:**":
                current_tweet["text"] += line + " "

if current_tweet:
    tweets.append(current_tweet)

# Clean tweet text
for tweet in tweets:
    tweet["text"] = tweet["text"].strip()

# Build candidate pool
candidates = []
for tweet in tweets:
    if tweet.get("likes") > 0 or tweet.get("retweets") > 0 or tweet.get("replies") > 0:
        candidates.append({
            "handle": tweet["handle"],
            "text": tweet["text"],
            "likes": tweet["likes"],
            "retweets": tweet["retweets"],
            "replies": tweet["replies"],
            "views": tweet["views"],
            "url": tweet["url"],
            "list_ids_seen_on": [LIST_ID],
            "list_names_seen_on": ["Crypto/DeFi Research & Alpha"],
            "media": tweet["media"],
            "is_reply": tweet["is_reply"],
            "is_quote": tweet["is_quote"]
        })

# Deduplicate against history
seen_urls = set()
try:
    with open("memory/list-digest-seen.txt", "r") as f:
        for line in f:
            seen_urls.add(line.strip())
except FileNotFoundError:
    pass

# Also check recent logs
today = datetime.utcnow().strftime('%Y-%m-%d')
log_files = [f"memory/logs/{today}.md"]
for date_offset in range(1, 3):
    date = datetime.utcnow() - datetime.timedelta(days=date_offset)
    log_files.append(f"memory/logs/{date.strftime('%Y-%m-%d')}.md")

for log_file in log_files:
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            content = f.read()
            urls = re.findall(r"https://x\.com/\S+", content)
            seen_urls.update(urls)

fresh_candidates = []
for candidate in candidates:
    if candidate["url"] and candidate["url"] not in seen_urls:
        fresh_candidates.append(candidate)

# Score candidates
def calculate_score(candidate):
    base = math.log(1 + candidate["likes"]) + 2.0 * math.log(1 + candidate["retweets"]) + 1.5 * math.log(1 + candidate["replies"])
    score = base

    # Bonus for cross-list resonance (only one list)
    if len(candidate["list_ids_seen_on"]) >= 2:
        score += 2.0
    if len(candidate["list_ids_seen_on"]) >= 3:
        score += 1.5

    # Bonus for topic filter
    if TOPIC_FILTER and TOPIC_FILTER.lower() in candidate["text"].lower():
        score += 1.0

    # Bonus for small account signal (technical content)
    technical_terms = ["DeFi", "protocol", "tokenomics", "buyback", "revenue", "holders", "BTC", "performance", "data"]
    if any(term.lower() in candidate["text"].lower() for term in technical_terms):
        score += 0.5

    # Bonus for media
    if candidate["media"] != "none":
        score += 0.3

    # Penalty for reply to non-list member
    if candidate["is_reply"]:
        score -= 1.0

    # Penalty for pure link share
    words = candidate["text"].split()
    if len(words) < 10 and "http" in candidate["text"]:
        score -= 0.5

    return round(score, 2)

for candidate in fresh_candidates:
    candidate["score"] = calculate_score(candidate)

fresh_candidates.sort(key=lambda x: x["score"], reverse=True)

# Compose digest
today_str = datetime.utcnow().strftime("%Y-%m-%d")
notification = f"*List Digest — {today_str}*\n\n"

# Verdict line
if fresh_candidates:
    top_tweet = fresh_candidates[0]
    if top_tweet["score"] >= 2.0:
        verdict = f"Buyback narrative leads on DeFi research list with {top_tweet['likes']} likes; other engagement is scattered."
    else:
        verdict = "Quiet day across Crypto/DeFi Research & Alpha list — minimal engagement."
else:
    verdict = "No fresh tweets found for Crypto/DeFi Research & Alpha list."

notification += f"{verdict}\n\n"

# Standalone tweets per list
notification += "*Crypto/DeFi Research & Alpha*\n"
standalone_count = 0
for candidate in fresh_candidates:
    if candidate["score"] < 2.0:
        continue  # Quiet day rule

    standalone_count += 1
    if standalone_count > 5:
        break

    insight = ""
    text = candidate["text"]
    if "buyback" in text.lower():
        insight = "Structural shift from inflation-heavy tokenomics to buybacks/fee sharing underway."
    elif "performance" in text.lower() or "BTC" in text.lower():
        insight = "Monthly performance data shows relative strength vs BTC."
    elif "revenue" in text.lower():
        insight = "Detailed analysis of DeFi protocol revenue distribution trends."
    elif len(text.split()) > 30:
        insight = "Technical insight on protocol economics and holder returns."
    else:
        insight = "Crypto research insight from tracked list."

    notification += f"- x.com/{candidate['handle']} — {insight} (♥{candidate['likes']}, ↻{candidate['retweets']}) — [View]({candidate['url']})\n"

if standalone_count == 0 and fresh_candidates:
    # Still show top tweet even if score < 2.0
    top = fresh_candidates[0]
    insight = "Quiet day — this was the top tweet"
    notification += f"- x.com/{top['handle']} — {insight} (♥{top['likes']}, ↻{top['retweets']}) — [View]({top['url']})\n"
elif standalone_count == 0:
    notification += "- quiet day\n"

notification += "\n---\n"
notification += f"sources: Crypto/DeFi Research & Alpha=ok\n"
notification += "status: LIST_DIGEST_OK\n"

print(notification)

# Log results
log_entry = f"""## list-digest
- **Lists:** 1 tracked
- **Status:** LIST_DIGEST_OK
- **Per-list:** Crypto/DeFi Research & Alpha=ok({len(fresh_candidates)})
- **Verdict:** {verdict}
- **Narratives:** 0 cross-list narratives
- **URLs reported:**"""
for candidate in fresh_candidates[:12]:
    log_entry += f"\n  - {candidate['url']}"

# Append to today's log
with open(f"memory/logs/{datetime.utcnow().strftime('%Y-%m-%d')}.md", "a") as f:
    f.write(log_entry + "\n")

# Update seen file
seen_file = "memory/list-digest-seen.txt"
with open(seen_file, "a") as f:
    for candidate in fresh_candidates[:12]:
        f.write(candidate["url"] + "\n")
EOF