"""
validators.py

Validation logic for detected input types.
Ensures safety, scope sanity, and correctness.
"""

from urllib.parse import urlparse
from ipaddress import ip_address, ip_network

from input_manager.models import InputType
from input_manager.exceptions import ValidationError


_INTERNAL_TLDS = {
    "local",
    "internal",
    "intranet",
    "corp",
    "lan",
}


def validate_input(input_type: InputType, raw_input: str) -> None:
    """
    Dispatch validation based on input type.

    Args:
        input_type (InputType): Detected input type.
        raw_input (str): Original user input.

    Raises:
        ValidationError: If validation fails.
    """
    if input_type == InputType.URL:
        _validate_url(raw_input)
    elif input_type == InputType.DOMAIN:
        _validate_domain(raw_input)
    elif input_type == InputType.IPV4:
        _validate_ipv4(raw_input)
    elif input_type == InputType.CIDR:
        _validate_cidr(raw_input)
    else:
        raise ValidationError(f"Unhandled input type: {input_type}")


def _validate_url(value: str) -> None:
    parsed = urlparse(value)

    if parsed.scheme.lower() not in {"http", "https"}:
        raise ValidationError("Only http and https URLs are allowed")

    if parsed.username or parsed.password:
        raise ValidationError("URLs with embedded credentials are not allowed")

    if not parsed.hostname:
        raise ValidationError("URL hostname is missing")

    _validate_host(parsed.hostname)


def _validate_domain(domain: str) -> None:
    if "." not in domain:
        raise ValidationError("Invalid domain format")

    tld = domain.rsplit(".", 1)[-1].lower()
    if tld in _INTERNAL_TLDS:
        raise ValidationError(f"Internal TLD '{tld}' is not allowed")


def _validate_ipv4(value: str) -> None:
    ip = ip_address(value)

    if not ip.is_global:
        raise ValidationError("Private or reserved IPv4 addresses are not allowed")


def _validate_cidr(value: str) -> None:
    network = ip_network(value, strict=False)

    if network.version != 4:
        raise ValidationError("Only IPv4 CIDR ranges are supported")

    if network.prefixlen < 8 or network.prefixlen > 32:
        raise ValidationError("CIDR prefix length must be between /8 and /32")

    if not network.is_global:
        raise ValidationError("Private or reserved CIDR ranges are not allowed")


def _validate_host(host: str) -> None:
    """
    Validate hostname or IP used inside a URL.
    """
    try:
        ip = ip_address(host)
        if not ip.is_global:
            raise ValidationError("URL host resolves to a private IP")
    except ValueError:
        # Host is not an IP, treat as domain
        _validate_domain(host)
