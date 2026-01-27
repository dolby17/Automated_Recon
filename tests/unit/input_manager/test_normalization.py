def test_single_domain_normalized_to_lowercase():
    from src.input_manager import normalize_targets

    result = normalize_targets("Example.COM")

    assert result == ["example.com"]


def test_protocol_is_removed():
    from src.input_manager import normalize_targets

    result = normalize_targets("example.com/")

    assert result == ["example.com"]



def test_whitespace_is_trimmed():
    from src.input_manager import normalize_targets

    result = normalize_targets("   example.com   ")

    assert result == ["example.com"]



def test_list_of_domains_is_normalized():
    from src.input_manager import normalize_targets

    result = normalize_targets(["Example.COM", "https://Test.com/"])

    assert result == ["example.com", "test.com"]



def test_duplicates_are_removed():
    from src.input_manager import normalize_targets

    result = normalize_targets(["Example.COM", "example.com", "https://example.com/"])

    assert result == ["example.com"]


import pytest

def test_empty_string_is_rejected():
    from src.input_manager import normalize_targets

    with pytest.raises(ValueError):
        normalize_targets("")
