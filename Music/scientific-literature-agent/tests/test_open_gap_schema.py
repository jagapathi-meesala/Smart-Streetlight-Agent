from pathlib import Path
import yaml
from jsonschema import Draft202012Validator
def test_manifest():
 m=yaml.safe_load((Path(__file__).resolve().parents[1]/"agent.yaml").read_text())
 schema={"type":"object","required":["name","version","description"],"properties":{"spec_version":{"type":"string","pattern":"^\\d+\\.\\d+\\.\\d+$"},"name":{"type":"string","pattern":"^[a-z][a-z0-9-]*$"},"version":{"type":"string","pattern":"^\\d+\\.\\d+\\.\\d+"},"description":{"type":"string","minLength":1}},"additionalProperties":False}
 Draft202012Validator(schema).validate({k:m[k] for k in ["spec_version","name","version","description"]})
 assert m["spec_version"]=="0.1.0"
