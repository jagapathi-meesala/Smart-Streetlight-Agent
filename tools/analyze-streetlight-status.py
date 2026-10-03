import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract

CONTRACT = ToolContract(
    required=["streetlight_id", "operational_status", "brightness", "power_watts", "ambient_light", "motion_detected", "last_maintenance_days"],
    properties={
        "streetlight_id": str, "operational_status": str, "brightness": (int, float),
        "power_watts": (int, float), "ambient_light": (int, float), "motion_detected": bool,
        "last_maintenance_days": (int, float),
    },
)

def analyze(data):
    CONTRACT.validate(data)
    status = data["operational_status"].lower()
    priority = "high" if status != "operational" or data["last_maintenance_days"] > 180 else "normal"
    reasons = []
    if status != "operational": reasons.append("streetlight is not marked operational")
    if data["last_maintenance_days"] > 180: reasons.append("maintenance interval exceeds 180 days")
    if not reasons: reasons.append("supplied operating indicators are within the defined rules")
    return {"streetlight_id": data["streetlight_id"], "status": status, "maintenance_priority": priority, "reasons": reasons}
