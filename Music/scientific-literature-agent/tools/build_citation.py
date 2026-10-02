from contracts.tool_contract import ToolContract,ToolMetadata,ToolResult,ToolValidationError
class BuildCitationTool(ToolContract):
    metadata=ToolMetadata("build-citation","Create a deterministic APA-like citation from supplied metadata.",{"type":"object","properties":{"authors":{"type":"array","items":{"type":"string","minLength":1},"minItems":1},"year":{"type":"integer","minimum":1},"title":{"type":"string","minLength":1},"venue":{"type":"string","minLength":1},"doi":{"type":"string","minLength":1}},"required":["authors","year","title","venue"],"additionalProperties":False})
    def validate(self,p):
        super().validate(p)
        if not isinstance(p.get("authors"),list) or not p["authors"] or not all(isinstance(a,str) and a.strip() for a in p["authors"]): raise ToolValidationError("authors must be a non-empty list of strings")
        for k in ("title","venue"):
            if not isinstance(p.get(k),str) or not p[k].strip(): raise ToolValidationError(f"{k} must be a non-empty string")
        if not isinstance(p.get("year"),int) or p["year"]<1: raise ToolValidationError("year must be positive integer")
    def execute(self,p):
        a=", ".join(p["authors"][:-1])+(f", & {p['authors'][-1]}" if len(p["authors"])>1 else ""); c=f"{a} ({p['year']}). {p['title']}. {p['venue']}."
        if p.get("doi"): c+=f" https://doi.org/{p['doi'].removeprefix('https://doi.org/')}"
        return ToolResult(True,{"style":"APA-like","citation":c})
