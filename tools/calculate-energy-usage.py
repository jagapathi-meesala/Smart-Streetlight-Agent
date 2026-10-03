import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from contracts.tool_contract import ToolContract

CONTRACT = ToolContract(
    required=["power_watts", "operating_hours", "number_of_lights"],
    properties={"power_watts": (int, float), "operating_hours": (int, float), "number_of_lights": int},
)

def calculate(data):
    CONTRACT.validate(data)
    if data["power_watts"] < 0 or data["operating_hours"] < 0 or data["number_of_lights"] < 0:
        raise ValueError("Energy inputs cannot be negative")
    wh = data["power_watts"] * data["operating_hours"] * data["number_of_lights"]
    return {"watt_hours": wh, "kilowatt_hours": wh / 1000, "total_consumption": wh / 1000}
