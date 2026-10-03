from contracts.tool_contract import ToolContract


class AdapterRegistry:
    def __init__(self):
        self._adapters = {}

    def register(self, name: str, adapter):
        if not name or not hasattr(adapter, "invoke"):
            raise ValueError("adapter must have a name and invoke method")
        self._adapters[name] = adapter

    def get(self, name: str):
        return self._adapters.get(name)

    def names(self):
        return sorted(self._adapters)
