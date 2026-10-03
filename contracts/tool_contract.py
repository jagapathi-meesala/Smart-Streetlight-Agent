class ToolContract:
    def __init__(self, required=None, properties=None):
        self.required = required or []
        self.properties = properties or {}

    def validate(self, data):
        if not isinstance(data, dict):
            raise ValueError("Input must be an object")
        missing = [k for k in self.required if k not in data]
        if missing:
            raise ValueError(f"Missing required fields: {', '.join(missing)}")
        unexpected = [k for k in data if k not in self.properties]
        if unexpected:
            raise ValueError(f"Unexpected fields: {', '.join(unexpected)}")
        for key, expected in self.properties.items():
            if key in data and expected is not None and not isinstance(data[key], expected):
                raise ValueError(f"Invalid type for {key}")
        return True
