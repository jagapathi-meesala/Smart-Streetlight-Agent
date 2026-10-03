import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract

CONTRACT = ToolContract(
    required=["operational_status", "brightness", "power_watts", "ambient_light", "motion_detected", "last_maintenance_days"],
    properties={"operational_status": str, "brightness": (int, float), "power_watts": (int, float), "ambient_light": (int, float), "motion_detected": bool, "last_maintenance_days": (int, float)},
)

def detect(data):
    CONTRACT.validate(data)
    faults = []
    if data["operational_status"].lower() != "operational": faults.append("lamp_off")
    if data["brightness"] < 20: faults.append("low_brightness")
    if data["power_watts"] <= 0: faults.append("abnormal_power")
    if data["last_maintenance_days"] > 180: faults.append("maintenance_overdue")
    return {"faults": faults, "fault_count": len(faults)}
