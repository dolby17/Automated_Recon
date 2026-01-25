"""
exceptions.py

Custom exception hierarchy for the Input Manager.
All input-related failures must raise one of these exceptions.
"""


class InputManagerError(Exception):
    """
    Base exception for all Input Manager errors.
    Catching this will catch all input-related failures.
    """
    pass


class DetectionError(InputManagerError):
    """
    Raised when input type detection fails or is ambiguous.
    """
    pass


class UnsupportedInputError(InputManagerError):
    """
    Raised when the input type is recognized but not supported
    in the current phase (e.g., IPv6, ASN).
    """
    pass


class ValidationError(InputManagerError):
    """
    Raised when input fails validation rules
    (e.g., private IP, malformed domain).
    """
    pass


class NormalizationError(InputManagerError):
    """
    Raised when normalization fails due to unexpected
    structure or missing components.
    """
    pass
