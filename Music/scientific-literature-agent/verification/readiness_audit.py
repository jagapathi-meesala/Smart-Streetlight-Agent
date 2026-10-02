from pathlib import Path
import re,sys
R=Path(__file__).resolve().parents[1]
files=["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
dirs=["adapters","config","contracts","core","skills","tools","tests","verification"]
errors=[]
for x in files:
 if not (R/x).is_file(): errors.append(f"missing file: {x}")
for x in dirs:
 if not (R/x).is_dir(): errors.append(f"missing directory: {x}")
t=(R/"EXPLAINABILITY.md").read_text() if (R/"EXPLAINABILITY.md").exists() else ""
req=["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]
for h in req:
 if t.count(h)!=1: errors.append(f"required heading count is not one: {h}")
for h in ["## Inputs","## Decision","## Limits"]:
 if re.search(rf"^{re.escape(h)}\s*$",t,re.M): errors.append(f"conflicting heading: {h}")
if errors:
 print("READINESS AUDIT: FAIL\n"+"\n".join("- "+e for e in errors));sys.exit(1)
print("READINESS AUDIT: PASS")
print(f"Checked {len(files)} files and {len(dirs)} directories.")
