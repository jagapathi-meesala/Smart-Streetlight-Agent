from .portable_adapter import *
class AdapterRegistry:
 def __init__(self): self._adapters={}
 def register(self,name,adapter):
  if not name or not isinstance(adapter,AgentAdapter): raise ValueError("adapter name and AgentAdapter required")
  self._adapters[name]=adapter
 def discover(self): return sorted(self._adapters)
 def get(self,name): return self._adapters[name]
def default_registry():
 r=AdapterRegistry()
 for n,c in (("openai",OpenAIAdapter),("crewai",CrewAIAdapter),("claude-code",ClaudeCodeAdapter),("lyzr",LyzrAdapter)): r.register(n,c())
 return r
