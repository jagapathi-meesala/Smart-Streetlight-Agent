from tools.search_literature import SearchLiteratureTool
from tools.build_citation import BuildCitationTool
def test_control_character(): assert not SearchLiteratureTool().run({"query":"ok\x00bad"}).ok
def test_missing_fields(): assert not BuildCitationTool().run({"authors":["A"],"year":2025}).ok
