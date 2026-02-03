from unittest.mock import patch, MagicMock

from core.context import ReconContext
from modules.subdomain_enum import SubdomainEnumerationModule


@patch("modules.subdomain_enum.requests.get")
def test_subdomain_enumeration_adds_domains(mock_get):
    mock_response = MagicMock()
    mock_response.raise_for_status.return_value = None
    mock_response.json.return_value = [
        {"name_value": "www.example.com"},
        {"name_value": "api.example.com\nmail.example.com"},
    ]

    mock_get.return_value = mock_response

    context = ReconContext(target="example.com")
    module = SubdomainEnumerationModule()

    module.run(context)

    assert "www.example.com" in context.domains
    assert "api.example.com" in context.domains
    assert "mail.example.com" in context.domains
    assert "example.com" in context.domains  # original target


@patch("modules.subdomain_enum.requests.get")
def test_subdomain_enumeration_handles_failure(mock_get):
    mock_get.side_effect = Exception

    context = ReconContext(target="example.com")
    module = SubdomainEnumerationModule()

    module.run(context)

    # Should still contain only the target
    assert context.domains == {"example.com"}
