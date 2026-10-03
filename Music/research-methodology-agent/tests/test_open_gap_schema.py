from pathlib import Path
import yaml
ROOT=Path(__file__).resolve().parents[1]

def test_manifest_shape():
    m=yaml.safe_load((ROOT/'agent.yaml').read_text()); assert m['spec_version']=='0.1.0'; assert m['name']=='research-methodology-agent'; assert all(isinstance(x,str) for x in m['skills'])

def test_tool_schemas_have_properties():
    for p in (ROOT/'tools').glob('*.yaml'):
        d=yaml.safe_load(p.read_text()); s=d['input_schema']; assert s['type']=='object' and isinstance(s['properties'],dict)
