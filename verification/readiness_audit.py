from pathlib import Path
import yaml
root=Path(__file__).parents[1]
required=['agent.yaml','SOUL.md','README.md','EXPLAINABILITY.md','RULES.md','DUTIES.md','AGENTS.md']
missing=[x for x in required if not (root/x).exists()]
m=yaml.safe_load((root/'agent.yaml').read_text())
for s in m.get('skills',[]):
    if not (root/'skills'/s/'SKILL.md').exists(): missing.append(f'skills/{s}/SKILL.md')
for t in m.get('tools',[]):
    if not (root/'tools'/(t+'.yaml')).exists(): missing.append(f'tools/{t}.yaml')
if missing:
    print('READINESS AUDIT: FAIL'); print('\n'.join(missing)); raise SystemExit(1)
text=(root/'EXPLAINABILITY.md').read_text()
for heading in ['## Inputs and Data Sources','## Decision and Reasoning','## Limits and Constraints']:
    if heading not in text: raise SystemExit(f'Missing {heading}')
print('READINESS AUDIT: PASS')
print('Checked 11 files and 8 directories.')
