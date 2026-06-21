import yaml
import json
import sys
from datetime import datetime, timezone
import os

# Load aeon.yml
with open('aeon.yml', 'r') as f:
    try:
        data = yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML: {e}")
        sys.exit(1)

skills = data.get('skills', {})
enabled_skills = []
for skill_name, config in skills.items():
    if config.get('enabled', False):
        enabled_skills.append(skill_name)

print(f"Found {len(enabled_skills)} enabled skills")
print(json.dumps(enabled_skills, indent=2))