from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def test_explainability_headings():
    t=(ROOT/'EXPLAINABILITY.md').read_text(); assert all(x in t for x in ['## Inputs and Data Sources','## Decision and Reasoning','## Limits and Constraints'])

def test_no_conflicting_headings():
    t=(ROOT/'EXPLAINABILITY.md').read_text(); assert '## Inputs\n' not in t and '## Decision\n' not in t and '## Limits\n' not in t
