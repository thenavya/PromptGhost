class ProviderError(Exception):
    """Base error raised by PromptGhost AI providers."""


class ProviderConfigurationError(ProviderError):
    """Raised when a provider is incorrectly configured."""


class ProviderRequestError(ProviderError):
    """Raised when an AI provider request fails."""