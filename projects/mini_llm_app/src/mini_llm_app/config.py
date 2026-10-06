import os
from dataclasses import dataclass

from dotenv import load_dotenv

from mini_llm_app.exceptions import ConfigError


load_dotenv()


@dataclass(frozen=True)
class Settings:
    api_key: str
    model: str
    log_level: str

    @classmethod
    def from_env(cls) -> "Settings":
        api_key = os.getenv("LLM_API_KEY")
        model = os.getenv("LLM_MODEL", "demo-model")
        log_level = os.getenv("LOG_LEVEL", "INFO")

        if not api_key:
            raise ConfigError(
                "LLM_API_KEY is not configured."
            )

        return cls(
            api_key=api_key,
            model=model,
            log_level=log_level,
        )