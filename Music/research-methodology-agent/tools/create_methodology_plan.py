"""Generate a reproducible methodology-plan template."""
from contracts.tool_contract import ToolContract


def execute(payload: dict) -> dict:
    question = payload["research_question"].strip()
    method = payload["method"].strip()
    if len(question) < 10 or len(method) < 3:
        raise ValueError("research_question and method must be meaningful")
    return {
        "research_question": question,
        "method": method,
        "plan": {
            "population_and_sampling": "Define target population, eligibility criteria, sampling frame, and sampling approach.",
            "variables": "Define primary outcome, exposures/intervention, covariates, and operational measurements.",
            "data_collection": "Specify instruments, timing, procedures, quality controls, and missing-data recording.",
            "analysis": "Pre-specify descriptive summaries, primary analysis, assumptions, sensitivity analyses, and reporting rules.",
            "validity": "Identify major sources of bias, confounding, measurement error, and steps to reduce them.",
            "ethics": "Confirm applicable consent, privacy, risk, and institutional review requirements before data collection.",
            "reproducibility": "Record protocol version, data dictionary, analysis code, and deviations from the plan.",
        },
        "limitations": ["This template does not determine an appropriate sample size without study-specific assumptions.", "Ethics and domain requirements must be reviewed by qualified personnel."],
    }


CONTRACT = ToolContract(
    "create-methodology-plan",
    "Create a structured, reproducible research methodology plan from a question and selected method.",
    {"type": "object", "required": ["research_question", "method"], "properties": {"research_question": {"type": "string"}, "method": {"type": "string"}}},
    execute,
)
