# Research Methodology Agent

A framework-independent research-planning agent for structuring research questions, identifying candidate study methodologies, and generating reproducible methodology plans.

## Architecture
The core is Python-only and independent of OpenAI, Claude, CrewAI, LangChain, or Lyzr. Tools implement a common contract; the registry discovers and executes them dynamically; adapters expose a framework-neutral integration point.

## Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Configuration
Runtime settings are read from environment variables. Copy `.env.example` into your environment as needed; no credentials are included.

## Tools
- `define-research-question`: structures a topic into a measurable question.
- `select-methodology`: identifies candidate designs from explicit characteristics.
- `create-methodology-plan`: creates a structured reproducible plan.

## Skills
- `research-question`
- `method-selection`
- `methodology-planning`

## Usage
```python
from core.agent_core import AgentCore
from tools import define_research_question, select_methodology, create_methodology_plan
agent = AgentCore()
for tool in (define_research_question, select_methodology, create_methodology_plan): agent.register(tool)
print(agent.execute('select-methodology', {'objective':'estimate an association'}))
```

## Testing
Run `pytest -q`, then `python3 verification/readiness_audit.py`. If installed, run `opengap validate` and report its actual result.

## Portability
The core tool contract is framework-independent. The repository provides an adapter interface but does not claim tested compatibility with a specific external SDK unless that integration is separately tested.

## Limitations
Method selection is rule-based and depends on the completeness and quality of supplied information. It does not replace statistical, domain, or ethics review and does not fabricate evidence or study results.
