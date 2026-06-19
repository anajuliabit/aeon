import json
import re
from datetime import datetime, timedelta, timezone

# Load cached data
with open('/home/runner/work/aeon/aeon/.xai-cache/agent-buzz.json', 'r') as f:
    data = json.load(f)

# Extract text
text = ""
for output in data['output']:
    if output['type'] == 'message':
        for content in output['content']:
            if content['type'] == 'output_text':
                text = content['text']

# Parse candidates
candidates = []
lines = text.strip().split('\n\n')
for block in lines:
    if not block.strip():
        continue
    if block.startswith('('):  # Skip footer
        continue

    # Parse handle
    handle_match = re.search(r'\*\*@(\w+)\*\*', block)
    if not handle_match:
        continue
    handle = handle_match.group(1)

    # Parse rest
    lines_in_block = block.split('\n')
    if len(lines_in_block) < 3:
        continue

    # Extract followers
    followers_text = lines_in_block[0]
    followers_match = re.search(r'followers: (\d+|null)', followers_text)
    follower_count = int(followers_match.group(1)) if followers_match and followers_match.group(1) != 'null' else None

    # Extract role
    role_match = re.search(r'role: (\w+)', followers_text)
    role = role_match.group(1) if role_match else 'anon'

    # Extract claim (second line)
    claim = lines_in_block[1].strip().strip('"')

    # Extract engagement numbers
    likes_match = re.search(r'likes: (\d+)', block)
    likes = int(likes_match.group(1)) if likes_match else 0

    retweets_match = re.search(r'retweets: (\d+)', block)
    retweets = int(retweets_match.group(1)) if retweets_match else 0

    replies_match = re.search(r'replies: (\d+)', block)
    replies = int(replies_match.group(1)) if replies_match else 0

    # Extract posted_at
    date_match = re.search(r'posted_at: (\S+)', block)
    posted_at = date_match.group(1) if date_match else ''

    # Extract direct_link
    link_match = re.search(r'direct_link: (\S+)', block)
    direct_link = link_match.group(1) if link_match else ''

    candidates.append({
        'handle': handle,
        'follower_count': follower_count,
        'role_guess': role,
        'claim': claim,
        'likes': likes,
        'retweets': retweets,
        'replies': replies,
        'posted_at': posted_at,
        'direct_link': direct_link
    })

print(f"Found {len(candidates)} candidates")
for i, c in enumerate(candidates):
    print(f"{i+1}. @{c['handle']} ({c['role_guess']}): {c['claim'][:50]}... Likes: {c['likes']}, RT: {c['retweets']}, Replies: {c['replies']}")