from urllib.parse import quote_plus
from contracts.tool_contract import ToolContract,ToolMetadata,ToolResult,ToolValidationError
class SearchLiteratureTool(ToolContract):
    metadata=ToolMetadata("search-literature","Build a safe deterministic literature-search request.",{"type":"object","properties":{"query":{"type":"string","minLength":2},"year_from":{"type":"integer","minimum":1800},"year_to":{"type":"integer","minimum":1800},"limit":{"type":"integer","minimum":1,"maximum":100}},"required":["query"],"additionalProperties":False})
    def validate(self,p):
        super().validate(p); q=p.get("query")
        if not isinstance(q,str) or len(q.strip())<2: raise ToolValidationError("query must contain at least two non-whitespace characters")
        if any(ord(c)<32 and c not in "\t\n" for c in q): raise ToolValidationError("query contains control characters")
        if "year_from" in p and not isinstance(p["year_from"],int): raise ToolValidationError("year_from must be an integer")
        if "year_to" in p and not isinstance(p["year_to"],int): raise ToolValidationError("year_to must be an integer")
        if p.get("year_from",1800)>p.get("year_to",9999): raise ToolValidationError("year_from cannot exceed year_to")
        if "limit" in p and (not isinstance(p["limit"],int) or not 1<=p["limit"]<=100): raise ToolValidationError("limit must be 1-100")
    def execute(self,p):
        q=" ".join(p["query"].split()); params=[f"q={quote_plus(q)}"]
        if "year_from" in p: params.append(f"year_from={p['year_from']}")
        if "year_to" in p: params.append(f"year_to={p['year_to']}")
        params.append(f"limit={p.get('limit',10)}")
        return ToolResult(True,{"query":q,"request_parameters":params,"note":"Request prepared; no external results are claimed."})
