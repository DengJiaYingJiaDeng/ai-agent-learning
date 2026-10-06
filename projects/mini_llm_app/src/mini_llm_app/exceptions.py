class MiniLLMError(Exception):
    """Base exception for mini_llm_app."""


class ConfigError(MiniLLMError):
    """Configuration is invalid."""



class InvalidPromptError(MiniLLMError):
    """Prompt is invalid."""


class LLMServiceError(MiniLLMError):
    """LLM service invocation failed."""