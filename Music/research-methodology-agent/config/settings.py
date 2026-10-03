"""Environment-backed runtime settings with no production secrets or defaults."""
import os


def get_setting(name: str, required: bool = False) -> str | None:
    value = os.getenv(name)
    if required and not value:
        raise ValueError(f"Required environment variable is missing: {name}")
    return value


def log_level() -> str:
    return get_setting("LOG_LEVEL") or "INFO"


def max_options() -> int:
    raw = get_setting("METHODOLOGY_MAX_OPTIONS")
    if not raw:
        return 5
    value = int(raw)
    if not 1 <= value <= 10:
        raise ValueError("METHODOLOGY_MAX_OPTIONS must be between 1 and 10")
    return value
