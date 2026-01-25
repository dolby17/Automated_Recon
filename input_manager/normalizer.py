"""
normalizer.py

Normalization logic for validated inputs.
Produces canonical NormalizedTarget objects.
"""

from urllib.parse import urlparse
from ipaddress import ip_address, ip_network

from input_manager.models import InputType, NormalizedTarget
from input_manager.exceptions import NormalizationError


def normalize_input(input_type: InputType, raw_input: str) -> NormalizedTarget:
    """
    Normalize validated input into a canonical NormalizedTarget.

    Args:
        input_type (InputType): Detected and validated input type.
        raw_input (str): Original user input.

    Returns:
        NormalizedTarget: Canonical representation.

    Raises:
        NormalizationError: If normalization fails unexpectedly.
    """
    try:
        if input_type == InputType.URL:
            return _normalize_url(raw_input)
        if input_type == InputType.DOMAIN:
            return _normalize_domain(raw_input)
        if input_type == InputType.IPV4:
            return _normalize_ipv4(raw_input)
        if input_type == InputType.CIDR:
            return _normalize_cidr(raw_input)
    except Exception as exc:
        raise NormalizationError(str(exc)) from exc

    raise NormalizationError(f"Unhandled input type: {input_type}")


def _normalize_url(value: str) -> NormalizedTarget:
    parsed = urlparse(value)

    scheme = parsed.scheme.lower()
    host = parsed.hostname.lower() if parsed.hostname else None

    if not host:
        raise NormalizationError("URL host missing during normalization")

    port = parsed.port
    if port is None:
        port = 443 if scheme == "https" else 80

    path = parsed.path or "/"

    return NormalizedTarget(
        original_input=value,
        input_type=InputType.URL,
        scheme=scheme,
        host=host,
        port=port,
        path=path,
    )


def _normalize_domain(value: str) -> NormalizedTarget:
    host = value.strip().lower().rstrip("/")

    return NormalizedTarget(
        original_input=value,
        input_type=InputType.DOMAIN,
        host=host,
    )


def _normalize_ipv4(value: str) -> NormalizedTarget:
    ip = ip_address(value)

    return NormalizedTarget(
        original_input=value,
        input_type=InputType.IPV4,
        ip=str(ip),
    )


def _normalize_cidr(value: str) -> NormalizedTarget:
    network = ip_network(value, strict=False)

    return NormalizedTarget(
        original_input=value,
        input_type=InputType.CIDR,
        cidr=str(network),
    )
