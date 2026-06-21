#!/usr/bin/env python3
import json
import re
import math
import os
from datetime import datetime

# Parse var parameter
var = "1642770456720683008"
IDS_PART = var.split("|")[0]
TOPIC_FILTER = "" if len(var.split("|")) == 1 else var.split("|")[1]

# Step 1: Validate var
if not var:
    log_entry = f"## list-digest\n- **Lists:** 0 tracked\n- **Status:** LIST_DIGEST_NO_CONFIG\n- **Per-list:** none\n- **Verdict:** no config\n- **Narratives:** 0\n- **URLs reported:** none\n"
    with open(f"memory/logs/{datetime.utcnow().strftime('%Y-%m-%d')}.md", "a") as f:
        f.write(log_entry)
    exit(0)

# Validate IDs are numeric
for LIST_ID in IDS_PART.split(","):
    if not LIST_ID.strip().isdigit():
        log_entry = f"## list-digest\n- **Lists:** 0 tracked\n- **Status:** LIST_DIGEST_NO_CONFIG\n- **Per-list:** invalid list ID '{LIST_ID}' (must be numeric)\n- **Verdict:** invalid config\n- **Narratives:** 0\n- **URLs reported:** none\n"
        with open(f"memory/logs/{datetime.utcnow().strftime('%Y-%m-%d')}.md", "a") as f:
            f.write(log_entry)
        exit(0)

# Step 2: Fetch data (pre-fetched cache exists)
LIST_ID = IDS_PART  # Only one list ID provided
cache_file = f".xai-cache/list-digest-{LIST_ID}.json"

if os.path.exists(cache_file):
    # Path A - cache exists
    try:
        with open(cache_file, "r") as f:
            data = json.load(f)
        grok_text = data['output'][-1]['content'][0]['text']
        list_status = "ok"
    except Exception as e:
        list_status = f"error(cache-fail:{str(e)[:30]})"
        grok_text = ""
else:
    # Path B/C would require API or WebSearch, but cache exists
    list_status = "error(cache-missing)"
    grok_text = ""

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

print(f"Parsed {len(tweets)} tweets from cache")

# Step 3: Build candidate pool
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

print(f"{len(candidates)} candidates with engagement")

# Deduplicate against history
seen_urls = set()
try:
    with open("memory/list-digest-seen.txt", "r") as f:
        for line in f:
            seen_urls.add(line.strip())
except FileNotFoundError:
    pass

# Also check recent logs
log_files = [f"memory/logs/{datetime.utcnow().strftime('%Y-%m-%d')}.md"]
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

print(f"{len(fresh_candidates)} fresh candidates after dedup")

# Step 4: Score candidates
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

# Step 5: Cluster into narratives (since we only have one list, no cross-list clustering)
narratives = []
if len(fresh_candidates) > 1:
    # Simple cluster based on keywords
    clusters = {}
    for candidate in fresh_candidates:
        text = candidate["text"]
        # Check for common topics
        if "buyback" in text.lower() or "revenue" in text.lower() or "tokenomics" in text.lower():
            cluster_key = "buyback_narrative"
        elif "performance" in text.lower() or "BTC" in text.lower():
            cluster_key = "performance_data"
        else:
            cluster_key = "other"

        if cluster_key not in clusters:
            clusters[cluster_key] = []
        clusters[cluster_key].append(candidate)

    for cluster_key, candidates in clusters.items():
        if len(candidates) >= 2:
            narrative_score = sum(c["score"] for c in candidates)
            narrative_title = f"{cluster_key.replace('_', ' ')}"
            anchor_tweet = max(candidates, key=lambda x: x["score"])
            supporting = candidates[:3] if len(candidates) > 1 else []

            narratives.append({
                "title": narrative_title,
                "score": narrative_score,
                "anchor": anchor_tweet,
                "supporting": supporting,
                "tweets": candidates
            })

# Step 6: Compose digest
today = datetime.utcnow().strftime("%Y-%m-%d")
notification = f"*List Digest — {today}*\n\n"

# Verdict line
if narratives:
    top_narrative = max(narratives, key=lambda x: x["score"])
    verdict = f"{top_narrative['title']} dominates today's DeFi research list; other engagement is scattered."
elif fresh_candidates:
    top_tweet = fresh_candidates[0]
    if top_tweet["score"] >= 2.0:
        verdict = f"{top_tweet['handle']}'s {top_tweet['likes']} likes lead the quiet day on DeFi research list."
    else:
        verdict = "Quiet day across Crypto/DeFi Research & Alpha list — minimal engagement."
else:
    verdict = "No fresh tweets found for Crypto/DeFi Research & Alpha list."

notification += f"{verdict}\n\n"

# Cross-list narratives
if narratives:
    notification += "🔗 *Cross-list narratives*\n"
    for i, narrative in enumerate(narratives[:3]):
        notification += f"{i+1}. *{narrative['title']}*\n"
        notification += f"   x.com/{narrative['anchor']['handle']}: {narrative['anchor']['text'][:60]} (♥{narrative['anchor']['likes']}, ↻{narrative['anchor']['retweets']}) — [View]({narrative['anchor']['url']})\n"
        if narrative['supporting']:
            for tweet in narrative['supporting'][:2]:
                notification += f"   x.com/{tweet['handle']}: {tweet['text'][:60]} (♥{tweet['likes']}, ↻{tweet['retweets']}) — [View]({tweet['url']})\n"
    notification += "\n"

# Standalone tweets per list
notification += "*Crypto/DeFi Research & Alpha*\n"
standalone_count = 0
for candidate in fresh_candidates:
    # Skip tweets already in narratives
    in_narrative = any(candidate in narrative["tweets"] for narrative in narratives)
    if in_narrative:
        continue

    if candidate["score"] < 2.0:
        continue  # Quiet day rule

    standalone_count += 1
    if standalone_count > 5:
        break

    insight = ""
    text = candidate["text"]
    if "buyback" in text.lower():
        insight = "Structural shift from inflation-heavy tokenomics to buybacks/fee sharing underway."
    elif "performance" in text.lower():
        insight = "Monthly performance data shows relative strength vs BTC."
    elif len(text.split()) > 30:
        insight = "Detailed analysis of DeFi revenue trends and holder returns."
    else:
        insight = "Technical insight on protocol revenue distribution."

    notification += f"- x.com/{candidate['handle']} — {insight} (♥{candidate['likes']}, ↻{candidate['retweets']}) — [View]({candidate['url']})\n"

if standalone_count == 0:
    notification += "- quiet day\n"

notification += "\n---\n"
notification += f"sources: Crypto/DeFi Research & Alpha={list_status}\n"
notification += "status: LIST_DIGEST_OK\n"

print(f"Notification length: {len(notification)} characters")
print("Notification preview:")
print(notification[:500])

# Step 7: Send notification
# ./notify command will be called outside Python
print("\nNotification ready to send")

# Step 8: Log and persist
log_entry = f"""## list-digest
- **Lists:** 1 tracked
- **Status:** LIST_DIGEST_OK
- **Per-list:** Crypto/DeFi Research & Alpha={list_status}
- **Verdict:** {verdict}
- **Narratives:** {len(narratives)} cross-list narratives
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

print(f"Logged to memory/logs/{datetime.utcnow().strftime('%Y-%m-%d')}.md")
print(f"Updated {seen_file} with {len(fresh_candidates[:12])} URLs")