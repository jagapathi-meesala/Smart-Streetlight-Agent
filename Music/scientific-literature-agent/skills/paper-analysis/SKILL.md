---
name: paper-analysis
description: Analyze supplied scientific paper text using evidence-grounded structure.
---
# Paper Analysis

## Purpose
Analyze supplied scientific paper text using evidence-grounded structure.

## Inputs
Paper text or an extracted document body.

## Processing
Detect common research sections from supplied text; missing information remains missing.

## Outputs
Counts, detected sections, and the evidence policy.

## Limitations
Section detection does not establish scientific validity.

## Expected behavior
Reject malformed inputs and never invent missing evidence.
