#!/usr/bin/env node
/**
 * Fetches aeon.yml from 79 GitHub forks and extracts skill configurations.
 * Uses gh api for fetching, custom YAML parser for skills section.
 * Writes JSON array to memory/topics/.fork_results_tmp.json
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const OUTPUT_PATH = '/home/runner/work/aeon/aeon/memory/topics/.fork_results_tmp.json';

const FORKS = [
  { full_name: "nigelon11/aeon", default_branch: "main" },
  { full_name: "webguy-cloud/aeon", default_branch: "main" },
  { full_name: "Loopershot/aeon", default_branch: "main" },
  { full_name: "s97472091-pixel/aeon", default_branch: "main" },
  { full_name: "usepaxterapp/aeon", default_branch: "main" },
  { full_name: "penguinxbt/aeon", default_branch: "main" },
  { full_name: "freezerboi/aeon", default_branch: "main" },
  { full_name: "anajuliabit/aeon-fork", default_branch: "main" },
  { full_name: "madmystic/aeon", default_branch: "main" },
  { full_name: "SamsShow/aeon", default_branch: "main" },
  { full_name: "Marr554/aeon", default_branch: "main" },
  { full_name: "alpenflow/aeon", default_branch: "main" },
  { full_name: "stefrogovskyi/aeon", default_branch: "main" },
  { full_name: "usephylax/aeon", default_branch: "main" },
  { full_name: "saivarmadpr/aeon", default_branch: "main" },
  { full_name: "Tholynceus/aeon", default_branch: "main" },
  { full_name: "logbookbase/aeon", default_branch: "main" },
  { full_name: "maredek-bot/aeon", default_branch: "main" },
  { full_name: "CharonAI-code/aeon", default_branch: "main" },
  { full_name: "KK-OS/aeon", default_branch: "main" },
  { full_name: "P9LLI/aeon", default_branch: "main" },
  { full_name: "adlai88/aeon", default_branch: "main" },
  { full_name: "vladimirvalcourt/aeon", default_branch: "main" },
  { full_name: "clawhunter/add-clawhunter-pack", default_branch: "main" },
  { full_name: "hurley87/aeon", default_branch: "main" },
  { full_name: "runchr-org/aeon", default_branch: "main" },
  { full_name: "brainlabors-dot/aeon", default_branch: "main" },
  { full_name: "rajkaria/aeon", default_branch: "main" },
  { full_name: "tenequm/aeon", default_branch: "main" },
  { full_name: "ziyosteve/aeon", default_branch: "main" },
  { full_name: "zszkey/aeon-1", default_branch: "main" },
  { full_name: "modelcollapse/aeon", default_branch: "main" },
  { full_name: "wrenwealth/aeon", default_branch: "main" },
  { full_name: "ghostx-dev/aeon", default_branch: "main" },
  { full_name: "sinfronterasai/aeon", default_branch: "main" },
  { full_name: "gitlumen-team/aeon", default_branch: "main" },
  { full_name: "ashneil12/aeon-upstream", default_branch: "main" },
  { full_name: "AdversaLLC/aeon", default_branch: "main" },
  { full_name: "anondevv69/bankr-space-aeon", default_branch: "main" },
  { full_name: "SahilParikh03/aeon", default_branch: "main" },
  { full_name: "mnemedb/aeon", default_branch: "main" },
  { full_name: "NASTYZUNI/aeon", default_branch: "main" },
  { full_name: "alfahadgm/aeon", default_branch: "main" },
  { full_name: "dannysrod/aeon", default_branch: "main" },
  { full_name: "chxoky/aeon", default_branch: "main" },
  { full_name: "daxaur/aeon", default_branch: "main" },
  { full_name: "aeoncity-hub/aeon", default_branch: "main" },
  { full_name: "beijiangqukuailian/aeon", default_branch: "main" },
  { full_name: "vigilcodes/aeon", default_branch: "main" },
  { full_name: "yindaqiu/aeon", default_branch: "main" },
  { full_name: "BBridgeers/aeon", default_branch: "main" },
  { full_name: "swarm-ai-research/aeon-atlas", default_branch: "main" },
  { full_name: "TakamiyaZee/aeon", default_branch: "main" },
  { full_name: "xBalbinus/aeon", default_branch: "main" },
  { full_name: "sparkleware/aeon", default_branch: "main" },
  { full_name: "codexvritra/aeon", default_branch: "main" },
  { full_name: "UIZorrot/aeon", default_branch: "main" },
  { full_name: "lawbworld-tech/aeon", default_branch: "main" },
  { full_name: "gitlawbounty/aeon", default_branch: "main" },
  { full_name: "0xShak/aeon", default_branch: "main" },
  { full_name: "taekwonv89/aeon", default_branch: "main" },
  { full_name: "0xMal0u/aeon", default_branch: "main" },
  { full_name: "youpsla/aeon", default_branch: "main" },
  { full_name: "antfleet-ops/aeon", default_branch: "main" },
  { full_name: "damo-nu11/aeon-minebean", default_branch: "main" },
  { full_name: "VibeSan7/aeon", default_branch: "main" },
  { full_name: "anomit/aeon", default_branch: "main" },
  { full_name: "enzoonchain/aeon", default_branch: "main" },
  { full_name: "AntFleet/aeon-bench", default_branch: "main" },
  { full_name: "takanafur/aeon", default_branch: "main" },
  { full_name: "madebyshun/blueagent-aeon", default_branch: "main" },
  { full_name: "usiclabs/aeon", default_branch: "main" },
  { full_name: "Da6hkin/aeon", default_branch: "main" },
  { full_name: "Boodszw/Boodszw_Bread", default_branch: "main" },
  { full_name: "ether-btc/aeon", default_branch: "main" },
  { full_name: "tomscaria/aeon", default_branch: "main" },
  { full_name: "yugo-engineer/aeon", default_branch: "main" },
  { full_name: "pezetel/aeon", default_branch: "main" },
  { full_name: "AmithKumar1/aeon", default_branch: "main" },
];

/**
 * Parse the skills section of an aeon.yml content string.
 * Handles:
 *   - Inline dict: `  skill-name: { enabled: true, schedule: "...", model: "...", var: "..." }`
 *   - Multi-line dict:
 *       skill-name:
 *         enabled: true
 *         schedule: "..."
 * Returns an object: { skillName: { enabled, model, var, schedule } }
 */
function parseSkills(yamlContent) {
  const skills = {};
  const lines = yamlContent.split('\n');

  let inSkillsSection = false;
  let currentSkillName = null;
  let currentSkillData = {};

  // Helper to save pending multi-line skill
  function flushCurrentSkill() {
    if (currentSkillName) {
      skills[currentSkillName] = {
        enabled: currentSkillData.enabled !== undefined ? currentSkillData.enabled : null,
        model: currentSkillData.model !== undefined ? currentSkillData.model : null,
        var: currentSkillData.var !== undefined ? currentSkillData.var : null,
        schedule: currentSkillData.schedule !== undefined ? currentSkillData.schedule : null,
      };
      currentSkillName = null;
      currentSkillData = {};
    }
  }

  for (let i = 0; i < lines.length; i++) {
    const rawLine = lines[i];
    // Count leading spaces for indent detection
    const indent = rawLine.length - rawLine.trimStart().length;
    // Fully trimmed line (no leading/trailing whitespace) for content matching
    const line = rawLine.trim();

    // Skip empty lines and pure comment lines
    if (line === '' || line.startsWith('#')) continue;

    // Detect skills: section start (top-level key at indent=0)
    if (indent === 0 && (line === 'skills:' || line.startsWith('skills: ') || line.startsWith('skills:#'))) {
      inSkillsSection = true;
      continue;
    }

    // If we see any other top-level key (indent=0), exit skills section
    if (indent === 0 && line !== '') {
      flushCurrentSkill();
      inSkillsSection = false;
      continue;
    }

    if (!inSkillsSection) continue;

    if (indent === 2) {
      // This is a skill definition line (2-space indent within skills:)
      flushCurrentSkill();

      // Try inline dict format: `skill-name: { ... }`
      const inlineMatch = line.match(/^([a-zA-Z0-9_\-\.]+):\s*\{(.*)\}/);
      if (inlineMatch) {
        const skillName = inlineMatch[1];
        // Strip trailing comment from the dict string
        const dictStr = inlineMatch[2].replace(/\s*#.*$/, '');
        const parsed = parseInlineDict(dictStr);
        skills[skillName] = {
          enabled: parsed.enabled !== undefined ? parsed.enabled : null,
          model: parsed.model !== undefined ? parsed.model : null,
          var: parsed.var !== undefined ? parsed.var : null,
          schedule: parsed.schedule !== undefined ? parsed.schedule : null,
        };
        continue;
      }

      // Try multi-line format: `skill-name:` or `skill-name: null` or `skill-name: ~`
      const multiLineMatch = line.match(/^([a-zA-Z0-9_\-\.]+):\s*(?:null|~)?\s*(?:#.*)?$/);
      if (multiLineMatch) {
        currentSkillName = multiLineMatch[1];
        currentSkillData = {};
        continue;
      }

    } else if (indent === 4 && currentSkillName) {
      // Property of current multi-line skill
      const propMatch = line.match(/^([a-zA-Z0-9_\-]+):\s*(.*)$/);
      if (propMatch) {
        const key = propMatch[1];
        // Strip inline comments for unquoted values
        let rawVal = propMatch[2].trim();
        if (key === 'enabled') {
          currentSkillData.enabled = parseYamlBool(rawVal);
        } else if (key === 'schedule') {
          currentSkillData.schedule = parseYamlString(rawVal);
        } else if (key === 'model') {
          currentSkillData.model = parseYamlString(rawVal);
        } else if (key === 'var') {
          currentSkillData.var = parseYamlString(rawVal);
        }
      }
    } else if (indent > 4 && currentSkillName) {
      // Deeper nesting within a skill - skip
      continue;
    } else if (indent === 2 || indent > 2) {
      // Still inside skills section, some other indented line
      continue;
    }
  }

  flushCurrentSkill();
  return skills;
}

/**
 * Parse an inline YAML dict string like:
 *   enabled: false, schedule: "0 7 * * *", var: ""
 * Returns an object with the parsed key-value pairs.
 */
function parseInlineDict(str) {
  const result = {};
  // Remove trailing comments from after closing brace
  // str is already the content inside { }
  // We need to handle quoted strings that may contain commas

  let i = 0;
  const s = str.trim();

  while (i < s.length) {
    // Skip whitespace
    while (i < s.length && /\s/.test(s[i])) i++;
    if (i >= s.length) break;

    // Read key
    let keyStart = i;
    while (i < s.length && s[i] !== ':' && s[i] !== ',') i++;
    const key = s.slice(keyStart, i).trim();
    if (!key) break;

    // Skip ':'
    if (s[i] === ':') i++;

    // Skip whitespace after colon
    while (i < s.length && s[i] === ' ') i++;

    // Read value
    let value = null;
    if (s[i] === '"' || s[i] === "'") {
      // Quoted string
      const quote = s[i];
      i++; // skip opening quote
      let val = '';
      while (i < s.length && s[i] !== quote) {
        if (s[i] === '\\' && i + 1 < s.length) {
          val += s[i + 1];
          i += 2;
        } else {
          val += s[i];
          i++;
        }
      }
      if (i < s.length) i++; // skip closing quote
      value = val;
    } else {
      // Unquoted value - read until comma or end
      let valStart = i;
      // But careful: might have inline comment after a comma
      while (i < s.length && s[i] !== ',' && s[i] !== '#') i++;
      value = s.slice(valStart, i).trim();
      // Parse unquoted values
      if (value === 'true') value = true;
      else if (value === 'false') value = false;
      else if (value === 'null' || value === '~' || value === '') value = null;
      else if (!isNaN(value) && value !== '') value = Number(value);
    }

    // Skip comma
    while (i < s.length && (s[i] === ',' || /\s/.test(s[i]))) {
      if (s[i] === '#') break; // inline comment - stop
      i++;
    }

    // Skip inline comment
    if (s[i] === '#') break;

    if (key) result[key] = value;
  }

  return result;
}

function parseYamlBool(val) {
  if (val === 'true') return true;
  if (val === 'false') return false;
  if (val === '' || val === 'null' || val === '~') return null;
  return null;
}

function parseYamlString(val) {
  if (val === '' || val === 'null' || val === '~') return null;
  // Strip quotes if present
  if ((val.startsWith('"') && val.endsWith('"')) ||
      (val.startsWith("'") && val.endsWith("'"))) {
    return val.slice(1, -1);
  }
  return val;
}

function fetchForkData(fork) {
  const { full_name, default_branch } = fork;

  try {
    const result = execSync(
      `gh api "repos/${full_name}/contents/aeon.yml?ref=${default_branch}" --jq '.content' 2>&1`,
      { encoding: 'utf8', timeout: 30000, stdio: ['pipe', 'pipe', 'pipe'] }
    );

    const raw = result.trim();

    if (!raw || raw === 'null') {
      return { full_name, status: 'no_aeon_yml', skills: {} };
    }

    // Check for error responses
    if (raw.includes('HTTP 404') || raw.includes('Not Found') || raw.toLowerCase().includes('not found')) {
      return { full_name, status: 'no_aeon_yml', skills: {} };
    }
    if (raw.includes('HTTP 403') || raw.includes('rate limit') || raw.toLowerCase().includes('rate limit')) {
      return { full_name, status: 'rate_limited', skills: {} };
    }

    // The content might include multi-line base64 with newlines embedded in JSON
    // Remove any whitespace/newlines in the base64 string
    const cleanB64 = raw.replace(/\s+/g, '');

    let content;
    try {
      content = Buffer.from(cleanB64, 'base64').toString('utf8');
    } catch (e) {
      return { full_name, status: 'yml_unreadable', skills: {} };
    }

    if (!content || content.trim() === '') {
      return { full_name, status: 'yml_invalid', skills: {} };
    }

    const skills = parseSkills(content);
    return { full_name, status: 'ok', skills };

  } catch (err) {
    const errMsg = err.message || String(err);
    if (errMsg.includes('404') || errMsg.toLowerCase().includes('not found')) {
      return { full_name, status: 'no_aeon_yml', skills: {} };
    }
    if (errMsg.includes('403') || errMsg.toLowerCase().includes('rate limit')) {
      return { full_name, status: 'rate_limited', skills: {} };
    }
    if (errMsg.includes('ETIMEDOUT') || errMsg.includes('timeout')) {
      return { full_name, status: 'timeout', skills: {} };
    }
    return { full_name, status: 'error', skills: {} };
  }
}

// Process all forks sequentially (to avoid rate limiting)
process.stderr.write(`Processing ${FORKS.length} forks...\n`);

const results = [];
for (let i = 0; i < FORKS.length; i++) {
  const fork = FORKS[i];
  process.stderr.write(`  [${i + 1}/${FORKS.length}] ${fork.full_name}... `);
  const result = fetchForkData(fork);
  results.push(result);
  process.stderr.write(`${result.status}\n`);
}

process.stderr.write('Done. Writing output...\n');
fs.writeFileSync(OUTPUT_PATH, JSON.stringify(results, null, 2), 'utf8');
process.stderr.write(`Written to ${OUTPUT_PATH}\n`);
