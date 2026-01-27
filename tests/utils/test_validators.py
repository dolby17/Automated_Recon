from src.utils.validators import is_valid_domain


def test_valid_domain():
    assert is_valid_domain("example.com") is True


def test_subdomain():
    assert is_valid_domain("api.example.com") is True


def test_invalid_characters():
    assert is_valid_domain("exa$mple.com") is False


def test_empty_string():
    assert is_valid_domain("") is False


def test_ip_address():
    assert is_valid_domain("192.168.1.1") is False


def test_trailing_dot():
    assert is_valid_domain("example.com.") is False
