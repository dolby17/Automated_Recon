from typing import List
from core.context import ReconContext
from modules.base import ReconModule


class ReconPipeline:
    """
    Executes recon modules sequentially.
    """

    def __init__(self, modules: List[ReconModule]):
        self.modules = modules

    def run(self, context: ReconContext) -> ReconContext:
        for module in self.modules:
            if not isinstance(module, ReconModule):
                raise TypeError(f"{module} is not a ReconModule")

            module.run(context)

        return context
