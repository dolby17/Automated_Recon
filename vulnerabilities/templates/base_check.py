from abc import ABC, abstractmethod

class BaseVulnCheck(ABC):
    """
    Abstract base class for all vulnerability checks
    """

    name = "base"
    severity = "info"

    def __init__(self, target, context):
        self.target = target
        self.context = context

    @abstractmethod
    def run(self):
        """
        Execute the vulnerability check.

        Returns:
            list[dict]: list of findings
        """
        pass
