import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
REQUEST_TIMEOUT_SECONDS = int(os.getenv("REQUEST_TIMEOUT_SECONDS", "20"))
MAX_RESULTS = int(os.getenv("MAX_RESULTS", "20"))
LITERATURE_API_URL = os.getenv("LITERATURE_API_URL", "")
USER_AGENT = os.getenv("LITERATURE_USER_AGENT", "ScientificLiteratureAgent/1.0")

def external_api_url() -> str:
    value = os.getenv("LITERATURE_API_URL")
    if not value:
        raise RuntimeError("Required environment variable LITERATURE_API_URL is not set")
    return value
