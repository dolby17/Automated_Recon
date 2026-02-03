from abc import ABC, abstractmethod
from core.context import ReconContext


class ReconModule(ABC):
    """
    Base class for all recon modules.
    Enforces a strict execution contract.
    """

    name: str = "base"

    @abstractmethod
    def run(self, context: ReconContext) -> None:
        """
        Execute recon logic and update the context.
        Must NOT return anything.
        """
        raise NotImplementedError
