"""Turn a broad research topic into a structured research question."""
from contracts.tool_contract import ToolContract


def execute(payload: dict) -> dict:
    topic = payload["topic"].strip()
    population = payload["population"].strip()
    outcome = payload["outcome"].strip()
    exposure = payload.get("exposure", "").strip()
    context = payload.get("context", "").strip()
    if len(topic) < 5 or len(population) < 2 or len(outcome) < 2:
        raise ValueError("topic, population, and outcome must be meaningful non-empty text")
    question = f"Among {population}, how is {outcome} related to {exposure or 'the study factor of interest'} in {context or 'the stated study context'}?"
    return {
        "question": question,
        "topic": topic,
        "population": population,
        "outcome": outcome,
        "exposure": exposure or None,
        "context": context or None,
        "assumptions": ["The supplied outcome is measurable.", "The population definition is operationalized before data collection."],
    }


CONTRACT = ToolContract(
    "define-research-question",
    "Structure a research topic into an explicit, measurable research question.",
    {"type": "object", "required": ["topic", "population", "outcome"], "properties": {"topic": {"type": "string"}, "population": {"type": "string"}, "outcome": {"type": "string"}, "exposure": {"type": "string"}, "context": {"type": "string"}}},
    execute,
)
