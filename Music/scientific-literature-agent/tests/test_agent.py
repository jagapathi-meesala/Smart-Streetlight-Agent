from core.agent_core import ScientificLiteratureAgent,ToolRegistry
from tools.search_literature import SearchLiteratureTool
from tools.analyze_paper import AnalyzePaperTool
from tools.build_citation import BuildCitationTool
def make_agent():
 r=ToolRegistry()
 for t in (SearchLiteratureTool(),AnalyzePaperTool(),BuildCitationTool()): r.register(t)
 return ScientificLiteratureAgent(r)
def test_capabilities(): assert make_agent().capabilities()==["analyze-paper","build-citation","search-literature"]
def test_unknown_tool(): assert not make_agent().run_tool("missing",{})["ok"]
