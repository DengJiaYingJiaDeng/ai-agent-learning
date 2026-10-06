import logging

from collections.abc import Callable

from mini_llm_app.config import Settings
from mini_llm_app.exceptions import (
    InvalidPromptError,
    LLMServiceError,
)

logger = logging.getLogger(__name__)
Transport = Callable[[str],str]

class LLMService:
    def __init__(
        self,
        settings:Settings,
        transport:Transport | None = None
    ) -> None:
        self.settings = settings

        self.transport = (
            transport
            if transport is not None
            else self._mock_transport
        )

    def chat(self,prompt:str) -> str:
        if not prompt.strip():
            raise InvalidPromptError(
                "Prompt cannot be empty."
            )

        logger.info(
            "Calling model=%s",
            self.settings.model,
        )

        try:
            return self.transport(prompt)

        except Exception as exc:
            logger.exception(
                "LLM invocation failed."
            )

            raise LLMServiceError(
                "Failed to call LLM service."
            ) from exc

    @staticmethod
    def _mock_transport(prompt: str) -> str:
        return f"Mock response: {prompt}"