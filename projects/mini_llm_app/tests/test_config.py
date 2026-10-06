import pytest

from mini_llm_app.config import Settings
from mini_llm_app.exceptions import ConfigError

def test_settings_from_env(monkeypatch):
    monkeypatch.setenv(
        "LLM_API_KEY",
        "test-key",
    )

    monkeypatch.setenv(
        "LLM_MODEL",
        "test-model",
    )

    settings = Settings.from_env()

    assert settings.api_key == "test-key"
    assert settings.model == "test-model"

def test_missing_api_key(monkeypatch):
    monkeypatch.delenv(
        "LLM_API_KEY",
        raising=False,
    )

    with pytest.raises(ConfigError):
        Settings.from_env()