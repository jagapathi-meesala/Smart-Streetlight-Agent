# Explainability

## Inputs and Data Sources
Inputs include a research topic or question, target population, outcomes, exposures, objectives, study-design constraints, and other fields explicitly supplied to the tools. Data sources are limited to user-provided study metadata and deterministic rules encoded in the agent; the agent does not silently retrieve or invent empirical datasets.

### Input Requirements
Each tool declares its required fields and validates their types at the contract layer. Missing or malformed required inputs are rejected rather than replaced with fabricated assumptions.

### Failure Handling
Invalid input returns a structured error without executing the domain operation. Unexpected fields are rejected to reduce accidental misuse and ambiguous interpretation.

## Decision and Reasoning
The decision process maps the supplied research objective and design characteristics to candidate methodologies using explicit deterministic rules. For example, randomized intervention studies map to a randomized-controlled-trial candidate, while observational association objectives map to an observational-analytic candidate when no stronger design signal is supplied.

### Rules Applied
Method selection considers intervention status, randomization, qualitative intent, longitudinal structure, and objective wording. Methodology plans then expand the selected method into population and sampling, variables, collection, analysis, validity, ethics, and reproducibility sections.

### Expected Outputs
Outputs include a structured research question, candidate methods with rationales and limitations, or a reproducible methodology-plan template. Outputs do not include fabricated results, invented citations, or claims that an ethics board or study has approved the plan.

### Worked Example
For a topic about whether an intervention changes an outcome in a defined population, the question tool makes the population, exposure, and outcome explicit. If randomization is supplied as feasible, the method-selection tool includes a randomized controlled trial candidate and explains the associated limitations.

## Limits and Constraints
The agent cannot determine whether a study is ethically acceptable, cannot establish causal validity from a research question alone, and cannot calculate a defensible sample size without study-specific assumptions. Domain-specific standards, measurement validity, power assumptions, recruitment feasibility, and statistical review may materially change the final protocol.

### Constraints
The methodology recommendations are planning aids and should be reviewed by qualified researchers before execution. The agent does not collect participants, submit registrations, access private records, or claim empirical evidence that was not supplied.

### Known Issues
Natural-language objective matching is intentionally conservative and may return an exploratory or observational candidate when the supplied description is underspecified. A human researcher must resolve ambiguity and document any deviations from the generated plan.

### Unsupported Behavior
The agent does not fabricate datasets, participant counts, p-values, effect sizes, citations, approvals, or study results. It also does not present a candidate methodology as proof that the resulting study will be valid.
