"""Framework-independent contract for agent tools."""
from dataclasses import dataclass
from typing import Any, Callable


@dataclass(frozen=True)
class ToolResult:
    ok: bool
    data: dict[str, Any]
    error: str | None = None


@dataclass(frozen=True)
class ToolContract:
    name: str
    description: str
    input_schema: dict[str, Any]
    execute: Callable[[dict[str, Any]], dict[str, Any]]

    def validate(self, payload: dict[str, Any]) -> None:
        if not isinstance(payload, dict):
            raise ValueError("Tool input must be an object")
        required = self.input_schema.get("required", [])
        properties = self.input_schema.get("properties", {})
        for key in required:
            if key not in payload:
                raise ValueError(f"Missing required field: {key}")
        for key in payload:
            if key not in properties:
                raise ValueError(f"Unexpected field: {key}")

    def run(self, payload: dict[str, Any]) -> ToolResult:
        try:
            self.validate(payload)
            return ToolResult(True, self.execute(payload))
        except (TypeError, ValueError) as exc:
            return ToolResult(False, {}, str(exc))
        except Exception:
            return ToolResult(False, {}, "Tool execution failed")
