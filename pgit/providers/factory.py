from pgit.providers.base import AIProvider
from pgit.providers.errors import ProviderConfigurationError
from pgit.providers.gemini import GeminiProvider
from pgit.providers.mock import MockProvider


def create_provider(name: str) -> AIProvider:
    """Create an AI provider from configuration."""

    if name == "mock":
        return MockProvider()

    if name == "gemini":
        return GeminiProvider()

    raise ProviderConfigurationError(
        f"Unknown provider: {name}"
    )