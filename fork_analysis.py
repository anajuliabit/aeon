#!/usr/bin/env python3
"""Fork skill digest analysis script."""
import subprocess
import json
import yaml
import sys
import os
import math
from collections import Counter
import concurrent.futures
import base64

UPSTREAM_DEFAULTS = {
    "morning-brief": {"enabled": True, "schedule": "0 7 * * *", "model": None, "var": ""},
    "daily-routine": {"enabled": True, "schedule": "0 7 * * *", "model": None, "var": ""},
    "rss-digest": {"enabled": False, "schedule": "0 7 * * *", "model": None, "var": ""},
    "hacker-news-digest": {"enabled": False, "schedule": "0 7 * * *", "model": None, "var": ""},
    "paper-digest": {"enabled": False, "schedule": "0 7 * * *", "model": None, "var": ""},
    "reddit-digest": {"enabled": False, "schedule": "0 7 * * *", "model": None, "var": ""},
    "telegram-digest": {"enabled": False, "schedule": "30 7 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "issue-triage": {"enabled": False, "schedule": "0 9 * * *", "model": None, "var": ""},
    "pr-triage": {"enabled": False, "schedule": "30 9 * * *", "model": None, "var": ""},
    "pr-review": {"enabled": False, "schedule": "0 9 * * *", "model": None, "var": ""},
    "auto-merge": {"enabled": False, "schedule": "0 14 * * *", "model": None, "var": ""},
    "github-monitor": {"enabled": False, "schedule": "0 9 * * *", "model": None, "var": ""},
    "github-issues": {"enabled": False, "schedule": "0 9 * * *", "model": None, "var": ""},
    "github-trending": {"enabled": True, "schedule": "0 9 * * *", "model": None, "var": ""},
    "github-releases": {"enabled": False, "schedule": "30 9 * * *", "model": None, "var": ""},
    "huggingface-trending": {"enabled": False, "schedule": "30 9 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "token-alert": {"enabled": True, "schedule": "0 12 * * *", "model": None, "var": ""},
    "token-movers": {"enabled": True, "schedule": "10 12 * * *", "model": None, "var": ""},
    "on-chain-monitor": {"enabled": True, "schedule": "20 12 * * *", "model": None, "var": ""},
    "defi-monitor": {"enabled": True, "schedule": "40 12 * * *", "model": None, "var": ""},
    "treasury-info": {"enabled": False, "schedule": "0 12 * * *", "model": None, "var": ""},
    "distribute-tokens": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "defi-overview": {"enabled": True, "schedule": "0 12 * * *", "model": None, "var": ""},
    "monitor-polymarket": {"enabled": False, "schedule": "30 12 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "monitor-kalshi": {"enabled": False, "schedule": "0 13 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "monitor-runners": {"enabled": False, "schedule": "0 12 * * *", "model": None, "var": ""},
    "token-pick": {"enabled": True, "schedule": "0 12 * * *", "model": None, "var": ""},
    "token-report": {"enabled": False, "schedule": "30 12 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "price-threshold-alert": {"enabled": False, "schedule": "*/30 * * * *", "model": "claude-sonnet-4-6", "var": ""},
    "market-context-refresh": {"enabled": True, "schedule": "0 13 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "btc-levels": {"enabled": True, "schedule": "15 */4 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "narrative-tracker": {"enabled": True, "schedule": "30 13 * * *", "model": None, "var": ""},
    "polymarket-comments": {"enabled": False, "schedule": "0 13 * * *", "model": None, "var": ""},
    "unlock-monitor": {"enabled": True, "schedule": "0 10 * * 1", "model": None, "var": ""},
    "aixbt-pulse": {"enabled": True, "schedule": "0 9,21 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "article": {"enabled": False, "schedule": "0 14 * * *", "model": None, "var": ""},
    "technical-explainer": {"enabled": False, "schedule": "30 14 * * *", "model": None, "var": ""},
    "digest": {"enabled": False, "schedule": "0 14 * * *", "model": None, "var": ""},
    "research-brief": {"enabled": False, "schedule": "0 14 * * *", "model": None, "var": ""},
    "deep-research": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "last30": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "paper-pick": {"enabled": False, "schedule": "0 14 * * *", "model": None, "var": ""},
    "search-skill": {"enabled": True, "schedule": "0 14 * * *", "model": None, "var": ""},
    "security-digest": {"enabled": True, "schedule": "0 14 * * *", "model": None, "var": ""},
    "idea-capture": {"enabled": False, "schedule": "0 14 * * *", "model": None, "var": ""},
    "deal-flow": {"enabled": True, "schedule": "0 14 * * 1", "model": None, "var": ""},
    "reg-monitor": {"enabled": True, "schedule": "0 14 * * 3", "model": None, "var": ""},
    "push-recap": {"enabled": False, "schedule": "0 15 * * *", "model": None, "var": ""},
    "repo-article": {"enabled": False, "schedule": "0 15 * * *", "model": None, "var": ""},
    "repo-actions": {"enabled": False, "schedule": "0 15 * * *", "model": None, "var": ""},
    "repo-pulse": {"enabled": False, "schedule": "0 15 * * *", "model": None, "var": ""},
    "star-milestone": {"enabled": False, "schedule": "15 15 * * *", "model": None, "var": ""},
    "star-momentum-alert": {"enabled": False, "schedule": "10 10 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "project-lens": {"enabled": False, "schedule": "30 15 * * 1,3,5", "model": None, "var": ""},
    "repo-scanner": {"enabled": False, "schedule": "0 15 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "skill-security-scan": {"enabled": True, "schedule": "0 16 * * 1", "model": None, "var": ""},
    "code-health": {"enabled": False, "schedule": "0 16 * * *", "model": None, "var": ""},
    "changelog": {"enabled": False, "schedule": "0 16 * * *", "model": None, "var": ""},
    "external-feature": {"enabled": False, "schedule": "30 16 * * *", "model": None, "var": ""},
    "vuln-scanner": {"enabled": True, "schedule": "0 16 * * 6", "model": None, "var": ""},
    "deploy-prototype": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "autoresearch": {"enabled": True, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "create-skill": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "fetch-tweets": {"enabled": False, "schedule": "0 17 * * *", "model": None, "var": "@moonwell OR @reppo OR @sherwoodagent OR $WOOD OR $MAMO"},
    "refresh-x": {"enabled": False, "schedule": "0 17 * * *", "model": None, "var": ""},
    "list-digest": {"enabled": True, "schedule": "0 17 * * *", "model": None, "var": "1642770456720683008"},
    "write-tweet": {"enabled": False, "schedule": "0 17 * * *", "model": None, "var": ""},
    "reply-maker": {"enabled": False, "schedule": "0 17 * * *", "model": None, "var": ""},
    "remix-tweets": {"enabled": False, "schedule": "30 17 * * *", "model": None, "var": ""},
    "tweet-roundup": {"enabled": False, "schedule": "0 17 * * *", "model": None, "var": ""},
    "agent-buzz": {"enabled": True, "schedule": "30 17 * * *", "model": None, "var": ""},
    "farcaster-digest": {"enabled": False, "schedule": "0 17 * * *", "model": None, "var": ""},
    "vibecoding-digest": {"enabled": False, "schedule": "30 17 * * *", "model": None, "var": ""},
    "channel-recap": {"enabled": False, "schedule": "0 17 * * 0", "model": None, "var": ""},
    "rss-feed": {"enabled": False, "schedule": "30 17 * * *", "model": None, "var": ""},
    "thread-formatter": {"enabled": False, "schedule": "30 17 * * *", "model": None, "var": ""},
    "update-gallery": {"enabled": False, "schedule": "0 18 * * 0", "model": None, "var": ""},
    "syndicate-article": {"enabled": False, "schedule": "30 15 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "goal-tracker": {"enabled": True, "schedule": "0 18 * * *", "model": None, "var": ""},
    "skill-health": {"enabled": True, "schedule": "0 18 * * *", "model": None, "var": ""},
    "skill-analytics": {"enabled": True, "schedule": "30 18 * * 3", "model": "claude-sonnet-4-6", "var": ""},
    "self-improve": {"enabled": True, "schedule": "0 18 1/2 * *", "model": None, "var": ""},
    "reflect": {"enabled": True, "schedule": "0 18 * * *", "model": None, "var": ""},
    "action-converter": {"enabled": True, "schedule": "0 18 * * *", "model": None, "var": ""},
    "startup-idea": {"enabled": False, "schedule": "0 18 * * *", "model": None, "var": ""},
    "tool-builder": {"enabled": False, "schedule": "reactive", "model": None, "var": ""},
    "skill-repair": {"enabled": False, "schedule": "reactive", "model": None, "var": ""},
    "evening-recap": {"enabled": True, "schedule": "0 21 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "thought-review": {"enabled": True, "schedule": "0 7,21 * * *", "model": None, "var": "24"},
    "vercel-projects": {"enabled": False, "schedule": "0 18 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "cost-report": {"enabled": True, "schedule": "0 7 * * 1", "model": "claude-sonnet-4-6", "var": ""},
    "ai-framework-watch": {"enabled": False, "schedule": "30 8 * * 1", "model": "claude-sonnet-4-6", "var": ""},
    "competitor-launch-radar": {"enabled": False, "schedule": "0 10 * * 1", "model": None, "var": " "},
    "fleet-state": {"enabled": False, "schedule": "0 8 * * 1", "model": "claude-sonnet-4-6", "var": ""},
    "fork-fleet": {"enabled": False, "schedule": "0 10 * * 1", "model": None, "var": ""},
    "fork-cohort": {"enabled": True, "schedule": "0 19 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "fork-release-tracker": {"enabled": False, "schedule": "30 19 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "contributor-spotlight": {"enabled": False, "schedule": "0 20 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "fork-first-run-alert": {"enabled": False, "schedule": "30 20 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "skill-evals": {"enabled": True, "schedule": "0 6 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "skill-update-check": {"enabled": True, "schedule": "0 19 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "spawn-instance": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "fleet-control": {"enabled": True, "schedule": "0 9,15 * * *", "model": None, "var": ""},
    "weekly-review": {"enabled": True, "schedule": "0 19 * * 1", "model": None, "var": ""},
    "weekly-shiplog": {"enabled": True, "schedule": "0 9 * * 1", "model": None, "var": ""},
    "skill-leaderboard": {"enabled": False, "schedule": "0 17 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "fork-contributor-leaderboard": {"enabled": False, "schedule": "30 17 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "contributor-reward": {"enabled": False, "schedule": "30 9 * * 1", "model": "claude-sonnet-4-6", "var": ""},
    "operator-scorecard": {"enabled": True, "schedule": "30 10 * * 1", "model": "claude-sonnet-4-6", "var": ""},
    "fork-skill-digest": {"enabled": True, "schedule": "30 18 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "fork-skill-gap": {"enabled": True, "schedule": "0 21 * * 0", "model": "claude-sonnet-4-6", "var": ""},
    "workflow-security-audit": {"enabled": False, "schedule": "0 16 * * 0", "model": None, "var": ""},
    "skill-graph": {"enabled": True, "schedule": "0 17 * * 0", "model": None, "var": ""},
    "skill-freshness": {"enabled": True, "schedule": "0 8 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "smithery-manifest": {"enabled": False, "schedule": "0 6 1/7 * *", "model": "claude-sonnet-4-6", "var": ""},
    "show-hn-draft": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "product-hunt-launch": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "v4-readiness": {"enabled": False, "schedule": "workflow_dispatch", "model": "claude-sonnet-4-6", "var": ""},
    "schedule-ads": {"enabled": False, "schedule": "0 8 * * *", "model": "claude-sonnet-4-6", "var": ""},
    "create-campaign": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "auto-workflow": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "onboard": {"enabled": False, "schedule": "workflow_dispatch", "model": None, "var": ""},
    "reppo-orchestrator": {"enabled": False, "schedule": None, "model": None, "var": ""},
    "reppo-trading-agent": {"enabled": False, "schedule": None, "model": None, "var": ""},
    "reppo-voter": {"enabled": False, "schedule": None, "model": None, "var": ""},
    "reppo-digest": {"enabled": False, "schedule": None, "model": None, "var": ""},
    "heartbeat": {"enabled": True, "schedule": "0 8,14,20 * * *", "model": None, "var": ""},
}

UPSTREAM_SKILLS = set([
    "action-converter","agent-buzz","ai-framework-watch","aixbt-pulse","article","auto-merge",
    "auto-workflow","autoresearch","btc-levels","changelog","channel-recap","code-health",
    "competitor-launch-radar","contributor-reward","contributor-spotlight","cost-report",
    "create-campaign","create-skill","daily-routine","deal-flow","deep-research","defi-monitor",
    "defi-overview","deploy-prototype","digest","distribute-tokens","evening-recap","external-feature",
    "farcaster-digest","fetch-tweets","fleet-control","fleet-state","fork-cohort",
    "fork-contributor-leaderboard","fork-first-run-alert","fork-fleet","fork-release-tracker",
    "fork-skill-digest","fork-skill-gap","github-issues","github-monitor","github-releases",
    "github-trending","goal-tracker","hacker-news-digest","heartbeat","huggingface-trending",
    "idea-capture","issue-triage","last30","list-digest","market-context-refresh","monitor-kalshi",
    "monitor-polymarket","monitor-runners","morning-brief","narrative-tracker","on-chain-monitor",
    "onboard","operator-scorecard","paper-digest","paper-pick","polymarket-comments","pr-review",
    "pr-triage","price-threshold-alert","product-hunt-launch","project-lens","push-recap",
    "reddit-digest","reflect","refresh-x","reg-monitor","remix-tweets","reply-maker","repo-actions",
    "repo-article","repo-pulse","repo-scanner","reppo-digest","reppo-orchestrator",
    "reppo-trading-agent","reppo-voter","research-brief","rss-digest","rss-feed","schedule-ads",
    "search-skill","security","security-digest","self-improve","show-hn-draft","skill-analytics",
    "skill-evals","skill-freshness","skill-graph","skill-health","skill-leaderboard","skill-repair",
    "skill-security-scan","skill-update-check","smithery-manifest","spawn-instance","star-milestone",
    "star-momentum-alert","startup-idea","syndicate-article","technical-explainer","telegram-digest",
    "thought-review","thread-formatter","token-alert","token-movers","token-pick","token-report",
    "tool-builder","treasury-info","tweet-roundup","unlock-monitor","update-gallery","v4-readiness",
    "vercel-projects","vibecoding-digest","vuln-scanner","weekly-review","weekly-shiplog",
    "workflow-security-audit","write-tweet",
])

UPSTREAM_TAGS = {
    "morning-brief": ["content"],
    "daily-routine": ["meta"],
    "rss-digest": ["content"],
    "hacker-news-digest": ["content"],
    "paper-digest": ["content"],
    "reddit-digest": ["content"],
    "telegram-digest": ["content"],
    "issue-triage": ["dev"],
    "pr-triage": ["dev"],
    "pr-review": ["dev"],
    "auto-merge": ["dev"],
    "github-monitor": ["dev"],
    "github-issues": ["dev"],
    "github-trending": ["research"],
    "github-releases": ["research"],
    "huggingface-trending": ["research"],
    "token-alert": ["crypto"],
    "token-movers": ["crypto"],
    "on-chain-monitor": ["crypto"],
    "defi-monitor": ["crypto"],
    "treasury-info": ["crypto"],
    "distribute-tokens": ["crypto"],
    "defi-overview": ["crypto"],
    "monitor-polymarket": ["crypto"],
    "monitor-kalshi": ["crypto"],
    "monitor-runners": ["meta"],
    "token-pick": ["crypto"],
    "token-report": ["crypto"],
    "price-threshold-alert": ["crypto"],
    "market-context-refresh": ["crypto"],
    "btc-levels": ["crypto"],
    "narrative-tracker": ["crypto"],
    "polymarket-comments": ["crypto"],
    "unlock-monitor": ["crypto"],
    "aixbt-pulse": ["crypto"],
    "article": ["content"],
    "technical-explainer": ["content"],
    "digest": ["content"],
    "research-brief": ["content"],
    "deep-research": ["research"],
    "last30": ["research"],
    "paper-pick": ["research"],
    "search-skill": ["research"],
    "security-digest": ["content"],
    "idea-capture": ["meta"],
    "deal-flow": ["research"],
    "reg-monitor": ["research"],
    "push-recap": ["dev"],
    "repo-article": ["content"],
    "repo-actions": ["dev"],
    "repo-pulse": ["research"],
    "star-milestone": ["meta"],
    "star-momentum-alert": ["meta"],
    "project-lens": ["content"],
    "repo-scanner": ["research"],
    "skill-security-scan": ["dev"],
    "code-health": ["dev"],
    "changelog": ["dev"],
    "external-feature": ["dev"],
    "vuln-scanner": ["dev"],
    "deploy-prototype": ["dev"],
    "autoresearch": ["meta"],
    "create-skill": ["meta"],
    "fetch-tweets": ["social"],
    "refresh-x": ["social"],
    "list-digest": ["social"],
    "write-tweet": ["social"],
    "reply-maker": ["social"],
    "remix-tweets": ["social"],
    "tweet-roundup": ["social"],
    "agent-buzz": ["social"],
    "farcaster-digest": ["social"],
    "vibecoding-digest": ["social"],
    "channel-recap": ["social"],
    "rss-feed": ["meta"],
    "thread-formatter": ["social"],
    "update-gallery": ["meta"],
    "syndicate-article": ["content"],
    "goal-tracker": ["meta"],
    "skill-health": ["meta"],
    "skill-analytics": ["meta"],
    "self-improve": ["meta"],
    "reflect": ["meta"],
    "action-converter": ["meta"],
    "startup-idea": ["research"],
    "tool-builder": ["meta"],
    "skill-repair": ["meta"],
    "evening-recap": ["meta"],
    "thought-review": ["meta"],
    "vercel-projects": ["dev"],
    "cost-report": ["meta"],
    "ai-framework-watch": ["research"],
    "competitor-launch-radar": ["research"],
    "fleet-state": ["meta"],
    "fork-fleet": ["meta"],
    "fork-cohort": ["meta"],
    "fork-release-tracker": ["meta"],
    "contributor-spotlight": ["meta"],
    "fork-first-run-alert": ["meta"],
    "skill-evals": ["meta"],
    "skill-update-check": ["meta"],
    "spawn-instance": ["meta"],
    "fleet-control": ["meta"],
    "weekly-review": ["meta"],
    "weekly-shiplog": ["meta"],
    "skill-leaderboard": ["meta"],
    "fork-contributor-leaderboard": ["meta"],
    "contributor-reward": ["meta"],
    "operator-scorecard": ["meta"],
    "fork-skill-digest": ["meta"],
    "fork-skill-gap": ["meta"],
    "workflow-security-audit": ["dev"],
    "skill-graph": ["meta"],
    "skill-freshness": ["meta"],
    "smithery-manifest": ["meta"],
    "show-hn-draft": ["meta"],
    "product-hunt-launch": ["meta"],
    "v4-readiness": ["meta"],
    "schedule-ads": ["meta"],
    "create-campaign": ["meta"],
    "auto-workflow": ["meta"],
    "onboard": ["meta"],
    "reppo-orchestrator": ["meta"],
    "reppo-trading-agent": ["meta"],
    "reppo-voter": ["meta"],
    "reppo-digest": ["meta"],
    "heartbeat": ["meta"],
    "security": ["dev"],
}

ALL_FORKS = [
    "modelcollapse/aeon","wrenwealth/aeon","ghostx-dev/aeon","sinfronterasai/aeon",
    "gitlumen-team/aeon","ashneil12/aeon-upstream","AdversaLLC/aeon","anondevv69/bankr-space-aeon",
    "SahilParikh03/aeon","mnemedb/aeon","NASTYZUNI/aeon","alfahadgm/aeon","dannysrod/aeon",
    "chxoky/aeon","daxaur/aeon","NurstarK/aeon-upstream","yyayourt/aeon","aeoncity-hub/aeon",
    "seuzht/aeon","beijiangqukuailian/aeon","rsavitt/aeon-upstream","ikkeflikkeri/aeon",
    "vigilcodes/aeon","BuiltByEcho/aeon","LiamVisionary/aeon","jianggaoyi/aeon","yindaqiu/aeon",
    "gdalabs/aeon","Atrium-Hermes/aeon","z-korp/aeon","BBridgeers/aeon","0xNN/aeon",
    "simistern/aeon","shulthz/aeon-work","0xbobzilla/aeon","swarm-ai-research/aeon-atlas",
    "Damoncrypto/aeon","likenow66/aeon","mandateseal/aeon","loessy/aeon","AntFleet/aeon",
    "houndflow/aeon","AIRYDER/aeon","ScoutAeon/Scout","NoctelXBT/aeon","KanekiCraynet/aeon",
    "TakamiyaZee/aeon","xBalbinus/aeon","needsomevibe/aeon","0xWCME/aeon","richard7463/aeon",
    "janicegrech1-hash/aeon","Keeleran/aeon","sparkleware/aeon","codexvritra/aeon","KingRwaz/aeon",
    "rimurucook/aeon","noelclaw/aeon","sarapsushi444-sudo/aeon","apolloclaws-oss/aeon",
    "dontlickfrogs/aeon","ryjin111/aeon-pack-pr","DoughBoiKush/aeon","jvbono/aeon","AFHUNTLY/aeon",
    "UIZorrot/aeon","masteramatajj-source/aeon","yehorcallmedai-maker/aeon","liquidpadbot/aeon",
    "shiyankuan-crypto/aeon","lawbworld-tech/aeon","luazhizhan/aeon","imthefounder/aeon",
    "sherwoodagent/aeon","gitlawbounty/aeon","bweick/aeon","0xShak/aeon","taekwonv89/aeon",
    "svenakira/aeon","happycamper-stix/aeon","cersei420/aeon","wx888/aeon","jonathanjoseph20/aeon",
    "danbuildss/aeon","smolboon/aeon","0xMal0u/aeon","youpsla/aeon","PyroFire-Labs/larry",
    "bitcoiner-lab/aeon","antfleet-ops/aeon","forge-executive/forge-executive","DABAGElover/aeon",
    "levi-oss-code/aeon","damo-nu11/aeon-minebean","We3In/vvvkerrnel","We3In/vvvkernel-skills-up",
    "We3In/aeon","abhirajprasad/aeon","coinhome190-spec/aeon","VibeSan7/aeon",
    "anomit/aeon","enzoonchain/aeon","sinan33644061-lab/aeon","wuyu663/aeon","DevZenPro/aeon",
    "AntFleet/aeon-bench","foreverxdord/aeon","oxkaiba/aeon","baseddevoloper/vvvkernel-skills",
    "takanafur/aeon","0xMortimer/aeon","lioapple/aeon","jiamicuisi-a11y/aeon",
    "madebyshun/blueagent-aeon","meichuanyi/aeon","usiclabs/aeon","Da6hkin/aeon","itr010038/aeon",
    "Boodszw/Boodszw_Bread","ether-btc/aeon","tomscaria/aeon","yugo-engineer/aeon",
    "pezetel/aeon","AmithKumar1/aeon",
]

def fetch_fork_yml(fork):
    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{fork}/contents/aeon.yml", "--jq", ".content"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0:
            err = result.stderr.lower() + result.stdout.lower()
            if "404" in err or "not found" in err:
                return None, "no_aeon_yml"
            if "409" in err:
                return None, "no_tree"
            if "403" in err:
                return None, "rate_limited"
            return None, "error"
        content_b64 = result.stdout.strip()
        if not content_b64:
            return None, "empty"
        content = base64.b64decode(content_b64.replace("\\n","").replace("\n","")).decode("utf-8", errors="replace")
        return content, "ok"
    except subprocess.TimeoutExpired:
        return None, "timeout"
    except Exception as e:
        return None, f"error"

def parse_fork_yml(content):
    try:
        data = yaml.safe_load(content)
        if not data or not isinstance(data, dict):
            return None, "yml_invalid"
        skills = data.get("skills", {})
        if not skills or not isinstance(skills, dict):
            return {}, []
        fork_skills = {}
        fork_only = []
        for skill_name, skill_cfg in skills.items():
            if skill_cfg is None:
                skill_cfg = {}
            if isinstance(skill_cfg, bool):
                skill_cfg = {"enabled": skill_cfg}
            if not isinstance(skill_cfg, dict):
                continue
            fork_skills[skill_name] = {
                "enabled": skill_cfg.get("enabled", None),
                "model": skill_cfg.get("model", None) or None,
                "var": skill_cfg.get("var", "") or "",
                "schedule": skill_cfg.get("schedule", None),
            }
            if skill_name not in UPSTREAM_SKILLS:
                fork_only.append(skill_name)
        return fork_skills, fork_only
    except yaml.YAMLError:
        return None, "yml_invalid"
    except Exception:
        return None, "parse_error"

def compute_divergence(fork_skills):
    enabled_diff = 0
    var_overrides = 0
    model_overrides = 0
    schedule_overrides = 0
    for skill_name, fc in fork_skills.items():
        if skill_name not in UPSTREAM_DEFAULTS:
            continue
        upstream = UPSTREAM_DEFAULTS[skill_name]
        if fc["enabled"] is not None and fc["enabled"] != upstream["enabled"]:
            enabled_diff += 1
        if fc["model"] is not None and fc["model"] != upstream["model"]:
            model_overrides += 1
        upstream_var = upstream.get("var","") or ""
        f_var = fc.get("var","") or ""
        if f_var and f_var != upstream_var:
            var_overrides += 1
        if fc["schedule"] is not None and fc["schedule"] != upstream.get("schedule"):
            schedule_overrides += 1
    return enabled_diff, var_overrides, model_overrides, schedule_overrides

def main():
    print(f"Fetching {len(ALL_FORKS)} forks...", flush=True)
    fork_results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as ex:
        fut_to_fork = {ex.submit(fetch_fork_yml, f): f for f in ALL_FORKS}
        done = 0
        for future in concurrent.futures.as_completed(fut_to_fork):
            fork = fut_to_fork[future]
            content, status = future.result()
            fork_results[fork] = {"content": content, "status": status}
            done += 1
            if done % 20 == 0:
                print(f"  {done}/{len(ALL_FORKS)} done", flush=True)

    print("Parsing...", flush=True)
    fork_data = {}
    for fork, res in fork_results.items():
        if res["status"] != "ok" or not res["content"]:
            fork_data[fork] = {
                "tier": "UNREADABLE", "status": res["status"],
                "skills": {}, "fork_only": [],
                "enabled_diff": 0, "var_overrides": 0,
                "model_overrides": 0, "schedule_overrides": 0,
                "fork_only_skill_count": 0,
            }
            continue
        parsed, parse_result = parse_fork_yml(res["content"])
        if parsed is None:
            fork_data[fork] = {
                "tier": "UNREADABLE", "status": parse_result,
                "skills": {}, "fork_only": [],
                "enabled_diff": 0, "var_overrides": 0,
                "model_overrides": 0, "schedule_overrides": 0,
                "fork_only_skill_count": 0,
            }
            continue
        fork_only = parse_result if isinstance(parse_result, list) else []
        ed, vo, mo, so = compute_divergence(parsed)
        total_signal = ed + vo + mo + so + len(fork_only)
        tier = "TEMPLATE" if total_signal == 0 else "CONFIGURED"
        fork_data[fork] = {
            "tier": tier, "status": "ok",
            "skills": parsed, "fork_only": fork_only,
            "enabled_diff": ed, "var_overrides": vo,
            "model_overrides": mo, "schedule_overrides": so,
            "fork_only_skill_count": len(fork_only),
        }

    n_active = len(ALL_FORKS)
    n_configured = sum(1 for f in fork_data.values() if f["tier"] == "CONFIGURED")
    n_template = sum(1 for f in fork_data.values() if f["tier"] == "TEMPLATE")
    n_unreadable = sum(1 for f in fork_data.values() if f["tier"] == "UNREADABLE")
    n_yml_invalid = sum(1 for f in fork_data.values() if "yml_invalid" in f.get("status",""))
    n_rate_limited = sum(1 for f in fork_data.values() if f.get("status","") == "rate_limited")
    n_trees_ok = sum(1 for f in fork_data.values() if f["status"] == "ok")

    print(f"Fleet: {n_active} active | {n_configured} configured | {n_template} template | {n_unreadable} unreadable", flush=True)

    if n_configured < 2:
        out = {"status": "FORK_SKILL_DIGEST_TEMPLATE_FLEET",
               "n_active": n_active, "n_configured": n_configured,
               "n_template": n_template, "n_unreadable": n_unreadable}
        print("RESULT:" + json.dumps(out))
        return

    # Step 6: Aggregate divergence
    skill_divergence = {}
    for skill_name in UPSTREAM_DEFAULTS:
        if skill_name not in UPSTREAM_SKILLS and skill_name not in UPSTREAM_DEFAULTS:
            continue
        upstream = UPSTREAM_DEFAULTS.get(skill_name)
        if not upstream:
            continue

        forks_enabled_count = 0
        forks_disabled_count = 0
        var_override_count = 0
        var_values = []
        model_override_count = 0
        model_values = []
        schedule_override_count = 0
        schedule_values = []

        for fork, fd in fork_data.items():
            if fd["tier"] != "CONFIGURED":
                continue
            fc = fd["skills"].get(skill_name)
            if not fc:
                continue
            f_enabled = fc.get("enabled")
            if f_enabled is not None:
                if f_enabled and not upstream["enabled"]:
                    forks_enabled_count += 1
                elif not f_enabled and upstream["enabled"]:
                    forks_disabled_count += 1
            f_model = fc.get("model")
            if f_model and f_model != upstream["model"]:
                model_override_count += 1
                model_values.append(f_model)
            upstream_var = upstream.get("var","") or ""
            f_var = fc.get("var","") or ""
            if f_var and f_var != upstream_var:
                var_override_count += 1
                var_values.append(f_var)
            f_schedule = fc.get("schedule")
            if f_schedule is not None and f_schedule != upstream.get("schedule"):
                schedule_override_count += 1
                schedule_values.append(str(f_schedule))

        total = (forks_enabled_count + forks_disabled_count + var_override_count +
                 model_override_count + schedule_override_count)
        if total == 0:
            continue

        divergence_pct = (forks_disabled_count if upstream["enabled"] else forks_enabled_count) / n_configured
        direction = "DISABLE_DOWNWARD" if upstream["enabled"] else "ENABLE_UPWARD"

        def top_val(vals):
            if not vals: return None
            ctr = Counter(vals)
            v, c = ctr.most_common(1)[0]
            return [v, c] if c >= 2 else None

        skill_divergence[skill_name] = {
            "forks_enabled_count": forks_enabled_count,
            "forks_disabled_count": forks_disabled_count,
            "upstream_enabled": upstream["enabled"],
            "divergence_pct": divergence_pct,
            "direction": direction,
            "var_override_count": var_override_count,
            "top_var_value": top_val(var_values),
            "model_override_count": model_override_count,
            "top_model_value": top_val(model_values),
            "schedule_override_count": schedule_override_count,
            "top_schedule_value": top_val(schedule_values),
        }

    # Step 7: Categorize
    META_TAGS = {"meta", "dev"}
    EXCLUDED_ENABLE_FLIP = set()
    for sn, tags in UPSTREAM_TAGS.items():
        if any(t in META_TAGS for t in tags):
            EXCLUDED_ENABLE_FLIP.add(sn)
    for sn, ud in UPSTREAM_DEFAULTS.items():
        if (ud.get("schedule") or "") in ("workflow_dispatch", "reactive"):
            EXCLUDED_ENABLE_FLIP.add(sn)

    model_threshold = max(2, math.ceil(n_configured * 0.40))
    var_threshold = max(2, math.ceil(n_configured * 0.30))

    buckets = {"DEFAULT_FLIP_ENABLE": [], "DEFAULT_FLIP_DISABLE": [],
               "MODEL_CONSENSUS": [], "VAR_HOTSPOT": [], "EMERGING": []}
    categorized = set()

    for sn, sd in skill_divergence.items():
        if sn in categorized:
            continue
        ud = UPSTREAM_DEFAULTS.get(sn, {})
        schedule = ud.get("schedule","") or ""

        if (sd["direction"] == "ENABLE_UPWARD"
                and sd["divergence_pct"] >= 0.50
                and schedule != "workflow_dispatch"
                and sn not in EXCLUDED_ENABLE_FLIP):
            buckets["DEFAULT_FLIP_ENABLE"].append({"skill": sn, "forks": sd["forks_enabled_count"], "pct": sd["divergence_pct"]})
            categorized.add(sn)
            continue
        if (sd["direction"] == "DISABLE_DOWNWARD"
                and sd["divergence_pct"] >= 0.50
                and sn != "heartbeat"):
            buckets["DEFAULT_FLIP_DISABLE"].append({"skill": sn, "forks": sd["forks_disabled_count"], "pct": sd["divergence_pct"]})
            categorized.add(sn)
            continue
        if sd["top_model_value"] and sd["top_model_value"][1] >= model_threshold:
            buckets["MODEL_CONSENSUS"].append({"skill": sn, "model": sd["top_model_value"][0], "forks": sd["top_model_value"][1]})
            categorized.add(sn)
            continue
        if sd["var_override_count"] >= var_threshold and sd["top_var_value"]:
            buckets["VAR_HOTSPOT"].append({"skill": sn, "var": sd["top_var_value"][0], "forks": sd["var_override_count"]})
            categorized.add(sn)
            continue
        if (sd["direction"] == "ENABLE_UPWARD"
                and 0.25 <= sd["divergence_pct"] < 0.50
                and schedule not in ("workflow_dispatch","reactive")):
            buckets["EMERGING"].append({"skill": sn, "pct": sd["divergence_pct"], "forks": sd["forks_enabled_count"]})
            categorized.add(sn)

    for b in ["DEFAULT_FLIP_ENABLE","DEFAULT_FLIP_DISABLE","EMERGING"]:
        buckets[b].sort(key=lambda x: x.get("pct",0), reverse=True)
    for b in ["MODEL_CONSENSUS","VAR_HOTSPOT"]:
        buckets[b].sort(key=lambda x: x.get("forks",0), reverse=True)

    # Step 8: fingerprints
    fingerprints = []
    for fork, fd in fork_data.items():
        if fd["tier"] != "CONFIGURED":
            continue
        total_overrides = fd["enabled_diff"] + fd["var_overrides"] + fd["model_overrides"] + fd["schedule_overrides"] + fd["fork_only_skill_count"]
        tag_counts = Counter()
        for sn, fc in fd["skills"].items():
            if fc.get("enabled") is True:
                for t in UPSTREAM_TAGS.get(sn, []):
                    tag_counts[t] += 1
        tag_counts["fork-only"] += fd["fork_only_skill_count"]
        total_enabled = sum(tag_counts.values())
        dominant = "mixed"
        if total_enabled > 0 and tag_counts:
            top_tag, top_count = tag_counts.most_common(1)[0]
            if top_count / total_enabled > 0.40:
                dominant = top_tag
        fingerprints.append({
            "fork": fork, "total_overrides": total_overrides,
            "dominant_category": dominant, "tag_counts": dict(tag_counts),
        })
    fingerprints.sort(key=lambda x: x["total_overrides"], reverse=True)

    fork_only_skills = []
    for fork, fd in fork_data.items():
        for sn in fd["fork_only"]:
            fork_only_skills.append({"fork": fork, "skill": sn})

    schedule_consensus = []
    for sn, sd in skill_divergence.items():
        if sd["top_schedule_value"] and sd["schedule_override_count"] >= 2:
            schedule_consensus.append({"skill": sn, "schedule": sd["top_schedule_value"][0], "forks": sd["schedule_override_count"]})
    schedule_consensus.sort(key=lambda x: x["forks"], reverse=True)

    appendix_rows = []
    for sn, sd in skill_divergence.items():
        total = (sd["forks_enabled_count"] + sd["forks_disabled_count"] +
                 sd["var_override_count"] + sd["model_override_count"] + sd["schedule_override_count"])
        if total > 0:
            enable_diff_val = sd["forks_enabled_count"] if not sd["upstream_enabled"] else -sd["forks_disabled_count"]
            appendix_rows.append({
                "skill": sn, "enable_diff": enable_diff_val,
                "var_overrides": sd["var_override_count"],
                "model_overrides": sd["model_override_count"],
                "schedule_overrides": sd["schedule_override_count"],
                "total": total,
            })
    appendix_rows.sort(key=lambda x: x["total"], reverse=True)

    flip_enable = buckets["DEFAULT_FLIP_ENABLE"]
    flip_disable = buckets["DEFAULT_FLIP_DISABLE"]
    model_consensus = buckets["MODEL_CONSENSUS"]
    emerging = buckets["EMERGING"]

    if flip_enable:
        t = flip_enable[0]
        verdict = f"{t['forks']} forks enable {t['skill']} (upstream defaults off) — flip the default"
    elif flip_disable:
        t = flip_disable[0]
        verdict = f"{t['forks']} forks disable {t['skill']} (upstream defaults on) — fleet is voting it as noise"
    elif model_consensus:
        t = model_consensus[0]
        verdict = f"{t['forks']} forks override {t['skill']} to {t['model']} — match upstream"
    elif fork_only_skills:
        t = fork_only_skills[0]
        verdict = f"{t['fork'].split('/')[0]} shipped {t['skill']} — not in upstream"
    elif emerging:
        t = emerging[0]
        verdict = f"{t['skill']} adoption building ({round(t['pct']*100)}% of configured) — watchlist"
    else:
        verdict = f"{n_configured} configured forks; no divergence pattern crossed flip threshold"

    result = {
        "verdict": verdict,
        "n_active": n_active, "n_configured": n_configured,
        "n_template": n_template, "n_unreadable": n_unreadable,
        "n_yml_invalid": n_yml_invalid, "n_rate_limited": n_rate_limited,
        "n_trees_ok": n_trees_ok,
        "buckets": buckets,
        "fingerprints": fingerprints[:5],
        "all_fingerprints_count": len(fingerprints),
        "fork_only_skills": fork_only_skills,
        "schedule_consensus": schedule_consensus[:5],
        "appendix_rows": appendix_rows[:30],
        "skill_divergence_sample": {
            k: v for k, v in list(skill_divergence.items())[:20]
        },
    }

    print("RESULT:" + json.dumps(result))

if __name__ == "__main__":
    main()
