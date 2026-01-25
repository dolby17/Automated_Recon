"""
manager.py

Orchestration layer for the Input Manager.
This is the single entry point for processing user input.
"""

from input_manager.detector import detect_input_type
from input_manager.validators import validate_input
from input_manager.normalizer import normalize_input
from input_manager.models import NormalizedTarget


class InputManager:
    """
    High-level interface for processing and normalizing user input.
    """

    def process(self, raw_input: str) -> NormalizedTarget:
        """
        Process raw user input through detection, validation,
        and normalization.

        Args:
            raw_input (str): User-provided target.

        Returns:
            NormalizedTarget: Canonical, validated target.

        Raises:
            InputManagerError subclasses on failure.
        """
        input_type = detect_input_type(raw_input)
        validate_input(input_type, raw_input)
        return normalize_input(input_type, raw_input)
