"""
models.py

Typed data models for the Input Manager.
These models define the canonical structure of validated input.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Optional


class InputType(Enum):
    """
    Enumeration of supported input types.
    """
    URL = "url"
    DOMAIN = "domain"
    IPV4 = "ipv4"
    CIDR = "cidr"


@dataclass(frozen=True)
class NormalizedTarget:
    """
    Canonical representation of a validated and normalized target.
    This object is immutable and safe to pass across modules.
    """

    original_input: str
    input_type: InputType

    # URL-related fields
    scheme: Optional[str] = None
    host: Optional[str] = None
    port: Optional[int] = None
    path: Optional[str] = None

    # IP/CIDR-related fields
    ip: Optional[str] = None
    cidr: Optional[str] = None
