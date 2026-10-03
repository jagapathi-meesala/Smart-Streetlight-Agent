from adapters.registry import AdapterRegistry

class A:
    def invoke(self, tool_name, payload): return {'ok':True}

def test_registry():
    r=AdapterRegistry(); r.register('generic',A()); assert r.names()==['generic']; assert r.get('generic') is not None
