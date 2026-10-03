"""Framework-neutral adapter interface."""
from abc import ABC, abstractmethod
from typing import Any


class PortableAdapter(ABC):
    framework_name = "framework-independent"

    @abstractmethod
    def invoke(self, tool_name: str, payload: dict[str, Any]) -> dict[str, Any]:
        raise NotImplementedError
