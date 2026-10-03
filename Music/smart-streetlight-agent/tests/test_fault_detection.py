import importlib.util

def load(path):
    s=importlib.util.spec_from_file_location("m",path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def test_faults():
    m=load("tools/detect-streetlight-faults.py")
    r=m.detect({"operational_status":"off","brightness":10,"power_watts":0,"ambient_light":5,"motion_detected":False,"last_maintenance_days":200})
    assert set(r["faults"]) == {"lamp_off","low_brightness","abnormal_power","maintenance_overdue"}
