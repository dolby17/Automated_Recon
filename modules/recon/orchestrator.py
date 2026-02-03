from typing import List, Dict

from core.context import ReconContext
from modules.recon.modules.base import ReconModule

class ReconOrchestrator:
    def __init__(self, targets: List[str]):
        self.targets = targets
        self.modules = []

    def register_module(self, module_cls: type[ReconModule]) -> None:
        self.modules.append(module_cls)

    def run(self) -> Dict[str, ReconContext]:
        results: Dict[str, ReconContext] = {}

        for target in self.targets:
            context = ReconContext(target)
            
            for module_cls in self.modules:
                module = module_cls()
                module.run(context)


                context.metadata["modules_run"].append(module.name)

            context.mark_finished()

            results[target] = context

        return results
