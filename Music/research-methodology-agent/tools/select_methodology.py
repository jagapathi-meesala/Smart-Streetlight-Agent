"""Select candidate methodologies from explicit research characteristics."""
from contracts.tool_contract import ToolContract


def execute(payload: dict) -> dict:
    objective = payload["objective"].strip().lower()
    intervention = bool(payload.get("intervention", False))
    randomization = bool(payload.get("randomization", False))
    qualitative = bool(payload.get("qualitative", False))
    longitudinal = bool(payload.get("longitudinal", False))
    if not objective:
        raise ValueError("objective must not be empty")

    options = []
    if qualitative:
        options.append(("qualitative-study", "Useful for understanding experiences, meanings, or processes.", "Requires a transparent sampling and coding strategy."))
    if intervention and randomization:
        options.append(("randomized-controlled-trial", "Random allocation supports comparison of intervention groups.", "Requires feasible allocation, outcome definitions, and ethical oversight."))
    elif intervention:
        options.append(("quasi-experimental-study", "Useful when an intervention exists but random allocation is not feasible.", "Confounding and selection effects require explicit handling."))
    if longitudinal:
        options.append(("longitudinal-observational-study", "Useful for examining change or temporal associations.", "Attrition and time-varying confounding can affect inference."))
    if not options:
        if any(word in objective for word in ("prevalence", "frequency", "describe", "distribution")):
            options.append(("cross-sectional-descriptive-study", "Provides a snapshot of characteristics at a defined time.", "Temporal ordering and causality are limited."))
        elif any(word in objective for word in ("association", "relationship", "predict")):
            options.append(("observational-analytic-study", "Estimates associations without assigning exposure.", "Association does not by itself establish causation."))
        else:
            options.append(("exploratory-study", "Useful when the phenomenon or measurement approach needs initial investigation.", "Findings may require confirmation in a subsequent study."))

    return {"objective": payload["objective"], "candidates": [{"method": a, "rationale": b, "limitations": c} for a, b, c in options]}


CONTRACT = ToolContract(
    "select-methodology",
    "Identify candidate study methodologies from explicit research characteristics.",
    {"type": "object", "required": ["objective"], "properties": {"objective": {"type": "string"}, "intervention": {"type": "boolean"}, "randomization": {"type": "boolean"}, "qualitative": {"type": "boolean"}, "longitudinal": {"type": "boolean"}}},
    execute,
)
