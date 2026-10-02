from pgit.providers.base import AIProvider


class MockProvider(AIProvider):
    """Temporary provider used for local development."""

    def generate(
        self,
        prompt: str,
        user_input: str,
    ) -> str:
        return "I am unsure about that."