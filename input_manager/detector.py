"""
detector.py

Responsible for detecting the type of raw user input.
"""

import re
from urllib.parse import urlparse
from ipaddress import ip_address, ip_network

from input_manager.models import InputType
from input_manager.exceptions import DetectionError, UnsupportedInputError


_DOMAIN_REGEX = re.compile(
    r"^(?!-)(?:[a-zA-Z0-9-]{1,63}\.)+[a-zA-Z]{2,63}$"
)


def detect_input_type(raw_input: str) -> InputType:
    """
    Detect the type of the given raw input.

    Args:
        raw_input (str): User-provided input string.

    Returns:
        InputType: Detected input type.

    Raises:
        DetectionError: If input is empty or ambiguous.
        UnsupportedInputError: If input type is recognized but unsupported.
    """

    if not raw_input or not raw_input.strip():
        raise DetectionError("Input is empty or whitespace")

    value = raw_input.strip()

    # 1. URL detection
    parsed = urlparse(value)
    if parsed.scheme and parsed.netloc:
        if parsed.scheme.lower() not in {"http", "https"}:
            raise UnsupportedInputError(
                f"Unsupported URL scheme: {parsed.scheme}"
            )
        return InputType.URL

    # 2. CIDR detection
    if "/" in value:
        try:
            network = ip_network(value, strict=False)
            if network.version == 6:
                raise UnsupportedInputError("IPv6 is not supported")
            return InputType.CIDR
        except ValueError:
            pass  # Not CIDR, continue detection

    # 3. IPv4 detection
    try:
        ip = ip_address(value)
        if ip.version == 6:
            raise UnsupportedInputError("IPv6 is not supported")
        return InputType.IPV4
    except ValueError:
        pass  # Not an IP, continue detection

    # 4. Domain detection
    if _DOMAIN_REGEX.match(value.lower()):
        return InputType.DOMAIN

    raise DetectionError(f"Unable to detect input type: {raw_input}")
