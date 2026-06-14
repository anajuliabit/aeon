#!/usr/bin/env node
/**
 * Fork skill digest analysis - fetches and analyzes aeon.yml from all active forks.
 * Line-by-line YAML parser to avoid regex-based blank-line cutoff bugs.
 */
import { spawn } from 'child_process';

const UPSTREAM_DEFAULTS = {
  "morning-brief": {enabled:true, schedule:"0 7 * * *", model:null, var:""},
  "daily-routine": {enabled:true, schedule:"0 7 * * *", model:null, var:""},
  "rss-digest": {enabled:false, schedule:"0 7 * * *", model:null, var:""},
  "hacker-news-digest": {enabled:false, schedule:"0 7 * * *", model:null, var:""},
  "paper-digest": {enabled:false, schedule:"0 7 * * *", model:null, var:""},
  "reddit-digest": {enabled:false, schedule:"0 7 * * *", model:null, var:""},
  "telegram-digest": {enabled:false, schedule:"30 7 * * *", model:"claude-sonnet-4-6", var:""},
  "issue-triage": {enabled:false, schedule:"0 9 * * *", model:null, var:""},
  "pr-triage": {enabled:false, schedule:"30 9 * * *", model:null, var:""},
  "pr-review": {enabled:false, schedule:"0 9 * * *", model:null, var:""},
  "auto-merge": {enabled:false, schedule:"0 14 * * *", model:null, var:""},
  "github-monitor": {enabled:false, schedule:"0 9 * * *", model:null, var:""},
  "github-issues": {enabled:false, schedule:"0 9 * * *", model:null, var:""},
  "github-trending": {enabled:true, schedule:"0 9 * * *", model:null, var:""},
  "github-releases": {enabled:false, schedule:"30 9 * * *", model:null, var:""},
  "huggingface-trending": {enabled:false, schedule:"30 9 * * *", model:"claude-sonnet-4-6", var:""},
  "token-alert": {enabled:true, schedule:"0 12 * * *", model:null, var:""},
  "token-movers": {enabled:true, schedule:"10 12 * * *", model:null, var:""},
  "on-chain-monitor": {enabled:true, schedule:"20 12 * * *", model:null, var:""},
  "defi-monitor": {enabled:true, schedule:"40 12 * * *", model:null, var:""},
  "treasury-info": {enabled:false, schedule:"0 12 * * *", model:null, var:""},
  "distribute-tokens": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "defi-overview": {enabled:true, schedule:"0 12 * * *", model:null, var:""},
  "monitor-polymarket": {enabled:false, schedule:"30 12 * * *", model:"claude-sonnet-4-6", var:""},
  "monitor-kalshi": {enabled:false, schedule:"0 13 * * *", model:"claude-sonnet-4-6", var:""},
  "monitor-runners": {enabled:false, schedule:"0 12 * * *", model:null, var:""},
  "token-pick": {enabled:true, schedule:"0 12 * * *", model:null, var:""},
  "token-report": {enabled:false, schedule:"30 12 * * *", model:"claude-sonnet-4-6", var:""},
  "price-threshold-alert": {enabled:false, schedule:"*/30 * * * *", model:"claude-sonnet-4-6", var:""},
  "market-context-refresh": {enabled:true, schedule:"0 13 * * *", model:"claude-sonnet-4-6", var:""},
  "btc-levels": {enabled:true, schedule:"15 */4 * * *", model:"claude-sonnet-4-6", var:""},
  "narrative-tracker": {enabled:true, schedule:"30 13 * * *", model:null, var:""},
  "polymarket-comments": {enabled:false, schedule:"0 13 * * *", model:null, var:""},
  "unlock-monitor": {enabled:true, schedule:"0 10 * * 1", model:null, var:""},
  "aixbt-pulse": {enabled:true, schedule:"0 9,21 * * *", model:"claude-sonnet-4-6", var:""},
  "article": {enabled:false, schedule:"0 14 * * *", model:null, var:""},
  "technical-explainer": {enabled:false, schedule:"30 14 * * *", model:null, var:""},
  "digest": {enabled:false, schedule:"0 14 * * *", model:null, var:""},
  "research-brief": {enabled:false, schedule:"0 14 * * *", model:null, var:""},
  "deep-research": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "last30": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "paper-pick": {enabled:false, schedule:"0 14 * * *", model:null, var:""},
  "search-skill": {enabled:true, schedule:"0 14 * * *", model:null, var:""},
  "security-digest": {enabled:true, schedule:"0 14 * * *", model:null, var:""},
  "idea-capture": {enabled:false, schedule:"0 14 * * *", model:null, var:""},
  "deal-flow": {enabled:true, schedule:"0 14 * * 1", model:null, var:""},
  "reg-monitor": {enabled:true, schedule:"0 14 * * 3", model:null, var:""},
  "push-recap": {enabled:false, schedule:"0 15 * * *", model:null, var:""},
  "repo-article": {enabled:false, schedule:"0 15 * * *", model:null, var:""},
  "repo-actions": {enabled:false, schedule:"0 15 * * *", model:null, var:""},
  "repo-pulse": {enabled:false, schedule:"0 15 * * *", model:null, var:""},
  "star-milestone": {enabled:false, schedule:"15 15 * * *", model:null, var:""},
  "star-momentum-alert": {enabled:false, schedule:"10 10 * * *", model:"claude-sonnet-4-6", var:""},
  "project-lens": {enabled:false, schedule:"30 15 * * 1,3,5", model:null, var:""},
  "repo-scanner": {enabled:false, schedule:"0 15 * * 0", model:"claude-sonnet-4-6", var:""},
  "skill-security-scan": {enabled:true, schedule:"0 16 * * 1", model:null, var:""},
  "code-health": {enabled:false, schedule:"0 16 * * *", model:null, var:""},
  "changelog": {enabled:false, schedule:"0 16 * * *", model:null, var:""},
  "external-feature": {enabled:false, schedule:"30 16 * * *", model:null, var:""},
  "vuln-scanner": {enabled:true, schedule:"0 16 * * 6", model:null, var:""},
  "deploy-prototype": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "autoresearch": {enabled:true, schedule:"workflow_dispatch", model:null, var:""},
  "create-skill": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "fetch-tweets": {enabled:false, schedule:"0 17 * * *", model:null, var:"@moonwell OR @reppo OR @sherwoodagent OR $WOOD OR $MAMO"},
  "refresh-x": {enabled:false, schedule:"0 17 * * *", model:null, var:""},
  "list-digest": {enabled:true, schedule:"0 17 * * *", model:null, var:"1642770456720683008"},
  "write-tweet": {enabled:false, schedule:"0 17 * * *", model:null, var:""},
  "reply-maker": {enabled:false, schedule:"0 17 * * *", model:null, var:""},
  "remix-tweets": {enabled:false, schedule:"30 17 * * *", model:null, var:""},
  "tweet-roundup": {enabled:false, schedule:"0 17 * * *", model:null, var:""},
  "agent-buzz": {enabled:true, schedule:"30 17 * * *", model:null, var:""},
  "farcaster-digest": {enabled:false, schedule:"0 17 * * *", model:null, var:""},
  "vibecoding-digest": {enabled:false, schedule:"30 17 * * *", model:null, var:""},
  "channel-recap": {enabled:false, schedule:"0 17 * * 0", model:null, var:""},
  "rss-feed": {enabled:false, schedule:"30 17 * * *", model:null, var:""},
  "thread-formatter": {enabled:false, schedule:"30 17 * * *", model:null, var:""},
  "update-gallery": {enabled:false, schedule:"0 18 * * 0", model:null, var:""},
  "syndicate-article": {enabled:false, schedule:"30 15 * * *", model:"claude-sonnet-4-6", var:""},
  "goal-tracker": {enabled:true, schedule:"0 18 * * *", model:null, var:""},
  "skill-health": {enabled:true, schedule:"0 18 * * *", model:null, var:""},
  "skill-analytics": {enabled:true, schedule:"30 18 * * 3", model:"claude-sonnet-4-6", var:""},
  "self-improve": {enabled:true, schedule:"0 18 1/2 * *", model:null, var:""},
  "reflect": {enabled:true, schedule:"0 18 * * *", model:null, var:""},
  "action-converter": {enabled:true, schedule:"0 18 * * *", model:null, var:""},
  "startup-idea": {enabled:false, schedule:"0 18 * * *", model:null, var:""},
  "tool-builder": {enabled:false, schedule:"reactive", model:null, var:""},
  "skill-repair": {enabled:false, schedule:"reactive", model:null, var:""},
  "evening-recap": {enabled:true, schedule:"0 21 * * *", model:"claude-sonnet-4-6", var:""},
  "thought-review": {enabled:true, schedule:"0 7,21 * * *", model:null, var:"24"},
  "vercel-projects": {enabled:false, schedule:"0 18 * * 0", model:"claude-sonnet-4-6", var:""},
  "cost-report": {enabled:true, schedule:"0 7 * * 1", model:"claude-sonnet-4-6", var:""},
  "ai-framework-watch": {enabled:false, schedule:"30 8 * * 1", model:"claude-sonnet-4-6", var:""},
  "competitor-launch-radar": {enabled:false, schedule:"0 10 * * 1", model:null, var:" "},
  "fleet-state": {enabled:false, schedule:"0 8 * * 1", model:"claude-sonnet-4-6", var:""},
  "fork-fleet": {enabled:false, schedule:"0 10 * * 1", model:null, var:""},
  "fork-cohort": {enabled:true, schedule:"0 19 * * 0", model:"claude-sonnet-4-6", var:""},
  "fork-release-tracker": {enabled:false, schedule:"30 19 * * 0", model:"claude-sonnet-4-6", var:""},
  "contributor-spotlight": {enabled:false, schedule:"0 20 * * 0", model:"claude-sonnet-4-6", var:""},
  "fork-first-run-alert": {enabled:false, schedule:"30 20 * * *", model:"claude-sonnet-4-6", var:""},
  "skill-evals": {enabled:true, schedule:"0 6 * * 0", model:"claude-sonnet-4-6", var:""},
  "skill-update-check": {enabled:true, schedule:"0 19 * * 0", model:"claude-sonnet-4-6", var:""},
  "spawn-instance": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "fleet-control": {enabled:true, schedule:"0 9,15 * * *", model:null, var:""},
  "weekly-review": {enabled:true, schedule:"0 19 * * 1", model:null, var:""},
  "weekly-shiplog": {enabled:true, schedule:"0 9 * * 1", model:null, var:""},
  "skill-leaderboard": {enabled:false, schedule:"0 17 * * 0", model:"claude-sonnet-4-6", var:""},
  "fork-contributor-leaderboard": {enabled:false, schedule:"30 17 * * 0", model:"claude-sonnet-4-6", var:""},
  "contributor-reward": {enabled:false, schedule:"30 9 * * 1", model:"claude-sonnet-4-6", var:""},
  "operator-scorecard": {enabled:true, schedule:"30 10 * * 1", model:"claude-sonnet-4-6", var:""},
  "fork-skill-digest": {enabled:true, schedule:"30 18 * * 0", model:"claude-sonnet-4-6", var:""},
  "fork-skill-gap": {enabled:true, schedule:"0 21 * * 0", model:"claude-sonnet-4-6", var:""},
  "workflow-security-audit": {enabled:false, schedule:"0 16 * * 0", model:null, var:""},
  "skill-graph": {enabled:true, schedule:"0 17 * * 0", model:null, var:""},
  "skill-freshness": {enabled:true, schedule:"0 8 * * *", model:"claude-sonnet-4-6", var:""},
  "smithery-manifest": {enabled:false, schedule:"0 6 1/7 * *", model:"claude-sonnet-4-6", var:""},
  "show-hn-draft": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "product-hunt-launch": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "v4-readiness": {enabled:false, schedule:"workflow_dispatch", model:"claude-sonnet-4-6", var:""},
  "schedule-ads": {enabled:false, schedule:"0 8 * * *", model:"claude-sonnet-4-6", var:""},
  "create-campaign": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "auto-workflow": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "onboard": {enabled:false, schedule:"workflow_dispatch", model:null, var:""},
  "reppo-orchestrator": {enabled:false, schedule:null, model:null, var:""},
  "reppo-trading-agent": {enabled:false, schedule:null, model:null, var:""},
  "reppo-voter": {enabled:false, schedule:null, model:null, var:""},
  "reppo-digest": {enabled:false, schedule:null, model:null, var:""},
  "heartbeat": {enabled:true, schedule:"0 8,14,20 * * *", model:null, var:""},
};

const UPSTREAM_SKILLS = new Set([
  ...Object.keys(UPSTREAM_DEFAULTS), "security"
]);

const UPSTREAM_TAGS = {
  "morning-brief":["content"],"daily-routine":["meta"],"rss-digest":["content"],
  "hacker-news-digest":["content"],"paper-digest":["content"],"reddit-digest":["content"],
  "telegram-digest":["content"],"issue-triage":["dev"],"pr-triage":["dev"],"pr-review":["dev"],
  "auto-merge":["dev"],"github-monitor":["dev"],"github-issues":["dev"],
  "github-trending":["research"],"github-releases":["research"],"huggingface-trending":["research"],
  "token-alert":["crypto"],"token-movers":["crypto"],"on-chain-monitor":["crypto"],
  "defi-monitor":["crypto"],"treasury-info":["crypto"],"distribute-tokens":["crypto"],
  "defi-overview":["crypto"],"monitor-polymarket":["crypto"],"monitor-kalshi":["crypto"],
  "monitor-runners":["meta"],"token-pick":["crypto"],"token-report":["crypto"],
  "price-threshold-alert":["crypto"],"market-context-refresh":["crypto"],"btc-levels":["crypto"],
  "narrative-tracker":["crypto"],"polymarket-comments":["crypto"],"unlock-monitor":["crypto"],
  "aixbt-pulse":["crypto"],"article":["content"],"technical-explainer":["content"],
  "digest":["content"],"research-brief":["content"],"deep-research":["research"],"last30":["research"],
  "paper-pick":["research"],"search-skill":["research"],"security-digest":["content"],
  "idea-capture":["meta"],"deal-flow":["research"],"reg-monitor":["research"],
  "push-recap":["dev"],"repo-article":["content"],"repo-actions":["dev"],"repo-pulse":["research"],
  "star-milestone":["meta"],"star-momentum-alert":["meta"],"project-lens":["content"],
  "repo-scanner":["research"],"skill-security-scan":["dev"],"code-health":["dev"],
  "changelog":["dev"],"external-feature":["dev"],"vuln-scanner":["dev"],"deploy-prototype":["dev"],
  "autoresearch":["meta"],"create-skill":["meta"],"fetch-tweets":["social"],"refresh-x":["social"],
  "list-digest":["social"],"write-tweet":["social"],"reply-maker":["social"],"remix-tweets":["social"],
  "tweet-roundup":["social"],"agent-buzz":["social"],"farcaster-digest":["social"],
  "vibecoding-digest":["social"],"channel-recap":["social"],"rss-feed":["meta"],
  "thread-formatter":["social"],"update-gallery":["meta"],"syndicate-article":["content"],
  "goal-tracker":["meta"],"skill-health":["meta"],"skill-analytics":["meta"],"self-improve":["meta"],
  "reflect":["meta"],"action-converter":["meta"],"startup-idea":["research"],"tool-builder":["meta"],
  "skill-repair":["meta"],"evening-recap":["meta"],"thought-review":["meta"],
  "vercel-projects":["dev"],"cost-report":["meta"],"ai-framework-watch":["research"],
  "competitor-launch-radar":["research"],"fleet-state":["meta"],"fork-fleet":["meta"],
  "fork-cohort":["meta"],"fork-release-tracker":["meta"],"contributor-spotlight":["meta"],
  "fork-first-run-alert":["meta"],"skill-evals":["meta"],"skill-update-check":["meta"],
  "spawn-instance":["meta"],"fleet-control":["meta"],"weekly-review":["meta"],
  "weekly-shiplog":["meta"],"skill-leaderboard":["meta"],"fork-contributor-leaderboard":["meta"],
  "contributor-reward":["meta"],"operator-scorecard":["meta"],"fork-skill-digest":["meta"],
  "fork-skill-gap":["meta"],"workflow-security-audit":["dev"],"skill-graph":["meta"],
  "skill-freshness":["meta"],"smithery-manifest":["meta"],"show-hn-draft":["meta"],
  "product-hunt-launch":["meta"],"v4-readiness":["meta"],"schedule-ads":["meta"],
  "create-campaign":["meta"],"auto-workflow":["meta"],"onboard":["meta"],
  "reppo-orchestrator":["meta"],"reppo-trading-agent":["meta"],"reppo-voter":["meta"],
  "reppo-digest":["meta"],"heartbeat":["meta"],"security":["dev"],
};

const ALL_FORKS = [
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
];

function runGhApi(fork) {
  return new Promise((resolve) => {
    const proc = spawn('gh', ['api', `repos/${fork}/contents/aeon.yml`, '--jq', '.content'], {timeout:30000});
    let stdout='', stderr='';
    proc.stdout.on('data', d => stdout += d);
    proc.stderr.on('data', d => stderr += d);
    proc.on('close', (code) => {
      if (code !== 0) {
        const err = (stderr + stdout).toLowerCase();
        if (err.includes('404') || err.includes('not found')) resolve({content:null, status:'no_aeon_yml'});
        else if (err.includes('409')) resolve({content:null, status:'no_tree'});
        else if (err.includes('403')) resolve({content:null, status:'rate_limited'});
        else resolve({content:null, status:'error'});
      } else {
        const b64 = stdout.trim().replace(/\n/g,'');
        if (!b64) { resolve({content:null, status:'empty'}); return; }
        try {
          const content = Buffer.from(b64,'base64').toString('utf8');
          resolve({content, status:'ok'});
        } catch(e) { resolve({content:null, status:'decode_error'}); }
      }
    });
    proc.on('error', () => resolve({content:null, status:'spawn_error'}));
  });
}

// Parse inline YAML config: { enabled: true/false, model: "...", var: "...", schedule: "..." }
function parseInlineConfig(configStr) {
  const cfg = {enabled:null, model:null, var:'', schedule:null};
  const em = configStr.match(/\benabled:\s*(true|false)/);
  if (em) cfg.enabled = em[1] === 'true';
  const mm = configStr.match(/\bmodel:\s*"([^"]+)"/);
  if (mm) cfg.model = mm[1];
  // var: with quotes
  const vm = configStr.match(/\bvar:\s*"([^"]*)"/);
  if (vm) cfg.var = vm[1];
  // schedule: with quotes
  const sm = configStr.match(/\bschedule:\s*"([^"]+)"/);
  if (sm) cfg.schedule = sm[1];
  else {
    const sm2 = configStr.match(/\bschedule:\s*([^\s,}"]+)/);
    if (sm2) cfg.schedule = sm2[1];
  }
  return cfg;
}

// Line-by-line aeon.yml parser — handles multi-line blocks and blank lines within skills:
function parseAeonYml(content) {
  try {
    const lines = content.split('\n');
    const skills = {};
    const forkOnly = [];
    let inSkills = false;
    let i = 0;

    while (i < lines.length) {
      const line = lines[i];

      // Top-level non-comment key detection
      if (line.match(/^[a-zA-Z]/)) {
        inSkills = line.startsWith('skills:');
        i++; continue;
      }

      if (!inSkills) { i++; continue; }

      // Skip blank lines and pure comment lines within skills section
      const trimmed = line.trim();
      if (!trimmed || trimmed.startsWith('#')) { i++; continue; }

      // Skill entry: exactly 2-space indent then name:
      const skillMatch = line.match(/^  ([a-zA-Z0-9_-]+):\s*(.*)/);
      if (!skillMatch) { i++; continue; }

      const skillName = skillMatch[1];
      let configStr = skillMatch[2].trim();

      // Remove inline comment (but be careful with quoted strings)
      // Strip trailing comment from configStr if it's after }
      const closeBrace = configStr.lastIndexOf('}');
      if (closeBrace !== -1) {
        configStr = configStr.substring(0, closeBrace + 1);
      }

      // Handle multi-line block: value starts with { alone or is empty
      if (configStr === '{' || (configStr === '' && !line.includes('false') && !line.includes('true'))) {
        let block = configStr;
        i++;
        while (i < lines.length) {
          const nl = lines[i];
          const ntrimmed = nl.trim();
          if (!ntrimmed || ntrimmed.startsWith('#')) { i++; continue; }
          if (nl.match(/^    /) || ntrimmed === '}') {
            block += ' ' + ntrimmed;
            i++;
            if (ntrimmed.includes('}')) break;
          } else {
            break;
          }
        }
        configStr = block;
      } else {
        i++;
      }

      if (!configStr) continue;

      const cfg = parseInlineConfig(configStr);
      skills[skillName] = cfg;
      if (!UPSTREAM_SKILLS.has(skillName)) forkOnly.push(skillName);
    }

    return {skills, forkOnly};
  } catch(e) {
    return null;
  }
}

function computeDivergence(forkSkills) {
  let enabledDiff=0, varOverrides=0, modelOverrides=0, scheduleOverrides=0;
  for (const [sn, fc] of Object.entries(forkSkills)) {
    const up = UPSTREAM_DEFAULTS[sn];
    if (!up) continue;
    if (fc.enabled !== null && fc.enabled !== up.enabled) enabledDiff++;
    if (fc.model && fc.model !== up.model) modelOverrides++;
    const upVar = (up.var || '').trim();
    const fVar = (fc.var || '').trim();
    if (fVar && fVar !== upVar) varOverrides++;
    if (fc.schedule !== null && fc.schedule !== up.schedule) scheduleOverrides++;
  }
  return {enabledDiff, varOverrides, modelOverrides, scheduleOverrides};
}

function topValue(arr) {
  if (!arr.length) return null;
  const counts = {};
  for (const v of arr) counts[v] = (counts[v]||0) + 1;
  const top = Object.entries(counts).sort((a,b)=>b[1]-a[1])[0];
  return top[1] >= 2 ? {value:top[0], count:top[1]} : null;
}

async function main() {
  process.stdout.write(`Fetching ${ALL_FORKS.length} forks...\n`);
  const CONCURRENCY = 15;
  const forkResults = {};

  for (let i = 0; i < ALL_FORKS.length; i += CONCURRENCY) {
    const batch = ALL_FORKS.slice(i, i + CONCURRENCY);
    const results = await Promise.all(batch.map(f => runGhApi(f).then(r => ({fork:f,...r}))));
    for (const r of results) forkResults[r.fork] = {content:r.content, status:r.status};
    process.stdout.write(`  ${Math.min(i+CONCURRENCY, ALL_FORKS.length)}/${ALL_FORKS.length}\n`);
  }

  process.stdout.write('Parsing...\n');
  const forkData = {};
  for (const [fork, res] of Object.entries(forkResults)) {
    if (res.status !== 'ok' || !res.content) {
      forkData[fork] = {tier:'UNREADABLE', status:res.status, skills:{}, forkOnly:[], enabledDiff:0, varOverrides:0, modelOverrides:0, scheduleOverrides:0, forkOnlySkillCount:0};
      continue;
    }
    const parsed = parseAeonYml(res.content);
    if (!parsed) {
      forkData[fork] = {tier:'UNREADABLE', status:'yml_invalid', skills:{}, forkOnly:[], enabledDiff:0, varOverrides:0, modelOverrides:0, scheduleOverrides:0, forkOnlySkillCount:0};
      continue;
    }
    const {skills, forkOnly} = parsed;
    const {enabledDiff, varOverrides, modelOverrides, scheduleOverrides} = computeDivergence(skills);
    const totalSignal = enabledDiff + varOverrides + modelOverrides + scheduleOverrides + forkOnly.length;
    const tier = totalSignal === 0 ? 'TEMPLATE' : 'CONFIGURED';
    forkData[fork] = {tier, status:'ok', skills, forkOnly, enabledDiff, varOverrides, modelOverrides, scheduleOverrides, forkOnlySkillCount:forkOnly.length};
  }

  const nActive = ALL_FORKS.length;
  const nConfigured = Object.values(forkData).filter(f=>f.tier==='CONFIGURED').length;
  const nTemplate = Object.values(forkData).filter(f=>f.tier==='TEMPLATE').length;
  const nUnreadable = Object.values(forkData).filter(f=>f.tier==='UNREADABLE').length;
  const nYmlInvalid = Object.values(forkData).filter(f=>f.status==='yml_invalid').length;
  const nRateLimited = Object.values(forkData).filter(f=>f.status==='rate_limited').length;
  const nTreesOk = Object.values(forkData).filter(f=>f.status==='ok').length;

  process.stdout.write(`Fleet: ${nActive} | configured:${nConfigured} | template:${nTemplate} | unreadable:${nUnreadable}\n`);

  // Debug: show first few configured/template samples
  const configured = Object.entries(forkData).filter(([,f])=>f.tier==='CONFIGURED').slice(0,3);
  for (const [fork, fd] of configured) {
    process.stdout.write(`  CONFIGURED: ${fork} enabledDiff=${fd.enabledDiff} varOverrides=${fd.varOverrides} forkOnly=${fd.forkOnlySkillCount}\n`);
  }
  const template = Object.entries(forkData).filter(([,f])=>f.tier==='TEMPLATE').slice(0,3);
  for (const [fork, fd] of template) {
    process.stdout.write(`  TEMPLATE: ${fork} skillCount=${Object.keys(fd.skills).length}\n`);
  }

  if (nConfigured < 2) {
    const out = {status:'FORK_SKILL_DIGEST_TEMPLATE_FLEET', nActive, nConfigured, nTemplate, nUnreadable};
    process.stdout.write('RESULT:' + JSON.stringify(out) + '\n');
    return;
  }

  // Aggregate divergence
  const skillDivergence = {};
  for (const sn of Object.keys(UPSTREAM_DEFAULTS)) {
    const upstream = UPSTREAM_DEFAULTS[sn];
    let forksEnabledCount=0, forksDisabledCount=0;
    const varValues=[], modelValues=[], scheduleValues=[];

    for (const fd of Object.values(forkData)) {
      if (fd.tier !== 'CONFIGURED') continue;
      const fc = fd.skills[sn];
      if (!fc) continue;
      if (fc.enabled !== null) {
        if (fc.enabled && !upstream.enabled) forksEnabledCount++;
        else if (!fc.enabled && upstream.enabled) forksDisabledCount++;
      }
      if (fc.model && fc.model !== upstream.model) modelValues.push(fc.model);
      const upVar = (upstream.var||'').trim();
      const fVar = (fc.var||'').trim();
      if (fVar && fVar !== upVar) varValues.push(fVar);
      if (fc.schedule !== null && fc.schedule !== upstream.schedule) scheduleValues.push(String(fc.schedule));
    }

    const total = forksEnabledCount + forksDisabledCount + varValues.length + modelValues.length + scheduleValues.length;
    if (total === 0) continue;

    const divergencePct = (upstream.enabled ? forksDisabledCount : forksEnabledCount) / nConfigured;
    const direction = upstream.enabled ? 'DISABLE_DOWNWARD' : 'ENABLE_UPWARD';
    skillDivergence[sn] = {
      forksEnabledCount, forksDisabledCount, upstreamEnabled:upstream.enabled,
      divergencePct, direction,
      varOverrideCount:varValues.length, topVarValue:topValue(varValues),
      modelOverrideCount:modelValues.length, topModelValue:topValue(modelValues),
      scheduleOverrideCount:scheduleValues.length, topScheduleValue:topValue(scheduleValues),
    };
  }

  // Categorize
  const META_TAGS = new Set(['meta','dev']);
  const EXCLUDED_ENABLE_FLIP = new Set();
  for (const [sn,tags] of Object.entries(UPSTREAM_TAGS)) {
    if (tags.some(t=>META_TAGS.has(t))) EXCLUDED_ENABLE_FLIP.add(sn);
  }
  for (const [sn,ud] of Object.entries(UPSTREAM_DEFAULTS)) {
    if (['workflow_dispatch','reactive'].includes(ud.schedule)) EXCLUDED_ENABLE_FLIP.add(sn);
  }

  const modelThreshold = Math.max(2, Math.ceil(nConfigured*0.40));
  const varThreshold = Math.max(2, Math.ceil(nConfigured*0.30));
  const buckets = {DEFAULT_FLIP_ENABLE:[], DEFAULT_FLIP_DISABLE:[], MODEL_CONSENSUS:[], VAR_HOTSPOT:[], EMERGING:[]};
  const categorized = new Set();

  for (const [sn, sd] of Object.entries(skillDivergence)) {
    if (categorized.has(sn)) continue;
    const schedule = (UPSTREAM_DEFAULTS[sn]||{}).schedule||'';
    if (sd.direction==='ENABLE_UPWARD' && sd.divergencePct>=0.50 && schedule!=='workflow_dispatch' && !EXCLUDED_ENABLE_FLIP.has(sn)) {
      buckets.DEFAULT_FLIP_ENABLE.push({skill:sn, forks:sd.forksEnabledCount, pct:sd.divergencePct}); categorized.add(sn); continue;
    }
    if (sd.direction==='DISABLE_DOWNWARD' && sd.divergencePct>=0.50 && sn!=='heartbeat') {
      buckets.DEFAULT_FLIP_DISABLE.push({skill:sn, forks:sd.forksDisabledCount, pct:sd.divergencePct}); categorized.add(sn); continue;
    }
    if (sd.topModelValue && sd.topModelValue.count>=modelThreshold) {
      buckets.MODEL_CONSENSUS.push({skill:sn, model:sd.topModelValue.value, forks:sd.topModelValue.count}); categorized.add(sn); continue;
    }
    if (sd.varOverrideCount>=varThreshold && sd.topVarValue) {
      buckets.VAR_HOTSPOT.push({skill:sn, var:sd.topVarValue.value, forks:sd.varOverrideCount}); categorized.add(sn); continue;
    }
    if (sd.direction==='ENABLE_UPWARD' && sd.divergencePct>=0.25 && sd.divergencePct<0.50 && !['workflow_dispatch','reactive'].includes(schedule)) {
      buckets.EMERGING.push({skill:sn, pct:sd.divergencePct, forks:sd.forksEnabledCount}); categorized.add(sn);
    }
  }
  ['DEFAULT_FLIP_ENABLE','DEFAULT_FLIP_DISABLE','EMERGING'].forEach(b=>buckets[b].sort((a,b)=>b.pct-a.pct));
  ['MODEL_CONSENSUS','VAR_HOTSPOT'].forEach(b=>buckets[b].sort((a,b)=>b.forks-a.forks));

  // Fingerprints
  const fingerprints = [];
  for (const [fork, fd] of Object.entries(forkData)) {
    if (fd.tier!=='CONFIGURED') continue;
    const totalOverrides = fd.enabledDiff+fd.varOverrides+fd.modelOverrides+fd.scheduleOverrides+fd.forkOnlySkillCount;
    const tagCounts = {};
    for (const [sn,fc] of Object.entries(fd.skills)) {
      if (fc.enabled===true) for (const t of (UPSTREAM_TAGS[sn]||[])) tagCounts[t]=(tagCounts[t]||0)+1;
    }
    tagCounts['fork-only']=(tagCounts['fork-only']||0)+fd.forkOnlySkillCount;
    const totalEnabled = Object.values(tagCounts).reduce((a,b)=>a+b,0);
    let dominant='mixed';
    if (totalEnabled>0&&Object.keys(tagCounts).length>0) {
      const top=Object.entries(tagCounts).sort((a,b)=>b[1]-a[1])[0];
      if (top[1]/totalEnabled>0.40) dominant=top[0];
    }
    fingerprints.push({fork, totalOverrides, dominantCategory:dominant, tagCounts});
  }
  fingerprints.sort((a,b)=>b.totalOverrides-a.totalOverrides);

  const forkOnlySkills=[];
  for (const [fork,fd] of Object.entries(forkData)) for (const sn of fd.forkOnly) forkOnlySkills.push({fork,skill:sn});

  const scheduleConsensus = Object.entries(skillDivergence)
    .filter(([,sd])=>sd.topScheduleValue&&sd.scheduleOverrideCount>=2)
    .map(([sn,sd])=>({skill:sn, schedule:sd.topScheduleValue.value, forks:sd.scheduleOverrideCount}))
    .sort((a,b)=>b.forks-a.forks).slice(0,5);

  const appendixRows = Object.entries(skillDivergence).map(([sn,sd])=>{
    const total=sd.forksEnabledCount+sd.forksDisabledCount+sd.varOverrideCount+sd.modelOverrideCount+sd.scheduleOverrideCount;
    return {skill:sn, enableDiff:sd.upstreamEnabled?-sd.forksDisabledCount:sd.forksEnabledCount, varOverrides:sd.varOverrideCount, modelOverrides:sd.modelOverrideCount, scheduleOverrides:sd.scheduleOverrideCount, total};
  }).filter(r=>r.total>0).sort((a,b)=>b.total-a.total).slice(0,30);

  let verdict;
  if (buckets.DEFAULT_FLIP_ENABLE.length) { const t=buckets.DEFAULT_FLIP_ENABLE[0]; verdict=`${t.forks} forks enable ${t.skill} (upstream defaults off) — flip the default`; }
  else if (buckets.DEFAULT_FLIP_DISABLE.length) { const t=buckets.DEFAULT_FLIP_DISABLE[0]; verdict=`${t.forks} forks disable ${t.skill} (upstream defaults on) — fleet is voting it as noise`; }
  else if (buckets.MODEL_CONSENSUS.length) { const t=buckets.MODEL_CONSENSUS[0]; verdict=`${t.forks} forks override ${t.skill} to ${t.model} — match upstream`; }
  else if (forkOnlySkills.length) { const t=forkOnlySkills[0]; verdict=`${t.fork.split('/')[0]} shipped ${t.skill} — not in upstream`; }
  else if (buckets.EMERGING.length) { const t=buckets.EMERGING[0]; verdict=`${t.skill} adoption building (${Math.round(t.pct*100)}% of configured) — watchlist`; }
  else verdict=`${nConfigured} configured forks; no divergence pattern crossed flip threshold`;

  const result = {
    verdict, nActive, nConfigured, nTemplate, nUnreadable, nYmlInvalid, nRateLimited, nTreesOk,
    buckets, fingerprints:fingerprints.slice(0,5), allFingerprintsCount:fingerprints.length,
    forkOnlySkills, scheduleConsensus, appendixRows,
    topDivergence: Object.entries(skillDivergence)
      .map(([sn,sd])=>({skill:sn,...sd}))
      .sort((a,b)=>(b.forksEnabledCount+b.forksDisabledCount)-(a.forksEnabledCount+a.forksDisabledCount))
      .slice(0,20),
  };

  process.stdout.write('RESULT:' + JSON.stringify(result) + '\n');
}

main().catch(e => { process.stderr.write('Error: '+e.message+'\n'); process.exit(1); });
