#!/usr/bin/env python3
import json
import re
import math
import sys
from datetime import datetime, timedelta

def parse_grok_response(text):
    """
    Parse the Grok response text to extract tweets.
    Expected format:
    1. **@handle**
       Tweet text...
       likes:N, retweets:N, replies:N, views:N
       https://x.com/handle/status/id
       media type: type
       (reply/original context)
    """
    tweets = []

    # Split by numbered items (1., 2., etc.)
    sections = re.split(r'\n\d+\.\s+\*\*@(\w+)\*\*', text)

    if len(sections) < 2:
        # Alternative parsing - look for handle patterns
        lines = text.split('\n')
        i = 0
        while i < len(lines):
            line = lines[i]
            # Check for tweet header pattern
            if re.match(r'\d+\.\s+\*\*@(\w+)\*\*', line):
                handle = re.search(r'\*\*@(\w+)\*\*', line).group(1)

                # Find tweet text (next lines until metrics)
                tweet_text = ''
                j = i + 1
                while j < len(lines) and not lines[j].strip().startswith('likes:'):
                    tweet_text += lines[j] + ' '
                    j += 1

                # Parse metrics
                likes = 0
                retweets = 0
                replies = 0
                views = 0
                url = ''
                media = 'none'
                is_reply = False

                while j < len(lines):
                    metric_line = lines[j].strip()
                    if metric_line.startswith('likes:'):
                        likes_match = re.search(r'likes:(\d+)', metric_line)
                        if likes_match:
                            likes = int(likes_match.group(1))
                        retweets_match = re.search(r'retweets:(\d+)', metric_line)
                        if retweets_match:
                            retweets = int(retweets_match.group(1))
                        replies_match = re.search(r'replies:(\d+)', metric_line)
                        if replies_match:
                            replies = int(replies_match.group(1))
                        views_match = re.search(r'views:(\d+)', metric_line)
                        if views_match:
                            views = int(views_match.group(1))
                    elif metric_line.startswith('https://x.com/'):
                        url = metric_line.strip()
                    elif metric_line.startswith('media type:'):
                        media_match = re.search(r'media type:\s*(\w+)', metric_line)
                        if media_match:
                            media = media_match.group(1)
                    elif '(reply to another user)' in metric_line or '(reply context:' in metric_line:
                        is_reply = True
                    elif '(original post)' in metric_line:
                        is_reply = False

                    j += 1
                    # Stop after we've parsed all metrics and URL
                    if url and 'likes:' in metric_line:
                        break

                tweet = {
                    'handle': handle,
                    'text': tweet_text.strip(),
                    'likes': likes,
                    'retweets': retweets,
                    'replies': replies,
                    'views': views,
                    'url': url,
                    'media': media,
                    'is_reply': is_reply,
                    'is_quote': False,
                    'list_ids_seen_on': ['1642770456720683008'],
                    'list_names_seen_on': ['Crypto/DeFi Research & Alpha']
                }
                tweets.append(tweet)

                i = j
            else:
                i += 1

    return tweets

def calculate_score(tweet):
    base = math.log(1 + tweet['likes']) + 2.0 * math.log(1 + tweet['retweets']) + 1.5 * math.log(1 + tweet['replies'])
    score = base

    # Bonus for cross-list resonance (only one list here)
    if len(tweet['list_ids_seen_on']) >= 2:
        score += 2.0
    if len(tweet['list_ids_seen_on']) >= 3:
        score += 1.5

    # Bonus for small account signal (technical content)
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

    return round(score, 2)

def main():
    # Read cached data
    with open('/home/runner/work/aeon/aeon/.xai-cache/list-digest-1642770456720683008.json', 'r') as f:
        data = json.load(f)

    text = data['output'][-1]['content'][0]['text']

    # Parse tweets
    tweets = parse_grok_response(text)

    # Read seen URLs
    seen_urls = set()
    try:
        with open('/home/runner/work/aeon/aeon/memory/list-digest-seen.txt', 'r') as f:
            seen_urls.update(line.strip() for line in f if line.strip())
    except FileNotFoundError:
        pass

    # Also check recent logs
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

    # Filter fresh tweets
    fresh_tweets = []
    for tweet in tweets:
        if tweet.get('url') and tweet['url'] not in seen_urls:
            tweet['score'] = calculate_score(tweet)
            fresh_tweets.append(tweet)

    # Sort by score
    fresh_tweets.sort(key=lambda x: x['score'], reverse=True)

    print(f"List: Crypto/DeFi Research & Alpha")
    print(f"Tweets parsed: {len(tweets)}")
    print(f"Fresh tweets: {len(fresh_tweets)}")
    print()

    # Print results
    for i, tweet in enumerate(fresh_tweets[:12]):
        print(f"{i+1}. @{tweet['handle']} - Score: {tweet['score']}")
        print(f"   Text: {tweet['text'][:80]}...")
        print(f"   Likes: {tweet['likes']}, RTs: {tweet['retweets']}, Replies: {tweet['replies']}")
        print(f"   URL: {tweet['url']}")
        print(f"   Media: {tweet['media']}, Reply: {tweet['is_reply']}")
        print()

if __name__ == '__main__':
    main()