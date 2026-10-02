from tools.search_literature import SearchLiteratureTool
from tools.analyze_paper import AnalyzePaperTool
from tools.build_citation import BuildCitationTool
def test_search(): assert SearchLiteratureTool().run({"query":"graph neural networks"}).ok
def test_bad_range(): assert not SearchLiteratureTool().run({"query":"abc","year_from":2025,"year_to":2020}).ok
def test_analysis(): assert AnalyzePaperTool().run({"text":"Abstract paper. Methods tested. Results observed. "+"x"*60}).data["sections_detected"]["methods"]
def test_citation(): assert "A Study" in BuildCitationTool().run({"authors":["Smith, J.","Doe, A."],"year":2025,"title":"A Study","venue":"Journal"}).data["citation"]
