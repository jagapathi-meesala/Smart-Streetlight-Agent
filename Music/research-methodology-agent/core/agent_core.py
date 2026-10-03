"""Dynamic framework-independent tool registry and execution core."""
from typing import Any
from contracts.tool_contract import ToolContract, ToolResult


class AgentCore:
    def __init__(self):
        self._tools: dict[str, ToolContract] = {}

    def register(self, tool: ToolContract) -> None:
        if tool.name in self._tools:
            raise ValueError(f"Tool already registered: {tool.name}")
        self._tools[tool.name] = tool

    def discover(self) -> list[str]:
        return sorted(self._tools)

    def execute(self, name: str, payload: dict[str, Any]) -> ToolResult:
        tool = self._tools.get(name)
        if tool is None:
            return ToolResult(False, {}, f"Unknown tool: {name}")
        return tool.run(payload)
