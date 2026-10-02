from pathlib import Path
R=Path(__file__).resolve().parents[1]
def test_explainability():
 t=(R/"EXPLAINABILITY.md").read_text()
 for h in ["## Inputs and Data Sources","## Decision and Reasoning","## Limits and Constraints"]: assert t.count(h)==1
 for s in ["## Inputs\n","## Decision\n","## Limits\n"]: assert s not in t
def test_skills():
 for s in ["literature-search","paper-analysis","citation-management"]: assert (R/"skills"/s/"SKILL.md").is_file()
