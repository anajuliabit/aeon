import subprocess
import json
import yaml
import sys
import base64
import concurrent.futures
import threading

FORKS = [
  {"full_name": "nigelon11/aeon", "default_branch": "main"},
  {"full_name": "webguy-cloud/aeon", "default_branch": "main"},
  {"full_name": "Loopershot/aeon", "default_branch": "main"},
  {"full_name": "s97472091-pixel/aeon", "default_branch": "main"},
  {"full_name": "usepaxterapp/aeon", "default_branch": "main"},
  {"full_name": "penguinxbt/aeon", "default_branch": "main"},
  {"full_name": "freezerboi/aeon", "default_branch": "main"},
  {"full_name": "anajuliabit/aeon-fork", "default_branch": "main"},
  {"full_name": "madmystic/aeon", "default_branch": "main"},
  {"full_name": "SamsShow/aeon", "default_branch": "main"},
  {"full_name": "Marr554/aeon", "default_branch": "main"},
  {"full_name": "alpenflow/aeon", "default_branch": "main"},
  {"full_name": "stefrogovskyi/aeon", "default_branch": "main"},
  {"full_name": "usephylax/aeon", "default_branch": "main"},
  {"full_name": "saivarmadpr/aeon", "default_branch": "main"},
  {"full_name": "Tholynceus/aeon", "default_branch": "main"},
  {"full_name": "logbookbase/aeon", "default_branch": "main"},
  {"full_name": "maredek-bot/aeon", "default_branch": "main"},
  {"full_name": "CharonAI-code/aeon", "default_branch": "main"},
  {"full_name": "KK-OS/aeon", "default_branch": "main"},
  {"full_name": "P9LLI/aeon", "default_branch": "main"},
  {"full_name": "adlai88/aeon", "default_branch": "main"},
  {"full_name": "vladimirvalcourt/aeon", "default_branch": "main"},
  {"full_name": "clawhunter/add-clawhunter-pack", "default_branch": "main"},
  {"full_name": "hurley87/aeon", "default_branch": "main"},
  {"full_name": "runchr-org/aeon", "default_branch": "main"},
  {"full_name": "brainlabors-dot/aeon", "default_branch": "main"},
  {"full_name": "rajkaria/aeon", "default_branch": "main"},
  {"full_name": "tenequm/aeon", "default_branch": "main"},
  {"full_name": "ziyosteve/aeon", "default_branch": "main"},
  {"full_name": "zszkey/aeon-1", "default_branch": "main"},
  {"full_name": "modelcollapse/aeon", "default_branch": "main"},
  {"full_name": "wrenwealth/aeon", "default_branch": "main"},
  {"full_name": "ghostx-dev/aeon", "default_branch": "main"},
  {"full_name": "sinfronterasai/aeon", "default_branch": "main"},
  {"full_name": "gitlumen-team/aeon", "default_branch": "main"},
  {"full_name": "ashneil12/aeon-upstream", "default_branch": "main"},
  {"full_name": "AdversaLLC/aeon", "default_branch": "main"},
  {"full_name": "anondevv69/bankr-space-aeon", "default_branch": "main"},
  {"full_name": "SahilParikh03/aeon", "default_branch": "main"},
  {"full_name": "mnemedb/aeon", "default_branch": "main"},
  {"full_name": "NASTYZUNI/aeon", "default_branch": "main"},
  {"full_name": "alfahadgm/aeon", "default_branch": "main"},
  {"full_name": "dannysrod/aeon", "default_branch": "main"},
  {"full_name": "chxoky/aeon", "default_branch": "main"},
  {"full_name": "daxaur/aeon", "default_branch": "main"},
  {"full_name": "aeoncity-hub/aeon", "default_branch": "main"},
  {"full_name": "beijiangqukuailian/aeon", "default_branch": "main"},
  {"full_name": "vigilcodes/aeon", "default_branch": "main"},
  {"full_name": "yindaqiu/aeon", "default_branch": "main"},
  {"full_name": "BBridgeers/aeon", "default_branch": "main"},
  {"full_name": "swarm-ai-research/aeon-atlas", "default_branch": "main"},
  {"full_name": "TakamiyaZee/aeon", "default_branch": "main"},
  {"full_name": "xBalbinus/aeon", "default_branch": "main"},
  {"full_name": "sparkleware/aeon", "default_branch": "main"},
  {"full_name": "codexvritra/aeon", "default_branch": "main"},
  {"full_name": "UIZorrot/aeon", "default_branch": "main"},
  {"full_name": "lawbworld-tech/aeon", "default_branch": "main"},
  {"full_name": "gitlawbounty/aeon", "default_branch": "main"},
  {"full_name": "0xShak/aeon", "default_branch": "main"},
  {"full_name": "taekwonv89/aeon", "default_branch": "main"},
  {"full_name": "0xMal0u/aeon", "default_branch": "main"},
  {"full_name": "youpsla/aeon", "default_branch": "main"},
  {"full_name": "antfleet-ops/aeon", "default_branch": "main"},
  {"full_name": "damo-nu11/aeon-minebean", "default_branch": "main"},
  {"full_name": "VibeSan7/aeon", "default_branch": "main"},
  {"full_name": "anomit/aeon", "default_branch": "main"},
  {"full_name": "enzoonchain/aeon", "default_branch": "main"},
  {"full_name": "AntFleet/aeon-bench", "default_branch": "main"},
  {"full_name": "takanafur/aeon", "default_branch": "main"},
  {"full_name": "madebyshun/blueagent-aeon", "default_branch": "main"},
  {"full_name": "usiclabs/aeon", "default_branch": "main"},
  {"full_name": "Da6hkin/aeon", "default_branch": "main"},
  {"full_name": "Boodszw/Boodszw_Bread", "default_branch": "main"},
  {"full_name": "ether-btc/aeon", "default_branch": "main"},
  {"full_name": "tomscaria/aeon", "default_branch": "main"},
  {"full_name": "yugo-engineer/aeon", "default_branch": "main"},
  {"full_name": "pezetel/aeon", "default_branch": "main"},
  {"full_name": "AmithKumar1/aeon", "default_branch": "main"},
]

lock = threading.Lock()
progress = [0]

def fetch_fork_data(fork):
    full_name = fork["full_name"]
    branch = fork["default_branch"]

    try:
        result = subprocess.run(
            ["gh", "api", f"repos/{full_name}/contents/aeon.yml?ref={branch}", "--jq", ".content"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode != 0 or not result.stdout.strip():
            err = result.stderr.lower()
            if "404" in err or "not found" in err or "null" in result.stdout.lower():
                return {"full_name": full_name, "status": "no_aeon_yml", "skills": {}}
            elif "403" in err or "rate limit" in err:
                return {"full_name": full_name, "status": "rate_limited", "skills": {}}
            else:
                return {"full_name": full_name, "status": "yml_unreadable", "skills": {}}

        raw = result.stdout.strip()
        if raw == "null":
            return {"full_name": full_name, "status": "no_aeon_yml", "skills": {}}

        content = base64.b64decode(raw).decode("utf-8", errors="replace")

        try:
            data = yaml.safe_load(content)
        except Exception:
            return {"full_name": full_name, "status": "yml_invalid", "skills": {}}

        if not data or not isinstance(data, dict):
            return {"full_name": full_name, "status": "yml_invalid", "skills": {}}

        skills_raw = data.get("skills", {}) or {}
        skills = {}
        for k, v in skills_raw.items():
            if v is None:
                v = {}
            if isinstance(v, dict):
                skills[k] = {
                    "enabled": v.get("enabled"),
                    "model": v.get("model"),
                    "var": v.get("var"),
                    "schedule": v.get("schedule"),
                }
            else:
                skills[k] = {"enabled": None, "model": None, "var": None, "schedule": None}

        with lock:
            progress[0] += 1
            sys.stderr.write(f"\r  Processed {progress[0]}/{len(FORKS)}: {full_name}    ")
            sys.stderr.flush()

        return {"full_name": full_name, "status": "ok", "skills": skills}

    except subprocess.TimeoutExpired:
        return {"full_name": full_name, "status": "timeout", "skills": {}}
    except Exception as e:
        return {"full_name": full_name, "status": f"error", "skills": {}}

sys.stderr.write(f"Processing {len(FORKS)} forks...\n")

with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    results = list(executor.map(fetch_fork_data, FORKS))

sys.stderr.write("\nDone.\n")

# Write directly to output file instead of stdout
output_path = "/home/runner/work/aeon/aeon/memory/topics/.fork_results_tmp.json"
with open(output_path, "w") as f:
    json.dump(results, f, indent=2)
sys.stderr.write(f"Written to {output_path}\n")
