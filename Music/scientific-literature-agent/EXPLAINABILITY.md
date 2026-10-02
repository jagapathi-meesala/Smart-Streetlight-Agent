# Explainability

## Inputs and Data Sources

The agent accepts research queries, optional publication-year bounds, supplied scientific paper text, and explicitly supplied bibliographic metadata. Data sources are limited to user-provided material and any external literature retrieval service that is explicitly configured and actually invoked; the deterministic tools do not pretend to have retrieved records.

### Input Requirements

Search requests require a non-empty query, paper analysis requires sufficient text, and citation formatting requires authors, year, title, and venue. Validation rejects malformed types, invalid year ranges, control characters, and missing required fields.

### Failure Handling

Invalid input produces a structured validation error instead of an unhandled exception. External retrieval is treated as unavailable unless a real retrieval system supplies results.

## Decision and Reasoning

The agent selects processing from the requested tool and its validated input schema rather than from a framework-specific chain. Search preparation normalizes the query and parameters, paper analysis detects explicit research-section markers, and citation management applies deterministic formatting to supplied metadata.

### Rules Applied

The search tool encodes request parameters, the analysis tool reports only sections detectable in supplied text, and the citation tool uses only explicitly provided fields. No rule permits the agent to fill missing evidence, authors, dates, results, or DOI information.

### Expected Outputs

Each tool returns structured data or an explicit error. Outputs expose limitations so downstream systems can distinguish transformation from scientific verification.

### Worked Example

A query such as `graph neural networks for traffic forecasting` is normalized and returned with deterministic request parameters. Supplied text containing `Abstract`, `Methods`, and `Results` reports those sections while an absent `Limitations` section remains absent.

## Limits and Constraints

The agent cannot establish scientific validity merely by detecting sections or formatting a citation. It cannot claim that external papers were searched or verified unless an actual configured retrieval system returns those records.

### Constraints

Runtime configuration is supplied through environment variables, and no API key or password is embedded in the repository. Adapter boundaries do not constitute provider-specific end-to-end certification.

### Known Issues

Section detection is lexical and may miss unconventional headings. Citation formatting does not validate metadata against an authoritative bibliographic service.

### Expected Safety Boundary

The agent must not expose secrets, invent citations, or turn missing evidence into factual claims. Human review remains appropriate for high-stakes literature synthesis and scientific conclusions.
