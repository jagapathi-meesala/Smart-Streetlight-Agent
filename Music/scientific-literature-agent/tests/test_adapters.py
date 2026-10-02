from adapters.registry import default_registry
def test_adapters(): assert default_registry().discover()==["claude-code","crewai","lyzr","openai"]
