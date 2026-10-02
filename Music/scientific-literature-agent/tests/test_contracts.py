from contracts.tool_contract import ToolContract,ToolMetadata,ToolResult
class Echo(ToolContract):
 metadata=ToolMetadata("echo","echo",{"type":"object"})
 def execute(self,p): return ToolResult(True,p)
def test_contract(): assert Echo().run({"x":1}).data=={"x":1}
def test_invalid(): assert not Echo().run([]).ok
