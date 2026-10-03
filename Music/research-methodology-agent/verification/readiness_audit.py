from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
required = ["agent.yaml","SOUL.md","README.md","AGENTS.md","DUTIES.md","RULES.md","EXPLAINABILITY.md",".env.example",".gitignore","requirements.txt","pytest.ini"]
dirs_ = ["adapters","config","contracts","core","skills","tools","tests","verification"]
for f in required:
    assert (ROOT/f).is_file(), f"missing file: {f}"
for d in dirs_:
    assert (ROOT/d).is_dir(), f"missing directory: {d}"
text = (ROOT/"EXPLAINABILITY.md").read_text()
for heading in ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]:
    assert text.count(heading) == 1, f"bad heading count: {heading}"
    assert text.split(heading,1)[1].strip(), f"empty section: {heading}"
for bad in ["## Inputs\n","## Decision\n","## Limits\n"]:
    assert bad not in text, f"conflicting heading: {bad.strip()}"
manifest = (ROOT/"agent.yaml").read_text()
assert 'spec_version: "0.1.0"' in manifest
assert re.search(r"name: research-methodology-agent", manifest)
print("READINESS AUDIT: PASS")
print("Checked 11 files and 8 directories.")
