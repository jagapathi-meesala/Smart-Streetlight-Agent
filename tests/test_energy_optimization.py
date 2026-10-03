import importlib.util

def load(path):
    s=importlib.util.spec_from_file_location("m",path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m

def test_energy():
    m=load("tools/calculate-energy-usage.py")
    assert m.calculate({"power_watts":50,"operating_hours":8,"number_of_lights":10})["kilowatt_hours"] == 4.0

def test_schedule_motion():
    m=load("tools/optimize-lighting-schedule.py")
    assert m.optimize({"current_hour":20,"ambient_light":10,"motion_level":1,"brightness_levels":[20,50,100]})["recommended_brightness"] == 100
