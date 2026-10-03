# Explainability

## Inputs and Data Sources
The agent uses only values supplied to each tool. It does not retrieve live sensor data or invent missing measurements.

## Decision and Reasoning
Decisions are deterministic rules based on operational status, brightness, power, ambient light, motion, maintenance age, and supplied configuration.

## Limits and Constraints
The agent cannot verify physical streetlights, access live IoT devices, resolve unknown sensor values, or guarantee that a recommendation reflects conditions not represented in the input data.

## Tool Inputs
Each tool documents its required fields in its YAML contract and implementation.

## Failure Handling
Invalid types, missing required values, unsupported values, and unexpected fields are rejected with clear errors.
