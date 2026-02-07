
from abc import ABC, abstractmethod

class BaseValidator(ABC):
    """
    Abstract base class for validators.
    """

    @abstractmethod
    def validate(self, finding):
        """
        Validate a finding.

        Args:
            finding (dict)

        Returns:
            tuple (bool, dict)
            bool  -> confirmed or not
            dict  -> enriched finding
        """
        pass
