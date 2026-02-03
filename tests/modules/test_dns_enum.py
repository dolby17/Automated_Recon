from unittest.mock import patch, MagicMock

from core.context import ReconContext
from modules.dns_enum import DNSEnumerationModule


@patch("dns.resolver.resolve")
def test_dns_enumeration_populates_context(mock_resolve):
    # Mock DNS answer
    mock_answer = MagicMock()
    mock_answer.__iter__.return_value = ["93.184.216.34"]
    mock_resolve.return_value = mock_answer

    context = ReconContext(target="example.com")
    module = DNSEnumerationModule()

    module.run(context)

    assert "A" in context.dns_records
    assert isinstance(context.dns_records["A"], list)


@patch("dns.resolver.resolve")
def test_dns_enumeration_handles_no_answer(mock_resolve):
    mock_resolve.side_effect = Exception

    context = ReconContext(target="example.com")
    module = DNSEnumerationModule()

    module.run(context)

    for record_type in module.RECORD_TYPES:
        assert record_type in context.dns_records
        assert context.dns_records[record_type] == []
