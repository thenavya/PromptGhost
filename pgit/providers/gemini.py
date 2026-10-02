import os

from google import genai

from pgit.providers.base import AIProvider
from pgit.providers.errors import (
    ProviderConfigurationError,
    ProviderRequestError,
)


class GeminiProvider(AIProvider):
    """Google Gemini AI provider."""

    def __init__(
        self,
        model: str = "gemini-3.5-flash-lite",
    ) -> None:
        api_key = os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ProviderConfigurationError(
                "GEMINI_API_KEY environment variable is not set."
            )

        self.client = genai.Client(
            api_key=api_key
        )

        self.model = model

    def generate(
        self,
        prompt: str,
        user_input: str,
    ) -> str:
        """Generate a response using Gemini."""

        contents = (
            f"{prompt}\n\n"
            f"User input:\n{user_input}"
        )

        try:
            response = self.client.models.generate_content(
                model=self.model,
                contents=contents,
            )
        except Exception as error:
            raise ProviderRequestError(
                f"Gemini request failed: {error}"
            ) from error

        if not response.text:
            raise ProviderRequestError(
                "Gemini returned an empty response."
            )

        return response.text