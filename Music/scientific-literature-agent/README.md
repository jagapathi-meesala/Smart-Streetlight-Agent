# Scientific Literature Agent

A framework-independent OpenGAP 0.1.0 agent for literature-search preparation, paper-text analysis, and citation formatting.

## Architecture

`agent.yaml` defines identity and capabilities. `core/` provides the dynamic registry, `contracts/` defines framework-neutral tool interfaces, `tools/` contains domain tools and schemas, `skills/` documents capabilities, and `adapters/` defines portability boundaries.

## Installation

Use Python 3.10+ and install `requirements.txt`.

## Configuration

Runtime values are environment variables; secrets are not stored in source.

## Tools

- search-literature
- analyze-paper
- build-citation

## Skills

- literature-search
- paper-analysis
- citation-management

## Usage

Register the three domain tools in `ToolRegistry` and call `ScientificLiteratureAgent.run_tool`. Results use `{ok, data, error}`.

## Testing

Run `pytest -q` and `python verification/readiness_audit.py`.

## Portability

Core logic has no dependency on OpenAI, CrewAI, Claude, or Lyzr. Adapter classes are boundaries only and are not claims of end-to-end provider certification.

## Limitations

The current tools do not perform external literature retrieval or independently verify scientific claims, metadata, peer-review status, or DOI resolution.
