import pytest
from core.agent_core import ToolRegistry
from tools.search_literature import SearchLiteratureTool
def test_discovery():
 r=ToolRegistry();r.register(SearchLiteratureTool());assert r.discover()==["search-literature"]
def test_duplicate():
 r=ToolRegistry();r.register(SearchLiteratureTool())
 with pytest.raises(ValueError):r.register(SearchLiteratureTool())
