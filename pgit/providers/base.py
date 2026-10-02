from abc import ABC, abstractmethod

from pgit.providers.errors import ProviderError


class AIProvider(ABC):
    """Base interface for AI providers."""

    @abstractmethod
    def generate(
        self,
        prompt: str,
        user_input: str,
    ) -> str:
        """Generate an AI response."""

        raise ProviderError(
            "AI provider did not implement generate()."
        )