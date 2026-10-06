from mini_llm_app.config import Settings
from mini_llm_app.logging_config import (
    configure_logging,
)
from mini_llm_app.llm_service import LLMService

def main() -> None:
    settings = Settings.from_env()

    configure_logging(settings.log_level)

    service = LLMService(settings)

    response = service.chat(
        "Hello,LLM!"
    )

    print(response)


if __name__ == "__main__":
    main()