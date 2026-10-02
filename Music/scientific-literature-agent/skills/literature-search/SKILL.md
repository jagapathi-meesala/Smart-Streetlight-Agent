---
name: literature-search
description: Prepare and structure scientific literature searches without fabricating search results.
---
# Literature Search

## Purpose
Prepare and structure scientific literature searches without fabricating search results.

## Inputs
A research query with optional publication-year bounds and result limit.

## Processing
Normalize whitespace, validate bounds, and create deterministic request parameters. External search results must come from an actual retrieval system.

## Outputs
A normalized query, request parameters, and explicit retrieval status.

## Limitations
It cannot verify papers or metadata without an external source.

## Expected behavior
Reject malformed inputs and never invent missing evidence.
