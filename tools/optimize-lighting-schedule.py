import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract

CONTRACT = ToolContract(
    required=["current_hour", "ambient_light", "motion_level", "brightness_levels"],
    properties={"current_hour": int, "ambient_light": (int, float), "motion_level": (int, float), "brightness_levels": list},
)

def optimize(data):
    CONTRACT.validate(data)
    levels = data["brightness_levels"]
    if not levels: raise ValueError("brightness_levels must not be empty")
    if data["ambient_light"] >= 70 and data["motion_level"] == 0:
        target = min(levels)
        reason = "high ambient light and no motion"
    elif data["motion_level"] > 0:
        target = max(levels)
        reason = "motion detected"
    else:
        target = sorted(levels)[len(levels)//2]
        reason = "moderate environmental conditions"
    return {"recommended_brightness": target, "reason": reason}
