from contracts.tool_contract import ToolContract,ToolResult
class ToolRegistry:
 def __init__(self): self._tools={}
 def register(self,tool):
  if not isinstance(tool,ToolContract): raise ValueError("tool must implement ToolContract")
  if tool.metadata.name in self._tools: raise ValueError(f"Tool already registered: {tool.metadata.name}")
  self._tools[tool.metadata.name]=tool
 def discover(self): return sorted(self._tools)
 def execute(self,name,payload): return self._tools[name].run(payload) if name in self._tools else ToolResult(False,error=f"unknown_tool: {name}")
class ScientificLiteratureAgent:
 def __init__(self,registry): self.registry=registry
 def capabilities(self): return self.registry.discover()
 def run_tool(self,name,payload):
  r=self.registry.execute(name,payload); return {"ok":r.ok,"data":r.data,"error":r.error}
