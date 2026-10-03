from pathlib import Path
import yaml

def test_manifest_references_exist():
    root=Path(__file__).parents[1]
    m=yaml.safe_load((root/'agent.yaml').read_text())
    for skill in m['skills']:
        assert (root/'skills'/skill/'SKILL.md').exists()
    for tool in m['tools']:
        assert (root/'tools'/(tool+'.yaml')).exists()

def test_manifest_basics():
    m=yaml.safe_load((Path(__file__).parents[1]/'agent.yaml').read_text())
    assert m['spec_version']=='0.1.0'
    assert m['name']=='smart-streetlight-agent'
