
import pytest
from unittest.mock import patch

from pgit.providers.factory import create_provider
from pgit.providers.errors import ProviderConfigurationError
from pgit.providers.mock import MockProvider


def test_create_mock_provider():
    provider = create_provider("mock")
    assert isinstance(provider, MockProvider)


@patch("pgit.providers.factory.GeminiProvider")
def test_create_gemini_provider(mock_gemini):
    create_provider("gemini")
    mock_gemini.assert_called_once_with()


def test_unknown_provider_raises_configuration_error():
    with pytest.raises(ProviderConfigurationError, match="Unknown provider"):
        create_provider("unknown")
