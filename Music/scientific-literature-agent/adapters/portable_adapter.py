from abc import ABC,abstractmethod
class AgentAdapter(ABC):
 @abstractmethod
 def invoke(self,instruction,context=None): raise NotImplementedError
class OpenAIAdapter(AgentAdapter):
 def invoke(self,instruction,context=None): return {"framework":"openai","status":"adapter-boundary-only","instruction":instruction,"context":context or {}}
class CrewAIAdapter(AgentAdapter):
 def invoke(self,instruction,context=None): return {"framework":"crewai","status":"adapter-boundary-only","instruction":instruction,"context":context or {}}
class ClaudeCodeAdapter(AgentAdapter):
 def invoke(self,instruction,context=None): return {"framework":"claude-code","status":"adapter-boundary-only","instruction":instruction,"context":context or {}}
class LyzrAdapter(AgentAdapter):
 def invoke(self,instruction,context=None): return {"framework":"lyzr","status":"adapter-boundary-only","instruction":instruction,"context":context or {}}
