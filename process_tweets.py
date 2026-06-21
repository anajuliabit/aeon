import json
import re
import math
from datetime import datetime, timedelta

# Read cached data
with open('/home/runner/work/aeon/aeon/.xai-cache/list-digest-1642770456720683008.json', 'r') as f:
    data = json.load(f)

# Extract the text response
text = data['output'][-1]['content'][0]['text']

# Parse list info
list_id = "1642770456720683008"
list_name = "Crypto/DeFi Research & Alpha"
list_description = "A curated list of DeFi, crypto, and AI-focused accounts sharing research, data, and market insights"

# Parse tweets from the text
tweets = []
current_tweet = {}

lines = text.split('\n')
i = 0
while i < len(lines):
    line = lines[i].strip()

    # Check for tweet marker like "1. **@Flowslikeosmo**"
    tweet_match = re.match(r'^(\d+)\.\s+\*\*@(\w+)\*\*', line)
    if tweet_match:
        if current_tweet:
            tweets.append(current_tweet)
        current_tweet = {
            'handle': tweet_match.group(2),
            'text': '',
            'likes': 0,
            'retweets': 0,
            'replies': 0,
            'views': 0,
            'url': '',
            'media': 'none',
            'is_reply': False,
            'is_quote': False,
            'list_ids_seen_on': [list_id],
            'list_names_seen_on': [list_name]
        }

        # Look for tweet text in next lines
        tweet_text_lines = []
        j = i + 1
        while j < len(lines) and not lines[j].strip().startswith('likes:'):
            tweet_text_lines.append(lines[j].strip())
            j += 1
        current_tweet['text'] = ' '.join(tweet_text_lines).strip()
        i = j - 1

    elif line.startswith('likes:'):
        # Parse engagement metrics
        likes_match = re.search(r'likes:(\d+)', line)
        retweets_match = re.search(r'retweets:(\d+)', line)
        replies_match = re.search(r'replies:(\d+)', line)
        views_match = re.search(r'views:(\d+)', line)

        if likes_match:
            current_tweet['likes'] = int(likes_match.group(1))
        if retweets_match:
            current_tweet['retweets'] = int(retweets_match.group(1))
        if replies_match:
            current_tweet['replies'] = int(replies_match.group(1))
        if views_match:
            current_tweet['views'] = int(views_match.group(1))

    elif line.startswith('https://x.com/'):
        current_tweet['url'] = line.strip()

    elif line.startswith('media type:'):
        media_match = re.search(r'media type:\s*(\w+)', line)
        if media_match:
            current_tweet['media'] = media_match.group(1)

    elif '(reply to another user)' in line or '(reply context: replying in a thread)' in line:
        current_tweet['is_reply'] = True

    elif '(original post)' in line:
        current_tweet['is_reply'] = False

    i += 1

# Add last tweet
if current_tweet:
    tweets.append(current_tweet)

# Read seen URLs
seen_urls = set()
try:
    with open('/home/runner/work/aeon/aeon/memory/list-digest-seen.txt', 'r') as f:
        seen_urls.update(line.strip() for line in f if line.strip())
except FileNotFoundError:
    pass

# Read recent logs for additional seen URLs
import glob
log_files = glob.glob('/home/runner/work/aeon/aeon/memory/logs/2026-06-*.md')
for log_file in log_files:
    try:
        with open(log_file, 'r') as f:
            content = f.read()
            urls = re.findall(r'https://x\.com/\S+', content)
            seen_urls.update(urls)
    except:
        pass

# Filter out seen tweets
fresh_tweets = []
for tweet in tweets:
    if 'url' in tweet and tweet['url']:
        if tweet['url'] not in seen_urls:
            fresh_tweets.append(tweet)
        else:
            print(f"Filtered out seen tweet: {tweet['url']}")

# Calculate signal scores
def calculate_score(tweet):
    base = math.log(1 + tweet['likes']) + 2.0 * math.log(1 + tweet['retweets']) + 1.5 * math.log(1 + tweet['replies'])
    score = base

    # Bonus for cross-list resonance (only one list here)
    if len(tweet['list_ids_seen_on']) >= 2:
        score += 2.0
    if len(tweet['list_ids_seen_on']) >= 3:
        score += 1.5

    # Bonus for topic filter (none set)

    # Bonus for small account signal (assume technical content)
    # Check if tweet text suggests technical/insider content
    technical_terms = ['DeFi', 'protocol', 'tokenomics', 'buyback', 'revenue', 'holders', 'BTC', 'performance', 'data']
    tweet_lower = tweet['text'].lower()
    if any(term.lower() in tweet_lower for term in technical_terms):
        score += 0.5

    # Bonus for media
    if tweet['media'] != 'none':
        score += 0.3

    # Penalty for reply to non-list member
    if tweet['is_reply']:
        score -= 1.0

    # Penalty for pure link share
    if len(tweet['text'].split()) < 10 and 'http' in tweet['text']:
        score -= 0.5

    return score

for tweet in fresh_tweets:
    tweet['score'] = calculate_score(tweet)

# Sort by score
fresh_tweets.sort(key=lambda x: x['score'], reverse=True)

print(f"List: {list_name}")
print(f"Description: {list_description}")
print(f"Total tweets parsed: {len(tweets)}")
print(f"Fresh tweets (not seen): {len(fresh_tweets)}")
print("\nFresh tweets with scores:")
for i, tweet in enumerate(fresh_tweets[:12]):
    print(f"{i+1}. @{tweet['handle']} - Score: {tweet['score']:.2f}")
    print(f"   Text: {tweet['text'][:100]}...")
    print(f"   Likes: {tweet['likes']}, RTs: {tweet['retweets']}, Replies: {tweet['replies']}")
    print(f"   URL: {tweet['url']}")
    print(f"   Media: {tweet['media']}, Is reply: {tweet['is_reply']}")
    print()