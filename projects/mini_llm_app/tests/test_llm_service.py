import pytest

from mini_llm_app.config import Settings
from mini_llm_app.exceptions import (
    InvalidPromptError,
    LLMServiceError,
)
from mini_llm_app.llm_service import LLMService

def build_settings() -> Settings:
    return Settings(
        api_key="test-key",
        model="test-model",
        log_level="INFO",
    )

def test_chat_success():
    def fake_transport(prompt: str) -> str:
        return f"answer:{prompt}"

    service = LLMService(
        build_settings(),
        transport=fake_transport,
    )

    result = service.chat("hello")

    assert result == "answer:hello"

def test_empty_prompt():
    service = LLMService(
        build_settings()
    )

    with pytest.raises(
        InvalidPromptError
    ):
        service.chat("   ")

def test_transport_failure():
    def broken_transport(prompt: str) -> str:
        raise RuntimeError("network down")

    service = LLMService(
        build_settings(),
        transport=broken_transport,
    )

    with pytest.raises(
        LLMServiceError
    ):
        service.chat("hello")