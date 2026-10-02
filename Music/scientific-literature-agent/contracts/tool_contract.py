from dataclasses import dataclass
from typing import Any

class ToolValidationError(ValueError): pass
class ToolExecutionError(RuntimeError): pass
@dataclass(frozen=True)
class ToolMetadata:
    name: str
    description: str
    input_schema: dict[str, Any]
@dataclass
class ToolResult:
    ok: bool
    data: dict[str, Any] | None = None
    error: str | None = None
class ToolContract:
    metadata: ToolMetadata
    def validate(self,payload):
        if not isinstance(payload,dict): raise ToolValidationError("Tool input must be an object")
    def execute(self,payload): raise NotImplementedError
    def run(self,payload):
        try:
            self.validate(payload); return self.execute(payload)
        except ToolValidationError as e: return ToolResult(False,error=f"validation_error: {e}")
        except ToolExecutionError as e: return ToolResult(False,error=f"execution_error: {e}")
        except Exception as e: return ToolResult(False,error=f"unexpected_error: {type(e).__name__}: {e}")
