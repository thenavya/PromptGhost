
import pytest
from unittest.mock import MagicMock, patch

from pgit.providers.gemini import GeminiProvider
from pgit.providers.errors import (
    ProviderConfigurationError,
    ProviderRequestError,
)


def test_missing_api_key_raises_configuration_error(monkeypatch):
    monkeypatch.delenv("GEMINI_API_KEY", raising=False)

    with pytest.raises(ProviderConfigurationError):
        GeminiProvider()


@patch("pgit.providers.gemini.genai.Client")
def test_successful_generation(mock_client_class, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-api-key")

    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    mock_client.models.generate_content.return_value.text = "Hello!"

    provider = GeminiProvider(model="test-model")
    result = provider.generate("Be helpful", "Hi")

    assert result == "Hello!"
    mock_client.models.generate_content.assert_called_once_with(
        model="test-model",
        contents="Be helpful\n\nUser input:\nHi",
    )


@patch("pgit.providers.gemini.genai.Client")
def test_request_failure_raises_provider_error(mock_client_class, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-api-key")

    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    mock_client.models.generate_content.side_effect = RuntimeError("network error")

    provider = GeminiProvider()

    with pytest.raises(ProviderRequestError, match="Gemini request failed"):
        provider.generate("Be helpful", "Hi")


@patch("pgit.providers.gemini.genai.Client")
def test_empty_response_raises_provider_error(mock_client_class, monkeypatch):
    monkeypatch.setenv("GEMINI_API_KEY", "test-api-key")

    mock_client = MagicMock()
    mock_client_class.return_value = mock_client
    mock_client.models.generate_content.return_value.text = None

    provider = GeminiProvider()

    with pytest.raises(ProviderRequestError, match="empty response"):
        provider.generate("Be helpful", "Hi")
