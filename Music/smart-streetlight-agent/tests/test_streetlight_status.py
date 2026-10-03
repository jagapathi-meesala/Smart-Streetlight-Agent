import importlib.util

def load(path):
    s=importlib.util.spec_from_file_location("m",path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def test_status():
    m=load("tools/analyze-streetlight-status.py")
    r=m.analyze({"streetlight_id":"SL-1","operational_status":"operational","brightness":80,"power_watts":50,"ambient_light":10,"motion_detected":True,"last_maintenance_days":20})
    assert r["maintenance_priority"] == "normal"

def test_status_rejects_extra():
    m=load("tools/analyze-streetlight-status.py")
    x={"streetlight_id":"SL-1","operational_status":"operational","brightness":80,"power_watts":50,"ambient_light":10,"motion_detected":True,"last_maintenance_days":20,"x":1}
    try: m.analyze(x); assert False
    except ValueError: pass
