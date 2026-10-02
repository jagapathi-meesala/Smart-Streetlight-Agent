import re
from contracts.tool_contract import ToolContract,ToolMetadata,ToolResult,ToolValidationError
class AnalyzePaperTool(ToolContract):
    metadata=ToolMetadata("analyze-paper","Extract structured research fields from supplied paper text.",{"type":"object","properties":{"text":{"type":"string","minLength":50}},"required":["text"],"additionalProperties":False})
    def validate(self,p):
        super().validate(p)
        if not isinstance(p.get("text"),str) or len(p["text"].strip())<50: raise ToolValidationError("text must contain at least 50 characters")
    def execute(self,p):
        t=" ".join(p["text"].split()); labels=("abstract","introduction","methods","methodology","results","discussion","conclusion","limitations")
        return ToolResult(True,{"character_count":len(t),"word_count":len(t.split()),"sections_detected":{x:bool(re.search(rf"\b{x}\b",t,re.I)) for x in labels},"evidence_policy":"Only supplied text is analyzed; absent information is not inferred."})
