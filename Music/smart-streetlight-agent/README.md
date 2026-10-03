# Smart Streetlight Agent

A framework-independent OpenGAP-compatible agent for streetlight monitoring, fault detection, lighting schedule recommendations, and energy calculations.

## Validation

```bash
pytest -q
python3 verification/readiness_audit.py
opengap validate
```

The agent does not require IoT hardware or external APIs for its core functions.
